# Project Validation Strategy Generation 0 Prompt

Every project must define its own Validation Strategy during Generation 0 or during the first safe MDE validation update.

Do not hard-code one validation setup for all projects.

Validation categories are reusable:

1. Functional Validation
2. Technical Validation
3. Usability Validation
4. UI Standards Validation
5. Mission Coverage Validation
6. Project-Specific External Validation

Validation tools are project-specific.

Previous choices such as Playwright, axe-core, Lighthouse, Pa11y, OWASP ZAP, Appium, Maestro, Detox, offline evaluation datasets, relevance metrics, latency benchmarks, or custom validators may be considered, but must not be assumed.

## Strategy Questions

Project Type:

- web app?
- mobile app?
- backend service?
- PDF/print artifact generator?
- AI/search/recommendation system?
- content generation system?
- data pipeline?
- client-facing workflow?
- internal tool?

Artifact Profiles:

- `pdf_generation`
- `print_layout`
- `web_ui`
- `mobile_ui`
- `form_workflow`
- `client_facing_document`
- `data_contract`
- `report_generation`
- `ai_generated_content`
- `public_content`
- `private_client_data`

Mission-Critical Workflows:

- who uses it?
- what must they accomplish?
- what failures would be painful or costly?

Validation Needs:

- what must be functionally correct?
- what must be technically reliable?
- what usability failures are likely?
- what UI standards apply?
- what mission coverage is required?
- what external validators fit this project?

Tool Selection:

- what existing mature tools are relevant?
- what custom MDE validators are needed?
- what tools are intentionally skipped for this phase and why?
- what validations are too expensive for every generation but required before release?

Create `.mde/validation-strategy.json` using `templates/validation-strategy.template.json`.

