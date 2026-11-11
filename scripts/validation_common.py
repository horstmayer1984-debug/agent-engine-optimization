#!/usr/bin/env python3
"""Shared helpers for the repository validators.

The baseline is intentionally finding-based, never file-based.  A baseline
entry is identified by (path, rule, detail) and stores an occurrence count.
Adding one more occurrence of a known issue therefore fails validation, while
removing an occurrence is reported as fixed debt.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
from typing import Iterable


BASELINE_SCHEMA_VERSION = 1


@dataclass
class Occurrence:
    path: str
    rule: str
    detail: str
    line: int | None = None
    message: str = ""


@dataclass
class FindingGroup:
    path: str
    rule: str
    detail: str
    count: int = 0
    lines: list[int] = field(default_factory=list)
    message: str = ""

    def as_baseline_entry(self) -> dict:
        return {
            "path": self.path,
            "rule": self.rule,
            "detail": self.detail,
            "count": self.count,
            "lines": sorted(set(self.lines)),
            "message": self.message,
        }


class Findings:
    def __init__(self) -> None:
        self._groups: dict[tuple[str, str, str], FindingGroup] = {}

    def add(
        self,
        path: str,
        rule: str,
        detail: str = "",
        line: int | None = None,
        message: str = "",
    ) -> None:
        key = (path, rule, detail)
        group = self._groups.get(key)
        if group is None:
            group = FindingGroup(path=path, rule=rule, detail=detail, message=message)
            self._groups[key] = group
        group.count += 1
        if line is not None:
            group.lines.append(line)
        if message and not group.message:
            group.message = message

    def groups(self) -> list[FindingGroup]:
        return sorted(
            self._groups.values(),
            key=lambda item: (item.path, item.rule, item.detail),
        )

    @property
    def occurrence_count(self) -> int:
        return sum(group.count for group in self._groups.values())

    @property
    def unique_count(self) -> int:
        return len(self._groups)

    @property
    def file_count(self) -> int:
        return len({group.path for group in self._groups.values()})

    def by_rule(self) -> dict[str, tuple[int, int]]:
        """Return rule -> (unique keys, occurrence count)."""
        keys: Counter[str] = Counter()
        occurrences: Counter[str] = Counter()
        for group in self._groups.values():
            keys[group.rule] += 1
            occurrences[group.rule] += group.count
        return {rule: (keys[rule], occurrences[rule]) for rule in sorted(keys)}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def source_commit(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return result.stdout.strip()


def load_baseline(path: Path) -> tuple[dict, dict]:
    if not path.exists():
        return {}, {}
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if payload.get("schema_version") != BASELINE_SCHEMA_VERSION:
        raise ValueError(
            f"Unsupported baseline schema in {path}: {payload.get('schema_version')!r}"
        )
    entries: dict[tuple[str, str, str], dict] = {}
    for entry in payload.get("findings", []):
        key = (entry["path"], entry["rule"], entry["detail"])
        if key in entries:
            raise ValueError(f"Duplicate baseline entry in {path}: {key!r}")
        entries[key] = entry
    return payload, entries


def write_baseline(
    path: Path,
    validator: str,
    findings: Findings,
    root: Path,
    metadata: dict | None = None,
) -> dict:
    payload = {
        "schema_version": BASELINE_SCHEMA_VERSION,
        "validator": validator,
        "generated_at": utc_now(),
        "source_commit": source_commit(root),
        "summary": {
            "occurrences": findings.occurrence_count,
            "unique_findings": findings.unique_count,
            "files": findings.file_count,
            "by_rule": {
                rule: {"unique": unique, "occurrences": occurrences}
                for rule, (unique, occurrences) in findings.by_rule().items()
            },
        },
        "findings": [group.as_baseline_entry() for group in findings.groups()],
    }
    if metadata:
        payload.update(metadata)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    temporary.replace(path)
    return payload


def compare(
    current: Findings,
    baseline_entries: dict[tuple[str, str, str], dict],
) -> tuple[list[tuple[FindingGroup, int]], list[tuple[str, str, str, int]]]:
    """Return new groups and fixed (path, rule, detail, count) tuples."""
    new: list[tuple[FindingGroup, int]] = []
    current_keys = {(group.path, group.rule, group.detail) for group in current.groups()}
    for group in current.groups():
        key = (group.path, group.rule, group.detail)
        old_count = int(baseline_entries.get(key, {}).get("count", 0))
        if group.count > old_count:
            new.append((group, group.count - old_count))

    fixed: list[tuple[str, str, str, int]] = []
    for key, entry in baseline_entries.items():
        if key not in current_keys:
            fixed.append((*key, int(entry.get("count", 0))))
            continue
        current_count = next(
            group.count
            for group in current.groups()
            if (group.path, group.rule, group.detail) == key
        )
        old_count = int(entry.get("count", 0))
        if current_count < old_count:
            fixed.append((*key, old_count - current_count))
    return new, fixed


def print_report(
    title: str,
    current: Findings,
    baseline_entries: dict[tuple[str, str, str], dict],
    baseline_path: Path,
    new: list[tuple[FindingGroup, int]],
    fixed: list[tuple[str, str, str, int]],
    max_details: int = 20,
) -> None:
    baseline_occurrences = sum(
        int(entry.get("count", 0)) for entry in baseline_entries.values()
    )
    new_occurrences = sum(delta for _, delta in new)
    fixed_occurrences = sum(delta for *_, delta in fixed)

    print(title)
    print(
        f"  Current: {current.occurrence_count} occurrences, "
        f"{current.unique_count} unique findings, {current.file_count} files"
    )
    print(
        f"  Baseline ({baseline_path.as_posix()}): {baseline_occurrences} occurrences, "
        f"{len(baseline_entries)} unique findings"
    )
    print(f"  New: {new_occurrences} occurrences in {len(new)} finding groups")
    print(f"  Fixed since baseline: {fixed_occurrences} occurrences in {len(fixed)} groups")

    if current.by_rule():
        print("  Current by rule:")
        for rule, (unique, occurrences) in current.by_rule().items():
            print(f"    {rule}: {occurrences} occurrences ({unique} unique)")

    if new:
        print("  NEW FINDINGS (validation fails):")
        for group, delta in new[:max_details]:
            location = group.path
            if group.lines:
                location += ":" + ",".join(str(line) for line in sorted(set(group.lines))[:5])
            print(f"    +{delta} {location} [{group.rule}] {group.detail}")
        if len(new) > max_details:
            print(f"    ... {len(new) - max_details} more new finding groups")

    if fixed and len(fixed) <= max_details:
        print("  FIXED FINDINGS (prune baseline with --update-baseline):")
        for path, rule, detail, delta in fixed:
            print(f"    -{delta} {path} [{rule}] {detail}")
    elif fixed:
        print(
            "  FIXED FINDINGS: "
            f"{len(fixed)} groups; run with --update-baseline to prune."
        )


def output_status(new: list, fixed: list) -> int:
    if new:
        return 1
    if fixed:
        return 1
    return 0


def iter_files(path: Path, suffix: str) -> Iterable[Path]:
    yield from sorted(path.rglob(f"*{suffix}"))
