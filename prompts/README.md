# Prompts

Use `session-router.prompt.md` first when deciding which prompt belongs in a Codex session.

The routing distinction matters:

- Existing MDE projects should be synced, not re-adopted.
- Existing non-MDE projects should get minimal adoption, not a full framework.
- Brand-new projects need Generation 0 before implementation.
- Central `mde` work uses central missions and import prompts.
- Existing projects can sync repository governance with `project-repository-governance-sync.prompt.md`.

Do not use a parent-folder Codex window for normal project coding.
Do not modify sibling repositories from the current session; read them for context only.
At session end or after two clean Validation Gate passes, submit meaningful code changes to GitHub or record the blocker.
For production-deployed projects, verify `main` is in sync with deployed production code or record the approved exception/blocker.
