# Generation 0 Validation Strategy

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

BDD is Functional Validation.
Quality Gate is deprecated as a standalone idea and replaced by Validation Gate.
Phase exit requires a Validation Gate plus a Second Validation Decision, not two BDD passes.

The second validation must be independently designed and value-added. It should usually generate different scenarios, checks, data, roles, environments, or validator angles from the first gate. Rerun the same exact deterministic checks only when that repetition can expose nondeterminism, environment sensitivity, external dependency instability, or a known flaky path. If no credible second-pass signal exists, record `second_validation_no_signal` with the reason.

Use `prompts/project-validation-strategy-generation0.prompt.md` and `templates/validation-strategy.template.json` to create `.mde/validation-strategy.json`.
