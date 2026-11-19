#!/usr/bin/env python3
"""Validate the generated Hugo site for SEO and AEO regressions.

The validator works on `public/` after a build.  It checks rendered metadata,
canonical/hreflang links, structured data, the Open Graph image asset, sitemap
targets, llms.txt, and the agent manifest.

Usage:
    python scripts/validate_seo.py
    python scripts/validate_seo.py --public public
    python scripts/validate_seo.py --update-baseline

Exit codes:
    0  no new findings and the baseline is current
    1  new findings, stale baseline entries, or a missing baseline
    2  configuration or baseline format error
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urljoin, urlsplit

from validation_common import Findings, compare, load_baseline, print_report, write_baseline


SITE_HOSTS = {"agent-engine-optimization.com", "www.agent-engine-optimization.com"}
CANONICAL_HOST = "agent-engine-optimization.com"
SITEMAP_NS = {
    "sm": "http://www.sitemaps.org/schemas/sitemap/0.9",
    "x": "http://www.w3.org/1999/xhtml",
}
DOCS_RE = re.compile(
    r"^/(?:(?P<lang>de|es|pt|ja)/)?docs/(?P<slug>[^/]+(?:/[^/]+)*)/?$"
)
FRONT_DATE_RE = re.compile(r"(?m)^date:\s*[\"']?(\d{4}-\d{2}-\d{2})")
HOME_ROUTES = {"/", "/de/", "/es/", "/ja/", "/pt/"}
DOCS_SECTION_ROUTES = {"/docs/", "/es/docs/", "/pt/docs/", "/de/docs/", "/ja/docs/"}
LANGUAGE_BLOCK_RE = re.compile(
    r"(?ms)^\s*\[languages\.([a-z-]+)\]\s*\n(.*?)(?=^\s*\[|\Z)"
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_attrs: dict[str, str] = {}
        self.title_parts: list[str] = []
        self.title_count = 0
        self._in_title = False
        self.metas: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.scripts: list[tuple[dict[str, str], str]] = []
        self._script_attrs: dict[str, str] | None = None
        self._script_parts: list[str] = []

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key.lower(): (value or "") for key, value in attrs}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = self._attrs(attrs)
        tag = tag.lower()
        if tag == "html":
            self.html_attrs.update(values)
        elif tag == "title":
            self.title_count += 1
            self._in_title = True
            self.title_parts = []
        elif tag == "meta":
            self.metas.append(values)
        elif tag == "link":
            self.links.append(values)
        elif tag == "script":
            self._script_attrs = values
            self._script_parts = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._script_attrs is not None:
            self.scripts.append((self._script_attrs, "".join(self._script_parts)))
            self._script_attrs = None
            self._script_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._script_attrs is not None:
            self._script_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_parts).split())


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_space(value: str) -> str:
    return " ".join(value.split())


def page_route(public: Path, path: Path) -> str | None:
    relative = path.relative_to(public).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    if is_not_found_page(relative):
        return None
    if relative.endswith(".html"):
        return "/" + relative
    return None


def is_not_found_page(relative: str) -> bool:
    return relative == "404.html" or relative.endswith("/404.html")


def meta_values(parser: PageParser, key: str, attribute: str = "name") -> list[str]:
    values = []
    for meta in parser.metas:
        if meta.get(attribute, "").lower() == key.lower():
            values.append(meta.get("content", ""))
    return values


def link_values(parser: PageParser, rel: str) -> list[str]:
    values = []
    for link in parser.links:
        if rel.lower() in link.get("rel", "").lower().split():
            values.append(link.get("href", ""))
    return values


def alternates(parser: PageParser) -> list[tuple[str, str]]:
    result = []
    for link in parser.links:
        if "alternate" not in link.get("rel", "").lower().split():
            continue
        language = link.get("hreflang", "").strip().lower()
        href = link.get("href", "").strip()
        if language:
            result.append((language, href))
    return result


def normalize_language(value: str) -> str:
    """Lowercase a language code without dropping its region subtag."""
    return value.strip().lower()


def expected_language_code(language_codes: dict[str, str], language: str) -> str:
    return language_codes.get(language, language).strip().lower()


def safe_urlsplit(url: str):
    """Parse a URL without letting malformed input abort the validator."""
    try:
        parsed = urlsplit(url)
        _ = parsed.port  # Force validation of a malformed port.
    except (TypeError, ValueError):
        return None
    return parsed


def url_hostname(parsed) -> str | None:
    try:
        return parsed.hostname
    except ValueError:
        return None


def language_codes_from_config(config: str, keys: list[str]) -> dict[str, str]:
    codes = {key: key for key in keys}
    for match in LANGUAGE_BLOCK_RE.finditer(config):
        key = match.group(1)
        code_match = re.search(
            r'(?m)^\s*languageCode\s*=\s*"([^"]+)"', match.group(2)
        )
        if code_match:
            codes[key] = code_match.group(1)
    return codes


def url_for_route(base_url: str, route: str) -> str:
    return base_url.rstrip("/") + route


def translation_group_key(route: str) -> tuple[str, str]:
    if route in HOME_ROUTES:
        return ("home", "")
    if route in DOCS_SECTION_ROUTES:
        return ("docs-section", "")
    match = DOCS_RE.match(route)
    if match:
        return ("docs", match.group("slug"))
    return ("page", route)


def page_language(route: str) -> str:
    if route == "/":
        return "en"
    first = route.strip("/").split("/", 1)[0]
    return first if first in {"es", "pt", "de", "ja"} else "en"


def expected_x_default(route: str, group_routes: list[str]) -> str:
    if page_language(route) == "en":
        return route
    for candidate in group_routes:
        if page_language(candidate) == "en":
            return candidate
    return "/"


def route_from_url(url: str) -> str | None:
    parsed = safe_urlsplit(url)
    if parsed is None:
        return None
    try:
        path = unquote(parsed.path)
    except (TypeError, ValueError):
        return None
    if not path or path == "/":
        return "/"
    if path.endswith(".html"):
        return path
    if not path.endswith("/"):
        path += "/"
    return path


def html_target_path(public: Path, route: str) -> Path:
    if route == "/":
        return public / "index.html"
    if route.endswith(".html"):
        return public / route.lstrip("/")
    return public / route.strip("/") / "index.html"


def is_alias(parser: PageParser) -> bool:
    return any(
        meta.get("http-equiv", "").lower() == "refresh" for meta in parser.metas
    )


def resolve_local_url(public: Path, url: str) -> Path | None:
    parsed = safe_urlsplit(url)
    if parsed is None:
        return None
    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc and url_hostname(parsed) not in SITE_HOSTS:
        return None
    try:
        path = unquote(parsed.path)
    except (TypeError, ValueError):
        return None
    if not path:
        return None
    return public / path.lstrip("/")


def png_dimensions(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n") or len(data) < 24:
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def svg_dimensions(path: Path) -> tuple[int, int] | None:
    text = read_text(path)[:2000]
    width = re.search(r'\bwidth=["\'](\d+)', text)
    height = re.search(r'\bheight=["\'](\d+)', text)
    if not width or not height:
        return None
    return int(width.group(1)), int(height.group(1))


def image_dimensions(path: Path) -> tuple[int, int] | None:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return png_dimensions(path)
    if suffix == ".svg":
        return svg_dimensions(path)
    return None


def walk_json(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from walk_json(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_json(item)


def parse_schema_graph(parser: PageParser) -> tuple[list[dict], list[str]]:
    graphs: list[dict] = []
    errors: list[str] = []
    for attrs, content in parser.scripts:
        if attrs.get("type", "").lower() != "application/ld+json":
            continue
        try:
            payload = json.loads(content)
        except json.JSONDecodeError as error:
            errors.append(str(error))
            continue
        if isinstance(payload, dict):
            if isinstance(payload.get("@graph"), list):
                graphs.extend(node for node in payload["@graph"] if isinstance(node, dict))
            else:
                graphs.append(payload)
    return graphs, errors


def collect_defined_ids(nodes: list[dict]) -> set[str]:
    defined: set[str] = set()
    for node in nodes:
        identifier = node.get("@id")
        if isinstance(identifier, str) and identifier:
            defined.add(identifier)
    return defined


def check_page(
    route: str,
    path: Path,
    parser: PageParser,
    base_url: str,
    public: Path,
    root: Path,
    findings: Findings,
    page_descriptions: dict[str, str],
    missing_assets: dict[str, set[str]],
    article_max_date: str | None,
    configured_image: str | None,
    language_codes: dict[str, str],
) -> None:
    relative_path = f"public/{path.relative_to(public).as_posix()}"
    language = page_language(route)

    if parser.title_count != 1:
        findings.add(
            path=relative_path,
            rule="seo.title_count",
            detail=f"count={parser.title_count}",
            message="A page must contain exactly one title element.",
        )
    elif not parser.title:
        findings.add(
            path=relative_path,
            rule="seo.title_empty",
            detail=route,
            message="Title element is empty.",
        )

    descriptions = [normalize_space(value) for value in meta_values(parser, "description")]
    if not descriptions or not any(descriptions):
        findings.add(
            path=relative_path,
            rule="seo.description_missing",
            detail=route,
            message="Meta description is missing or empty.",
        )
    if len([value for value in descriptions if value]) > 1:
        findings.add(
            path=relative_path,
            rule="seo.description_multiple",
            detail=str(len(descriptions)),
            message="More than one meta description was rendered.",
        )

    canonical = [value for value in link_values(parser, "canonical") if value]
    if not canonical:
        findings.add(
            path=relative_path,
            rule="seo.canonical_missing",
            detail=route,
            message="Canonical URL is missing.",
        )
    elif len(canonical) > 1:
        findings.add(
            path=relative_path,
            rule="seo.canonical_multiple",
            detail=str(len(canonical)),
            message="More than one canonical URL was rendered.",
        )
    else:
        expected = url_for_route(base_url, route)
        actual = canonical[0]
        actual_parsed = safe_urlsplit(actual)
        expected_parsed = safe_urlsplit(expected)
        if actual_parsed is None or expected_parsed is None:
            findings.add(
                path=relative_path,
                rule="seo.canonical_invalid",
                detail=actual,
                message="Canonical URL is not a valid absolute URL.",
            )
        elif actual_parsed.path != expected_parsed.path:
            findings.add(
                path=relative_path,
                rule="seo.canonical_not_self",
                detail=actual,
                message=f"Canonical does not point to {expected}.",
            )

    html_lang = parser.html_attrs.get("lang", "").strip().lower()
    expected_html_lang = expected_language_code(language_codes, language)
    if not html_lang:
        findings.add(
            path=relative_path,
            rule="seo.html_lang_missing",
            detail=route,
            message="The html element has no lang attribute.",
        )
    elif normalize_language(html_lang) != expected_html_lang:
        findings.add(
            path=relative_path,
            rule="seo.html_lang_wrong",
            detail=f"expected={expected_html_lang},actual={html_lang}",
            message="The html lang attribute does not match the page language.",
        )

    spanish_route = None
    docs_match = DOCS_RE.match(route)
    if docs_match and language in {"de", "pt", "ja"}:
        spanish_route = f"/es/docs/{docs_match.group('slug')}/"
    if spanish_route and page_descriptions.get(route) and page_descriptions.get(spanish_route):
        if page_descriptions[route] == page_descriptions[spanish_route]:
            findings.add(
                path=relative_path,
                rule="seo.description_from_spanish",
                detail=spanish_route,
                message="Rendered meta description is identical to the Spanish page.",
            )

    og_image_tags = meta_values(parser, "og:image", "property")
    og_images = [value for value in og_image_tags if value]
    if not og_images:
        findings.add(
            path=relative_path,
            rule="seo.og_image_missing",
            detail=route,
            message="Open Graph image is missing.",
        )
    if len(og_image_tags) > 1:
        findings.add(
            path=relative_path,
            rule="seo.og_image_multiple",
            detail=str(len(og_image_tags)),
            message="More than one Open Graph image tag was rendered.",
        )
    for image_url in og_images:
        parsed_image = safe_urlsplit(image_url)
        if parsed_image is None:
            findings.add(
                path=relative_path,
                rule="seo.og_image_invalid",
                detail=image_url,
                message="Open Graph image URL is not valid.",
            )
            continue
        if not parsed_image.netloc:
            findings.add(
                path=relative_path,
                rule="seo.og_image_not_absolute",
                detail=image_url,
                message="Open Graph image must use an absolute URL.",
            )
            continue
        local = resolve_local_url(public, image_url)
        if local is not None and not local.exists():
            missing_assets.setdefault(image_url, set()).add(relative_path)

    if route in HOME_ROUTES and configured_image and og_images:
        expected_image = url_for_route(base_url, configured_image)
        if any(image_url != expected_image for image_url in og_images):
            findings.add(
                path=relative_path,
                rule="seo.og_image_home_not_default",
                detail=f"expected={expected_image},actual={','.join(og_images)}",
                message="A home page must use the configured Open Graph image.",
            )

    schema_nodes, schema_errors = parse_schema_graph(parser)
    for error in schema_errors:
        findings.add(
            path=relative_path,
            rule="seo.jsonld_invalid",
            detail=error,
            message="JSON-LD is not valid JSON.",
        )
    defined_ids = collect_defined_ids(schema_nodes)
    for node in schema_nodes:
        node_type = node.get("@type")
        types = node_type if isinstance(node_type, list) else [node_type]
        if "Article" in types and not node.get("inLanguage"):
            findings.add(
                path=relative_path,
                rule="seo.schema_inlanguage_missing",
                detail=route,
                message="Article JSON-LD has no inLanguage.",
            )
        in_language = node.get("inLanguage")
        if isinstance(in_language, str) and in_language.strip():
            expected_in_language = expected_language_code(language_codes, language)
            if normalize_language(in_language) != expected_in_language:
                findings.add(
                    path=relative_path,
                    rule="seo.schema_inlanguage_wrong",
                    detail=f"expected={language},actual={in_language}",
                    message="Structured-data language does not match the page.",
                )
        publisher = node.get("publisher")
        if isinstance(publisher, dict):
            publisher_id = publisher.get("@id")
            if isinstance(publisher_id, str) and publisher_id and publisher_id not in defined_ids:
                findings.add(
                    path=relative_path,
                    rule="seo.schema_publisher_unresolved",
                    detail=publisher_id,
                    message="publisher @id is not defined in the page JSON-LD graph.",
                )


def validate_not_found_page(
    relative_path: str,
    route: str,
    parser: PageParser,
    base_url: str,
    public: Path,
    findings: Findings,
    missing_assets: dict[str, set[str]],
) -> None:
    """Validate the non-indexable 404 pages without documentation rules."""
    values = alternates(parser)
    if values:
        codes = sorted({code for code, _ in values})
        findings.add(
            path=relative_path,
            rule="seo.hreflang_on_404",
            detail=",".join(codes),
            message="A 404 page must not emit hreflang links, including x-default.",
        )
        for code, href in values:
            target_route = route_from_url(href)
            if target_route is None or not html_target_path(public, target_route).exists():
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_on_404_target_invalid",
                    detail=f"{code}:{href}",
                    message="hreflang on a 404 page does not resolve to a generated HTML page.",
                )

    canonical = [value for value in link_values(parser, "canonical") if value]
    if not canonical:
        findings.add(
            path=relative_path,
            rule="seo.canonical_missing",
            detail=route,
            message="Canonical URL is missing.",
        )
    elif len(canonical) > 1:
        findings.add(
            path=relative_path,
            rule="seo.canonical_multiple",
            detail=str(len(canonical)),
            message="More than one canonical URL was rendered.",
        )
    else:
        expected = url_for_route(base_url, route)
        actual = canonical[0]
        actual_parsed = safe_urlsplit(actual)
        expected_parsed = safe_urlsplit(expected)
        if actual_parsed is None or expected_parsed is None:
            findings.add(
                path=relative_path,
                rule="seo.canonical_invalid",
                detail=actual,
                message="Canonical URL is not a valid absolute URL.",
            )
        elif actual_parsed.path != expected_parsed.path:
            findings.add(
                path=relative_path,
                rule="seo.canonical_not_self",
                detail=actual,
                message=f"Canonical does not point to {expected}.",
            )

    og_image_tags = meta_values(parser, "og:image", "property")
    og_images = [value for value in og_image_tags if value]
    if not og_images:
        findings.add(
            path=relative_path,
            rule="seo.og_image_missing",
            detail=route,
            message="Open Graph image is missing.",
        )
    if len(og_image_tags) > 1:
        findings.add(
            path=relative_path,
            rule="seo.og_image_multiple",
            detail=str(len(og_image_tags)),
            message="More than one Open Graph image tag was rendered.",
        )
    for image_url in og_images:
        parsed_image = safe_urlsplit(image_url)
        if parsed_image is None:
            findings.add(
                path=relative_path,
                rule="seo.og_image_invalid",
                detail=image_url,
                message="Open Graph image URL is not valid.",
            )
            continue
        if not parsed_image.netloc:
            findings.add(
                path=relative_path,
                rule="seo.og_image_not_absolute",
                detail=image_url,
                message="Open Graph image must use an absolute URL.",
            )
            continue
        local = resolve_local_url(public, image_url)
        if local is None:
            continue
        if not local.exists():
            missing_assets.setdefault(image_url, set()).add(relative_path)
            continue
        try:
            dimensions = image_dimensions(local)
        except OSError:
            dimensions = None
        if dimensions != (1200, 630):
            findings.add(
                path=relative_path,
                rule="seo.og_image_dimensions",
                detail=f"{dimensions[0]}x{dimensions[1]}" if dimensions else "invalid",
                message="The 404 Open Graph image must be a valid 1200x630 image.",
            )


def validate_hreflang(
    pages: dict[str, tuple[Path, PageParser]],
    base_url: str,
    public: Path,
    language_codes: dict[str, str],
    expected_codes: dict[str, set[str]],
    x_default_routes: dict[str, str],
    alias_routes: set[str],
    findings: Findings,
) -> None:
    allowed_codes = {code.lower() for code in language_codes.values()} | {"x-default"}
    alternates_by_route = {
        route: alternates(parser) for route, (_, parser) in pages.items()
    }

    for route, (path, parser) in sorted(pages.items()):
        relative_path = f"public/{path.relative_to(public).as_posix()}"
        values = alternates_by_route[route]
        if not values:
            findings.add(
                path=relative_path,
                rule="seo.hreflang_missing",
                detail=route,
                message="No alternate hreflang links were rendered.",
            )
            continue

        codes = [code for code, _ in values]
        normalized = [normalize_language(code) for code in codes]
        own_code = expected_language_code(language_codes, page_language(route))
        expected = {code.lower() for code in expected_codes[route]}

        if own_code not in codes:
            findings.add(
                path=relative_path,
                rule="seo.hreflang_self_missing",
                detail=own_code,
                message="The page does not declare its own language as hreflang.",
            )
        else:
            expected_self = url_for_route(base_url, route)
            expected_self_parsed = safe_urlsplit(expected_self)
            self_links = [href for code, href in values if code == own_code]
            self_matches = False
            for href in self_links:
                parsed_self = safe_urlsplit(href)
                if (
                    parsed_self is not None
                    and expected_self_parsed is not None
                    and parsed_self.path == expected_self_parsed.path
                ):
                    self_matches = True
                    break
            if not self_matches:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_self_mismatch",
                    detail=f"expected={expected_self},actual={','.join(self_links)}",
                    message="The self-referencing hreflang does not point to this page.",
                )

        for code in sorted(expected):
            if code not in codes:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_incomplete",
                    detail=code,
                    message=f"Missing hreflang for {code}.",
                )

        for code in codes:
            if code == "x-default":
                continue
            if code not in expected:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_unexpected",
                    detail=code,
                    message=f"Hreflang for {code} is not an existing translation of this page.",
                )
            if code not in allowed_codes:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_invalid_code",
                    detail=code,
                    message=f"Hreflang code {code} is not configured for this site.",
                )

        for code, href in values:
            parsed = safe_urlsplit(href)
            if parsed is None:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_url_invalid",
                    detail=href,
                    message="Hreflang URL is not a valid URL.",
                )
                continue
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_not_absolute",
                    detail=href,
                    message="Hreflang URL must be absolute.",
                )
                continue
            hostname = url_hostname(parsed)
            if hostname not in SITE_HOSTS:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_not_absolute",
                    detail=f"{href} (host={hostname})",
                    message="Hreflang URL must use the site host.",
                )
                continue
            target_route = route_from_url(href)
            if target_route is None:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_url_invalid",
                    detail=href,
                    message="Hreflang URL is not a valid URL.",
                )
                continue
            if target_route in alias_routes:
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_target_alias",
                    detail=href,
                    message="Hreflang points to a redirect alias.",
                )
                continue
            if not html_target_path(public, target_route).exists():
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_target_missing",
                    detail=href,
                    message="Hreflang target does not resolve to a generated HTML page.",
                )

        xdefault_links = [href for code, href in values if code == "x-default"]
        if not xdefault_links:
            findings.add(
                path=relative_path,
                rule="seo.hreflang_x_default_missing",
                detail=route,
                message="No x-default hreflang was rendered.",
            )
        else:
            expected_xdefault = url_for_route(base_url, x_default_routes[route])
            expected_xdefault_parsed = safe_urlsplit(expected_xdefault)
            for href in xdefault_links:
                parsed = safe_urlsplit(href)
                if parsed is None or expected_xdefault_parsed is None:
                    continue
                if (
                    parsed.scheme not in {"http", "https"}
                    or url_hostname(parsed) not in SITE_HOSTS
                    or parsed.path != expected_xdefault_parsed.path
                ):
                    findings.add(
                        path=relative_path,
                        rule="seo.hreflang_x_default_wrong",
                        detail=f"expected={expected_xdefault},actual={href}",
                        message="x-default does not match the English equivalent of this page.",
                    )

        exact_duplicates = sorted(
            code for code, count in Counter(codes).items() if count > 1
        )
        normalized_duplicates = sorted(
            code
            for code, count in Counter(normalized).items()
            if count > 1 and code not in exact_duplicates
        )
        for code in exact_duplicates + normalized_duplicates:
            findings.add(
                path=relative_path,
                rule="seo.hreflang_duplicate",
                detail=code,
                message=f"Duplicate hreflang value: {code}",
            )

    for route, (path, _) in sorted(pages.items()):
        relative_path = f"public/{path.relative_to(public).as_posix()}"
        for code, href in alternates_by_route[route]:
            if code == "x-default":
                continue
            parsed = safe_urlsplit(href)
            if parsed is None or url_hostname(parsed) not in SITE_HOSTS:
                continue
            target_route = route_from_url(href)
            if target_route is None or target_route == route or target_route not in pages:
                continue
            target_values = alternates_by_route[target_route]
            if not any(
                route_from_url(back_href) == route
                for back_code, back_href in target_values
                if back_code != "x-default"
            ):
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_not_reciprocal",
                    detail=target_route,
                    message="The hreflang target does not link back to this page.",
                )


def validate_assets(
    public: Path,
    root: Path,
    base_url: str,
    configured_image: str | None,
    missing_assets: dict[str, set[str]],
    findings: Findings,
) -> None:
    for image_url, pages in sorted(missing_assets.items()):
        parsed = safe_urlsplit(image_url)
        image_path = parsed.path if parsed is not None else image_url
        findings.add(
            path="public" + image_path,
            rule="aeo.og_image_asset_missing",
            detail=image_url,
            message=f"Referenced by {len(pages)} rendered pages but not present in public/.",
        )

    if not configured_image:
        findings.add(
            path="config.toml",
            rule="aeo.og_image_not_configured",
            detail="params.images",
            message="No default Open Graph image is configured.",
        )
        return

    image_path = public / configured_image.lstrip("/")
    if not image_path.exists():
        return
    dimensions = image_dimensions(image_path)
    if image_path.suffix.lower() == ".png" and dimensions is None:
        findings.add(
            path=f"public/{configured_image.lstrip('/')}",
            rule="aeo.og_image_format",
            detail=image_path.suffix,
            message="The configured .png asset is not a valid PNG file.",
        )
        return
    if dimensions != (1200, 630):
        findings.add(
            path=f"public/{configured_image.lstrip('/')}",
            rule="aeo.og_image_dimensions",
            detail=f"{dimensions[0]}x{dimensions[1]}" if dimensions else "unknown",
            message="Open Graph image should be 1200x630.",
        )


@dataclass
class SitemapEntry:
    route: str
    child_path: Path
    links: list[tuple[str, str]]
    loc_url: str


def sitemap_root_kind(root: ET.Element) -> str:
    return root.tag.rsplit("}", 1)[-1].lower()


def sitemap_relative_path(public: Path, path: Path) -> str:
    return f"public/{path.relative_to(public).as_posix()}"


def sitemap_child_path(public: Path, child_url: str) -> Path | None:
    parsed = safe_urlsplit(child_url)
    if (
        parsed is None
        or parsed.scheme not in {"http", "https"}
        or not parsed.netloc
        or url_hostname(parsed) not in SITE_HOSTS
    ):
        return None
    try:
        path = unquote(parsed.path)
    except (TypeError, ValueError):
        return None
    if not path:
        return None
    return public / path.lstrip("/")


def sitemap_target_path(public: Path, url: str) -> Path | None:
    parsed = safe_urlsplit(url)
    if (
        parsed is None
        or parsed.scheme not in {"http", "https"}
        or not parsed.netloc
        or url_hostname(parsed) not in SITE_HOSTS
    ):
        return None
    try:
        path = unquote(parsed.path)
    except (TypeError, ValueError):
        return None
    if not path:
        return None
    if path == "/":
        return public / "index.html"
    if path.endswith(".html"):
        return public / path.lstrip("/")
    if not path.endswith("/"):
        path += "/"
    return public / path.lstrip("/") / "index.html"


def check_sitemap_url_entries(
    public: Path,
    root: ET.Element,
    relative_path: str,
    findings: Findings,
) -> None:
    for index, url_node in enumerate(root.findall("sm:url", SITEMAP_NS), 1):
        loc_node = url_node.find("sm:loc", SITEMAP_NS)
        if loc_node is None or not (loc_node.text or "").strip():
            findings.add(
                path=relative_path,
                rule="aeo.sitemap_url_loc_missing",
                detail=f"url={index}",
                message="A sitemap URL entry has no non-empty loc.",
            )
            continue
        url = loc_node.text.strip()
        target = sitemap_target_path(public, url)
        if target is None:
            findings.add(
                path=relative_path,
                rule="aeo.sitemap_url_invalid",
                detail=url,
                message="Sitemap URL is not a valid URL.",
            )
            continue
        if not target.exists():
            findings.add(
                path=relative_path,
                rule="aeo.sitemap_url_missing_page",
                detail=url,
                message="Sitemap URL does not resolve to a generated HTML page.",
            )


def validate_sitemap(public: Path, base_url: str, findings: Findings) -> None:
    sitemap = public / "sitemap.xml"
    if not sitemap.exists():
        findings.add(
            path="public/sitemap.xml",
            rule="aeo.sitemap_missing",
            detail="sitemap.xml",
            message="Root sitemap is missing.",
        )
        return
    try:
        root = ET.fromstring(sitemap.read_bytes())
    except ET.ParseError as error:
        findings.add(
            path="public/sitemap.xml",
            rule="aeo.sitemap_invalid",
            detail=str(error),
            message="Root sitemap is not valid XML.",
        )
        return

    kind = sitemap_root_kind(root)
    if kind == "sitemapindex":
        sitemap_nodes = root.findall("sm:sitemap", SITEMAP_NS)
        if not sitemap_nodes:
            findings.add(
                path="public/sitemap.xml",
                rule="aeo.sitemap_index_empty",
                detail="sitemapindex",
                message="The root sitemap index contains no sitemap entries.",
            )
        for index, sitemap_node in enumerate(sitemap_nodes, 1):
            loc_node = sitemap_node.find("sm:loc", SITEMAP_NS)
            if loc_node is None or not (loc_node.text or "").strip():
                findings.add(
                    path="public/sitemap.xml",
                    rule="aeo.sitemap_index_loc_missing",
                    detail=f"entry={index}",
                    message="A sitemap index entry has no non-empty loc.",
                )
                continue
            child_url = loc_node.text.strip()
            child_path = sitemap_child_path(public, child_url)
            if child_path is None:
                findings.add(
                    path="public/sitemap.xml",
                    rule="aeo.sitemap_child_invalid_url",
                    detail=child_url,
                    message="Child sitemap URL is not a valid URL.",
                )
                continue
            if not child_path.exists():
                findings.add(
                    path="public/sitemap.xml",
                    rule="aeo.sitemap_child_missing",
                    detail=child_url,
                    message="Child sitemap referenced by the index is missing.",
                )
                continue
            try:
                child = ET.fromstring(child_path.read_bytes())
            except ET.ParseError as error:
                findings.add(
                    path=sitemap_relative_path(public, child_path),
                    rule="aeo.sitemap_invalid",
                    detail=str(error),
                    message="Child sitemap is not valid XML.",
                )
                continue
            child_kind = sitemap_root_kind(child)
            if child_kind != "urlset":
                findings.add(
                    path=sitemap_relative_path(public, child_path),
                    rule="aeo.sitemap_child_root_invalid",
                    detail=child_kind,
                    message="Child sitemap root must be a urlset.",
                )
                continue
            check_sitemap_url_entries(
                public, child, sitemap_relative_path(public, child_path), findings
            )
    elif kind == "urlset":
        findings.add(
            path="public/sitemap.xml",
            rule="aeo.sitemap_root_unexpected",
            detail="urlset",
            message="Root sitemap is a urlset; a sitemap index was expected.",
        )
        check_sitemap_url_entries(public, root, "public/sitemap.xml", findings)
    else:
        findings.add(
            path="public/sitemap.xml",
            rule="aeo.sitemap_root_invalid",
            detail=root.tag,
            message="Root sitemap is neither a sitemap index nor a urlset.",
        )


def load_sitemap_entries(public: Path, findings: Findings) -> list[SitemapEntry]:
    index = public / "sitemap.xml"
    if not index.exists():
        return []
    try:
        root = ET.fromstring(index.read_bytes())
    except ET.ParseError:
        return []

    entries: list[SitemapEntry] = []

    def collect(root_node: ET.Element, child_path: Path) -> None:
        for url in root_node.findall("sm:url", SITEMAP_NS):
            loc_node = url.find("sm:loc", SITEMAP_NS)
            if loc_node is None or not (loc_node.text or "").strip():
                continue
            loc_url = loc_node.text.strip()
            parsed_loc = safe_urlsplit(loc_url)
            if (
                parsed_loc is None
                or parsed_loc.scheme not in {"http", "https"}
                or not parsed_loc.netloc
            ):
                continue
            route = route_from_url(loc_url)
            if route is None:
                continue
            links = []
            for link in url.findall("x:link", SITEMAP_NS):
                code = (link.get("hreflang") or "").strip().lower()
                href = (link.get("href") or "").strip()
                if code:
                    links.append((code, href))
            entries.append(SitemapEntry(route, child_path, links, loc_url))

    kind = sitemap_root_kind(root)
    if kind == "sitemapindex":
        for loc in root.findall("sm:sitemap/sm:loc", SITEMAP_NS):
            if not loc.text:
                continue
            child_url = loc.text.strip()
            child_path = sitemap_child_path(public, child_url)
            if child_path is None or not child_path.exists():
                continue
            try:
                child = ET.fromstring(child_path.read_bytes())
            except ET.ParseError:
                continue
            if sitemap_root_kind(child) != "urlset":
                continue
            collect(child, child_path)
    elif kind == "urlset":
        collect(root, index)

    first_by_route: dict[str, SitemapEntry] = {}
    for entry in entries:
        first = first_by_route.get(entry.route)
        if first is None:
            first_by_route[entry.route] = entry
            continue
        findings.add(
            path=sitemap_relative_path(public, entry.child_path),
            rule="aeo.sitemap_duplicate_loc",
            detail=(
                f"{entry.route} (first: {first.loc_url} in "
                f"{sitemap_relative_path(public, first.child_path)})"
            ),
            message="Duplicate sitemap loc entry.",
        )
    return entries


def validate_sitemap_hreflang(
    public: Path,
    pages: dict[str, tuple[Path, PageParser]],
    html_alternates: dict[str, list[tuple[str, str]]],
    alias_routes: set[str],
    language_codes: dict[str, str],
    findings: Findings,
) -> None:
    entries = load_sitemap_entries(public, findings)
    if not entries:
        return
    allowed_codes = {code.lower() for code in language_codes.values()} | {
        "x-default"
    }
    entries_by_route: dict[str, SitemapEntry] = {}
    for entry in entries:
        entries_by_route.setdefault(entry.route, entry)

    for entry in sorted(
        entries, key=lambda item: (item.route, str(item.child_path), item.loc_url)
    ):
        route = entry.route
        child_path = entry.child_path
        links = entry.links
        relative_path = sitemap_relative_path(public, child_path)
        codes = [code for code, _ in links]

        expected_code = expected_language_code(
            language_codes, page_language(route)
        )
        self_codes = {
            code
            for code, href in links
            if code != "x-default" and route_from_url(href) == route
        }
        if self_codes != {expected_code}:
            findings.add(
                path=relative_path,
                rule="aeo.sitemap_hreflang_self_missing",
                detail=(
                    f"{route} expected={expected_code} "
                    f"actual={','.join(sorted(self_codes)) or 'none'}"
                ),
                message=(
                    "Sitemap entry does not declare exactly its own route and "
                    "language as hreflang."
                ),
            )

        for code in codes:
            if code != "x-default" and code not in allowed_codes:
                findings.add(
                    path=relative_path,
                    rule="aeo.sitemap_hreflang_invalid_code",
                    detail=code,
                    message=f"Sitemap hreflang code {code} is not configured.",
                )

        duplicates = sorted(
            code for code, count in Counter(codes).items() if count > 1
        )
        for code in duplicates:
            findings.add(
                path=relative_path,
                rule="aeo.sitemap_hreflang_duplicate",
                detail=code,
                message=f"Duplicate sitemap hreflang value: {code}",
            )

        for code, href in links:
            if code == "x-default":
                continue
            parsed = safe_urlsplit(href)
            if parsed is None:
                findings.add(
                    path=relative_path,
                    rule="aeo.sitemap_hreflang_url_invalid",
                    detail=href,
                    message="Sitemap hreflang URL is not a valid URL.",
                )
                continue
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                findings.add(
                    path=relative_path,
                    rule="aeo.sitemap_hreflang_not_absolute",
                    detail=href,
                    message="Sitemap hreflang URL must be absolute.",
                )
                continue
            hostname = url_hostname(parsed)
            if hostname not in SITE_HOSTS:
                findings.add(
                    path=relative_path,
                    rule="aeo.sitemap_hreflang_not_absolute",
                    detail=f"{href} (host={hostname})",
                    message="Sitemap hreflang URL must use the site host.",
                )
                continue
            target_route = route_from_url(href)
            if target_route is None:
                findings.add(
                    path=relative_path,
                    rule="aeo.sitemap_hreflang_url_invalid",
                    detail=href,
                    message="Sitemap hreflang URL is not a valid URL.",
                )
                continue
            if target_route in alias_routes:
                findings.add(
                    path=relative_path,
                    rule="aeo.sitemap_hreflang_target_missing",
                    detail=f"{href} (alias)",
                    message="Sitemap hreflang target is a redirect alias.",
                )
                continue
            if not html_target_path(public, target_route).exists():
                findings.add(
                    path=relative_path,
                    rule="aeo.sitemap_hreflang_target_missing",
                    detail=href,
                    message="Sitemap hreflang target does not resolve to a generated HTML page.",
                )

        for code, href in links:
            if code == "x-default":
                continue
            parsed = safe_urlsplit(href)
            if parsed is None or url_hostname(parsed) not in SITE_HOSTS:
                continue
            target_route = route_from_url(href)
            if (
                target_route is None
                or target_route == route
                or target_route not in entries_by_route
            ):
                continue
            target_entry = entries_by_route[target_route]
            if not any(
                route_from_url(back_href) == route
                for back_code, back_href in target_entry.links
                if back_code != "x-default"
            ):
                findings.add(
                    path=relative_path,
                    rule="aeo.sitemap_hreflang_not_reciprocal",
                    detail=target_route,
                    message="Sitemap hreflang target does not link back to this entry.",
                )

    for entry in sorted(
        entries, key=lambda item: (item.route, str(item.child_path), item.loc_url)
    ):
        route = entry.route
        if route not in pages:
            continue
        relative_path = sitemap_relative_path(public, entry.child_path)
        html_links = [
            (code, href)
            for code, href in html_alternates.get(route, [])
            if code != "x-default"
        ]
        sitemap_links = [
            (code, href) for code, href in entry.links if code != "x-default"
        ]
        html_codes = {code for code, _ in html_links}
        sitemap_codes = {code for code, _ in sitemap_links}
        if html_codes != sitemap_codes:
            findings.add(
                path=relative_path,
                rule="seo.hreflang_sitemap_mismatch",
                detail=f"codes html={sorted(html_codes)},sitemap={sorted(sitemap_codes)}",
                message="HTML and sitemap hreflang code sets differ.",
            )
            continue
        for code in sorted(html_codes & sitemap_codes):
            html_href = next(href for link_code, href in html_links if link_code == code)
            sitemap_href = next(
                href for link_code, href in sitemap_links if link_code == code
            )
            if route_from_url(html_href) != route_from_url(sitemap_href):
                findings.add(
                    path=relative_path,
                    rule="seo.hreflang_sitemap_mismatch",
                    detail=f"{code}:html={html_href},sitemap={sitemap_href}",
                    message="HTML and sitemap hreflang targets differ.",
                )


def validate_aeo_files(root: Path, base_url: str, findings: Findings) -> None:
    content_dir = root / "content" / "docs"
    english_slugs = sorted(
        path.stem
        for path in content_dir.glob("*.md")
        if not re.search(r"\.(de|es|pt|ja)\.md$", path.name)
    )
    llms_path = root / "static" / "llms.txt"
    if not llms_path.exists():
        findings.add(
            path="static/llms.txt",
            rule="aeo.llms_txt_missing",
            detail="llms.txt",
            message="llms.txt is missing.",
        )
    else:
        llms = read_text(llms_path)
        urls = set(re.findall(r"\((https://agent-engine-optimization\.com/docs/[^)]+)\)", llms))
        for slug in english_slugs:
            if slug == "_index":
                continue
            expected = f"{base_url.rstrip('/')}/docs/{slug}/"
            if expected not in urls:
                findings.add(
                    path="static/llms.txt",
                    rule="aeo.llms_txt_missing_article",
                    detail=expected,
                    message=f"English article is not listed: {slug}",
                )

    manifest_path = root / "static" / ".well-known" / "agent-manifest.json"
    if not manifest_path.exists():
        findings.add(
            path="static/.well-known/agent-manifest.json",
            rule="aeo.agent_manifest_missing",
            detail="agent-manifest.json",
            message="Agent manifest is missing.",
        )
        return
    try:
        manifest = json.loads(read_text(manifest_path))
    except json.JSONDecodeError as error:
        findings.add(
            path="static/.well-known/agent-manifest.json",
            rule="aeo.agent_manifest_invalid",
            detail=str(error),
            message="Agent manifest is not valid JSON.",
        )
        return

    languages = manifest.get("languages", [])
    if not isinstance(languages, list):
        languages = []
    for language in ("en", "es", "pt", "de", "ja"):
        if language not in languages:
            findings.add(
                path="static/.well-known/agent-manifest.json",
                rule="aeo.agent_manifest_language_missing",
                detail=language,
                message=f"Agent manifest does not list {language}.",
            )

    updated = manifest.get("updated")
    latest_content_date = None
    dates = []
    for path in content_dir.glob("*.md"):
        match = FRONT_DATE_RE.search(read_text(path))
        if match:
            dates.append(match.group(1))
    if dates:
        latest_content_date = max(dates)
    if updated and latest_content_date and str(updated) < latest_content_date:
        findings.add(
            path="static/.well-known/agent-manifest.json",
            rule="aeo.agent_manifest_updated_stale",
            detail=f"{updated}<{latest_content_date}",
            message="Agent manifest update date predates the newest content.",
        )

    for node in walk_json(manifest):
        url = node.get("url")
        if isinstance(url, str) and url.startswith("/"):
            findings.add(
                path="static/.well-known/agent-manifest.json",
                rule="aeo.agent_manifest_relative_url",
                detail=url,
                message="Manifest capability URLs must be absolute.",
            )


def validate(root: Path, public: Path) -> Findings:
    config_path = root / "config.toml"
    config = read_text(config_path)
    base_match = re.search(r'(?m)^\s*baseURL\s*=\s*"([^"]+)"', config)
    if not base_match:
        raise ValueError("baseURL is missing from config.toml")
    base_url = base_match.group(1)
    configured_image_match = re.search(
        r'(?ms)^\s*images\s*=\s*\[\s*"([^"]+)"', config
    )
    configured_image = configured_image_match.group(1) if configured_image_match else None
    configured_languages = re.findall(r"(?m)^\s*\[languages\.([a-z-]+)\]", config)
    language_codes = language_codes_from_config(config, configured_languages)

    html_files = sorted(public.rglob("*.html"))
    if not html_files:
        raise ValueError(f"No generated HTML files found under {public}")

    findings = Findings()
    pages: dict[str, tuple[Path, PageParser]] = {}
    not_found_pages: list[tuple[str, PageParser]] = []
    alias_routes: set[str] = set()
    page_descriptions: dict[str, str] = {}
    missing_assets: dict[str, set[str]] = defaultdict(set)
    article_dates = [
        match.group(1)
        for path in (root / "content" / "docs").glob("*.md")
        if (match := FRONT_DATE_RE.search(read_text(path)))
    ]
    article_max_date = max(article_dates) if article_dates else None

    for path in html_files:
        relative = path.relative_to(public).as_posix()
        parser = PageParser()
        parser.feed(read_text(path))
        if is_not_found_page(relative):
            not_found_pages.append((relative, parser))
            continue
        route = page_route(public, path)
        if route is None:
            continue
        if is_alias(parser):
            alias_routes.add(route)
            continue
        pages[route] = (path, parser)
        descriptions = [normalize_space(value) for value in meta_values(parser, "description")]
        page_descriptions[route] = next((value for value in descriptions if value), "")

    routes_by_group: dict[tuple[str, str], list[str]] = defaultdict(list)
    for route in pages:
        routes_by_group[translation_group_key(route)].append(route)

    expected_codes: dict[str, set[str]] = {}
    x_default_routes: dict[str, str] = {}
    for route in pages:
        group_routes = routes_by_group[translation_group_key(route)]
        expected_codes[route] = {
            expected_language_code(language_codes, page_language(member))
            for member in group_routes
        }
        x_default_routes[route] = expected_x_default(route, group_routes)

    for route, (path, parser) in sorted(pages.items()):
        check_page(
            route=route,
            path=path,
            parser=parser,
            base_url=base_url,
            public=public,
            root=root,
            findings=findings,
            page_descriptions=page_descriptions,
            missing_assets=missing_assets,
            article_max_date=article_max_date,
            configured_image=configured_image,
            language_codes=language_codes,
        )

    for relative, parser in sorted(not_found_pages):
        validate_not_found_page(
            relative_path=f"public/{relative}",
            route=f"/{relative}",
            parser=parser,
            base_url=base_url,
            public=public,
            findings=findings,
            missing_assets=missing_assets,
        )

    validate_hreflang(
        pages=pages,
        base_url=base_url,
        public=public,
        language_codes=language_codes,
        expected_codes=expected_codes,
        x_default_routes=x_default_routes,
        alias_routes=alias_routes,
        findings=findings,
    )
    validate_assets(
        public=public,
        root=root,
        base_url=base_url,
        configured_image=configured_image,
        missing_assets=missing_assets,
        findings=findings,
    )
    validate_sitemap(public, base_url, findings)
    validate_sitemap_hreflang(
        public=public,
        pages=pages,
        html_alternates={
            route: alternates(parser) for route, (_, parser) in pages.items()
        },
        alias_routes=alias_routes,
        language_codes=language_codes,
        findings=findings,
    )
    validate_aeo_files(root, base_url, findings)
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (default: parent of scripts/)",
    )
    parser.add_argument(
        "--public",
        type=Path,
        help="Generated site directory (default: <root>/public)",
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        help="Baseline JSON (default: <root>/validation/seo-baseline.json)",
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="Write the current findings to the baseline after checking for new debt.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow --update-baseline to bless new findings.",
    )
    parser.add_argument(
        "--max-details",
        type=int,
        default=20,
        help="Maximum new/fixed finding groups to print.",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    public = (args.public or root / "public").resolve()
    baseline_path = (args.baseline or root / "validation" / "seo-baseline.json").resolve()

    try:
        current = validate(root, public)
        _, baseline_entries = load_baseline(baseline_path)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    new, fixed = compare(current, baseline_entries)
    if args.update_baseline:
        if baseline_entries and new and not args.force:
            print_report(
                "SEO/AEO validation baseline update refused",
                current,
                baseline_entries,
                baseline_path,
                new,
                fixed,
                args.max_details,
            )
            print(
                "New findings must be reviewed or fixed before blessing the baseline. "
                "Use --force only after explicit review."
            )
            return 1
        payload = write_baseline(
            baseline_path,
            validator="seo",
            findings=current,
            root=root,
            metadata={"public_dir": "public"},
        )
        print(
            f"Wrote {baseline_path.as_posix()}: {payload['summary']['occurrences']} "
            f"occurrences, {payload['summary']['unique_findings']} unique findings."
        )
        return 0

    print_report(
        "SEO/AEO validation",
        current,
        baseline_entries,
        baseline_path,
        new,
        fixed,
        args.max_details,
    )
    if not baseline_entries:
        print(f"No baseline found. Create it with: --baseline {baseline_path.as_posix()} --update-baseline")
        return 1
    if new:
        print("FAIL: new SEO/AEO findings detected.")
        return 1
    if fixed:
        print("FAIL: baseline contains fixed findings; run --update-baseline to prune it.")
        return 1
    print("PASS: no new SEO/AEO findings; baseline is current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
