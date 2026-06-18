# Codex Mission: Add MDE Session Router, Existing-MDE Sync, Just-In-Time Learning, and Generation 0 Validation Strategy

You are working inside the `mde` repo.

This is an add-on mission after the initial portfolio memory / migration bootstrap.

Do **not** rerun the original bootstrap mission.
Do **not** recreate files that already exist unless updating them is necessary.
Do **not** merge repositories.
Do **not** move product/client repositories into `mde`.
Do **not** create a dashboard, database, CLI, or web app in this generation.

The goal is to fix four gaps:

1. Clarify which prompt to use in each kind of Codex session.
2. Add a specific flow for projects that already use MDE and already have an open Codex window.
3. Add just-in-time reusable learning so a lesson discovered in one project is applied to future relevant work in another project without forcing immediate portfolio-wide rewrites.
4. Add the missing Generation 0 project-specific Validation Strategy discipline.

---

# Strategic Context

MDE is the core platform investment for North Valley Intel.

The projects remain separate repositories.

The central `mde` repo is the shared platform memory, not a monorepo.

Codex windows and ChatGPT conversations do not share memory automatically. Therefore MDE must create durable file-based memory that future agents can read.

Important current reality:

- Some repos already use MDE and may already have Codex windows open.
- Some repos partially use MDE.
- Some repos do not use MDE yet.
- New projects will be created later.
- Some lessons discovered in one repo should influence future work in other repos.
- But lessons should usually be applied just-in-time, not by automatically changing every related repo immediately.

---

# Core Rules

## Repos stay independent

Default model:

```text
One repo = one Codex window
```

Use the central `mde` repo for shared memory, patterns, validators, context packs, ledgers, and handoff prompts.

Use project repos for project-specific implementation.

## Do not over-migrate

For existing projects:

```text
Record first.
Standardize second.
Automate third.
```

## Do not re-adopt MDE in projects that already use MDE

If a repo already has meaningful MDE artifacts, do not run the full adoption prompt.

Instead, add or update only the project-local sync contract and the just-in-time learning hooks.

## Validation tools are project-specific

Validation categories are reusable.

Validation tools are selected per project during Generation 0 or the first safe validation strategy update.

Previous tool choices may inform decisions but must not be blindly reused.

## Lessons apply just-in-time by default

When a reusable issue is discovered in one repo, do not automatically modify every related repo.

Instead:

1. Record the issue signature.
2. Add or update the relevant context pack.
3. Add or update a validator candidate.
4. Tag the applicability conditions.
5. Apply the lesson automatically the next time a future generation touches a matching artifact/profile.

Portfolio-wide audit or remediation should require an explicit request.

---

# Required New / Updated Structure

Create or update these files inside the `mde` repo.

```text
prompts/
  README.md
  session-router.prompt.md
  existing-mde-open-session-sync.prompt.md
  existing-mde-new-session-start.prompt.md
  existing-non-mde-open-session-bridge.prompt.md
  existing-non-mde-new-session-adopt.prompt.md
  new-project-generation0-bootstrap.prompt.md
  project-validation-strategy-generation0.prompt.md
  applicable-learning-check.prompt.md
  session-end-learning-triage-and-sync.prompt.md
  central-import-project-outbox.prompt.md

runbooks/
  session-routing.md
  just-in-time-learning.md
  generation0-validation-strategy.md

context-packs/
  README.md
  pdf-generation.md
  ui-forms.md
  printable-artifacts.md

knowledge/
  issue-signatures.jsonl

validators/
  README.md
  pdf/
    README.md
    pdf-margin-safety.md
  usability/
    README.md
    form-data-preservation.md
  ui-standards/
    README.md
    affordance-integrity.md

templates/
  validation-strategy.template.json
  context-pack.template.md
  issue-signature.template.json
  project-outbox-sync.template.json
```

If some of these already exist, update them rather than duplicating.

Also update existing files if present:

```text
portfolio/PROJECTS.yaml
portfolio/MIGRATION_STATUS.yaml
portfolio/STATUS.md
briefings/current-platform-brief.md
briefings/chatgpt-handoff.md
templates/project-local-mde-contract.md
MISSION.md
MISSION_UPDATES.md
```

---

# 1. Session Router

Create `prompts/session-router.prompt.md` and `runbooks/session-routing.md`.

