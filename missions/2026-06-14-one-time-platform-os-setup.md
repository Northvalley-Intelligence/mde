# Codex Mission: One-Time MDE Platform Operating System Setup

You are working in the central `mde` repo.

This mission consolidates the scattered MDE setup work into one idempotent update.

Run this once in the central `mde` repo.

If previous portfolio/migration files already exist, update them instead of duplicating them.
If earlier prompts or runbooks exist, merge the new concepts into them.
Do not delete useful historical information.
Do not restart the MDE architecture from scratch.

---

# Strategic Context

MDE is the core platform investment for North Valley Intel.

The goal is to make personalized software economically viable by using AI agents, durable project memory, validation, and continuous learning.

The Jacob Family app is a case study for personalized software. It is not a side project.

Client websites, website assessment, demand data generation, proposals, invoices, PDFs, CRM, content, and mobile apps should all teach MDE over time.

MDE should support separate repositories, separate Codex windows, and evolving skills.

Do not merge repositories into a monorepo.

Use the central `mde` repo as the shared platform memory and coordination layer.

---

# Core Problem To Solve

Ferosh has many connected repositories and will continue adding more.

Codex windows do not automatically share memory.
ChatGPT conversations do not automatically share memory.
Individual project repos may learn useful lessons that should improve the MDE platform.
New projects should get a quick start from the latest MDE knowledge.
MDE should be checked regularly to ensure it is actually learning from project work.

The platform needs durable files that let future agents answer:

- What projects exist?
- How are projects connected?
- Which projects already use MDE?
- Which projects need migration?
- Which skills/prompts should be used in each situation?
- What reusable lessons were discovered?
- Which validators or guardrails should apply just-in-time?
- Which lessons should become blog posts, LinkedIn posts, or book notes?
- Which local project outboxes need to be imported into central MDE?
- Is MDE improving or only accumulating notes?

---

# Operating Model

Keep separate repos.

Default daily work model:

```text
One repo = one Codex window
```

Examples:

```text
mde
  shared memory, lessons, skills, patterns, validators, prompts, content seeds

codex-skills
  actual reusable Codex skill implementation when promoted

jacob-family
  family web app / personalized software case study

jacob-family-mobile or jacob-family-ios
  iPhone/mobile companion app for the family software

demand-data-generation
  data generation for website assessment and client acquisition

local-website-growth-assessment
  assessment report generator

proposals
  client-facing proposal/report formatting

northvalley-client-success
  CRM/client success/support system

client-website-build-brief-generator
  generates latest client website build prompts, intake needs, technical briefs, and validation plans

client website repo
  one repo per client website, potentially transferable to client ownership
```

A parent-folder Codex window may be used only for cross-repo inspection or orchestration when explicitly requested.
Do not use a parent-folder window as the normal daily coding environment.

---

# Important Direction: Skill Over Static Templates

Do not rely on static website templates as the primary bootstrap mechanism.

MDE is still evolving.
A static template freezes old assumptions.
A skill can load the latest MDE knowledge, validators, issue signatures, context packs, and project rules.

Use:

```text
repo for ownership
skill for creation
central mde for evolving knowledge
```

For a new client website:

```text
Create an empty or minimal client repo/folder
Run the current MDE skill or generated bootstrap prompt
MDE creates project-specific mission, validation strategy, client intake, and implementation plan
Implementation starts after Generation 0
```

Do not blindly copy code from previous client websites.

---

# Scope Of This Mission

This mission should update the central `mde` repo so it contains:

1. Portfolio memory
2. Project registry
3. Dependency graph
4. Migration/session router
5. Just-in-time reusable learning guardrails
6. Generation 0 validation strategy rules
7. Skill-driven project bootstrap rules
8. Planned project launch packs for the next three projects
9. Client website skill/bootstrap support
10. Regular MDE learning audit support
11. Skill update packages/candidates for `codex-skills`
12. Handoff files for Codex and ChatGPT
13. Runbooks and prompts for day-to-day use

