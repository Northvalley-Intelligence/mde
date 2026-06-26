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
Quality Gate is deprecated as a standalone idea and replaced by explicit validation gates.
Phase readiness for meaningful user-facing or mission-critical work requires a Primary Validation Gate plus a Third-Person Validation Gate, not two BDD passes.

The Primary Validation Gate proves the implementation works functionally and technically. The Third-Person Validation Gate is a separate gate that independently reviews the result from the user's point of view. It should usually generate different scenarios, checks, data, roles, environments, or validator angles from the Primary Validation Gate, with special attention to usability and mission fit. Rerun the same exact deterministic checks only when that repetition can expose nondeterminism, environment sensitivity, external dependency instability, concurrency/timing behavior, or a known flaky path.

Every Third-Person Validation Gate should record its outcome and whether it produced new findings, changed a decision, added coverage, or found no new issues. If repeated third-person gates add no signal, tune the gate strategy and reevaluate it instead of treating duplicate reruns as evidence.

Use `prompts/project-validation-strategy-generation0.prompt.md` and `templates/validation-strategy.template.json` to create `.mde/validation-strategy.json`.