They must clearly describe which prompt Ferosh should use in each case.

Use this routing table:

```text
CASE A: Central mde repo, Codex open
Use when: updating shared MDE memory, prompts, patterns, validators, context packs, ledgers, or briefings.
Prompt: central work does not need project adoption. Use the specific central mission or import prompt.

CASE B: Existing project already uses MDE, Codex window already open
Use when: repo already has MISSION.md, MISSION_UPDATES.md, .mde/, generations, validation, or similar MDE artifacts.
Prompt: prompts/existing-mde-open-session-sync.prompt.md
Important: do not re-adopt MDE and do not restart the session.

CASE C: Existing project already uses MDE, no Codex window open yet
Use when: starting new Codex session in a repo that already uses MDE.
Prompt: prompts/existing-mde-new-session-start.prompt.md

CASE D: Existing project does not use MDE, Codex window already open
Use when: project has an active Codex session but no meaningful MDE structure yet.
Prompt: prompts/existing-non-mde-open-session-bridge.prompt.md

CASE E: Existing project does not use MDE, no Codex window open yet
Use when: opening Codex for an old repo that needs minimal MDE adoption.
Prompt: prompts/existing-non-mde-new-session-adopt.prompt.md

CASE F: Brand-new project
Use when: starting a new project from scratch.
Prompt: prompts/new-project-generation0-bootstrap.prompt.md

CASE G: Central mde import from project outbox
Use when: a project produced .mde/outbox events, lessons, impacts, skill candidates, or content seeds.
Prompt: prompts/central-import-project-outbox.prompt.md
```

The router must explicitly say:

```text
Do not use the non-MDE adoption prompt in a repo that already uses MDE.
Do not use the full project bootstrap just to continue an existing session.
Do not use a parent-folder Codex window for normal coding.
```

---

# 2. Existing MDE Project + Open Codex Window

Create `prompts/existing-mde-open-session-sync.prompt.md`.

This prompt is for a project that already uses MDE and already has a Codex session open.

It should say:

```text
You are in an existing Codex session for a repository that already uses MDE.

Do not re-adopt MDE.
Do not restart the mission.
Do not rewrite MISSION.md unless the mission actually changed.
Do not rebuild the .mde folder from scratch.
Do not discard existing generations, validation runs, findings, or mission updates.

Your job is to bridge this already-MDE project into the central MDE portfolio memory and just-in-time learning discipline.

Before continuing work:

1. Read this repo's MISSION.md if available.
2. Read this repo's MISSION_UPDATES.md if available.
3. Read this repo's .mde/project.json if available.
4. Read this repo's .mde/state.json, .mde/generations, .mde/validation-runs, or equivalent if available.
5. Read ../mde/briefings/current-platform-brief.md if available.
6. Read ../mde/portfolio/PROJECTS.yaml if available.
7. Read ../mde/portfolio/DEPENDENCIES.yaml if available.
8. Read ../mde/context-packs/README.md and any context packs that match this project or current task.
9. Read ../mde/knowledge/issue-signatures.jsonl if available.

Then create or update only the missing sync files:

.mde/outbox/portfolio-sync.json
.mde/outbox/events.jsonl
.mde/outbox/lessons.jsonl
.mde/outbox/impacts.jsonl
.mde/outbox/content-seeds.jsonl
.mde/outbox/skill-update-candidates.jsonl

If .mde/project.json exists, preserve it and only add missing fields such as:

- artifact_profiles
- central_mde_sync_status
- context_packs
- validation_strategy_status
- downstream_dependencies
- upstream_dependencies

Do not make broad unrelated changes.

Before implementation, perform Applicable Learning Check:

- What artifact type is being touched?
- Which context packs apply?
- Which prior issue signatures apply?
- Which validators or checks should be included in this generation?
- Which downstream repos could be affected?

At the end of the session, perform Learning Triage and Sync:

1. What changed?
2. What validation ran?
3. What reusable issue signatures were discovered?
4. What context packs should be updated?
5. What validator candidates were discovered?
6. What central MDE skill update candidates were discovered?
7. What content/blog/book seeds were discovered?
8. What downstream projects are affected?
9. What outbox records were written?
10. What should be imported into central mde?

Do not dump code. Summarize in mission language.
```

---

# 3. Existing MDE Project + New Codex Window

