# Form Data Preservation Validator Candidate

Goal:
Prevent users from losing entered data after validation errors, failed submissions, reloads, or recoverable workflow errors.

Applies to:

- `form_workflow`
- `web_ui`
- `mobile_ui`
- `client_facing_workflow`

Suggested checks:

- Submit forms with one invalid field and several valid fields.
- Confirm valid user-entered values remain visible after validation failure.
- Confirm errors appear near affected fields.
- Confirm the user can correct the error without repeating previously successful work.
- Confirm partial success states are clear when a workflow has multiple steps.

Run policy:

- When forms, validation, submission handlers, or persistence logic change.
- Before phase exit for mission-critical user workflows.

Default severity:
Critical for workflows that collect important user, family, client, payment, or operational data. High otherwise.

