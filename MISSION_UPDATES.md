# Mission Updates

## 2026-06-12

- Bootstrapped portfolio memory for connected projects.
- Added incremental migration discipline: record first, standardize second, automate third.
- Added cross-repo dependency and workflow tracking.
- Added existing Codex session bridge prompts and runbooks.
- Added learning triage for reusable patterns, validators, skill update candidates, and content seeds.
- Added Codex and ChatGPT handoff artifacts.
- Added session routing for central MDE work, existing-MDE sessions, non-MDE sessions, brand-new projects, and project outbox imports.
- Added existing-MDE open-session sync so already-MDE projects are not re-adopted or restarted.
- Added just-in-time reusable learning through context packs, issue signatures, and validator candidates.
- Added Generation 0 project-specific Validation Strategy discipline.
- Recorded that Quality Gate is deprecated as standalone terminology; phase exit uses a project-specific Validation Gate plus a Second Validation Review.

## 2026-06-14

- Consolidated MDE Platform OS setup for separate repos and Codex windows.
- Added planned launch packs for `client-website-build-brief-generator`, `northvalley-client-success`, and `jacob-family-mobile`.
- Added starter packs and context packs for client website builds, client success CRM, personalized family software, mobile companion apps, and assessment-to-build workflows.
- Added skill-driven client website bootstrap prompt and runbook.
- Added regular MDE learning audit prompt, runbook, and optional helper scripts.
- Added project outbox contract for local-to-central sync.
- Added `skill-packages/mde-skill-next` for future promotion into `codex-skills`.
- Added central issue signature seeds and expanded content/skill candidate ledgers.

## 2026-06-25

- Added repository ownership boundary: a Codex session may read related repos for context but may write only inside its session home repository.
- Added GitHub submission discipline: after meaningful code changes or validation readiness, code should be committed and pushed, or a blocker must be recorded.
- Added production parity discipline: production-deployed projects must keep `main` traceable to deployed production code unless a documented staged-release exception is approved.
- Added summary-first communication discipline: MDE sessions should communicate what agents are doing, why it matters, mission outcomes, validation, risks, commits, and file references instead of raw code or diffs unless explicitly requested.

## 2026-06-26

- Tightened validation discipline: the Second Validation Review must act like an independent third-person reviewer for meaningful user-facing or mission-critical work. It should look for usability, mission-fit, role, workflow, edge-case, data-shape, environment, or integration problems the first gate may have missed. Track whether each review found new issues, changed decisions, added coverage, or found no new issues so MDE can tune and reevaluate its value.
