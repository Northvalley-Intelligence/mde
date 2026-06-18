# Codex Mission: Bootstrap MDE Portfolio Memory and Migration Discipline

You are working inside the `mde` repo.

This mission is primarily for the `mde` repo.

Do not merge repositories.
Do not move product/client repositories into `mde`.
Do not build a dashboard, database, CLI, or web app yet.
Do not attempt to fully migrate every project in this generation.

The goal is to create a lightweight file-based memory, migration, and coordination layer for many independent but connected repositories.

Use Markdown, YAML, and JSONL.
Keep the implementation simple, durable, and easy for future agents to read.

---

# Strategic Context

MDE is the core platform investment for North Valley Intel.

The long-term goal is to make personalized software economically viable.

The Jacob Family app is a case study proving that personalized software can be built and maintained economically. It is not a side project.

Other client, product, content, and operations projects should continuously teach MDE.

When issues are found in real projects, such as:

- UI bugs
- validation failures
- report formatting problems
- proposal generation issues
- cross-repo data contract problems
- deployment issues
- client delivery problems
- voucher or PDF formatting problems

those lessons should be captured and, when appropriate, promoted into:

- reusable MDE patterns
- reusable validators
- skill update candidates
- blog ideas
- LinkedIn ideas
- book notes

Codex windows do not share memory automatically.
ChatGPT and Codex do not share memory automatically.
Existing Codex windows may already be open and may not yet be using MDE.
Some repositories may have partial MDE artifacts.
Some repositories may have no MDE artifacts yet.

Therefore, MDE must create durable artifacts that carry context across repos, Codex windows, and future conversations.

Do not rely on chat history.
Use files as durable memory.

---

# Operating Model

Keep separate repositories.

Default daily work model:

```text
One repo = one Codex window
```

Examples:

```text
Codex window in jacob-family
  Fix app UI or family software behavior.

Codex window in demand-data-generation
  Update data collection or schema.

Codex window in local-website-growth-assessment
  Regenerate assessment reports.

Codex window in proposals
  Format and regenerate client proposal.

Codex window in mde
  Update shared memory, lessons, patterns, validators, content seeds.
```

A parent-folder Codex window may be used only for cross-repo coordination and inspection when explicitly requested.

Do not use a parent-folder window as the normal coding environment because it increases the risk of editing the wrong repo or mixing concerns.

The `mde` repo is the shared platform memory, not a monorepo.

---

# Known Repositories / Projects

Use these known projects to initialize the portfolio registry.

## codex-skills

Contains the MDE skill used by Codex.

## mde

MDE architecture, philosophy, platform notes, LinkedIn/blog/book material, and shared platform memory.

## jacoob-family-app

Customized family software, older or TODO direction.

## jacob-family

Current/latest family web app implementation and personalized software case study.

## medinaclean.com

Current client project. Will migrate to MDE.

## northvalleyintel.com

Company website. Will migrate to MDE.

## demand-data-generation

Data generation project used for lead acquisition and website assessments.
Produces data consumed by website assessment/reporting workflows.
Built or being migrated using MDE.

## local-website-growth-assessment

Assessment report generator. Consumes demand data and produces website quality/growth assessment outputs.
Will migrate to MDE.

## proposals

Formats assessment outputs into client/prospect reports before sending.
Consumes demand-data-generation and local-website-growth-assessment outputs.

## northvalley-business-cards

Public GitHub repo for creating business cards.

## northvalley-receipts-invoices-flyers

Private repo for official North Valley Intel formatting assets, logo usage, receipts, invoices, flyers, vouchers, etc.

## software-cost-ai-era

Possible duplicate or source material for MDE thinking.

## feroshjacob

Hosts actual blog posts referenced from LinkedIn.

---

# Objective

Create the initial MDE Portfolio Memory and Migration Discipline inside the `mde` repo.

This system should help future agents understand:

