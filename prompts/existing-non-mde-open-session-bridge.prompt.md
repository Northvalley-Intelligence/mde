# Existing Non-MDE Open Session Bridge Prompt

You are in an existing Codex session for a repository that does not meaningfully use MDE yet.

Use this only for non-MDE or barely-MDE projects with an already open Codex window.

Do not restart the session.
Do not rewrite history.
Do not perform a large refactor.
Do not force full MDE migration before project work can continue.

Create minimal local MDE context:

- `MISSION.md` if missing
- `MISSION_UPDATES.md` if missing
- `.mde/project.json`
- `.mde/outbox/events.jsonl`
- `.mde/lessons-local.jsonl`

Then summarize:

- current session focus
- known upstream dependencies
- known downstream dependencies
- current validation status if known
- migration risks
- next recommended MDE adoption step

If this repo affects other projects, record a project-local event in `.mde/outbox/events.jsonl`.

Then continue the current project work.

