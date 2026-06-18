# UI Forms Context Pack

Applicable artifact profiles:

- `form_workflow`
- `web_ui`
- `mobile_ui`

Known issue signatures:

- `FORM_DATA_LOST_ON_VALIDATION_FAILURE`
- `ERROR_MESSAGE_NOT_FIELD_SPECIFIC`
- `DISABLED_ACTION_WITHOUT_REASON`
- `FAKE_BUTTON_OR_DEAD_ACTION`

Checks:

- User input survives validation failure.
- Errors appear near affected fields.
- User does not repeat previously successful work.
- Recovery path is clear.
- Disabled actions explain why they are unavailable.
- Clickable-looking elements perform meaningful actions.