1. What projects exist
2. How projects depend on each other
3. Which workflows cross repository boundaries
4. Which projects already use MDE
5. Which projects need migration
6. Which existing Codex sessions need bridge instructions
7. What lessons from projects should improve MDE
8. What lessons may become blog/book content
9. What handoff context should be given to future Codex or ChatGPT sessions
10. What downstream projects may be affected when one repo changes

---

# Migration Principle

Do not block existing work waiting for a perfect migration.

Migration should be incremental.

Use this rule:

```text
Record first.
Standardize second.
Automate third.
```

For repositories that do not yet use MDE, create enough structure to preserve context and support handoffs.
Do not force a full MDE conversion immediately.

For existing Codex windows, do not restart just to adopt MDE.
Instead, bridge the session by asking it to summarize current state and produce project-local MDE outbox events.

---

# Required Structure

Create or update this structure inside the `mde` repo:

```text
portfolio/
  PROJECTS.yaml
  DEPENDENCIES.yaml
  FLOWS.yaml
  STATUS.md
  MIGRATION_STATUS.yaml

ledger/
  events.jsonl
  decisions.jsonl
  lessons.jsonl
  content-seeds.jsonl
  skill-update-candidates.jsonl

patterns/
  README.md

validators/
  README.md

migration/
  README.md
  MIGRATION_PLAN.md
  EXISTING_SESSIONS.md
  PROJECT_ADOPTION_ORDER.md

runbooks/
  README.md
  cross-repo-change.md
  regenerate-website-assessment.md
  regenerate-proposal.md
  promote-project-learning.md
  capture-content-seed.md
  adopt-mde-in-existing-project.md
  bridge-existing-codex-session.md

briefings/
  current-platform-brief.md
  chatgpt-handoff.md
  codex-handoff-template.md

prompts/
  existing-codex-session-bridge.prompt.md
  adopt-mde-in-existing-project.prompt.md
  new-codex-session-start.prompt.md
  codex-session-end-triage.prompt.md
  cross-repo-impact-check.prompt.md

templates/
  project-record.template.yaml
  dependency-record.template.yaml
  event-record.template.json
  lesson-record.template.json
  content-seed.template.json
  generation-handoff.template.md
  project-local-mde-contract.md
```

If similar files already exist, update them instead of duplicating.

---

# Project Registry

Create `portfolio/PROJECTS.yaml`.

Each project should have fields like:

```yaml
- id: demand-data-generation
  name: Demand Data Generation
  type: product
  repo_or_path: "../demand-data-generation"
  status: active
  mde_status: partial
  migration_priority: 1
  business_role: "Generates data used for lead acquisition and website assessments."
  owner: "Ferosh"
  confidentiality: private
  upstream_dependencies: []
  downstream_dependencies:
    - local-website-growth-assessment
    - proposals
  primary_artifacts:
    - "assessment input data"
    - "demand signals"
  current_session_status: unknown
  notes: ""
```

Use thoughtful classifications.

Suggested `type` values:

```text
platform
product
client
content
operations
personal-case-study
public-asset
```

Suggested `status` values:

```text
active
planned
paused
archived
unknown
```

Suggested `mde_status` values:

```text
not_started
partial
active
migrated
unknown
```

Suggested `confidentiality` values:

```text
public
private
client-confidential
unknown
```

Suggested `current_session_status` values:

```text
no_known_session
existing_session_unbridged
existing_session_bridged
unknown
```

---

# Migration Status

Create `portfolio/MIGRATION_STATUS.yaml`.

Track adoption without requiring all projects to migrate at once.

Example:

```yaml
migration:
  strategy: "incremental"
  rule: "Record first, standardize second, automate third."
  projects:
    - project: mde
      mde_status: active
      next_step: "Bootstrap portfolio memory."
      priority: 0
      reason: "Shared memory must exist before other migrations."

    - project: demand-data-generation
      mde_status: partial
      next_step: "Add project-local .mde contract and outbox events for data contract changes."
      priority: 1
      reason: "Upstream dependency for assessment and proposal workflows."

    - project: local-website-growth-assessment
      mde_status: partial
      next_step: "Add project-local MDE contract and consume demand-data-generation events."
      priority: 2
      reason: "Consumes generated data and produces assessment outputs."

    - project: proposals
      mde_status: not_started
      next_step: "Add project-local MDE contract and proposal regeneration runbook."
      priority: 3
      reason: "Client-facing artifact formatting depends on assessment output."
```