This mission may optionally update `../codex-skills/mde-skill` if that sibling repo exists and is safe to edit.
If it is not accessible or editing sibling repos is unsafe, create a skill update package inside this `mde` repo instead.

Do not build a dashboard.
Do not build a database.
Do not build a complex CLI.
Small optional helper scripts are allowed if they are simple, file-based, and easy to inspect.

---

# Known Projects

Initialize or update central MDE records for these known projects:

- `codex-skills`
  - contains the MDE skill used by Codex

- `mde`
  - platform memory, architecture, philosophy, content/book notes, shared MDE coordination

- `jacoob-family-app`
  - older/TODO customized family software direction

- `jacob-family`
  - current/latest web implementation for Jacob Family personalized software

- `medinaclean.com`
  - current client project, will use MDE

- `northvalleyintel.com`
  - company website, will use MDE

- `demand-data-generation`
  - data generation for lead acquisition and website assessment

- `local-website-growth-assessment`
  - assessment report generator consuming demand data

- `proposals`
  - formats assessment/proposal documents for prospects/clients

- `northvalley-business-cards`
  - public business-card generator repo

- `northvalley-receipts-invoices-flyers`
  - private official document/branding/receipts/invoices/flyers/vouchers repo

- `software-cost-ai-era`
  - possible duplicate/source material for MDE thinking

- `feroshjacob`
  - blog posts referenced from LinkedIn

Also add planned/new projects:

- `client-website-build-brief-generator`
  - creates latest client website prompt/brief based on assessment reports, validation logic, MDE lessons, and client intake needs

- `northvalley-client-success`
  - CRM/client success/support system for North Valley clients

- `jacob-family-mobile` or `jacob-family-ios`
  - iPhone/mobile companion to Jacob Family web app while keeping the web interface

Use `jacob-family-mobile` as the default project id unless existing naming suggests otherwise.

---

# Required Directory Structure In Central `mde`

Create or update this structure.

```text
portfolio/
  PROJECTS.yaml
  DEPENDENCIES.yaml
  FLOWS.yaml
  STATUS.md
  MIGRATION_STATUS.yaml
  PROJECT_LAUNCH_STATUS.yaml

ledger/
  events.jsonl
  decisions.jsonl
  lessons.jsonl
  content-seeds.jsonl
  skill-update-candidates.jsonl
  issue-signatures.jsonl

patterns/
  README.md
  pdf-generation/
  form-usability/
  client-website/
  mobile-apps/
  client-success/

validators/
  README.md
  pdf/
  usability/
  ui-standards/
  website-build/
  mobile/

context-packs/
  README.md
  pdf-generation.md
  client-website-build.md
  client-success-crm.md
  personalized-family-software.md
  mobile-companion-app.md
  website-assessment-to-build.md

starter-packs/
  README.md
  client-website-build-brief-generator/
  client-success-crm/
  mobile-companion-app/
  new-client-website/

project-launches/
  README.md
  client-website-build-brief-generator/
  northvalley-client-success/
  jacob-family-mobile/

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
  sync-existing-mde-project.md
  just-in-time-learning.md
  new-project-generation0.md
  new-client-website-bootstrap.md
  regular-mde-learning-audit.md
  promote-skill-update.md

briefings/
  current-platform-brief.md
  chatgpt-handoff.md
  codex-handoff-template.md

prompts/
  session-router.prompt.md
  existing-mde-open-session-sync.prompt.md
  existing-mde-new-session-start.prompt.md
  existing-non-mde-open-session-bridge.prompt.md
  existing-non-mde-new-session-adopt.prompt.md
  new-project-generation0-bootstrap.prompt.md
  new-client-website-skill-bootstrap.prompt.md
  project-validation-strategy-generation0.prompt.md
  applicable-learning-check.prompt.md
  session-end-learning-triage-and-sync.prompt.md
  regular-mde-learning-audit.prompt.md
  central-import-project-outbox.prompt.md
  skill-update-promotion.prompt.md
  cross-repo-impact-check.prompt.md

skill-packages/
  README.md
  mde-skill-next/
    README.md
    SKILL_UPDATE_PLAN.md
    mde-core-behavior.md
    generation0-project-bootstrap.md
    validation-gate.md
    applicable-learning-check.md
    session-end-learning-triage.md
    regular-learning-audit.md
    new-client-website-bootstrap.md

templates/
  project-record.template.yaml
  dependency-record.template.yaml
  event-record.template.json
  lesson-record.template.json
  content-seed.template.json
  issue-signature.template.json
  validation-strategy.template.json
  generation-handoff.template.md
  project-local-mde-contract.md
  project-outbox-contract.md

scripts/
  README.md
  import_project_outboxes.py
  summarize_mde_learning.py
```

