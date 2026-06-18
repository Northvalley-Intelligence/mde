# Adopt MDE In Existing Project

1. Do not refactor code first.
2. Create project-local `.mde` identity.
3. Record current state.
4. Record upstream and downstream dependencies.
5. Add outbox for cross-repo events.
6. Add local lessons ledger.
7. Add validation and generation artifacts later as real work happens.

Minimal required files:

- `.mde/project.json`
- `.mde/outbox/events.jsonl`
- `.mde/lessons-local.jsonl`