Create `prompts/existing-mde-new-session-start.prompt.md`.

This prompt is for opening a fresh Codex window in a repo that already uses MDE.

It should say:

```text
You are starting a new Codex session in a repository that already uses MDE.

Do not run full MDE adoption.
Do not regenerate the mission unless asked.
Do not rebuild existing MDE artifacts.

Start by reading:

1. MISSION.md
2. MISSION_UPDATES.md
3. .mde/project.json
4. .mde/state.json if available
5. latest .mde/generations entry if available
6. latest .mde/validation-runs entry if available
7. ../mde/briefings/current-platform-brief.md if available
8. ../mde/portfolio/PROJECTS.yaml if available
9. ../mde/portfolio/DEPENDENCIES.yaml if available
10. ../mde/context-packs/README.md and matching context packs
11. ../mde/knowledge/issue-signatures.jsonl if available

Then report:

- current mission focus
- last known generation/validation status
- applicable reusable MDE lessons
- likely downstream impacts
- whether validation strategy exists
- whether project-local central sync outbox exists

If the sync outbox is missing, create only the missing outbox files.

Before making changes, perform Applicable Learning Check.
```

---

# 4. Existing Non-MDE Project Cases

Create `prompts/existing-non-mde-open-session-bridge.prompt.md`.

This can be based on the existing bridge prompt if present, but make it explicit that this is only for non-MDE or barely-MDE projects with an already open Codex window.

Create `prompts/existing-non-mde-new-session-adopt.prompt.md`.

This can be based on the existing adoption prompt if present, but make it explicit that this is only for repos that do not already meaningfully use MDE.

Both prompts should use minimal adoption:

```text
MISSION.md if missing
MISSION_UPDATES.md if missing
.mde/project.json
.mde/outbox/events.jsonl
.mde/lessons-local.jsonl
```

Do not force full MDE migration before project work can continue.

---

# 5. New Project Generation 0 Bootstrap

Create `prompts/new-project-generation0-bootstrap.prompt.md`.

This is for a brand-new project.

It must include the Generation 0 project-specific validation strategy discipline.

It should say:

```text
You are starting a brand-new project using MDE.

Generation 0 is not implementation.
Generation 0 creates mission clarity, project identity, validation strategy, applicable context, and initial project state.

Before writing implementation code:

1. Create MISSION.md
2. Create MISSION_UPDATES.md
3. Create .mde/project.json
4. Create .mde/state.json
5. Create .mde/outbox/events.jsonl
6. Create .mde/lessons-local.jsonl
7. Generate initial BDD inventory
8. Create initial task graph
9. Create initial risk register
10. Create project-specific Validation Strategy
11. Perform Applicable Learning Check against central MDE context packs
12. Produce Generation 0 readiness assessment

Do not assume validation tools from previous projects.

Validation categories are reusable.
Validation tools are project-specific.

Create .mde/validation-strategy.json before implementation.
```

It must invoke or inline the project validation strategy prompt below.

---

# 6. Generation 0 Project-Specific Validation Strategy

Create `prompts/project-validation-strategy-generation0.prompt.md` and `runbooks/generation0-validation-strategy.md`.

This is the missing discipline from the original bootstrap.

It must say:

```text
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
```

The strategy must ask:

```text
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
- pdf_generation
- print_layout
- web_ui
- mobile_ui
- form_workflow
- client_facing_document
- data_contract
- report_generation
- ai_generated_content
- public_content
- private_client_data

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
```

Create `.mde/validation-strategy.json` with this shape:

```json
{
  "strategy_id": "VALSTRAT-001",
  "project_type": "",
  "artifact_profiles": [],
  "mission_phase": "Generation 0",
  "selected_validations": [
    {
      "category": "Functional",
      "required": true,
      "priority": "Critical",
      "tools_or_methods": ["BDD"],
      "reason": "Validates mission-critical behavior."
    }
  ],
  "external_validators": [],
  "mde_native_validators": [],
  "skipped_validations": [
    {
      "category": "",
      "reason": "",
      "revisit_when": ""
    }
  ],
  "expensive_validations": [
    {
      "name": "",
      "run_policy": "release_only | before_phase_exit | on_affected_changes | manual"
    }
  ],
  "second_run_policy": {
    "description": "Two independent Validation Gate passes are required for phase exit, but the second run is risk-based.",
    "rerun_required": [
      "all critical validations",
      "validations that failed in the first run",
      "validations affected by code or artifact changes",
      "validations related to unresolved high risks",
      "non-deterministic or environment-sensitive validations"
    ],
    "may_skip_with_reason": [
      "validations clearly unaffected by changes",
      "expensive validations with stable prior results",
      "validations not relevant to the current phase"
    ]
  }
}
```