Recommended initial migration order:

```text
0. mde
1. demand-data-generation
2. local-website-growth-assessment
3. proposals
4. jacob-family
5. medinaclean.com
6. northvalleyintel.com
7. feroshjacob
8. northvalley-receipts-invoices-flyers
9. northvalley-business-cards
10. jacoob-family-app
11. software-cost-ai-era
```

This order can change, but record why.

---

# Dependency Graph

Create `portfolio/DEPENDENCIES.yaml`.

Track how projects depend on each other.

At minimum include:

```yaml
dependencies:
  - id: DEP-001
    from: demand-data-generation
    to: local-website-growth-assessment
    type: data_contract
    description: "Website assessment report consumes generated demand/website quality data."
    contract_artifacts:
      - "output schema"
      - "sample generated data"
    risk_level: high
    validation_needed:
      - "schema compatibility"
      - "sample report generation"

  - id: DEP-002
    from: local-website-growth-assessment
    to: proposals
    type: report_input
    description: "Proposal formatting consumes assessment report outputs."
    contract_artifacts:
      - "assessment report output"
      - "proposal input fields"
    risk_level: high
    validation_needed:
      - "proposal regeneration"
      - "formatting validation"
```

The purpose is to let agents identify downstream impact when a repo changes.

---

# Workflow Map

Create `portfolio/FLOWS.yaml`.

Track important cross-repo workflows.

At minimum include:

```yaml
flows:
  - id: FLOW-WEB-ASSESSMENT-TO-PROPOSAL
    name: Website assessment to client proposal
    purpose: "Generate website assessment data, convert it into an assessment report, then format it into a proposal for a client or prospect."
    steps:
      - project: demand-data-generation
        action: "Generate or update source data"
      - project: local-website-growth-assessment
        action: "Regenerate website assessment report"
      - project: proposals
        action: "Format/send client-facing proposal"
    validation:
      - "Data contract compatibility"
      - "Report generation succeeds"
      - "Proposal formatting succeeds"
      - "Human-readable report is clear"
    content_opportunity:
      - "Lessons about connected AI workflows"
      - "Lessons about data contracts across agent-built products"

  - id: FLOW-PROJECT-LESSON-TO-MDE
    name: Project lesson to MDE improvement
    purpose: "Convert project-specific issues into reusable MDE lessons, patterns, validators, or skill updates."
    steps:
      - project: any
        action: "Discover issue or complete generation"
      - project: mde
        action: "Record lesson"
      - project: mde
        action: "Decide whether to promote into pattern, validator, skill update, or content seed"
```

---

# Event Ledger

Create `ledger/events.jsonl`.

This is append-only.

Every meaningful cross-project event should be recorded as one JSON object per line.

Event types may include:

```text
generation_completed
data_contract_changed
artifact_generated
report_regenerated
proposal_regenerated
client_delivery
bug_fixed
validation_failed
validation_passed
mde_lesson_discovered
pattern_candidate_discovered
validator_candidate_discovered
skill_update_candidate_discovered
content_seed_discovered
dependency_changed
migration_started
migration_completed
session_bridged
```

Create the file with one initial event documenting that the portfolio memory system was initialized.

Event record shape:

```json
{
  "event_id": "EVT-YYYY-MM-DD-001",
  "timestamp": "YYYY-MM-DDTHH:MM:SS-04:00",
  "project": "mde",
  "event_type": "generation_completed",
  "generation": "GEN-000",
  "summary": "Initialized MDE Portfolio Memory and Migration Discipline.",
  "why_it_matters": "Creates durable cross-repo memory for Codex, ChatGPT, existing sessions, and future MDE work.",
  "changed_artifacts": [],
  "upstream": [],
  "downstream_impacts": [],
  "reusable_learning": [],
  "content_seed_ids": [],
  "confidentiality": "private"
}
```

