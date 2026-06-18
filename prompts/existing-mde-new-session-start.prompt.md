# Existing MDE New Session Start Prompt

You are starting a new Codex session in a repository that already uses MDE.

Do not run full MDE adoption.
Do not regenerate the mission unless asked.
Do not rebuild existing MDE artifacts.

Start by reading:

1. `MISSION.md`
2. `MISSION_UPDATES.md`
3. `.mde/project.json`
4. `.mde/state.json` if available
5. latest `.mde/generations` entry if available
6. latest `.mde/validation-runs` entry if available
7. `../mde/briefings/current-platform-brief.md` if available
8. `../mde/portfolio/PROJECTS.yaml` if available
9. `../mde/portfolio/DEPENDENCIES.yaml` if available
10. `../mde/context-packs/README.md` and matching context packs
11. `../mde/knowledge/issue-signatures.jsonl` if available

Then report:

- current mission focus
- last known generation and validation status
- applicable reusable MDE lessons
- likely downstream impacts
- whether validation strategy exists
- whether project-local central sync outbox exists

If the sync outbox is missing, create only the missing outbox files.

Before making changes, perform Applicable Learning Check.

