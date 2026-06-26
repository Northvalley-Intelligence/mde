# Repository Governance

The MDE skill should enforce these repository rules in every project session.

## Writable Scope

The current session home repository is the only writable project.

The agent may read related repositories for context. It must not edit, format, install dependencies, commit, push, deploy, migrate, or reset sibling repositories.

If another repo needs changes, create a handoff/outbox record and open Codex in that target repository.

## GitHub Submission Gate

After meaningful code/config/deploy changes, and after validation readiness, the agent should:

1. Check git status.
2. Commit the session-home repo changes when appropriate.
3. Push the branch or create the expected PR.
4. Record the branch and commit SHA.

If submission is blocked, record the exact blocker and next action.

## Production Parity Gate

For production-deployed projects, the agent should verify and record:

- production deployment source
- deployed production commit or deployment identifier
- whether the deployed commit is reachable from `origin/main`
- whether `origin/main` and `origin/prod` are synchronized when a `prod` branch exists
- any approved staged-release exception

Do not mark production readiness complete when local code, GitHub, and production deployment source disagree.