If any of these already exist, merge rather than duplicate.

---

# Portfolio Registry Requirements

Update `portfolio/PROJECTS.yaml`.

Every project record should include:

```yaml
id: ""
name: ""
type: platform | product | client | content | operations | personal-case-study | public-asset | planned-product
repo_or_path: "../repo-name"
status: active | planned | paused | archived | unknown
mde_status: not_started | partial | active | migrated | unknown
migration_priority: 0
business_role: ""
owner: "Ferosh"
confidentiality: public | private | client-confidential | unknown
artifact_profiles: []
upstream_dependencies: []
downstream_dependencies: []
primary_artifacts: []
current_session_status: no_known_session | existing_session_unbridged | existing_session_bridged | unknown
skill_bootstrap_required: true | false
notes: ""
```

Add artifact profiles thoughtfully.

Examples:

```yaml
artifact_profiles:
  - pdf_generation
  - client_facing_document
  - website_assessment
  - client_website
  - crm
  - mobile_app
  - personalized_software
  - content_publication
  - data_generation
  - proposal_generation
```

These profiles allow just-in-time learning.

Example:

If a PDF margin overflow lesson exists, it applies to future generations in projects tagged with:

```text
pdf_generation
print_layout
client_facing_document
```

Do not run portfolio-wide remediation automatically.
Apply lessons just-in-time when a future generation touches a relevant artifact type.

---

# Planned Project Records

Add or update planned records for these three projects.

## 1. Client Website Build Brief Generator

Suggested repo:

```text
client-website-build-brief-generator
```

Purpose:

```text
Generate the latest client website build prompt, client intake checklist, technical brief, website mission, content needs, and validation plan using assessment reports and current MDE validation logic.
```

Consumes:

- demand-data-generation outputs
- local-website-growth-assessment reports
- MDE validation logic
- client intake data
- current website lessons/context packs

Produces:

- client questions
- website build mission
- technical implementation brief
- content-needed checklist
- validation strategy suggestion
- Codex prompt for building a client website

## 2. North Valley Client Success

Suggested repo:

```text
northvalley-client-success
```

Purpose:

```text
CRM/client success/support system for North Valley clients so each client receives better software help, support tracking, delivery history, and future MDE mission handoff.
```

This is more than a traditional CRM.
It should track:

- client profile
- websites/projects
- support requests
- software requests
- delivery history
- context for future Codex/MDE work
- client confidentiality
- recurring problems
- opportunity for new personalized software

## 3. Jacob Family Mobile

Suggested repo:

```text
jacob-family-mobile
```

Purpose:

```text
iPhone/mobile companion for Jacob Family personalized software while preserving the web interface.
```

Treat this as part of the Jacob Family personalized software product, not a separate unrelated product.

It should depend on explicit contracts with `jacob-family`:

- API/data contract
- auth/session behavior
- family privacy rules
- notification behavior
- offline expectations
- mobile usability validation

---

# Dependency Graph Requirements

Update `portfolio/DEPENDENCIES.yaml`.

At minimum include dependencies for:

```text
demand-data-generation -> local-website-growth-assessment
local-website-growth-assessment -> proposals
demand-data-generation -> client-website-build-brief-generator
local-website-growth-assessment -> client-website-build-brief-generator
client-website-build-brief-generator -> future client website repos
future client website repos -> northvalley-client-success
jacob-family -> jacob-family-mobile
mde -> all MDE-enabled projects
project local outbox -> central mde ledger
```

Each dependency should include:

```yaml
id: DEP-...
from: ...
to: ...
type: data_contract | report_input | prompt_input | support_context | api_contract | platform_learning | validation_context
summary: ""
contract_artifacts: []
risk_level: critical | high | medium | low
validation_needed: []
notes: ""
```

---

# Workflow Map Requirements

Update `portfolio/FLOWS.yaml`.

Include these workflows:

## FLOW-WEB-ASSESSMENT-TO-PROPOSAL

Existing workflow:

```text
demand-data-generation
  -> local-website-growth-assessment
  -> proposals
```

## FLOW-WEB-ASSESSMENT-TO-WEBSITE-BUILD-BRIEF

New workflow:

```text
demand-data-generation
  -> local-website-growth-assessment
  -> client-website-build-brief-generator
  -> client website repo
```

## FLOW-CLIENT-WEBSITE-TO-SUPPORT

New workflow:

```text
client website repo
  -> northvalley-client-success
  -> future support/software missions
```

## FLOW-JACOB-FAMILY-WEB-TO-MOBILE

New workflow:

```text
jacob-family web app
  -> jacob-family-mobile
  -> shared family software lessons
  -> MDE personalized software patterns
```

## FLOW-PROJECT-LESSON-TO-MDE

Existing/general workflow:

```text
project generation
  -> local .mde outbox
  -> central mde ledger
  -> pattern/validator/context-pack/skill-update/content seed
```

## FLOW-MDE-REGULAR-LEARNING-AUDIT

New workflow:

```text
central mde audit
  -> read project registry
  -> read project outboxes if accessible
  -> import events/lessons/content seeds
  -> check whether MDE is learning
  -> update briefings and recommendations
```

---

# Session Router Requirements

Create or update `prompts/session-router.prompt.md`.

This file should tell Ferosh which prompt to use in each situation.

Required cases:

```text
CASE A: Working in central mde repo
  Use central MDE mission prompts or regular learning audit.

CASE B: Existing project already uses MDE + Codex window already open
  Use prompts/existing-mde-open-session-sync.prompt.md

CASE C: Existing project already uses MDE + no Codex window open yet
  Use prompts/existing-mde-new-session-start.prompt.md

CASE D: Existing project does not use MDE + Codex window already open
  Use prompts/existing-non-mde-open-session-bridge.prompt.md

CASE E: Existing project does not use MDE + no Codex window open yet
  Use prompts/existing-non-mde-new-session-adopt.prompt.md

CASE F: Brand-new non-client project
  Use prompts/new-project-generation0-bootstrap.prompt.md

CASE G: Brand-new client website repo/folder
  Use prompts/new-client-website-skill-bootstrap.prompt.md

CASE H: End of any meaningful project session
  Use prompts/session-end-learning-triage-and-sync.prompt.md

CASE I: Regular central check whether MDE is learning
  Use prompts/regular-mde-learning-audit.prompt.md

CASE J: Promote central MDE learning into codex-skills
  Use prompts/skill-update-promotion.prompt.md
```

Make this router very clear and non-ambiguous.

---

# Existing MDE Project With Open Codex Session

Create `prompts/existing-mde-open-session-sync.prompt.md`.

This is important.

It is for a repo that already uses MDE and already has a Codex session open.

It should say:

