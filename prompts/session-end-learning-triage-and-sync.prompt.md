# Session-End Learning Triage And Sync Prompt

Before ending, perform MDE Learning Triage and Sync.

Report in mission language, not code dumps. The user should see what happened and why it matters, not raw implementation text.
Do not paste raw code, raw diffs, or long command output unless explicitly requested.
If the response must be short, prioritize: blockers/decisions, mission impact, validation, Critical/High findings, short GitHub/deploy status, short files/components, next action. Keep GitHub/deploy and files/components terse by default; expand only if Ferosh asks.

Answer:

1. What changed?
2. What artifact profiles were touched?
3. What validation ran?
4. Did the Validation Gate pass or fail?
5. Did the Third-Person Validation Gate run when the work was meaningful, user-facing, or mission-critical?
6. What was the Third-Person Validation Gate outcome and value added: new findings, decisions changed, coverage added, or no new findings?
7. Did we discover a reusable issue signature?
8. Does a central context pack need to be updated?
9. Does a validator need to be created or improved?
10. Is this a skill update candidate?
11. Is this a blog, book, or content seed?
12. Are downstream repos affected immediately?
13. Should this lesson apply just-in-time to future generations?
14. What was written to `.mde/outbox`?
15. What should central `mde` import?
16. Were meaningful code/config/deploy changes committed and pushed to GitHub? Include branch and commit SHA, or record the blocker.
17. If the project is production-deployed, is `main` in sync with deployed production code? Include deployed commit/source, or record the approved staged-release exception/blocker.
18. Did this session avoid modifying sibling repositories? If any downstream repo needs changes, name the required target-repo Codex session.

If a reusable lesson was discovered, record it in `.mde/outbox/lessons.jsonl`.
If a new issue signature was discovered, record it in `.mde/outbox/impacts.jsonl` or a suitable outbox record.
If content-worthy, record it in `.mde/outbox/content-seeds.jsonl`.
If MDE skill behavior should change, record it in `.mde/outbox/skill-update-candidates.jsonl`.

Do not end a meaningful code session by leaving unsubmitted work silently. If GitHub submission is not possible, record why and what must happen next.
