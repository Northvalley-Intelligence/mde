# New Codex Session Start Prompt

For clearer routing, prefer `prompts/existing-mde-new-session-start.prompt.md` for projects that already use MDE, or `prompts/existing-non-mde-new-session-adopt.prompt.md` for existing projects that do not.

Before starting work:

1. Read this repository's `MISSION.md` if available.
2. Read this repository's `.mde/project.json` if available.
3. Read `../mde/briefings/current-platform-brief.md` if available.
4. Read `../mde/portfolio/DEPENDENCIES.yaml` if available.
5. Tell me whether this work may affect downstream projects.
6. Tell me whether this repo needs MDE migration before work can safely continue.

Do not make broad unrelated changes.
Do not modify sibling repositories from this session. Related repos may be read for context only.
At session end or after two clean Validation Gate passes, submit meaningful code changes to GitHub or record the blocker.
For production-deployed projects, verify `main` is in sync with the deployed production code or record an approved staged-release exception.