The runbook must also say:

```text
BDD is Functional Validation.
Quality Gate is deprecated as a standalone idea and replaced by Validation Gate.
Phase exit requires two independent Validation Gate passes, not two BDD passes.
```

---

# 7. Just-In-Time Learning

Create `prompts/applicable-learning-check.prompt.md` and `runbooks/just-in-time-learning.md`.

The Applicable Learning Check runs before implementation in any MDE-aware project.

It should say:

```text
Before implementation, check whether central MDE contains lessons relevant to this generation.

Inputs:
- current task
- project artifact_profiles
- files/artifacts likely to be changed
- central context packs
- central issue signatures
- project validation strategy

Ask:

1. What artifact type is this generation touching?
2. Which project artifact profiles apply?
3. Which context packs apply?
4. Which known issue signatures apply?
5. Which validators or checks should be added to this generation?
6. Are any downstream projects affected?
7. Should this generation update local validation strategy?

Do not apply unrelated lessons.
Do not automatically modify other repos.
Do not run portfolio-wide remediation unless explicitly requested.
```

Use the PDF example:

```text
If a prior invoice repo generation discovered PDF text overflow into margins, record issue signature PDF_TEXT_OVERFLOW_MARGIN.

When a future proposal repo generation touches PDF generation, MDE should automatically load the pdf-generation context pack and include PDF margin safety checks.

But MDE should not automatically regenerate all proposal PDFs at the time the invoice bug is fixed.
```

---

# 8. Context Packs

Create `context-packs/README.md`.

A context pack is reusable MDE knowledge that applies to a class of future work.

Context packs should be loaded just-in-time when a generation matches relevant artifact profiles.

Create initial context packs:

## `context-packs/pdf-generation.md`

Include lessons:

```text
Applicable artifact profiles:
- pdf_generation
- print_layout
- client_facing_document
- report_generation

Known issue signatures:
- PDF_TEXT_OVERFLOW_MARGIN
- PDF_CONTENT_CLIPPED
- PDF_HEADER_FOOTER_OVERLAP
- PDF_BAD_PAGE_BREAK
- PDF_TABLE_OVERFLOW

Checks:
- long text wraps or truncates intentionally
- text stays inside safe margins
- tables do not exceed page width
- headers and footers do not overlap body content
- page breaks do not split important content awkwardly
- generated PDF is validated in PDF/print mode, not only browser view
```

## `context-packs/ui-forms.md`

Include lessons:

```text
Applicable artifact profiles:
- form_workflow
- web_ui
- mobile_ui

Known issue signatures:
- FORM_DATA_LOST_ON_VALIDATION_FAILURE
- ERROR_MESSAGE_NOT_FIELD_SPECIFIC
- DISABLED_ACTION_WITHOUT_REASON

Checks:
- user input survives validation failure
- errors appear near affected fields
- user does not repeat previously successful work
- recovery path is clear
```

## `context-packs/printable-artifacts.md`

Include lessons:

```text
Applicable artifact profiles:
- print_layout
- pdf_generation
- business_document
- client_facing_document

Checks:
- print/PDF output fits page constraints
- branding remains visible and not distorted
- page breaks are acceptable
- official logo and contact details are correct
```

---

# 9. Issue Signatures

Create `knowledge/issue-signatures.jsonl` with initial examples.

Include at least:

```json
{
  "issue_signature": "PDF_TEXT_OVERFLOW_MARGIN",
  "category": "UI Standards / Usability",
  "severity_default": "High",
  "applies_to_artifact_profiles": ["pdf_generation", "print_layout", "client_facing_document", "report_generation"],
  "summary": "Generated PDF text overflows outside safe page margins.",
  "prevention": "Validate PDF output with long/adversarial text and safe margin checks before treating the artifact as complete.",
  "context_pack": "context-packs/pdf-generation.md",
  "validator_candidate": "validators/pdf/pdf-margin-safety.md"
}
```

