# Second Validation Review

Purpose: make the second validation add a third-person reviewer perspective instead of repeating the first gate.

Use this for meaningful user-facing or mission-critical work after the first project-specific Validation Gate passes.

## Reviewer Stance

The reviewer should act as if they did not build the change.

Ask:

- Does the result actually satisfy the mission from the user's point of view?
- Did the base fix work but leave a usability problem?
- Would each relevant role understand what to do next?
- Is the most common workflow still efficient?
- Are important actions visible, timely, and clearly named?
- Are error, empty, loading, recovery, and stale-state cases handled?
- Did the fix create clutter, duplicate controls, misleading status, or hidden work?
- Does persisted state resolve the related task, notification, request, invite, approval, or workflow object?

## Different Signal

Prefer a different validation angle from the first gate:

- different user role
- different data shape
- different workflow order
- edge case or recovery path
- mobile or narrow viewport
- live/staging/production environment
- accessibility or keyboard behavior
- usability review of the rendered UI
- integration boundary or stale persisted state

Rerun the same exact deterministic test set only when the risk is:

- nondeterminism
- environment sensitivity
- external dependency instability
- concurrency or timing behavior
- known flaky path

Record that reason explicitly.

## Value Tracking

Every Second Validation Review must record:

- reviewer perspective used
- different signal attempted
- new findings count by severity
- decisions changed
- coverage added
- whether product code changed after the review
- final outcome: `new_findings`, `decision_changed`, `coverage_added`, or `no_new_findings`

If the review finds no new issues, record `no_new_findings`; do not call it a failure.

If five consecutive relevant Second Validation Reviews add no findings, no decision changes, and no coverage, tune the second-review checklist or validator. Do not remove the review by default.

## Reporting Shape

Keep reports concise:

- Second validation: third-person usability/mission review
- Value added: new finding, decision changed, coverage added, or no new findings
- Follow-up: fixed, accepted, deferred, or tune validator
