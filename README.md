# Mission-Driven Engineering

Mission-Driven Engineering (MDE) is a file-first operating discipline for using AI agents to build complete applications, not just generate code.

MDE treats mission, validation, memory, and learning as durable project artifacts. The goal is mission advancement: code is one artifact, but the product outcome, validation evidence, risk reduction, and reusable learning determine whether the work is actually done.

This repository is the reusable MDE backbone. It is shared memory and operating discipline, not a monorepo. Project repositories stay separate and synchronize only explicit, central-worthy learning.

## What This Repository Contains

- `prompts/`: session routing, Generation 0, validation strategy, learning audit, outbox sync, and skill promotion prompts.
- `runbooks/`: operational guides for adopting MDE, validating projects, promoting learning, and coordinating across repos.
- `context-packs/`: reusable just-in-time learning for artifact types such as PDFs, forms, client websites, mobile companions, and printable outputs.
- `templates/`: structured MDE records for projects, validation strategies, lessons, issue signatures, content seeds, and handoffs.
- `validators/`: validation guidance and candidate validators for recurring quality risks.
- `starter-packs/` and `project-launches/`: bootstrap packs for new MDE-enabled projects.
- `knowledge/`: reusable issue signatures that help future projects avoid known failure modes.
- `skill-packages/`: proposed updates for Codex skills that carry MDE behavior forward.

## Core Concepts

### Mission First

Start with a mission, not a code prompt. The mission describes what is being built, why it matters, who benefits, constraints, assumptions, and success criteria.

Human-facing mission changes belong in `MISSION_UPDATES.md`. Detailed agent state belongs in structured `.mde/` files inside each project repo.

### Artifact Lanes

MDE separates artifacts by audience:

- Human artifacts: concise mission, status, and decision summaries.
- Agent artifacts: structured state for retrieval, traceability, planning, and validation.
- Deploy artifacts: release and environment metadata needed for reproducible delivery.

This separation keeps humans oriented while giving agents durable, machine-readable context.

### Summary-First Communication

MDE treats code as implementation evidence, not the user-facing completion artifact. Progress updates, command-result explanations, final responses, handoffs, generation summaries, and status docs should summarize:

- what the agent is doing now
- why the action matters
- mission impact
- short files or components touched
- validation run and result
- Critical/High findings and blockers
- short commit and deployment status
- next action

Do not paste raw code, raw diffs, or long command output unless the user explicitly asks. Use file references, short excerpts, commit SHAs, validation evidence, and concise status summaries instead.

When output is constrained, keep this priority order:

1. Ferosh's blocking ask or decision needed.
2. Current action and why it matters.
3. Mission impact.
4. Validation status and Critical/High findings.
5. Short GitHub submission and deployment status.
6. Short files or components touched.
7. Next action.

Items 5 and 6 should stay compact by default: use branch/commit/deploy/parity state and component or file-area names, then expand only when the user asks.

Drop first: raw diffs, raw code, long logs, and line-by-line implementation narration.

### Generation 0

Every new MDE project starts with Generation 0 before implementation.

Generation 0 defines:

- mission and project identity
- dependencies and downstream impact
- risk register and initial task graph
- project-specific Validation Strategy
- reusable context packs and issue signatures relevant to the artifact profile

Existing projects can adopt MDE incrementally. Record first, standardize second, automate third.

### Project-Specific Validation Strategy

MDE does not hard-code one validation setup for every project. Validation categories are reusable, but validation tools and evidence are selected per project.

Core validation categories:

- Functional Validation
- Technical Validation
- Usability Validation
- UI Standards Validation
- Mission Coverage Validation
- Project-Specific External Validation

BDD belongs inside Functional Validation. It is important, but it is not the whole readiness model.

### Validation Gate

`Quality Gate` is deprecated as a standalone concept.

Phase exit is:

```text
Validation Gate passes, then the Second Validation Decision adds independent signal or records why no second-pass signal exists
```

A Validation Gate is the project-specific validation run selected for the current phase. It may include BDDs, tests, static checks, accessibility checks, usability review, UI standards review, deployment checks, data checks, or other project-relevant evidence.