```text
You are already inside an MDE-enabled project with an active Codex session.
Do not adopt MDE again.
Do not restart the mission.
Do not rewrite existing MISSION.md unless mission changed.
Do not rebuild .mde from scratch.
Preserve existing generations, validation runs, findings, and mission updates.

Your task is to add or update only the missing central sync pieces:

- .mde/outbox/events.jsonl
- .mde/outbox/lessons.jsonl
- .mde/outbox/impacts.jsonl
- .mde/outbox/content-seeds.jsonl
- .mde/outbox/skill-update-candidates.jsonl
- .mde/outbox/portfolio-sync.json

Then perform Applicable Learning Check using central MDE context if available:

- ../mde/briefings/current-platform-brief.md
- ../mde/portfolio/PROJECTS.yaml
- ../mde/portfolio/DEPENDENCIES.yaml
- ../mde/ledger/issue-signatures.jsonl
- ../mde/context-packs/

Continue the current work.
At session end, run Learning Triage and Sync.
```

---

# Just-In-Time Learning Guardrails

Create or update:

```text
context-packs/README.md
ledger/issue-signatures.jsonl
prompts/applicable-learning-check.prompt.md
runbooks/just-in-time-learning.md
```

Core rule:

```text
Do not apply every lesson everywhere immediately.
Apply reusable lessons just-in-time when a future generation touches a relevant artifact type.
```

Example:

A PDF margin overflow bug is found in `northvalley-receipts-invoices-flyers`.

Do NOT automatically regenerate all PDFs in all repos.
Do NOT automatically edit `proposals` immediately.

Instead:

1. Fix the source bug.
2. Extract reusable issue signature:

```text
PDF_TEXT_OVERFLOW_MARGIN
```

3. Tag applicability:

```text
pdf_generation
print_layout
client_facing_document
```

4. Add/update context pack:

```text
context-packs/pdf-generation.md
```

5. Add/update validator candidate:

```text
validators/pdf/pdf-margin-safety.md
```

6. Next time a project tagged `pdf_generation` generates/modifies a PDF, the MDE skill automatically loads the PDF context pack and checks for margin overflow.

Applicable Learning Check should answer:

```text
What artifact type is this generation touching?
Which project artifact profiles apply?
Which issue signatures are relevant?
Which context packs should be loaded?
Which validators/guardrails should be included in validation strategy?
What lessons are not relevant and should be ignored?
```

---

# Generation 0 Validation Strategy

Create or update:

```text
prompts/project-validation-strategy-generation0.prompt.md
prompts/new-project-generation0-bootstrap.prompt.md
runbooks/new-project-generation0.md
templates/validation-strategy.template.json
```

Core rule:

```text
Validation categories are reusable.
Validation tools are project-specific.
Every new project must define .mde/validation-strategy.json during Generation 0.
Previous tool choices may inform decisions but must not be assumed correct for the new project.
```

Replace old language:

```text
2 BDD passes + Quality Gate
```

with:

```text
2 independent Validation Gate passes
```

BDD is part of Functional Validation.
Quality Gate is deprecated as a standalone concept and folded into Validation Gate.

Validation categories:

1. Functional Validation
   - BDD scenarios
   - mission behavior
   - permissions
   - persistence
   - side effects
   - downstream workflows

2. Technical Validation
   - build
   - tests
   - deployment
   - data integrity
   - observability
   - failure detection/recovery

3. Usability Validation
   - error recovery
   - data preservation after validation failure
   - unnecessary steps
   - workflow friction
   - feedback clarity

4. UI Standards Validation
   - consistency
   - accessibility
   - affordance integrity
   - no fake buttons
   - no dead links
   - no misleading controls

5. Mission Coverage Validation
   - critical mission objectives: 100%
   - critical mission updates: 100%
   - high-priority objectives/updates: target 90%+
   - gaps must be fixed, accepted, or explicitly deferred

6. Project-Specific External Validation
   - selected during Generation 0
   - examples only, not hardcoded:
     - web: Playwright, axe-core, Lighthouse, OWASP ZAP
     - PDF/print: PDF geometry checks, print-mode rendering, long-text adversarial samples
     - mobile: Appium, Maestro, Detox, platform accessibility tools
     - AI/search: relevance metrics, latency benchmarks, grounding checks, custom eval sets

Second Validation Gate run should be risk-based.
It must rerun:

- all Critical validations
- all validations that failed in run 1
- validations affected by code changes
- validations related to unresolved High risks
- non-deterministic or environment-sensitive checks

It may skip validations clearly unaffected by changes, but every skip needs a reason.

If code changes are required after pass 1, pass count resets.

---

# Generation Evidence And MDE Observability

Create or update documentation and templates so every meaningful generation records:

```text
Generation id
Mission phase
Focus
Files changed
Production files changed
Test files changed
Config/docs changed
Lines added
Lines deleted
Net LOC change
Validation findings by tool/category
Critical findings
High findings
Medium findings
Resolved findings
Repeated findings
Validator usefulness signal
Gate result
Reusable lessons
Downstream impacts
Content seeds
Skill update candidates
```

LOC is not a success metric.
LOC is evidence.

Interpretation examples:

```text
Net LOC -300 + critical findings resolved = likely simplification
Net LOC +1200 + same failures = possible overengineering
Validator ran many times with no findings = review relevance
Validator produced mostly false positives = tune or replace
```

Create or update:

```text
templates/generation-handoff.template.md
runbooks/promote-project-learning.md
prompts/session-end-learning-triage-and-sync.prompt.md
```

---

# Regular MDE Learning Audit

Create:

```text
prompts/regular-mde-learning-audit.prompt.md
runbooks/regular-mde-learning-audit.md
scripts/import_project_outboxes.py
scripts/summarize_mde_learning.py
```

Purpose:

Ferosh wants to run a regular central check to see whether MDE is actually learning while he works on individual projects.

This does not run in the background automatically unless Ferosh wires it into automation later.
It must be runnable manually in a central `mde` Codex session.

Regular audit should:

1. Read `portfolio/PROJECTS.yaml`
2. For accessible sibling repos, look for:

```text
../project/.mde/outbox/events.jsonl
../project/.mde/outbox/lessons.jsonl
../project/.mde/outbox/impacts.jsonl
../project/.mde/outbox/content-seeds.jsonl
../project/.mde/outbox/skill-update-candidates.jsonl
../project/.mde/outbox/portfolio-sync.json
```

3. Import new records into central ledgers without duplicating.
4. Update `briefings/current-platform-brief.md`.
5. Update `briefings/chatgpt-handoff.md`.
6. Summarize whether MDE learned anything new.
7. Identify stale projects with no recent sync.
8. Identify repeated issues that should become validators/patterns.
9. Identify skill update candidates ready for promotion.
10. Identify content seeds worth developing.
11. Recommend next central MDE improvement.

The audit should produce a human summary:

```text
MDE Learning Audit Summary

Projects checked:
...
Outboxes imported:
...
New lessons:
...
Reusable patterns suggested:
...
Validator candidates:
...
Skill update candidates:
...
Content seeds:
...
Projects not syncing:
...
Is MDE learning? yes/no/partial
Recommended next action:
...
```

The scripts should be optional helpers.
They should not replace the human-readable prompt/runbook.
If scripts cannot safely determine paths or parse files, they should fail gracefully and explain what to do manually.

---

# Skill Packages And codex-skills Update

Create:

```text
skill-packages/mde-skill-next/
```

This should contain the proposed next version of the MDE skill behavior.

It should include:

1. Core MDE behavior
2. Generation lifecycle
3. Generation 0 project bootstrap
4. Validation Gate model
5. Applicable Learning Check
6. Skill-driven client website bootstrap
7. Session-end Learning Triage
8. Regular MDE Learning Audit
9. Project outbox contract
10. Central import behavior
11. Handoff discipline

Also create/update:

```text
ledger/skill-update-candidates.jsonl
prompts/skill-update-promotion.prompt.md
runbooks/promote-skill-update.md
```

If `../codex-skills/mde-skill` exists and this mission has permission to edit it safely, update it with the promoted MDE skill behavior.

If not, do not fail.
Instead, produce a clear report:

```text
Skill package created in mde/skill-packages/mde-skill-next/.
To apply it, open Codex in codex-skills and run prompts/skill-update-promotion.prompt.md.
```