```json
{
  "issue_signature": "FORM_DATA_LOST_ON_VALIDATION_FAILURE",
  "category": "Usability",
  "severity_default": "Critical",
  "applies_to_artifact_profiles": ["form_workflow", "web_ui", "mobile_ui"],
  "summary": "User-entered form data is cleared after a validation error.",
  "prevention": "Preserve valid user input and show field-specific recovery guidance.",
  "context_pack": "context-packs/ui-forms.md",
  "validator_candidate": "validators/usability/form-data-preservation.md"
}
```

```json
{
  "issue_signature": "FAKE_BUTTON_OR_DEAD_ACTION",
  "category": "UI Standards",
  "severity_default": "High",
  "applies_to_artifact_profiles": ["web_ui", "mobile_ui", "client_facing_workflow"],
  "summary": "An element looks clickable but performs no meaningful action, or an important action lacks a clear affordance.",
  "prevention": "Apply affordance integrity rule: if it looks clickable, it must do something useful; if it does something useful, it should look clickable.",
  "context_pack": "context-packs/ui-forms.md",
  "validator_candidate": "validators/ui-standards/affordance-integrity.md"
}
```

---

# 10. Validators

Create validator documentation stubs.

Do not build full implementations unless trivial.

## `validators/pdf/pdf-margin-safety.md`

Define:

```text
Goal:
Prevent generated PDFs from overflowing into unsafe margins, clipping content, or hiding important text.

Applies to:
- pdf_generation
- print_layout
- client_facing_document
- report_generation

Suggested checks:
- generate sample PDFs with realistic and adversarial long text
- inspect rendered PDF or extracted text bounding boxes
- fail if content crosses safe margin boundaries
- fail if table/image/content is clipped
- fail if header/footer overlaps body content

Run policy:
- when PDF templates change
- when PDF data schema changes
- when client-facing PDF is generated or regenerated
- before phase/release validation

Default severity:
High, Critical if client-facing or legal/financial artifact.
```

## `validators/usability/form-data-preservation.md`

Define checks for form data preservation after validation failure.

## `validators/ui-standards/affordance-integrity.md`

Define checks for fake buttons, dead links, hidden actions, and disabled controls without explanation.

---

# 11. Project-Local Sync Contract Update

Update `templates/project-local-mde-contract.md`.

For projects that already use MDE, the minimum central sync addition is:

```text
.mde/outbox/
  portfolio-sync.json
  events.jsonl
  lessons.jsonl
  impacts.jsonl
  content-seeds.jsonl
  skill-update-candidates.jsonl
```

`portfolio-sync.json` should include:

```json
{
  "project_id": "",
  "project_name": "",
  "mde_status": "active | partial | migrated | not_started",
  "artifact_profiles": [],
  "context_packs": [],
  "validation_strategy_status": "missing | draft | active | needs_update",
  "latest_generation": "",
  "latest_validation_gate_result": "unknown | pass | fail",
  "upstream_dependencies": [],
  "downstream_dependencies": [],
  "last_sync_note": ""
}
```

Project-local outbox records are written by project Codex windows.

Central `mde` imports them using `prompts/central-import-project-outbox.prompt.md`.

---

# 12. Central Import Prompt

Create `prompts/central-import-project-outbox.prompt.md`.

It should say:

```text
You are in the central mde repo.

Import project-local MDE outbox records from a project repo.

Inputs:
- path to project repo
- project .mde/outbox/portfolio-sync.json
- project .mde/outbox/events.jsonl
- project .mde/outbox/lessons.jsonl
- project .mde/outbox/impacts.jsonl
- project .mde/outbox/content-seeds.jsonl
- project .mde/outbox/skill-update-candidates.jsonl

Tasks:

1. Update portfolio/PROJECTS.yaml if project metadata changed.
2. Update portfolio/DEPENDENCIES.yaml if dependency information changed.
3. Append meaningful events to ledger/events.jsonl.
4. Append reusable lessons to ledger/lessons.jsonl.
5. Append content seeds to ledger/content-seeds.jsonl.
6. Append skill update candidates to ledger/skill-update-candidates.jsonl.
7. Update knowledge/issue-signatures.jsonl if a reusable issue signature was discovered.
8. Update or create context packs if a reusable lesson should apply just-in-time to future work.
9. Update briefings/current-platform-brief.md.
10. Update briefings/chatgpt-handoff.md if the user may need to discuss this outside Codex.

Do not blindly import project-only noise.
Do not make every local lesson global.
Preserve confidentiality labels.
```