The second validation is not a blind rerun. It must be independently designed and value-added. It should usually generate different scenarios, checks, data, roles, environments, or validator angles from the first gate. Rerunning the same exact deterministic test set counts only when it can expose nondeterminism, environment sensitivity, external dependency instability, or a known flaky path, and the reason must be recorded. If no credible second-pass signal exists, record `second_validation_no_signal` instead of spending time on ceremony.

### Just-In-Time Learning

Reusable learning is applied when the current work matches relevant artifact profiles. MDE uses:

- context packs
- issue signatures
- validator candidates
- project outbox records
- skill update candidates

Lessons should not automatically rewrite every related repo. Load the relevant learning when a future project touches the matching artifact type.

### Session Routing

Use `prompts/session-router.prompt.md` before choosing a Codex prompt.

The router distinguishes central MDE work, existing MDE projects with open sessions, existing MDE projects with new sessions, non-MDE projects being adopted, brand-new projects, brand-new client websites, session-end learning sync, regular learning audits, and skill promotion.

Hard rules:

- Do not re-adopt a repo that already uses MDE.
- Do not use a full project bootstrap just to continue an existing session.
- Do not use a parent-folder Codex window for normal project coding.

### Cross-Repo Learning

Project repos own their implementation. Central MDE imports only useful cross-repo learning through project outboxes:

- events
- lessons
- impacts
- content seeds
- skill update candidates
- portfolio sync records

Central learning can later become context packs, validators, templates, runbooks, or skill updates.

### Repository Ownership

One repo equals one writable Codex session. A session may read sibling repos for dependency context, but it must not edit, format, install, commit, push, or deploy another project. Cross-project changes are routed through outbox records, central MDE imports, handoff notes, or a new Codex session opened in the target repo.

### GitHub And Production Parity

After meaningful code changes or validation readiness, the project should be submitted to GitHub. If a commit or push cannot be completed, record the exact blocker in the generation evidence and final handoff.

For production-deployed projects, production must be traceable to the submitted GitHub commit. `main` should match the production deployment source unless a documented staged-release exception exists. Do not mark production readiness complete when local code, `origin/main`, and deployed production code disagree.

## Quick Start

1. Pick the right prompt with `prompts/session-router.prompt.md`.
2. For a new project, run `prompts/new-project-generation0-bootstrap.prompt.md`.
3. Define the project Validation Strategy with `prompts/project-validation-strategy-generation0.prompt.md` and `templates/validation-strategy.template.json`.
4. Load relevant context packs and issue signatures before implementation.
5. Validate with the project-specific Validation Gate, then make the Second Validation Decision.
6. Submit meaningful code changes to GitHub or record the blocker.
7. End meaningful sessions with `prompts/session-end-learning-triage-and-sync.prompt.md`.
8. Promote central-worthy learning with `prompts/central-import-project-outbox.prompt.md`.

## Public Example Implementations

These public repositories show MDE applied to real tools and websites:

- [local-website-growth-assessment](https://github.com/Northvalley-Intelligence/local-website-growth-assessment): local website assessment tooling that turns a website review into structured findings, validation evidence, and improvement direction.
- [client-website-build-brief-generator](https://github.com/Northvalley-Intelligence/client-website-build-brief-generator): a generator for client website launch packs, including assessment-to-build traceability, SEO/AEO service-area strategy, technical build prompts, and validation planning.
- [northvalleyintel.com](https://github.com/Northvalley-Intelligence/northvalleyintel.com): a public website implementation that can be inspected as an example of MDE-supported delivery for Northvalley Intelligence.

## Public Scope

This public repo is the reusable MDE backbone. Local private ledgers, active portfolio state, personal working notes, and client/private handoff material are intentionally excluded from Git.

## License

MDE is released under the [Apache License 2.0](LICENSE). Reuse is encouraged, including for commercial and internal projects. The license permits use, modification, and distribution while preserving copyright and license notices.

The license does not grant trademark rights to the Northvalley Intelligence name, marks, or branding.