Do not silently overwrite the existing skill.
Preserve prior skill files where possible.

---

# New Client Website Skill Bootstrap

Create:

```text
prompts/new-client-website-skill-bootstrap.prompt.md
starter-packs/new-client-website/
context-packs/client-website-build.md
context-packs/website-assessment-to-build.md
runbooks/new-client-website-bootstrap.md
```

This is for Ferosh to use when starting a new client website repo/folder.

The skill should:

1. Identify client and business context.
2. Load current central MDE context if available.
3. Load relevant website assessment output if available.
4. Load client website build context pack.
5. Run Generation 0.
6. Create client-safe local MDE structure.
7. Generate required client questions.
8. Generate content-needed checklist.
9. Generate website build mission.
10. Generate technical implementation brief.
11. Generate validation strategy.
12. Generate initial task graph.
13. Avoid copying old client code blindly.
14. Avoid exposing internal MDE notes in client-owned repo.
15. End with local outbox event and learning triage.

Client website repo should contain:

```text
MISSION.md
MISSION_UPDATES.md
.mde/project.json
.mde/validation-strategy.json
.mde/outbox/events.jsonl
.mde/lessons-local.jsonl
docs/client-intake-needed.md
docs/content-needed-from-client.md
docs/website-build-brief.md
docs/launch-validation-plan.md
```

Do not include private central MDE ledgers, internal cross-client lessons, private content seeds, or confidential notes in a client-owned candidate repo.

---

# Project Launch Packs For Three Planned Projects

For each planned project, create a launch pack under:

```text
project-launches/<project-id>/
```

Each launch pack should include:

```text
README.md
bootstrap.prompt.md
MISSION.seed.md
mde-project.seed.json
validation-strategy.seed.json
context-packs-to-load.md
first-generation-checklist.md
```

## Launch pack: client-website-build-brief-generator

Must include:

- mission seed
- dependencies on demand data and assessment reports
- expected outputs
- client intake schema ideas
- validation strategy for prompt/brief quality
- checks for stale assessment data
- checks for missing client details
- checks for privacy/confidentiality
- content seed opportunity

## Launch pack: northvalley-client-success

Must include:

- mission seed
- client confidentiality rules
- support/request lifecycle
- client/project relationship model
- MDE mission handoff integration
- validation strategy for CRM workflows
- future support event outbox

## Launch pack: jacob-family-mobile

Must include:

- mission seed
- relationship to jacob-family web app
- API/data contract assumptions
- iPhone/mobile validation strategy
- mobile usability checks
- privacy/offline/notifications considerations
- personalized software case study learning goals

These launch packs are not static code templates.
They are MDE startup packages.

---

# Project-Local Outbox Contract

Create/update:

```text
templates/project-outbox-contract.md
templates/project-local-mde-contract.md
```

Every MDE-enabled project should eventually have:

```text
.mde/
  project.json
  validation-strategy.json
  generations/
  validation-runs/
  findings.json
  lessons-local.jsonl
  outbox/
    events.jsonl
    lessons.jsonl
    impacts.jsonl
    content-seeds.jsonl
    skill-update-candidates.jsonl
    portfolio-sync.json
```

Minimal adoption requires:

```text
.mde/project.json
.mde/outbox/events.jsonl
.mde/lessons-local.jsonl
```

Already-MDE projects should not be migrated again.
They should only add missing outbox/sync artifacts.

---

# Ledgers

Update or create central ledgers.

## `ledger/events.jsonl`

Append an event for this one-time platform operating system setup.

## `ledger/lessons.jsonl`

Append lessons:

1. MDE needs durable cross-window memory.
2. Static templates can freeze old assumptions; evolving skill-driven bootstrap is better while MDE is still changing.
3. Reusable bug fixes should become just-in-time guardrails, not forced portfolio-wide rewrites.
4. Regular MDE learning audits are needed to ensure individual project work improves the platform.

## `ledger/content-seeds.jsonl`

