#!/usr/bin/env python3
"""Inspect or import project .mde/outbox records into central MDE ledgers.

This is intentionally conservative:
- reads portfolio/PROJECTS.yaml
- checks sibling repo paths from repo_or_path
- dry-runs by default
- with --write, imports JSONL records only when an id-like field is not already present
- preserves source records as-is
- prints a human summary
"""

from __future__ import annotations

import json
import hashlib
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - graceful local fallback
    yaml = None


ROOT = Path(__file__).resolve().parents[1]

OUTBOX_TO_LEDGER = {
    "events.jsonl": ROOT / "ledger" / "events.jsonl",
    "lessons.jsonl": ROOT / "ledger" / "lessons.jsonl",
    "content-seeds.jsonl": ROOT / "ledger" / "content-seeds.jsonl",
    "skill-update-candidates.jsonl": ROOT / "ledger" / "skill-update-candidates.jsonl",
}

ID_FIELDS = [
    "event_id",
    "lesson_id",
    "content_id",
    "content_seed_id",
    "seed_id",
    "candidate_id",
    "issue_signature",
    "impact_id",
]

PROJECT_FIELDS = ["project_id", "project", "source_project"]
TIME_FIELDS = ["timestamp", "occurred_at", "created_at", "recorded_at", "date"]
TYPE_FIELDS = ["event_type", "type", "lesson_type"]


def load_projects() -> list[dict]:
    path = ROOT / "portfolio" / "PROJECTS.yaml"
    if not path.exists():
        print("Missing portfolio/PROJECTS.yaml; run manual audit.", file=sys.stderr)
        return []
    if yaml is None:
        print("PyYAML is unavailable; using limited PROJECTS.yaml parser.", file=sys.stderr)
        projects: list[dict] = []
        current: dict | None = None
        for raw in path.read_text().splitlines():
            line = raw.strip()
            if line.startswith("- id:"):
                if current:
                    projects.append(current)
                current = {"id": line.split(":", 1)[1].strip().strip('"')}
            elif current is not None and line.startswith("repo_or_path:"):
                current["repo_or_path"] = line.split(":", 1)[1].strip().strip('"')
        if current:
            projects.append(current)
        return projects
    data = yaml.safe_load(path.read_text()) or {}
    return list(data.get("projects", []))


def sibling_outboxes_outside_portfolio(projects: list[dict]) -> list[str]:
    portfolio_paths = {
        (ROOT / project["repo_or_path"]).resolve()
        for project in projects
        if project.get("repo_or_path") and project.get("repo_or_path") != "."
    }
    outside: list[str] = []
    for sibling in ROOT.parent.iterdir():
        if not sibling.is_dir() or sibling.resolve() in portfolio_paths:
            continue
        if (sibling / ".mde" / "outbox").exists():
            outside.append(sibling.name)
    return sorted(outside)


def read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    if not path.exists():
        return records
    for line_no, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            print(f"Skipping invalid JSONL {path}:{line_no}: {exc}", file=sys.stderr)
    return records


def record_key(record: dict) -> str | None:
    for field in ID_FIELDS:
        value = record.get(field)
        if value:
            return f"{field}:{value}"

    project = next((str(record.get(field)) for field in PROJECT_FIELDS if record.get(field)), "")
    time = next((str(record.get(field)) for field in TIME_FIELDS if record.get(field)), "")
    record_type = next((str(record.get(field)) for field in TYPE_FIELDS if record.get(field)), "")
    summary = str(record.get("summary") or record.get("core_insight") or "")
    if project and summary:
        return f"composite:{project}:{time}:{record_type}:{summary}"

    canonical = json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return f"sha256:{hashlib.sha256(canonical.encode('utf-8')).hexdigest()}"


def existing_keys(path: Path) -> set[str]:
    return {key for key in (record_key(r) for r in read_jsonl(path)) if key}


def append_records(dest: Path, records: list[dict]) -> int:
    dest.parent.mkdir(parents=True, exist_ok=True)
    seen = existing_keys(dest)
    imported = 0
    with dest.open("a", encoding="utf-8") as handle:
        for record in records:
            key = record_key(record)
            if key and key in seen:
                continue
            handle.write(json.dumps(record, separators=(",", ":"), ensure_ascii=False) + "\n")
            if key:
                seen.add(key)
            imported += 1
    return imported


def importable_record_count(dest: Path, records: list[dict]) -> int:
    seen = existing_keys(dest)
    importable = 0
    for record in records:
        key = record_key(record)
        if key in seen:
            continue
        seen.add(key)
        importable += 1
    return importable


def main() -> int:
    write = "--write" in sys.argv[1:]
    projects = load_projects()
    outside_portfolio = sibling_outboxes_outside_portfolio(projects)
    checked = 0
    imported_total = 0
    missing_outboxes: list[str] = []

    for project in projects:
        repo = project.get("repo_or_path")
        project_id = project.get("id", repo)
        if not repo or repo == ".":
            continue
        outbox = (ROOT / repo / ".mde" / "outbox").resolve()
        checked += 1
        if not outbox.exists():
            missing_outboxes.append(str(project_id))
            continue
        for outbox_name, ledger_path in OUTBOX_TO_LEDGER.items():
            records = read_jsonl(outbox / outbox_name)
            if not records:
                continue
            if write:
                imported_total += append_records(ledger_path, records)
            else:
                imported_total += importable_record_count(ledger_path, records)

    print("MDE Outbox Import Summary")
    print(f"Projects checked: {checked}")
    print(f"Mode: {'write' if write else 'dry-run'}")
    print(f"Records {'imported' if write else 'available to import'}: {imported_total}")
    print(f"Projects without accessible outbox: {', '.join(missing_outboxes) if missing_outboxes else 'none'}")
    print(
        "Sibling outboxes outside portfolio: "
        f"{', '.join(outside_portfolio) if outside_portfolio else 'none'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
