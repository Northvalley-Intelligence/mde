# Second Validation Review

After the first project-specific Validation Gate passes, meaningful user-facing or mission-critical work needs a second validation from an independent third-person perspective.

The review should not default to rerunning the same deterministic checks. It should try to add a different signal:

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

Every Second Validation Review must record:

- reviewer perspective used
- different signal attempted
- new findings count by severity
- decisions changed
- coverage added
- whether product code changed after the review
- final outcome: `new_findings`, `decision_changed`, `coverage_added`, or `no_new_findings`

If five consecutive relevant reviews add no findings, no decision changes, and no coverage, recommend tuning the second-review checklist or validator. Do not remove the review by default.
