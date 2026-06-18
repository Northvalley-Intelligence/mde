# Existing Codex Session Bridge Prompt

For clearer routing, prefer:

- `prompts/existing-mde-open-session-sync.prompt.md` when the project already uses MDE.
- `prompts/existing-non-mde-open-session-bridge.prompt.md` when the project does not meaningfully use MDE yet.

You are in an existing Codex session for this repository.
We are adopting the MDE portfolio memory discipline without restarting the session.

Do not rewrite history.
Do not perform a large refactor.

Before continuing, create or update minimal local MDE context:

1. Create `.mde/project.json` if missing.
2. Create `.mde/outbox/events.jsonl` if missing.
3. Create `.mde/lessons-local.jsonl` if missing.
4. Summarize the current session focus.
5. Identify whether current work affects downstream projects.
6. If downstream impact exists, create an event in `.mde/outbox/events.jsonl`.
7. Produce a short handoff note that can be copied into the central `mde` repo.

Use the central MDE portfolio files when available:

- `../mde/briefings/current-platform-brief.md`
- `../mde/portfolio/DEPENDENCIES.yaml`
- `../mde/portfolio/PROJECTS.yaml`

Then continue the current project work.
