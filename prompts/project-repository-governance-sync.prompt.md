# Project Repository Governance Sync Prompt

Use this from inside a project repo, not from central `mde`.

Purpose: apply the current MDE repository ownership, GitHub submission, and production parity rules to this project.

Hard rules:

- Write only inside this project repo.
- Read central `../mde` artifacts for context when available.
- Do not modify sibling repos.
- Do not deploy or push until project validation and user approval rules are satisfied.

Read:

1. `MISSION.md`
2. `MISSION_UPDATES.md`
3. `.mde/state.json`
4. `.mde/validation-strategy.json`
5. latest `.mde/generations/` and `.mde/validation-runs/`
6. `deploy/` artifacts if present
7. `../mde/runbooks/repository-governance.md`
8. `../mde/briefings/current-platform-brief.md`

Then update only missing or stale project-local MDE artifacts:

- `.mde/validation-strategy.json`: add repository governance checks if missing
- `.mde/generation-summary.md` or local status doc: note GitHub submission and production parity expectations
- deploy/release evidence: add fields for deployed commit/source only if the project already has deploy artifacts
- `.mde/outbox/events.jsonl`: record that governance sync ran, when useful for central import

Report:

1. Current branch and working tree state.
2. Whether the project has a GitHub remote.
3. Whether code is currently submitted to GitHub.
4. Whether the project appears production-deployed.
5. If production-deployed, whether deployed code is traceable to `origin/main`.
6. Whether a `prod` branch exists and whether it matches `origin/main`.
7. What local MDE artifacts were updated.
8. Any blocker to enforcing the rules.

Do not make product code changes unless explicitly requested.
