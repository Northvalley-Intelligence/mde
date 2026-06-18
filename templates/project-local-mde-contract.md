# Project-Local MDE Contract

Each project using MDE should eventually have:

```text
.mde/
  project.json
  validation-strategy.json
  generations/
  validation-runs/
  findings.json
  lessons-local.jsonl
  outbox/
    events.jsonl
    lessons.jsonl
    impacts.jsonl
    content-seeds.jsonl
    skill-update-candidates.jsonl
    portfolio-sync.json
```

Recommended where appropriate:

```text
MISSION.md
MISSION_UPDATES.md
```

Minimal adoption for an existing project only requires:

```text
.mde/project.json
.mde/outbox/events.jsonl
.mde/lessons-local.jsonl
```

Do not require full MDE validation or generation structure before normal project work can continue.

For projects that already use MDE, the minimum central sync addition is:

```text
.mde/outbox/
  portfolio-sync.json
  events.jsonl
  lessons.jsonl
  impacts.jsonl
  content-seeds.jsonl
  skill-update-candidates.jsonl
```

`portfolio-sync.json` should include:

```json
{
  "project_id": "",
  "project_name": "",
  "mde_status": "active | partial | migrated | not_started",
  "artifact_profiles": [],
  "context_packs": [],
  "validation_strategy_status": "missing | draft | active | needs_update",
  "latest_generation": "",
  "latest_validation_gate_result": "unknown | pass | fail",
  "upstream_dependencies": [],
  "downstream_dependencies": [],
  "last_sync_note": ""
}
```

Each project-local event that has cross-repo impact should be copied or promoted into:

```text
mde/ledger/events.jsonl
```

Project-local outbox records are written by project Codex windows. Central `mde` imports them using `prompts/central-import-project-outbox.prompt.md`.

Already-MDE projects should not be migrated again. They should only add missing outbox/sync artifacts.

Client-owned candidate repos must not include central private MDE ledgers, cross-client lessons, private content seeds, or confidential internal notes.
