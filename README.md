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
Validation Gate passed twice
```

A Validation Gate is the project-specific validation run selected for the current phase. It may include BDDs, tests, static checks, accessibility checks, usability review, UI standards review, deployment checks, data checks, or other project-relevant evidence.

The second pass is risk-based and should run with no implementation changes between clean passes.

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

## Quick Start

1. Pick the right prompt with `prompts/session-router.prompt.md`.
2. For a new project, run `prompts/new-project-generation0-bootstrap.prompt.md`.
3. Define the project Validation Strategy with `prompts/project-validation-strategy-generation0.prompt.md` and `templates/validation-strategy.template.json`.
4. Load relevant context packs and issue signatures before implementation.
5. Validate with the project-specific Validation Gate, then run the required second pass.
6. End meaningful sessions with `prompts/session-end-learning-triage-and-sync.prompt.md`.
7. Promote central-worthy learning with `prompts/central-import-project-outbox.prompt.md`.

## Public Example Implementations

These public repositories show MDE applied to real tools and websites:

- [local-website-growth-assessment](https://github.com/Northvalley-Intelligence/local-website-growth-assessment): local website assessment tooling that turns a website review into structured findings, validation evidence, and improvement direction.
- [client-website-build-brief-generator](https://github.com/Northvalley-Intelligence/client-website-build-brief-generator): a generator for client website launch packs, including assessment-to-build traceability, SEO/AEO service-area strategy, technical build prompts, and validation planning.
- [northvalleyintel.com](https://github.com/Northvalley-Intelligence/northvalleyintel.com): a public website implementation that can be inspected as an example of MDE-supported delivery for Northvalley Intelligence.

## Public Scope

This public repo is the reusable MDE backbone. Local private ledgers, active portfolio state, personal working notes, and client/private handoff material are intentionally excluded from Git.
