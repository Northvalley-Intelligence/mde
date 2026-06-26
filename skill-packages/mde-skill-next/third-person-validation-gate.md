# Third-Person Validation Gate

After the Primary Validation Gate passes, meaningful user-facing or mission-critical work needs a Third-Person Validation Gate.

This gate should not default to rerunning the same deterministic checks. It should try to add a different signal:

- usability and mission fit
- different user role
- different data shape
- different workflow order
- edge case or recovery path
- mobile or narrow viewport
- live/staging/production environment
- accessibility or keyboard behavior
- integration boundary or stale persisted state

Same-test reruns count only when repetition can expose nondeterminism, environment sensitivity, external dependency instability, concurrency/timing issues, or a known flaky path. Record the reason.

Every Third-Person Validation Gate must record:

- gate outcome: `pass`, `fail`, `accepted_with_findings`, or `deferred_with_reason`
- reviewer perspective used
- different signal attempted
- new findings count by severity
- decisions changed
- coverage added
- whether product code changed after the gate
- final value outcome: `new_findings`, `decision_changed`, `coverage_added`, or `no_new_findings`

If five consecutive relevant gates add no findings, no decision changes, and no coverage, recommend tuning the gate checklist or validator. Do not remove the gate by default.
