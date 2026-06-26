# MDE Session Router Prompt

Decide which MDE prompt to use before starting or continuing a Codex session.

Global repository rule: a session may read related repos for context, but it may write only inside the repository that is the session home. Do not edit, format, commit, push, deploy, migrate, or reset sibling repos from this session. If another repo needs changes, create a handoff/outbox record and open Codex in that repo.

Global communication rule: MDE agent-to-user updates are summary-first by default. During work and in final responses, do not paste raw code, raw diffs, or long command output unless Ferosh explicitly asks. Summarize what is happening, why it matters, mission impact, validation, findings, short changed files/components, short commit/deploy status, and next action.

When output is reduced, preserve this order: blocking ask or decision needed, current action and why it matters, mission impact, validation and Critical/High findings, short GitHub/deploy status, short files/components touched, next action. Keep GitHub/deploy and files/components entries compact by default, then expand only if Ferosh asks. Omit raw code, raw diffs, long logs, and line-by-line implementation narration first.

## CASE A: Working In Central `mde` Repo

Use when updating shared MDE memory, prompts, patterns, validators, context packs, ledgers, launch packs, skill packages, or briefings.

Prompt: use the specific central MDE mission, `prompts/regular-mde-learning-audit.prompt.md`, or `prompts/central-import-project-outbox.prompt.md`.

## CASE B: Existing Project Already Uses MDE, Codex Window Already Open

Use when the repo already has `MISSION.md`, `MISSION_UPDATES.md`, `.mde/`, generations, validation, or similar MDE artifacts.

Prompt: `prompts/existing-mde-open-session-sync.prompt.md`

Important: do not re-adopt MDE and do not restart the session.

## CASE C: Existing Project Already Uses MDE, No Codex Window Open Yet

Use when starting a new Codex session in a repo that already uses MDE.

Prompt: `prompts/existing-mde-new-session-start.prompt.md`

## CASE D: Existing Project Does Not Use MDE, Codex Window Already Open

Use when a project has an active Codex session but no meaningful MDE structure yet.

Prompt: `prompts/existing-non-mde-open-session-bridge.prompt.md`

## CASE E: Existing Project Does Not Use MDE, No Codex Window Open Yet

Use when opening Codex for an old repo that needs minimal MDE adoption.

Prompt: `prompts/existing-non-mde-new-session-adopt.prompt.md`

## CASE F: Brand-New Non-Client Project

Use when starting a new project from scratch.

Prompt: `prompts/new-project-generation0-bootstrap.prompt.md`

## CASE G: Brand-New Client Website Repo/Folder

Use when starting a new client website repo or folder.

Prompt: `prompts/new-client-website-skill-bootstrap.prompt.md`

## CASE H: End Of Any Meaningful Project Session

Use before closing a meaningful project Codex session.

Prompt: `prompts/session-end-learning-triage-and-sync.prompt.md`

## CASE I: Regular Central Check Whether MDE Is Learning

Use from the central `mde` repo.

Prompt: `prompts/regular-mde-learning-audit.prompt.md`

## CASE J: Promote Central MDE Learning Into `codex-skills`

Use when skill candidates are ready to become actual skill behavior.

Prompt: `prompts/skill-update-promotion.prompt.md`

## Project Repository Governance Sync

Use from inside a project repo when applying repository ownership, GitHub submission, and production parity rules to that one project.

Prompt: `prompts/project-repository-governance-sync.prompt.md`

## Central Import From Project Outbox

Use when a project produced `.mde/outbox` events, lessons, impacts, skill candidates, or content seeds.

Prompt: `prompts/central-import-project-outbox.prompt.md`

## Hard Rules

Do not use the non-MDE adoption prompt in a repo that already uses MDE.
Do not use the full project bootstrap just to continue an existing session.
Do not use a parent-folder Codex window for normal coding.
Do not modify sibling repositories from the current session.
After meaningful code changes or validation readiness, submit work to GitHub or record the blocker.
For production-deployed projects, keep `main` in sync with deployed production code unless an approved staged-release exception is documented.
Do not dump raw code or diffs in MDE progress updates, handoffs, or final responses unless explicitly requested.
