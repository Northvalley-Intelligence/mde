# BDD Coverage Model

BDD generation remains qualitative first.

Each BDD must answer:

- What real-world behavior matters?
- Who is the user?
- What state do they start in?
- What action do they take?
- What outcome proves the feature works?
- What permissions, persistence, side effects, or downstream workflow must also be true?

Coverage metrics are used only to identify gaps.

They do not replace judgment.

## Coverage Dimensions

Track BDD coverage across these dimensions:

1. Mission Objective Coverage
   - Which mission objectives are covered by at least one BDD?

2. User Role Coverage
   - Which users or actors are represented?

3. Workflow Coverage
   - Which real-world workflows are validated?

4. Risk Coverage
   - Which known risks have BDDs?

5. Mission Update Coverage
   - Which mission updates changed behavior and are reflected in BDDs?

6. Persistence / Permission / Side Effect Coverage
   - Which hidden system obligations are tested?

## Coverage Target

The target is not 100%.

The target is:

- 100% coverage for Critical mission objectives
- 90% coverage for High-priority mission objectives and mission updates
- Explicit acceptance or deferral for uncovered Medium/Low items

## Coverage Artifact

Maintain:

.mde/bdd-coverage.json

Example:

{
  "mission_objective_coverage": {
    "covered": 9,
    "total": 10,
    "percent": 90
  },
  "mission_update_coverage": {
    "covered": 7,
    "total": 8,
    "percent": 87.5
  },
  "risk_coverage": {
    "covered": 5,
    "total": 6,
    "percent": 83.3
  },
  "uncovered_items": [
    {
      "type": "mission_update",
      "id": "MU-004",
      "summary": "Reports must explain why a score changed.",
      "decision": "Needs BDD before phase exit"
    }
  ]
}

## Rule

A phase cannot exit if:

- any Critical/high mission objective has no BDD
- any Critical/high mission update has no BDD
- BDD coverage for Critical/High mission objectives is below 90%
- uncovered items do not have an explicit defer/accept decision