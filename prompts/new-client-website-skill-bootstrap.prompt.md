# New Client Website Skill Bootstrap Prompt

You are starting a brand-new client website repo or folder using MDE.

Do not copy old client website code blindly.
Do not expose private central MDE ledgers, cross-client lessons, internal content seeds, or confidential strategy notes in a client-owned candidate repo.

Use skill-driven Generation 0 before implementation.

Tasks:

1. Identify the client and business context.
2. Load current central MDE context if available.
3. Load relevant website assessment output if available.
4. Load `context-packs/client-website-build.md`.
5. Load `context-packs/website-assessment-to-build.md` when assessment output exists.
6. Create client-safe local MDE structure.
7. Generate required client questions.
8. Generate content-needed checklist.
9. Generate website build mission.
10. Generate technical implementation brief.
11. Generate project-specific validation strategy.
12. Generate initial task graph.
13. End with local outbox event and learning triage.

Client website repo should contain:

```text
MISSION.md
MISSION_UPDATES.md
.mde/project.json
.mde/validation-strategy.json
.mde/outbox/events.jsonl
.mde/lessons-local.jsonl
docs/client-intake-needed.md
docs/content-needed-from-client.md
docs/website-build-brief.md
docs/launch-validation-plan.md
```

Keep the repo client-safe. Central MDE owns reusable learning and internal strategy.

