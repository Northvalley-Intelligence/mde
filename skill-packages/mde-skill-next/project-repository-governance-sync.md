# Project Repository Governance Sync

The MDE skill should support a project-local sync mode for applying repository governance.

Use it only when the current Codex session home is the target project repo.

The sync should:

- read central MDE governance context if available
- update only project-local MDE/status/deploy artifacts
- add repository governance checks to the project validation strategy if missing
- detect GitHub remote, current branch, working tree state, and push status
- detect whether the project is production-deployed
- verify production commit/source and `main` parity when deploy artifacts exist
- record blockers instead of silently accepting unsubmitted or drifted code

It must not modify sibling repositories.
