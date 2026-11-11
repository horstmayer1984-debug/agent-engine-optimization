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
SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
DOCS_RE = re.compile(r"^/(?:(?P<lang>de|es|pt|ja)/)?docs/(?P<slug>[^/]+)/?$")
FRONT_DATE_RE = re.compile(r"(?m)^date:\s*[\"']?(\d{4}-\d{2}-\d{2})")


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
    if relative == "404.html" or relative.endswith("/404.html"):
        return None
    if relative.endswith(".html"):
        return "/" + relative
    return None


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
    return value.strip().lower().split("-")[0]


def url_for_route(base_url: str, route: str) -> str:
    return base_url.rstrip("/") + route


def route_for_docs(language: str, slug: str) -> str:
    return f"/docs/{slug}/" if language == "en" else f"/{language}/docs/{slug}/"


def expected_route_languages(route: str) -> bool:
    return (
        route == "/"
        or route in {"/docs/", "/es/docs/", "/pt/docs/", "/de/docs/", "/ja/docs/"}
        or bool(DOCS_RE.match(route))
    )


def page_language(route: str) -> str:
    if route == "/":
        return "en"
    first = route.strip("/").split("/", 1)[0]
    return first if first in {"es", "pt", "de", "ja"} else "en"


def is_alias(parser: PageParser) -> bool:
    return any(
        meta.get("http-equiv", "").lower() == "refresh" for meta in parser.metas
    )


def resolve_local_url(public: Path, url: str) -> Path | None:
    parsed = urlsplit(url)
    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc and parsed.hostname not in SITE_HOSTS:
        return None
    path = unquote(parsed.path)
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
    configured_languages: list[str],
    public: Path,
    root: Path,
    findings: Findings,
    page_descriptions: dict[str, str],
    missing_assets: dict[str, set[str]],
    article_max_date: str | None,
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
        if urlsplit(actual).path != urlsplit(expected).path:
            findings.add(
                path=relative_path,
                rule="seo.canonical_not_self",
                detail=actual,
                message=f"Canonical does not point to {expected}.",
            )

    html_lang = parser.html_attrs.get("lang", "").strip().lower()
    if not html_lang:
        findings.add(
            path=relative_path,
            rule="seo.html_lang_missing",
            detail=route,
            message="The html element has no lang attribute.",
        )
    elif normalize_language(html_lang) != language:
        findings.add(
            path=relative_path,
            rule="seo.html_lang_wrong",
            detail=f"expected={language},actual={html_lang}",
            message="The html lang attribute does not match the page language.",
        )

    hreflang_values = alternates(parser)
    languages = {normalize_language(value) for value, _ in hreflang_values}
    if not hreflang_values:
        findings.add(
            path=relative_path,
            rule="seo.hreflang_missing",
            detail=route,
            message="No alternate hreflang links were rendered.",
        )
    else:
        if language not in languages:
            findings.add(
                path=relative_path,
                rule="seo.hreflang_self_missing",
                detail=language,
                message="The page does not declare its own language as hreflang.",
            )
        if expected_route_languages(route):
            for expected_language in configured_languages:
                if expected_language not in languages:
                    findings.add(
                        path=relative_path,
                        rule="seo.hreflang_incomplete",
                        detail=expected_language,
                        message=f"Missing hreflang for {expected_language}.",
                    )
        if "x-default" not in languages:
            findings.add(
                path=relative_path,
                rule="seo.hreflang_x_default_missing",
                detail=route,
                message="No x-default hreflang was rendered.",
            )
        duplicates = sorted(
            value for value, count in Counter(languages).items() if count > 1
        )
        for value in duplicates:
            findings.add(
                path=relative_path,
                rule="seo.hreflang_duplicate",
                detail=value,
                message=f"Duplicate hreflang value: {value}",
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

    og_images = [value for value in meta_values(parser, "og:image", "property") if value]
    if not og_images:
        findings.add(
            path=relative_path,
            rule="seo.og_image_missing",
            detail=route,
            message="Open Graph image is missing.",
        )
    for image_url in og_images:
        if not urlsplit(image_url).netloc:
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
            if normalize_language(in_language) != language:
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


def validate_assets(
    public: Path,
    root: Path,
    base_url: str,
    configured_image: str | None,
    missing_assets: dict[str, set[str]],
    findings: Findings,
) -> None:
    for image_url, pages in sorted(missing_assets.items()):
        parsed = urlsplit(image_url)
        findings.add(
            path="public" + parsed.path,
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

    child_locs = [loc.text.strip() for loc in root.findall("sm:sitemap/sm:loc", SITEMAP_NS) if loc.text]
    for child_url in child_locs:
        child_path = public / unquote(urlsplit(child_url).path).lstrip("/")
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
                path=f"public/{child_path.relative_to(public).as_posix()}",
                rule="aeo.sitemap_invalid",
                detail=str(error),
                message="Child sitemap is not valid XML.",
            )
            continue
        for loc in child.findall("sm:url/sm:loc", SITEMAP_NS):
            if not loc.text:
                continue
            url = loc.text.strip()
            path = unquote(urlsplit(url).path)
            target = public / ("index.html" if path == "/" else path.lstrip("/") + "index.html")
            if path.endswith(".html"):
                target = public / path.lstrip("/")
            if not target.exists():
                findings.add(
                    path=f"public/{child_path.relative_to(public).as_posix()}",
                    rule="aeo.sitemap_url_missing_page",
                    detail=url,
                    message="Sitemap URL does not resolve to a generated HTML page.",
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

    html_files = sorted(public.rglob("*.html"))
    if not html_files:
        raise ValueError(f"No generated HTML files found under {public}")

    findings = Findings()
    pages: dict[str, tuple[Path, PageParser]] = {}
    page_descriptions: dict[str, str] = {}
    missing_assets: dict[str, set[str]] = defaultdict(set)
    article_dates = [
        match.group(1)
        for path in (root / "content" / "docs").glob("*.md")
        if (match := FRONT_DATE_RE.search(read_text(path)))
    ]
    article_max_date = max(article_dates) if article_dates else None

    for path in html_files:
        route = page_route(public, path)
        if route is None:
            continue
        parser = PageParser()
        parser.feed(read_text(path))
        if is_alias(parser):
            continue
        pages[route] = (path, parser)
        descriptions = [normalize_space(value) for value in meta_values(parser, "description")]
        page_descriptions[route] = next((value for value in descriptions if value), "")

    for route, (path, parser) in sorted(pages.items()):
        check_page(
            route=route,
            path=path,
            parser=parser,
            base_url=base_url,
            configured_languages=configured_languages,
            public=public,
            root=root,
            findings=findings,
            page_descriptions=page_descriptions,
            missing_assets=missing_assets,
            article_max_date=article_max_date,
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
