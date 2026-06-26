# Central Import Project Outbox Prompt

You are in the central `mde` repo.

Import project-local MDE outbox records from a project repo.

Read project repos only. Do not modify the source project repo during central import.

Inputs:

- path to project repo
- project `.mde/outbox/portfolio-sync.json`
- project `.mde/outbox/events.jsonl`
- project `.mde/outbox/lessons.jsonl`
- project `.mde/outbox/impacts.jsonl`
- project `.mde/outbox/content-seeds.jsonl`
- project `.mde/outbox/skill-update-candidates.jsonl`

Tasks:

1. Update `portfolio/PROJECTS.yaml` if project metadata changed.
2. Update `portfolio/DEPENDENCIES.yaml` if dependency information changed.
3. Append meaningful events to `ledger/events.jsonl`.
4. Append reusable lessons to `ledger/lessons.jsonl`.
5. Append content seeds to `ledger/content-seeds.jsonl`.
6. Append skill update candidates to `ledger/skill-update-candidates.jsonl`.
7. Update `knowledge/issue-signatures.jsonl` if a reusable issue signature was discovered.
8. Update or create context packs if a reusable lesson should apply just-in-time to future work.
9. Update `briefings/current-platform-brief.md`.
10. Update `briefings/chatgpt-handoff.md` if the user may need to discuss this outside Codex.

Do not blindly import project-only noise.
Do not make every local lesson global.
Preserve confidentiality labels.