---

# Lessons Ledger

Create `ledger/lessons.jsonl`.

A lesson is anything learned from a project that may help future MDE work.

Lesson types:

```text
project_only
reusable_pattern
validator_improvement
skill_improvement
content_insight
business_process
client_delivery
migration
```

Create the file with an initial lesson explaining that MDE needs durable memory because separate Codex windows do not share context.

Lesson record shape:

```json
{
  "lesson_id": "LESSON-YYYY-MM-DD-001",
  "timestamp": "YYYY-MM-DDTHH:MM:SS-04:00",
  "source_project": "mde",
  "source_event": "EVT-YYYY-MM-DD-001",
  "lesson_type": "reusable_pattern",
  "summary": "MDE needs durable cross-window memory.",
  "problem": "Separate Codex windows and ChatGPT conversations do not automatically share project context.",
  "mde_implication": "Use portfolio registries, ledgers, briefings, and handoff templates as persistent memory.",
  "recommended_destination": "patterns/cross-repo-memory.md",
  "promotion_status": "candidate",
  "content_potential": true,
  "confidentiality": "private"
}
```

---

# Content Seeds

Create `ledger/content-seeds.jsonl`.

This is for future LinkedIn posts, blog posts, talks, or book chapters.

Do not force every lesson to become content.
Capture only useful stories.

Create one initial content seed about cross-repo memory for agentic software.

Content seed shape:

```json
{
  "content_id": "CONTENT-YYYY-MM-DD-001",
  "timestamp": "YYYY-MM-DDTHH:MM:SS-04:00",
  "source_project": "mde",
  "source_event": "EVT-YYYY-MM-DD-001",
  "theme": "Agentic software needs durable cross-repo memory",
  "working_title": "The Problem Is Not That AI Forgets, It Is That We Do Not Give It a Memory",
  "core_insight": "Separate repos and separate AI windows create invisible dependencies unless the platform records events, dependencies, and handoffs as durable artifacts.",
  "possible_outline": [
    "Separate repos create invisible dependencies",
    "Chat windows do not share memory",
    "Durable artifacts become the coordination layer",
    "MDE turns project work into platform learning"
  ],
  "public_safe": true,
  "redaction_notes": "Avoid naming private client details unless approved.",
  "status": "seeded"
}
```

---

# Skill Update Candidates

Create `ledger/skill-update-candidates.jsonl`.

Track possible updates to `codex-skills/mde-skill`.

Important:

Do not automatically update the shared skill for every local lesson.
Skill updates should be candidates first.

Create an initial candidate suggesting that the MDE skill should include learning triage, handoff discipline, and migration discipline.

Candidate shape:

```json
{
  "candidate_id": "SKILL-CANDIDATE-YYYY-MM-DD-001",
  "timestamp": "YYYY-MM-DDTHH:MM:SS-04:00",
  "source_project": "mde",
  "summary": "Add Learning Triage, Handoff Discipline, and Migration Discipline to the MDE skill.",
  "reason": "Every generation should decide whether local work produced reusable MDE learning, validator improvements, skill updates, content seeds, or downstream impacts.",
  "proposed_skill_change": "Update MDE skill so every generation ends with Learning Triage and produces a handoff note when cross-repo context matters. Existing projects should be migrated gradually using project-local MDE contracts.",
  "risk": "Too much ceremony if applied to trivial changes.",
  "status": "candidate"
}
```

---

# Briefings

Create `briefings/current-platform-brief.md`.

This should be a concise current-state summary that any Codex window or ChatGPT conversation can read.

Include:

```text
# Current MDE Platform Brief

## What MDE Is

## Current Strategic Goal

## Active Projects

## Current Migration Status

## Key Project Dependencies

## Current Cross-Repo Workflows

## Recent Important Events

## Open Cross-Project Impacts

## Existing Codex Sessions To Bridge

## Reusable Lessons Waiting for Promotion

## Skill Update Candidates

## Content Seeds

## What To Tell A New Agent
```

