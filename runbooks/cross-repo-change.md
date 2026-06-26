# Cross-Repo Change Runbook

This runbook coordinates cross-repo impact. It does not authorize editing another repository from the current session.

1. Identify source project.
2. Identify changed artifact.
3. Check `portfolio/DEPENDENCIES.yaml` for downstream projects.
4. Record event in source project `.mde/outbox/events.jsonl` if available.
5. Record central event in `mde/ledger/events.jsonl` if cross-project impact exists.
6. Create downstream impact list.
7. Decide if downstream projects need immediate updates.
8. If downstream code must change, create a handoff note and open Codex with that downstream repo as the home folder.
9. Record reusable lesson if applicable.
10. Record content seed if there is a good story.
11. Update `briefings/current-platform-brief.md` from central `mde` only.
12. Create handoff note for the next Codex window.

Hard rule: do not edit, format, commit, push, deploy, migrate, or reset downstream repos from the source project session.

## Example

If `demand-data-generation` changes output schema:

Impacted:

- `local-website-growth-assessment`
- `proposals`

Required checks:

- Schema compatibility
- Assessment report regeneration
- Proposal regeneration
- Formatting validation