Append content seeds for:

1. Agentic software needs durable memory.
2. Why templates are too static when the process is still learning.
3. Personalized software as a case study through Jacob Family app.
4. The difference between fixing a bug and teaching a platform.

## `ledger/skill-update-candidates.jsonl`

Append candidates for:

1. Skill-driven bootstrap.
2. Just-in-time applicable learning check.
3. Regular MDE learning audit.
4. Generation 0 project-specific validation strategy.
5. Session-end learning triage and sync.

## `ledger/issue-signatures.jsonl`

Seed example issue signatures:

```text
PDF_TEXT_OVERFLOW_MARGIN
FORM_VALIDATION_CLEARS_VALID_INPUT
FAKE_BUTTON_NO_MEANINGFUL_ACTION
DEAD_LINK_CLIENT_FACING_DOCUMENT
DUPLICATE_PRIMARY_ACTIONS
PRINT_LAYOUT_PAGE_BREAK_OVERLAP
```

Mark them as examples/seeds, not all confirmed issues.

---

# Briefings

Update:

```text
briefings/current-platform-brief.md
briefings/chatgpt-handoff.md
briefings/codex-handoff-template.md
```

They must now explain:

- MDE is the core platform investment.
- Repos remain separate.
- Skill-driven bootstrap is preferred over static templates.
- New client websites get their own repos and run MDE skill Generation 0.
- Existing MDE project with open Codex window uses the existing-MDE open-session sync prompt.
- Regular MDE learning audit should be run from central `mde`.
- The three planned projects and how to launch them.
- How project outboxes feed central MDE.
- How ChatGPT can be given handoff context without retelling the whole story.

---

# Update Mission Documents

Update or create:

```text
MISSION.md
MISSION_UPDATES.md
```

Add that MDE now includes:

- portfolio memory
- skill-driven bootstrap
- Generation 0 validation strategy
- just-in-time reusable learning
- project outbox sync
- session router
- regular learning audit
- planned project launch packs
- content/book note capture

---

# Safety And Confidentiality

Some repos are public.
Some are private.
Some contain client-sensitive information.
Some future repos may be transferred to clients.

Rules:

1. Do not place central MDE private ledgers in client-owned candidate repos.
2. Do not expose cross-client lessons in client repos.
3. Content seeds must include `public_safe` and `redaction_notes`.
4. If unsure, mark content as not public-safe.
5. Client website repos should contain only client-safe project MDE artifacts.
6. Central MDE owns reusable learning and internal strategy.

---

# Idempotency Rules

This mission must be safe to run after the earlier bootstrap prompt.

If a file exists:

- preserve it
- update it
- append new records where appropriate
- do not duplicate duplicate sections
- do not erase historical ledgers

For JSONL ledgers:

- append new records only if equivalent records do not already exist
- use stable ids where possible
- avoid duplicate seeds

For YAML files:

- update existing project records if present
- add missing fields
- do not reorder destructively unless necessary

---

# Final Report

After implementation, provide this concise summary:

```text
MDE One-Time Platform OS Setup Summary

Created/Updated:
- ...

Skill behavior prepared:
- ...

Project launch packs created:
- client-website-build-brief-generator
- northvalley-client-success
- jacob-family-mobile

Session router:
- ...

Regular learning audit:
- ...

How Ferosh should use this next:
1. Open a new Codex window in each planned project repo.
2. Use the launch pack bootstrap prompt for that project.
3. For a new client website repo, use the new-client-website skill bootstrap prompt.
4. At the end of project sessions, run session-end learning triage.
5. Regularly run the MDE learning audit in central mde.

If codex-skills was updated:
- ...

If codex-skills was not updated:
- explain where the skill package was created and how to promote it.

Open risks:
- ...

Recommended next generation:
- ...
```

Do not dump full file contents unless necessary.
Focus on the operational result: one central MDE setup that enables new project quick starts, skill-driven client website bootstrap, regular platform learning checks, and continuous MDE improvement from separate repos.
