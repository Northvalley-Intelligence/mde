# Handoff Discipline

Before work, read local mission/state and central context when available.

After meaningful work, record validation status, downstream impacts, reusable lessons, outbox records, and next steps.

ChatGPT handoffs should include enough context to avoid retelling the project history.

Handoffs and user-facing progress updates should be summary-first. Do not include raw code, raw diffs, or long command output unless explicitly requested.

Handoffs must also include:

- GitHub submission status: branch and commit SHA, or exact blocker
- production parity status for deployed projects: deployed commit/source and `main` sync state, or approved exception/blocker
- repository ownership status: confirm no sibling repos were modified, or name the target-repo session required
