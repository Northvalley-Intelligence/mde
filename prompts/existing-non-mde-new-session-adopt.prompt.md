# Existing Non-MDE New Session Adopt Prompt

You are starting a new Codex session in an existing repository that does not meaningfully use MDE yet.

Use this only for repos that do not already have meaningful MDE artifacts.

Do not refactor application code unless required.
Do not generate a large process framework.
Do not force full MDE migration before project work can continue.

Create minimal local MDE context:

- `MISSION.md` if missing
- `MISSION_UPDATES.md` if missing
- `.mde/project.json`
- `.mde/outbox/events.jsonl`
- `.mde/lessons-local.jsonl`

Then produce:

- current project summary
- known upstream dependencies
- known downstream dependencies
- current validation status if known
- migration risks
- next recommended MDE adoption step

If this repo is connected to other projects, record a project-local event in `.mde/outbox/events.jsonl`.