---

# 13. Session-End Learning Triage and Sync

Create `prompts/session-end-learning-triage-and-sync.prompt.md`.

This should replace or enhance the existing session-end triage prompt.

It should say:

```text
Before ending, perform MDE Learning Triage and Sync.

Report in mission language, not code dumps.

Answer:

1. What changed?
2. What artifact profiles were touched?
3. What validation ran?
4. Did the Validation Gate pass or fail?
5. Did we discover a reusable issue signature?
6. Does a central context pack need to be updated?
7. Does a validator need to be created or improved?
8. Is this a skill update candidate?
9. Is this a blog/book/content seed?
10. Are downstream repos affected immediately?
11. Should this lesson apply just-in-time to future generations?
12. What was written to .mde/outbox?
13. What should central mde import?

If a reusable lesson was discovered, record it in .mde/outbox/lessons.jsonl.
If a new issue signature was discovered, record it in .mde/outbox/impacts.jsonl or a suitable outbox record.
If content-worthy, record it in .mde/outbox/content-seeds.jsonl.
If MDE skill behavior should change, record it in .mde/outbox/skill-update-candidates.jsonl.
```

---

# 14. Update Portfolio Project Schema

Update `portfolio/PROJECTS.yaml` entries to support:

```yaml
artifact_profiles:
  - pdf_generation
  - print_layout
  - web_ui
  - form_workflow
  - data_contract
  - report_generation
  - client_facing_document

context_packs:
  - pdf-generation
  - ui-forms

validation_strategy_status: missing | draft | active | needs_update
central_sync_status: not_started | partial | active
```

Use best-effort classifications for known projects.

Examples:

```yaml
- id: proposals
  artifact_profiles:
    - pdf_generation
    - report_generation
    - client_facing_document
    - print_layout
  context_packs:
    - pdf-generation
    - printable-artifacts
  validation_strategy_status: missing
```

```yaml
- id: northvalley-receipts-invoices-flyers
  artifact_profiles:
    - pdf_generation
    - print_layout
    - business_document
    - client_facing_document
  context_packs:
    - pdf-generation
    - printable-artifacts
  validation_strategy_status: missing
```

```yaml
- id: jacob-family
  artifact_profiles:
    - web_ui
    - form_workflow
    - personalized_software
  context_packs:
    - ui-forms
  validation_strategy_status: unknown
```

---

# 15. Update Briefings

Update `briefings/current-platform-brief.md` to include:

```text
## Session Routing
Which prompt to use for each kind of Codex session.

## Just-In-Time Learning
Reusable lessons are applied when future work touches matching artifact profiles.

## Generation 0 Validation Strategy
New projects and first safe validation updates must define project-specific validation strategy.

## Known Context Packs
List current context packs.

## Known Issue Signatures
List important issue signatures.
```

Update `briefings/chatgpt-handoff.md` similarly so Ferosh can paste it into ChatGPT without retelling the story.

---

# 16. Update Mission Documents

Update `MISSION.md` and `MISSION_UPDATES.md` to record this MDE improvement.

The update should say:

```text
MDE now distinguishes session routing cases, including projects that already use MDE with open Codex windows.

MDE now supports just-in-time reusable learning through context packs and issue signatures.

MDE now requires project-specific Validation Strategy during Generation 0 for new projects or during the first safe validation update for existing projects.

Quality Gate is deprecated as a standalone concept. Phase exit is based on two independent Validation Gate passes.
```

---

# Final Report

After implementation, provide a concise summary:

```text
MDE Session Router + JIT Learning + Gen0 Validation Update Summary

Created:
- ...

Updated:
- ...

New session routing:
- existing MDE + open Codex: ...
- existing MDE + new Codex: ...
- non-MDE + open Codex: ...
- non-MDE + new Codex: ...
- brand-new project: ...

Generation 0 validation strategy:
- ...

Just-in-time learning:
- ...

What Ferosh should run next:
- ...

Open risks:
- ...
```

Do not dump full file contents unless necessary.
