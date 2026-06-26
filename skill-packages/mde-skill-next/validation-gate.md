# Validation Gate

Quality Gate is not a standalone phase gate.

Phase readiness for meaningful user-facing or mission-critical work requires a Primary Validation Gate plus a Third-Person Validation Gate. BDD is part of Functional Validation, not the whole gate.

The Primary Validation Gate proves the implementation works functionally and technically.

The Third-Person Validation Gate is a separate gate, not a second pass. It independently reviews the result from the user's point of view, with special attention to usability, mission fit, role fit, workflow fit, edge cases, data shape, environment, and integration boundaries. It should usually generate different scenarios, checks, data, roles, environments, or validator angles from the Primary Validation Gate.

Rerunning the same exact deterministic checks counts only when repetition can expose nondeterminism, environment sensitivity, external dependency instability, concurrency/timing issues, or a known flaky path. Record the reason.

Every Third-Person Validation Gate must record outcome:

- pass
- fail
- accepted with findings
- deferred with reason

It must also record value added:

- new findings
- decisions changed
- coverage added
- no new findings

If repeated third-person gates add no findings, no decision changes, and no coverage, tune the gate strategy and reevaluate its value. Do not remove the gate by default; improve the reviewer angle first.

After validation readiness, run Repository Governance checks before claiming the phase is complete:

- meaningful code/config/deploy changes committed and pushed, or blocker recorded
- current session did not modify sibling repositories
- for production-deployed projects, deployed production commit/source is recorded
- `main` is synchronized with production deployment source, or an approved staged-release exception is documented
