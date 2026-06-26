# Session-End Learning Triage

Every meaningful session should ask:

- What changed?
- What validation ran?
- Did the Third-Person Validation Gate run when the work was meaningful, user-facing, or mission-critical?
- What was the Third-Person Validation Gate outcome and value added: new findings, decisions changed, coverage added, or no new findings?
- What reusable lesson or issue signature was discovered?
- What context pack or validator should update?
- What content seed or skill candidate emerged?
- What downstream projects are affected?
- What should central `mde` import?
- Was meaningful code/config/deploy work committed and pushed to GitHub?
- If production-deployed, is `main` in sync with deployed production code?
- Were sibling repositories left unmodified?

Do not end meaningful code sessions with silent unsubmitted work. If push/PR creation is blocked, record the blocker and next action.

Report the result at summary level. The user should see mission impact, validation, risks, short files/components, short commit/deploy status, and next action, not raw code or diffs unless explicitly requested. Expand those short status fields only when Ferosh asks.
