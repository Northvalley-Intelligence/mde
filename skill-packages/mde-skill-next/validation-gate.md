# Validation Gate

Quality Gate is not a standalone phase gate.

Phase exit requires a project-specific Validation Gate plus a Second Validation Review. BDD is part of Functional Validation, not the whole gate.

The second validation is not a blind rerun. For meaningful user-facing or mission-critical work, it is a required independent third-person review of the result. It should usually generate different scenarios, checks, data, roles, environments, or validator angles from the first gate, with special attention to usability and mission fit.

Rerunning the same exact deterministic checks counts only when repetition can expose nondeterminism, environment sensitivity, external dependency instability, concurrency/timing issues, or a known flaky path. Record the reason.

Every Second Validation Review must record value added:

- new findings
- decisions changed
- coverage added
- no new findings

If repeated second reviews add no findings, no decision changes, and no coverage, tune the second-review strategy and reevaluate its value. Do not remove the second review by default; improve the reviewer angle first.

After validation readiness, run Repository Governance checks before claiming the phase is complete:

- meaningful code/config/deploy changes committed and pushed, or blocker recorded
- current session did not modify sibling repositories
- for production-deployed projects, deployed production commit/source is recorded
- `main` is synchronized with production deployment source, or an approved staged-release exception is documented
