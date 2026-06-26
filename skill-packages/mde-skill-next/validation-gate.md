# Validation Gate

Quality Gate is not a standalone phase gate.

Phase exit requires a project-specific Validation Gate plus a Second Validation Decision. BDD is part of Functional Validation, not the whole gate.

The second validation is not a blind rerun. It must be independently designed and value-added. It should usually generate different scenarios, checks, data, roles, environments, or validator angles from the first gate.

Rerunning the same exact deterministic checks counts only when repetition can expose nondeterminism, environment sensitivity, external dependency instability, concurrency/timing issues, or a known flaky path. Record the reason. If no credible second-pass signal exists, record `second_validation_no_signal` instead of treating a duplicate rerun as evidence.

After validation readiness, run Repository Governance checks before claiming the phase is complete:

- meaningful code/config/deploy changes committed and pushed, or blocker recorded
- current session did not modify sibling repositories
- for production-deployed projects, deployed production commit/source is recorded
- `main` is synchronized with production deployment source, or an approved staged-release exception is documented
