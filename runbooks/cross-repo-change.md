# Cross-Repo Change Runbook

1. Identify source project.
2. Identify changed artifact.
3. Check `portfolio/DEPENDENCIES.yaml` for downstream projects.
4. Record event in source project `.mde/outbox/events.jsonl` if available.
5. Record central event in `mde/ledger/events.jsonl` if cross-project impact exists.
6. Create downstream impact list.
7. Decide if downstream projects need immediate updates.
8. Record reusable lesson if applicable.
9. Record content seed if there is a good story.
10. Update `briefings/current-platform-brief.md`.
11. Create handoff note for the next Codex window.

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

