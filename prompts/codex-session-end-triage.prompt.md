# Codex Session End Triage Prompt

Superseded for MDE-aware work by `prompts/session-end-learning-triage-and-sync.prompt.md`. Use this older prompt only when a shorter legacy triage is sufficient.

Before ending, perform MDE Learning Triage.

Tell me:

1. What changed?
2. Did validation pass?
3. Was this project-only learning?
4. Is there a reusable MDE pattern?
5. Is there a validator improvement?
6. Is there a skill update candidate?
7. Is there a blog, book, or content seed?
8. Are downstream repos affected?
9. Should an event be added to `.mde/outbox/events.jsonl`?
10. Should the central `mde` repo be updated?

Do not dump code. Summarize in mission language.
