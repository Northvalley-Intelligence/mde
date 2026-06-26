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
Phase exit requires a Validation Gate plus a Second Validation Review, not two BDD passes.

For meaningful user-facing or mission-critical work, the second validation is required and should act like an independent third-person reviewer. It should usually generate different scenarios, checks, data, roles, environments, or validator angles from the first gate, with special attention to usability and mission fit. Rerun the same exact deterministic checks only when that repetition can expose nondeterminism, environment sensitivity, external dependency instability, concurrency/timing behavior, or a known flaky path.

Every Second Validation Review should record whether it produced new findings, changed a decision, added coverage, or found no new issues. If repeated second reviews add no signal, tune the review strategy and reevaluate it instead of treating duplicate reruns as evidence.

Use `prompts/project-validation-strategy-generation0.prompt.md` and `templates/validation-strategy.template.json` to create `.mde/validation-strategy.json`.
