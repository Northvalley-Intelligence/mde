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
Phase exit requires two independent Validation Gate passes, not two BDD passes.

Use `prompts/project-validation-strategy-generation0.prompt.md` and `templates/validation-strategy.template.json` to create `.mde/validation-strategy.json`.