Create `briefings/chatgpt-handoff.md`.

This should be optimized for pasting into ChatGPT when asking for help.

It should include enough context so Ferosh does not need to retell the story.

Use this style:

```text
I am Ferosh Jacob. I am building MDE as the core platform for North Valley Intel.

MDE helps build personalized software economically.

My projects are separate repos, but connected.

Current active projects:
...

Current migration status:
...

Current issue:
...

Recent events:
...

Open decisions:
...

Please answer using this context.
```

Create `briefings/codex-handoff-template.md`.

This should be a reusable template to paste into a new Codex window.

---

# Migration Files

Create `migration/MIGRATION_PLAN.md`.

Explain:

```text
The goal is not to migrate every repo at once.
The goal is to gradually add enough MDE structure to each project so learning, validation, and cross-repo impacts are not lost.
```

Include migration phases:

```text
Phase 0: Bootstrap MDE portfolio memory in the mde repo.
Phase 1: Record all projects and dependencies.
Phase 2: Bridge existing Codex sessions.
Phase 3: Add minimal project-local MDE contract to highest-impact repos.
Phase 4: Add validation/generation artifacts as projects naturally receive work.
Phase 5: Promote repeated lessons into shared patterns, validators, or skill updates.
```

Create `migration/EXISTING_SESSIONS.md`.

Track current Codex sessions that Ferosh may already have open.

Include columns:

```text
Project
Session status
Last known focus
MDE adoption status
Bridge prompt pasted? yes/no/unknown
Handoff captured? yes/no/unknown
Downstream impacts known?
Next action
```

Initialize rows for known projects with unknowns when necessary.

Create `migration/PROJECT_ADOPTION_ORDER.md`.

Explain why migration should start with:

```text
mde
→ demand-data-generation
→ local-website-growth-assessment
→ proposals
```

because this is the most important cross-repo workflow for revenue and client delivery.

Then migrate:

```text
jacob-family
→ medinaclean.com
→ northvalleyintel.com
→ operations/content repos
```

unless real work makes a different repo urgent.

---

# Project-Local MDE Contract

Create `templates/project-local-mde-contract.md`.

Each project using MDE should eventually have:

```text
.mde/
  project.json
  generations/
  validation-runs/
  findings.json
  lessons-local.jsonl
  outbox/
    events.jsonl
```

Also recommend, where appropriate:

```text
MISSION.md
MISSION_UPDATES.md
```

Minimal adoption for an existing project only requires:

```text
.mde/project.json
.mde/outbox/events.jsonl
.mde/lessons-local.jsonl
```

Do not require full MDE validation/generation structure before normal project work can continue.

Each project-local event that has cross-repo impact should be copied or promoted into:

```text
mde/ledger/events.jsonl
```

---

# Prompts For Existing and Future Codex Sessions

Create `prompts/existing-codex-session-bridge.prompt.md`.

This is for Ferosh to paste into a Codex window that is already open.

It should say:

```text
You are in an existing Codex session for this repository.
We are adopting the MDE portfolio memory discipline without restarting the session.

Do not rewrite history.
Do not perform a large refactor.

Before continuing, create or update minimal local MDE context:

1. Create `.mde/project.json` if missing.
2. Create `.mde/outbox/events.jsonl` if missing.
3. Create `.mde/lessons-local.jsonl` if missing.
4. Summarize the current session focus.
5. Identify whether current work affects downstream projects.
6. If downstream impact exists, create an event in `.mde/outbox/events.jsonl`.
7. Produce a short handoff note that can be copied into the central `mde` repo.

Use the central MDE portfolio files when available:

- `../mde/briefings/current-platform-brief.md`
- `../mde/portfolio/DEPENDENCIES.yaml`
- `../mde/portfolio/PROJECTS.yaml`

Then continue the current project work.
```

Create `prompts/adopt-mde-in-existing-project.prompt.md`.

This is for a repo that has not started using MDE yet.

It should say:

