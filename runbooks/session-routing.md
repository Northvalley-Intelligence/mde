# Session Routing

Use this runbook before choosing a prompt for Codex work.

Global repository rule: a session may read sibling repos for context, but it may write only inside the repository that is the session home. If another project needs changes, record the impact and open a Codex session in that project root.

## Routing Table

| Case | Use When | Prompt |
| --- | --- | --- |
| A: Central `mde` repo, Codex open | Updating shared MDE memory, prompts, patterns, validators, context packs, ledgers, or briefings | Use the specific central mission or `prompts/central-import-project-outbox.prompt.md` |
| B: Existing project already uses MDE, Codex window already open | Repo already has meaningful MDE artifacts and the session is already active | `prompts/existing-mde-open-session-sync.prompt.md` |
| C: Existing project already uses MDE, no Codex window open yet | Starting a fresh Codex session in an MDE-aware repo | `prompts/existing-mde-new-session-start.prompt.md` |
| D: Existing project does not use MDE, Codex window already open | Active session exists but project has no meaningful MDE structure | `prompts/existing-non-mde-open-session-bridge.prompt.md` |
| E: Existing project does not use MDE, no Codex window open yet | Opening an old repo that needs minimal MDE adoption | `prompts/existing-non-mde-new-session-adopt.prompt.md` |
| F: Brand-new non-client project | Starting from scratch | `prompts/new-project-generation0-bootstrap.prompt.md` |
| G: Brand-new client website repo/folder | Starting a client website repo or folder | `prompts/new-client-website-skill-bootstrap.prompt.md` |
| H: End of meaningful project session | Closing project work with learning and sync | `prompts/session-end-learning-triage-and-sync.prompt.md` |
| I: Regular central learning audit | Checking whether MDE is learning from project work | `prompts/regular-mde-learning-audit.prompt.md` |
| J: Promote skill update | Moving central learning into `codex-skills` | `prompts/skill-update-promotion.prompt.md` |
| Project governance sync | Applying repository ownership, GitHub submission, and production parity rules to one project | `prompts/project-repository-governance-sync.prompt.md` |
| Central import from project outbox | A project produced `.mde/outbox` records for central MDE | `prompts/central-import-project-outbox.prompt.md` |

## Guardrails

Do not use the non-MDE adoption prompt in a repo that already uses MDE.
Do not use the full project bootstrap just to continue an existing session.
Do not use a parent-folder Codex window for normal coding.
Do not modify sibling repositories from the current session.
At session end or after two clean Validation Gate passes, submit meaningful code changes to GitHub or record the blocker.
For production-deployed projects, verify `main` is in sync with the deployed production code or record an approved staged-release exception.
