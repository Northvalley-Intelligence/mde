# Adopt MDE In Existing Project Prompt

For clearer routing, prefer `prompts/existing-non-mde-new-session-adopt.prompt.md`. Do not use either adoption prompt in a repo that already meaningfully uses MDE.

Adopt minimal MDE structure for this existing repository.

Do not refactor application code unless required.
Do not generate a large process framework.

Create:

- `MISSION.md` if missing
- `MISSION_UPDATES.md` if missing
- `.mde/project.json`
- `.mde/outbox/events.jsonl`
- `.mde/lessons-local.jsonl`

Then produce:

- Current project summary
- Known upstream dependencies
- Known downstream dependencies
- Current validation status if known
- Migration risks
- Next recommended MDE adoption step

If this repo is connected to other projects, record a project-local event in `.mde/outbox/events.jsonl`.
