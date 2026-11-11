#!/usr/bin/env python3
"""Validate repository content structure and known language defects.

Usage:
    python scripts/validate_content.py
    python scripts/validate_content.py --update-baseline
    python scripts/validate_content.py --baseline validation/content-baseline.json

Exit codes:
    0  no new findings and the baseline is current
    1  new findings, stale baseline entries, or a missing baseline
    2  configuration or baseline format error
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from validation_common import Findings, compare, load_baseline, print_report, write_baseline


LANGUAGES = ("en", "es", "pt", "de", "ja")
TRANSLATIONS = ("es", "pt", "de", "ja")
LANGUAGE_SUFFIXES = {f".{language}.md": language for language in TRANSLATIONS}
SITE_HOSTS = {"agent-engine-optimization.com", "www.agent-engine-optimization.com"}
REQUIRED_FIELDS = ("title", "description", "date", "weight", "category")
FRONT_MATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.S)
FRONT_KEY_RE = re.compile(r"(?m)^([A-Za-z_][A-Za-z0-9_]*)\s*:")
FIELD_RE_TEMPLATE = r'(?m)^{key}:\s*"?(.*?)"?\s*$'
VALID_LINK_RE = re.compile(r"\]\(\s*(?:<([^>\s]+)>|([^)\s]+))")
BROKEN_LINK_RE = re.compile(r"\]\s+\(\s*(?:<([^>\s]+)>|([^)\s]+))")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_NO_SPACE_RE = re.compile(r"^ {0,3}#{1,6}[^\s#]")
HEADING_AFTER_RULE_RE = re.compile(r"^ {0,3}-{3,}\s*#{1,6}\s*")
SEPARATOR_ONLY_RE = re.compile(r"^\s*\|?[\s:|-]+\|?\s*$")
GLUED_SEPARATOR_RE = re.compile(r"^\s*-{3,}\s*\|\s*\|")
VALID_SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
UNKNOWN_LANGUAGE_SUFFIX_RE = re.compile(r"\.[a-z]{2}(?:-[A-Za-z]{2})?\.md$")


def language_for(path: Path) -> str:
    for suffix, language in LANGUAGE_SUFFIXES.items():
        if path.name.endswith(suffix):
            return language
    return "en"


def slug_for(path: Path) -> str:
    name = path.name
    for suffix in LANGUAGE_SUFFIXES:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name[:-3] if name.endswith(".md") else name


def relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def field_value(front_matter: str, key: str) -> str:
    match = re.search(FIELD_RE_TEMPLATE.format(key=re.escape(key)), front_matter)
    if not match:
        return ""
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def parse_front_matter(text: str) -> tuple[str, str, int] | None:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None
    body_start = match.end()
    body_line = text[:body_start].count("\n") + 1
    return match.group(1), text[body_start:], body_line


def visible_lines(body: str, first_line: int) -> list[tuple[int, str]]:
    """Return non-fenced lines with their original line numbers."""
    result: list[tuple[int, str]] = []
    in_fence = False
    for offset, line in enumerate(body.splitlines()):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            result.append((first_line + offset, line))
    return result


def mask_inline_code(line: str) -> str:
    return INLINE_CODE_RE.sub(lambda match: " " * len(match.group(0)), line)


def target_from_match(match: re.Match[str]) -> str:
    return (match.group(1) or match.group(2) or "").strip()


def normalize_internal_target(target: str) -> str | None:
    """Return the normalized path for same-site links, otherwise None."""
    target = target.strip()
    if not target:
        return None
    parsed = urlsplit(target)
    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc and parsed.hostname not in SITE_HOSTS:
        return None
    if not parsed.netloc and not target.startswith("/"):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    return path


def split_table_cells(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    if not value.strip():
        return []
    return [cell.strip() for cell in value.split("|")]


def is_separator_candidate(line: str) -> bool:
    if not SEPARATOR_ONLY_RE.fullmatch(line):
        return False
    return "-" in line or line.strip() == "|"


def scan_tables(lines: list[tuple[int, str]], findings: Findings, path: str) -> None:
    index = 0
    while index < len(lines) - 1:
        header_line_number, header = lines[index]
        next_line = lines[index + 1][1]
        if "|" not in header or not is_separator_candidate(next_line):
            index += 1
            continue

        header_cells = split_table_cells(header)
        separator_block: list[tuple[int, str]] = []
        cursor = index + 1
        while cursor < len(lines) and is_separator_candidate(lines[cursor][1]):
            separator_block.append(lines[cursor])
            cursor += 1

        if not separator_block:
            index += 1
            continue

        expected_columns = len(header_cells)
        for line_number, separator in separator_block:
            cells = split_table_cells(separator)
            valid = (
                expected_columns > 0
                and len(cells) == expected_columns
                and all(VALID_SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)
            )
            if valid:
                continue
            if separator.strip() == "|":
                rule = "markdown.table_separator_empty"
                message = "Lone pipe where a table separator is required."
            else:
                rule = "markdown.table_separator"
                message = "Malformed Markdown table separator."
            findings.add(
                path=path,
                rule=rule,
                detail=separator.strip(),
                line=line_number,
                message=message,
            )
        index = max(cursor, index + 1)


def scan_body(
    path: str,
    language: str,
    lines: list[tuple[int, str]],
    findings: Findings,
    docs_root: Path,
) -> None:
    for line_number, raw_line in lines:
        line = mask_inline_code(raw_line)

        if GLUED_SEPARATOR_RE.match(raw_line):
            findings.add(
                path=path,
                rule="markdown.table_separator_glued",
                detail=raw_line.strip(),
                line=line_number,
                message="Table separator and first row are glued onto one line.",
            )

        if language in {"de", "pt", "ja"}:
            for match in VALID_LINK_RE.finditer(line):
                target = target_from_match(match)
                normalized = normalize_internal_target(target)
                if normalized and normalized.startswith("/es/docs/"):
                    findings.add(
                        path=path,
                        rule="link.spanish_in_translation",
                        detail=normalized,
                        line=line_number,
                        message="Translation links to the Spanish documentation.",
                    )

        for match in BROKEN_LINK_RE.finditer(line):
            target = target_from_match(match)
            if not target.startswith(("/", "http://", "https://", "#")):
                continue
            findings.add(
                path=path,
                rule="link.broken_space",
                detail=target,
                line=line_number,
                message="Markdown link has whitespace between label and target.",
            )
            if language in {"de", "pt", "ja"}:
                normalized = normalize_internal_target(target)
                if normalized and normalized.startswith("/es/docs/"):
                    findings.add(
                        path=path,
                        rule="link.spanish_in_translation",
                        detail=normalized,
                        line=line_number,
                        message="Broken translation link points to Spanish documentation.",
                    )

        for match in VALID_LINK_RE.finditer(line):
            target = target_from_match(match)
            normalized = normalize_internal_target(target)
            if normalized:
                check_internal_target(normalized, path, line_number, findings, docs_root)

        if HEADING_AFTER_RULE_RE.match(raw_line):
            findings.add(
                path=path,
                rule="markdown.heading_after_rule",
                detail=raw_line.strip(),
                line=line_number,
                message="Heading is glued to a horizontal rule.",
            )
        elif HEADING_NO_SPACE_RE.match(raw_line):
            findings.add(
                path=path,
                rule="markdown.heading_no_space",
                detail=raw_line.strip(),
                line=line_number,
                message="Heading marker is missing a space.",
            )


def check_internal_target(
    normalized: str,
    path: str,
    line_number: int,
    findings: Findings,
    docs_root: Path,
) -> None:
    match = re.fullmatch(r"/(?:(en|es|pt|de|ja)/)?docs/([^/]+)/?", normalized)
    if not match:
        return
    explicit_language, slug = match.groups()
    if explicit_language == "en":
        findings.add(
            path=path,
            rule="link.explicit_en_prefix",
            detail=normalized,
            line=line_number,
            message="/en/docs/ is not served as a canonical route (404).",
        )
        return
    language = explicit_language or "en"
    expected = docs_root / (f"{slug}.md" if language == "en" else f"{slug}.{language}.md")
    if expected.exists():
        return
    findings.add(
        path=path,
        rule="link.internal_target_missing",
        detail=normalized,
        line=line_number,
        message=f"Target file does not exist: {expected.name}",
    )


def validate(root: Path) -> Findings:
    docs_root = root / "content" / "docs"
    findings = Findings()
    if not docs_root.is_dir():
        raise FileNotFoundError(f"Missing content directory: {docs_root}")

    files = sorted(docs_root.glob("*.md"))
    records: list[dict] = []
    by_slug: dict[str, dict[str, dict]] = {}

    for path in files:
        relative_path = relative(root, path)
        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            findings.add(
                path=relative_path,
                rule="encoding.bom",
                detail="utf-8-bom",
                message="UTF-8 BOM is not allowed.",
            )
            data = data[3:]
        try:
            text = data.decode("utf-8", errors="strict")
        except UnicodeDecodeError as error:
            findings.add(
                path=relative_path,
                rule="encoding.invalid_utf8",
                detail=f"byte-{error.start}",
                message=str(error),
            )
            continue
        if "\ufffd" in text:
            findings.add(
                path=relative_path,
                rule="encoding.replacement_character",
                detail="U+FFFD",
                message="Replacement character found in source.",
            )

        language = language_for(path)
        slug = slug_for(path)
        if not any(path.name.endswith(suffix) for suffix in LANGUAGE_SUFFIXES):
            if UNKNOWN_LANGUAGE_SUFFIX_RE.search(path.name):
                findings.add(
                    path=relative_path,
                    rule="file.unknown_language_suffix",
                    detail=path.name.rsplit(".", 2)[-2],
                    message="Unrecognized language suffix.",
                )

        parsed = parse_front_matter(text)
        if parsed is None:
            findings.add(
                path=relative_path,
                rule="front_matter.missing",
                detail="front-matter",
                line=1,
                message="YAML front matter is missing or malformed.",
            )
            records.append({"path": relative_path, "language": language, "slug": slug})
            continue
        front_matter, body, body_line = parsed

        keys = [match.group(1) for match in FRONT_KEY_RE.finditer(front_matter)]
        for key, count in ((key, keys.count(key)) for key in set(keys)):
            if count > 1:
                findings.add(
                    path=relative_path,
                    rule="front_matter.duplicate_key",
                    detail=key,
                    line=body_line,
                    message=f"Front matter key appears {count} times.",
                )

        values = {key: field_value(front_matter, key) for key in REQUIRED_FIELDS}
        values["metaDescription"] = field_value(front_matter, "metaDescription")
        values["metaTitle"] = field_value(front_matter, "metaTitle")
        values["summary"] = field_value(front_matter, "summary")
        values["lastmod"] = field_value(front_matter, "lastmod")

        for key in REQUIRED_FIELDS:
            if not values[key]:
                findings.add(
                    path=relative_path,
                    rule="front_matter.missing_field",
                    detail=key,
                    line=1,
                    message=f"Required front matter field missing: {key}",
                )
        if values["date"] and not DATE_RE.fullmatch(values["date"]):
            findings.add(
                path=relative_path,
                rule="front_matter.invalid_date",
                detail=values["date"],
                line=1,
                message="Date must use YYYY-MM-DD.",
            )
        if values["weight"] and not values["weight"].isdigit():
            findings.add(
                path=relative_path,
                rule="front_matter.invalid_weight",
                detail=values["weight"],
                line=1,
                message="Weight must be an integer.",
            )

        lines = visible_lines(body, body_line)
        scan_tables(lines, findings, relative_path)
        scan_body(relative_path, language, lines, findings, docs_root)

        record = {
            "path": relative_path,
            "language": language,
            "slug": slug,
            "weight": values["weight"],
            "metaDescription": values["metaDescription"],
            "description": values["description"],
        }
        records.append(record)
        by_slug.setdefault(slug, {})[language] = record

    for slug, translations in sorted(by_slug.items()):
        for language in LANGUAGES:
            if language in translations:
                continue
            filename = f"{slug}.md" if language == "en" else f"{slug}.{language}.md"
            findings.add(
                path=f"content/docs/{filename}",
                rule="translation.missing",
                detail=language,
                message=f"Missing {language} version for slug '{slug}'.",
            )

    for slug, translations in sorted(by_slug.items()):
        spanish = translations.get("es", {})
        spanish_meta = " ".join(spanish.get("metaDescription", "").split())
        spanish_description = " ".join(spanish.get("description", "").split())
        for language in ("de", "pt", "ja"):
            translation = translations.get(language)
            if not translation:
                continue
            translated_meta = " ".join(translation.get("metaDescription", "").split())
            if translated_meta and spanish_meta and translated_meta == spanish_meta:
                findings.add(
                    path=translation["path"],
                    rule="metadata.meta_description_from_spanish",
                    detail=translated_meta,
                    message="Localized metaDescription is identical to Spanish.",
                )
            translated_description = " ".join(translation.get("description", "").split())
            if (
                translated_description
                and spanish_description
                and translated_description == spanish_description
            ):
                findings.add(
                    path=translation["path"],
                    rule="metadata.description_from_spanish",
                    detail=translated_description,
                    message="Localized description is identical to Spanish.",
                )

    weights: dict[str, dict[str, list[str]]] = {language: {} for language in LANGUAGES}
    for record in records:
        weight = record.get("weight", "")
        if weight:
            weights[record["language"]].setdefault(weight, []).append(record["path"])
    for language, values in weights.items():
        for weight, paths in values.items():
            if len(paths) < 2:
                continue
            for path in paths:
                findings.add(
                    path=path,
                    rule="weight.duplicate",
                    detail=weight,
                    message=f"Weight {weight} is used by {len(paths)} {language} files.",
                )

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
        "--baseline",
        type=Path,
        help="Baseline JSON (default: <root>/validation/content-baseline.json)",
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
    baseline_path = (args.baseline or root / "validation" / "content-baseline.json").resolve()

    try:
        current = validate(root)
        _, baseline_entries = load_baseline(baseline_path)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    new, fixed = compare(current, baseline_entries)

    if args.update_baseline:
        if baseline_entries and new and not args.force:
            print_report(
                "Content validation baseline update refused",
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
            validator="content",
            findings=current,
            root=root,
        )
        print(
            f"Wrote {baseline_path.as_posix()}: {payload['summary']['occurrences']} "
            f"occurrences, {payload['summary']['unique_findings']} unique findings."
        )
        return 0

    print_report(
        "Content validation",
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
        print("FAIL: new content findings detected.")
        return 1
    if fixed:
        print("FAIL: baseline contains fixed findings; run --update-baseline to prune it.")
        return 1
    print("PASS: no new content findings; baseline is current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
