# Repository Governance

Purpose: keep MDE work submitted, traceable, and contained to the correct project.

## Repository Ownership Boundary

Default rule: one repo equals one writable Codex session.

Allowed from the current session home:

- read related project files for dependency context
- read central `mde` briefings, context packs, portfolio records, and issue signatures
- write files inside the current session home repository
- write project-local outbox records for the current project
- when the session home is central `mde`, import project outbox records into central MDE ledgers

Not allowed from the current session home:

- edit sibling project files
- run formatters or generators that modify sibling repos
- install dependencies into sibling repos
- commit, push, deploy, migrate, or reset sibling repos
- silently fix downstream projects from an upstream project session

If a downstream project needs code changes, record the impact and start or request a Codex session with that downstream repo as the home folder.

## GitHub Submission Gate

At the end of a meaningful code session, and after a second clean Validation Gate pass, check submission state:

1. Run `git status --short --branch`.
2. Confirm the changed files belong to the session home repo.
3. Commit meaningful code/config/deploy changes.
4. Push the branch or create the required PR when project workflow requires PR review.
5. Record the branch and commit SHA in the generation evidence or session handoff.

If commit or push cannot be completed because there is no remote, no authentication, failing checks, user-deferred changes, or a dirty worktree that should not be committed, record the blocker explicitly. Do not call the phase submitted.

Documentation-only or private ignored MDE memory updates may be left local when they are intentionally not tracked, but the final handoff must say so.

## Production Parity Gate

For production-deployed projects:

1. Identify the production deployment source: usually `main`, sometimes a documented `prod` branch or deploy workflow source.
2. Verify the production deployed commit SHA is recorded in `deploy/` evidence, release checks, hosting metadata, or the deployment tool output.
3. Verify the deployed production commit is reachable from `origin/main`.
4. If a `prod` branch exists, verify `origin/main` and `origin/prod` are synchronized unless there is a documented approved staged-release exception.
5. Do not mark production readiness complete while local code, `origin/main`, the deploy source branch, and production deployed commit disagree.

If the hosting provider does not expose a commit SHA, record the best available deployment identifier and the GitHub commit used to deploy.
