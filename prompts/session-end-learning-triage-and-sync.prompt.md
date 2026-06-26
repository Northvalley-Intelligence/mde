# Session-End Learning Triage And Sync Prompt

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
9. Is this a blog, book, or content seed?
10. Are downstream repos affected immediately?
11. Should this lesson apply just-in-time to future generations?
12. What was written to `.mde/outbox`?
13. What should central `mde` import?
14. Were meaningful code/config/deploy changes committed and pushed to GitHub? Include branch and commit SHA, or record the blocker.
15. If the project is production-deployed, is `main` in sync with deployed production code? Include deployed commit/source, or record the approved staged-release exception/blocker.
16. Did this session avoid modifying sibling repositories? If any downstream repo needs changes, name the required target-repo Codex session.

If a reusable lesson was discovered, record it in `.mde/outbox/lessons.jsonl`.
If a new issue signature was discovered, record it in `.mde/outbox/impacts.jsonl` or a suitable outbox record.
If content-worthy, record it in `.mde/outbox/content-seeds.jsonl`.
If MDE skill behavior should change, record it in `.mde/outbox/skill-update-candidates.jsonl`.

Do not end a meaningful code session by leaving unsubmitted work silently. If GitHub submission is not possible, record why and what must happen next.