```text
Adopt minimal MDE structure for this existing repository.

Do not refactor application code unless required.
Do not generate a large process framework.

Create:

- MISSION.md if missing
- MISSION_UPDATES.md if missing
- .mde/project.json
- .mde/outbox/events.jsonl
- .mde/lessons-local.jsonl

Then produce:

- current project summary
- known upstream dependencies
- known downstream dependencies
- current validation status if known
- migration risks
- next recommended MDE adoption step

If this repo is connected to other projects, record a project-local event in `.mde/outbox/events.jsonl`.
```

Create `prompts/new-codex-session-start.prompt.md`.

This is for every new repo-specific Codex session.

It should say:

```text
Before starting work:

1. Read this repository's MISSION.md if available.
2. Read this repository's .mde/project.json if available.
3. Read ../mde/briefings/current-platform-brief.md if available.
4. Read ../mde/portfolio/DEPENDENCIES.yaml if available.
5. Tell me whether this work may affect downstream projects.
6. Tell me whether this repo needs MDE migration before work can safely continue.

Do not make broad unrelated changes.
```

Create `prompts/codex-session-end-triage.prompt.md`.

This is for the end of every meaningful Codex session.

It should say:

```text
Before ending, perform MDE Learning Triage.

Tell me:

1. What changed?
2. Did validation pass?
3. Was this project-only learning?
4. Is there a reusable MDE pattern?
5. Is there a validator improvement?
6. Is there a skill update candidate?
7. Is there a blog/book/content seed?
8. Are downstream repos affected?
9. Should an event be added to .mde/outbox/events.jsonl?
10. Should the central mde repo be updated?

Do not dump code. Summarize in mission language.
```

Create `prompts/cross-repo-impact-check.prompt.md`.

This is for when one repo changes something that may affect others.

It should say:

```text
Check cross-repo impact.

Use:

- ../mde/portfolio/DEPENDENCIES.yaml
- ../mde/portfolio/FLOWS.yaml
- this repo's .mde/outbox/events.jsonl

Identify:

1. What changed?
2. Which upstream/downstream projects are affected?
3. Which artifacts or data contracts changed?
4. Which runbooks should be executed next?
5. Which validations are required?
6. Which handoff note should be created?
```

---

# Runbooks

Create `runbooks/cross-repo-change.md`.

Include this process:

```text
1. Identify source project
2. Identify changed artifact
3. Check DEPENDENCIES.yaml for downstream projects
4. Record event in source project .mde/outbox/events.jsonl if available
5. Record central event in mde/ledger/events.jsonl if cross-project impact exists
6. Create downstream impact list
7. Decide if downstream projects need immediate updates
8. Record reusable lesson if applicable
9. Record content seed if there is a good story
10. Update current-platform-brief.md
11. Create handoff note for next Codex window
```

Include this example:

```text
If demand-data-generation changes output schema:

Impacted:
- local-website-growth-assessment
- proposals

Required checks:
- schema compatibility
- assessment report regeneration
- proposal regeneration
- formatting validation
```

Create `runbooks/adopt-mde-in-existing-project.md`.

Explain the minimal migration path:

```text
1. Do not refactor code first.
2. Create project-local .mde identity.
3. Record current state.
4. Record upstream/downstream dependencies.
5. Add outbox for cross-repo events.
6. Add local lessons ledger.
7. Add validation/generation artifacts later as real work happens.
```

Create `runbooks/bridge-existing-codex-session.md`.

Explain how to migrate an already-open session without losing its work:

```text
1. Paste the existing-codex-session-bridge prompt.
2. Ask Codex to summarize current session state.
3. Ask Codex to create minimal .mde files if missing.
4. Ask Codex to identify downstream impacts.
5. Ask Codex to produce a handoff note.
6. Copy important outbox events into the central mde ledger when appropriate.
```

Create `runbooks/promote-project-learning.md`.

Every generation should end with MDE Learning Triage.

Ask:

```text
What did we learn?

Is it:
1. Project-only learning?
2. Reusable MDE pattern?
3. Validator improvement?
4. Skill update candidate?
5. Content/blog/book insight?
6. Business process improvement?
```

