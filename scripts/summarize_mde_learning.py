#!/usr/bin/env python3
"""Summarize central MDE learning ledgers."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return records


def main() -> int:
    ledgers = {
        "events": ROOT / "ledger" / "events.jsonl",
        "lessons": ROOT / "ledger" / "lessons.jsonl",
        "content_seeds": ROOT / "ledger" / "content-seeds.jsonl",
        "skill_candidates": ROOT / "ledger" / "skill-update-candidates.jsonl",
        "issue_signatures": ROOT / "ledger" / "issue-signatures.jsonl",
    }

    print("MDE Learning Summary")
    for name, path in ledgers.items():
        records = read_jsonl(path)
        print(f"{name}: {len(records)}")

    candidates = read_jsonl(ledgers["skill_candidates"])
    open_candidates = [c for c in candidates if c.get("status") in {None, "candidate"}]
    print(f"open_skill_candidates: {len(open_candidates)}")

    signatures = read_jsonl(ledgers["issue_signatures"])
    print("issue_signature_examples:")
    for record in signatures[:10]:
        print(f"- {record.get('issue_signature', 'unknown')}: {record.get('summary', '')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

