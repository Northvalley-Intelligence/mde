# Affordance Integrity Validator Candidate

Goal:
Prevent fake buttons, dead links, hidden critical actions, and disabled controls without explanation.

Applies to:

- `web_ui`
- `mobile_ui`
- `client_facing_workflow`
- `internal_tool`

Suggested checks:

- Click every element that visually presents as actionable.
- Fail if a visible action does nothing useful.
- Fail if important workflow actions are not visually discoverable.
- Fail if disabled actions do not explain why they are unavailable.
- Confirm keyboard focus and accessible names exist for actionable controls.

Run policy:

- When navigation, task lists, dashboards, forms, or action controls change.
- Before phase exit for user-facing workflows.

Default severity:
High. Critical if the dead action blocks mission-critical work or misleads a user about completion.