Promotion rules:

```text
Do not promote everything.

Promote only if:
- likely to recur across projects
- improves validation or generation quality
- reduces future maintenance cost
- improves personalized software delivery
- helps explain MDE publicly
```

Include examples:

```text
Jacob Family UI bug:
- form validation clears user input
- project fix: update form behavior
- MDE lesson: add usability validator for data preservation
- content seed: AI-generated apps often pass BDDs but fail recovery usability

Voucher formatting bug:
- print layout breaks on page boundary
- project fix: update print CSS/template
- MDE lesson: printable artifacts require print-mode validation
- validator candidate: PDF/print layout validation
- content seed: printed business artifacts need validation, not just visual review
```

Create `runbooks/regenerate-website-assessment.md`.

Include:

```text
Inputs:
- demand-data-generation outputs
- website target/client data
- assessment configuration

Steps:
1. Check latest demand-data-generation event
2. Verify data schema version
3. Run local-website-growth-assessment
4. Validate report output
5. Record artifact_generated event
6. Check whether proposals must be regenerated
```

Create `runbooks/regenerate-proposal.md`.

Include:

```text
Inputs:
- assessment report
- client/prospect details
- proposal template
- pricing/offer details

Steps:
1. Check latest assessment report event
2. Generate proposal
3. Validate formatting
4. Validate public/client-safe content
5. Record proposal_regenerated event
6. Capture content seed if useful
```

Create `runbooks/capture-content-seed.md`.

Explain how to capture a future blog, LinkedIn, or book idea from project work.

---

# Templates

Create templates for:

```text
templates/project-record.template.yaml
templates/dependency-record.template.yaml
templates/event-record.template.json
templates/lesson-record.template.json
templates/content-seed.template.json
templates/generation-handoff.template.md
templates/project-local-mde-contract.md
```

---

# Handoff Discipline

Document this rule clearly.

Before starting work in any Codex window:

1. Read project-local `MISSION.md` if available
2. Read project-local `.mde/project.json` if available
3. Read `mde/briefings/current-platform-brief.md`
4. Check `mde/portfolio/DEPENDENCIES.yaml`
5. Check whether the work affects downstream projects

After completing work in any Codex window:

1. Write generation summary locally
2. Record cross-project event if relevant
3. Record lesson if relevant
4. Record content seed if useful
5. Update `mde/briefings/current-platform-brief.md` if platform context changed
6. Produce a handoff note

For already-open Codex sessions:

1. Do not restart automatically
2. Paste `prompts/existing-codex-session-bridge.prompt.md`
3. Capture current state
4. Create minimal local MDE files
5. Record downstream impacts
6. Continue work

---

# Update Mission Documents

Update `MISSION.md` and `MISSION_UPDATES.md` if they exist.

Explain that MDE now includes:

- portfolio memory
- incremental migration
- cross-repo coordination
- project dependency tracking
- existing session bridging
- learning triage
- content seed capture
- Codex/ChatGPT handoff discipline

If these files do not exist, create simple initial versions.

---

# Important Constraints

Do not overbuild.
Do not create a SaaS dashboard.
Do not create a database.
Do not create a CLI.
Do not require all repos to move.
Do not require all repos to fully migrate immediately.
Do not block normal project work.
Do not make every lesson global.
Do not expose private client information in public-facing content.
Do not use the parent-folder Codex window as the normal coding environment.

Use simple files first.

---

# Final Report

After implementation, provide this concise summary:

```text
MDE Portfolio Memory and Migration Summary

Created:
- ...

Updated:
- ...

Migration model:
- ...

How to use before a Codex session:
- ...

How to bridge an existing Codex session:
- ...

How to use after a Codex session:
- ...

Example connected workflow:
- demand-data-generation changes
- local-website-growth-assessment must update
- proposals may need regeneration
- lesson/content seed should be captured

Open risks:
- ...

Recommended next generation:
- ...
```

Do not dump full file contents unless necessary.
Focus on how this improves cross-repo coordination, MDE learning, migration, and future blog/book writing.
