# Third-Person Validation Gate

Purpose: make the post-primary validation a distinct gate that adds a third-person user and mission perspective instead of repeating the first gate.

Use this for meaningful user-facing or mission-critical work after the Primary Validation Gate passes.

## Gate Stance

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

Prefer a different validation angle from the Primary Validation Gate:

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

## Outcome And Value Tracking

Every Third-Person Validation Gate must record:

- gate outcome: `pass`, `fail`, `accepted_with_findings`, or `deferred_with_reason`
- reviewer perspective used
- different signal attempted
- new findings count by severity
- decisions changed
- coverage added
- whether product code changed after the gate
- final value outcome: `new_findings`, `decision_changed`, `coverage_added`, or `no_new_findings`

If the gate finds no new issues, record `no_new_findings`; do not call it a failure.

If five consecutive relevant Third-Person Validation Gates add no findings, no decision changes, and no coverage, tune the gate checklist or validator. Do not remove the gate by default.

## Reporting Shape

Keep reports concise:

- Third-person gate: usability/mission review
- Outcome: pass, fail, accepted with findings, or deferred with reason
- Value added: new finding, decision changed, coverage added, or no new findings
- Follow-up: fixed, accepted, deferred, or tune validator
