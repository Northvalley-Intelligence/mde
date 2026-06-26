# Regular MDE Learning Audit Prompt

You are in the central `mde` repo.

Run a regular MDE learning audit to check whether individual project work is improving the platform.

Do not modify project repos unless explicitly requested.
Do not import project-only noise.
Preserve confidentiality labels.
Sibling repos are read-only during this audit. If a project needs code or MDE artifact changes, record a follow-up and open Codex in that project root.

Audit steps:

1. Read `portfolio/PROJECTS.yaml`.
2. For accessible sibling repos, look for `.mde/outbox` files.
3. Import new central-worthy records without duplicating existing records.
4. Update central ledgers when records are reusable or cross-project relevant.
5. Update `briefings/current-platform-brief.md`.
6. Update `briefings/chatgpt-handoff.md` when useful.
7. Identify stale projects with no recent sync.
8. Identify repeated issues that should become validators or patterns.
9. Identify skill update candidates ready for promotion.
10. Identify content seeds worth developing.
11. Recommend the next central MDE improvement.

Produce:

```text
MDE Learning Audit Summary

Projects checked:
...
Outboxes imported:
...
New lessons:
...
Reusable patterns suggested:
...
Validator candidates:
...
Skill update candidates:
...
Content seeds:
...
Projects not syncing:
...
Is MDE learning? yes/no/partial
Recommended next action:
...
```
