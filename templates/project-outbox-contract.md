# Project Outbox Contract

Every MDE-enabled project should eventually have:

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

Minimal adoption requires:

```text
.mde/project.json
.mde/outbox/events.jsonl
.mde/lessons-local.jsonl
```

Already-MDE projects should not be migrated again. They should add only missing outbox/sync artifacts.

Project outbox files are local write targets. Central `mde` imports central-worthy records during regular learning audits or explicit import sessions.

