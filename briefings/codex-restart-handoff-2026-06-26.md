# Codex Restart Handoff - 2026-06-26

Purpose: preserve the relevant central MDE context while moving Codex work from the iCloud workspace to a local folder.

Current source workspace:

```text
/Users/feroshjacob/Library/Mobile Documents/com~apple~CloudDocs/code/mde
```

## Current Git State

Central `mde` was clean and pushed before this handoff file was added.

```text
branch: main
remote: origin/main
repository governance baseline commit: 0894065 Add repository governance gates
previous commits:
- 64af0fe Add Apache 2.0 license
- 49b579c Add public MDE example links
- 9dc1176 Publish MDE backbone
```

When reopening in the new local folder, verify:

```text
git log --oneline --decorate -3
git status --short --branch
```

Expected result: `HEAD -> main, origin/main` at this handoff commit or a later commit, with `0894065 Add repository governance gates` visible in recent history and no tracked changes.

## Important Migration Note

This public repo intentionally ignores local private MDE memory:

```text
.mde/
ledger/
portfolio/
migration/
briefings/current-platform-brief.md
briefings/chatgpt-handoff.md
```

If you clone from GitHub into the new local folder, the tracked MDE backbone and this handoff will be available, but those ignored private files will not be restored from GitHub.

If you need the full private local memory, copy the old workspace folder or copy the ignored paths above from the iCloud location into the new local folder. If you only need continuity for the next Codex session, this handoff plus the pushed tracked files are enough.

## Latest MDE State

Local ignored MDE state at the time this handoff was written:

```json
{
  "project": "mde",
  "current_phase": "repository-governance-rollout",
  "current_generation": "GEN-004",
  "mission_version": "2026-06-14",
  "validation_strategy_version": "2026-06-25-repository-governance",
  "validation_gate_pass_count": 2,
  "last_updated": "2026-06-25T21:48:13-04:00"
}
```

`GEN-004` completed the repository governance rollout:

- Central MDE now says a Codex session may read related repos for context but may write only inside the session home repo.
- Session end and second clean Validation Gate pass now require GitHub submission or an explicit blocker.
- Production-deployed projects must record deployed commit/source and keep `main` in sync with production unless an approved staged-release exception exists.
- `prompts/project-repository-governance-sync.prompt.md` gives each project a local rollout path.
- `runbooks/roll-out-repository-governance.md` contains the bridge prompt for already-open Codex windows.
- `skill-packages/mde-skill-next` contains repository governance behavior ready for promotion from the `codex-skills` repo.

Validation for `GEN-004` passed twice:

- repository governance artifact coverage check: 12/12
- JSON/JSONL parse check: 155 parsed records
- `git diff --check`: pass
- learning summary: 44 events, 27 lessons, 20 content seeds, 24 skill candidates, 6 issue signatures
- outbox dry-run: 0 records available to import

## Open Finding

Nonblocking Medium finding from `GEN-003`:

```text
MDE-AUDIT-2026-06-25-001
Six sibling repos have .mde/outbox records but are not listed in portfolio/PROJECTS.yaml:
cjwelding, ecommmerce-eval, growth, jacob-family-android, jacob-family-ios, resplendenttea.
```

Recommendation: run a portfolio reconciliation pass before importing those outboxes so central MDE knows ownership, confidentiality, artifact profiles, and dependencies.

## New Governance Files

Key tracked files added or updated by commit `0894065`:

```text
runbooks/repository-governance.md
runbooks/roll-out-repository-governance.md
prompts/project-repository-governance-sync.prompt.md
prompts/session-router.prompt.md
prompts/session-end-learning-triage-and-sync.prompt.md
templates/validation-strategy.template.json
skill-packages/mde-skill-next/repository-governance.md
skill-packages/mde-skill-next/project-repository-governance-sync.md
skill-packages/mde-skill-next/validation-gate.md
skill-packages/mde-skill-next/handoff-discipline.md
```

Also updated: `MISSION.md`, `MISSION_UPDATES.md`, `README.md`, prompt/runbook indexes, and project outbox/template contracts.

## Exact Bridge Prompt For Already-Open Project Windows

Paste this into any already-open Codex project session:

```text
Read ../mde/prompts/project-repository-governance-sync.prompt.md and ../mde/runbooks/repository-governance.md, then apply the rules to this project only. Do not modify sibling repos. From now on, after meaningful code changes or two clean Validation Gate passes, submit this project's code to GitHub or record the blocker. If this project is production-deployed, verify main is in sync with deployed production code or record the approved exception/blocker.
```

This refreshes that already-open session without pretending it reloaded the MDE skill.

## Per-Project Rollout For New Project Sessions

For a project that does not already have an open Codex window:

1. Open Codex with that project as the home folder.
2. Run:

```text
../mde/prompts/project-repository-governance-sync.prompt.md
```

3. Let that project session update only project-local MDE/status/deploy artifacts.
4. If code changed, commit and push from that project session.
5. If production-deployed, record deployed commit/source and verify `main` parity.

## Next Actions

1. Move or clone `mde` into the new local folder.
2. If preserving private local memory, copy ignored `.mde/`, `ledger/`, `portfolio/`, `migration/`, and private briefing files from the old iCloud workspace.
3. Open a new Codex session in the new local `mde` folder.
4. Tell it:

```text
Read briefings/codex-restart-handoff-2026-06-26.md, then continue central MDE work from the repository-governance rollout state.
```

5. Open a separate Codex session in `codex-skills` and promote `skill-packages/mde-skill-next` using:

```text
../mde/prompts/skill-update-promotion.prompt.md
```

6. Bridge any already-open project Codex windows with the bridge prompt above.
7. For production projects, prioritize governance sync first.
8. Reconcile outbox-bearing sibling repos not yet in central portfolio memory.

## Hard Rules To Preserve After Restart

- Do not modify sibling repos from the current session.
- Read related repos for context only.
- Cross-project changes require a handoff/outbox record and a Codex session opened in the target repo.
- After meaningful code/config/deploy changes or two clean Validation Gate passes, commit and push or record the blocker.
- For production-deployed projects, `main` must be traceable to deployed production code unless an approved staged-release exception is documented.
- Central `mde` imports central-worthy project outbox records; it does not silently patch project repos.
