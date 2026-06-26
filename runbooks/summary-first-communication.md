# Summary-First Communication

Purpose: keep MDE agent-to-user communication focused on mission progress instead of code volume.

Default rule: user-facing MDE communication should be summary-first, not code-first.

## Output Priority Order

When output is reduced, preserve this order:

1. Ferosh's blocking ask or decision needed.
2. Current action and why it matters.
3. Mission impact.
4. Validation status and Critical/High findings.
5. Short GitHub branch, commit, PR, deployment, or production parity status.
6. Short files or components touched.
7. Next action.

Items 5 and 6 should be compact by default. Use a one-line branch/commit/deploy/parity status and a short list or count of touched areas; provide deeper file lists, diffs, or implementation detail only when Ferosh asks.

Drop first:

- raw diffs
- raw code
- long logs
- line-by-line implementation narration
- repeated command output

Use summary-first communication for:

- progress updates while the agent is working
- command-result explanations
- final responses
- generation summaries
- handoffs
- status docs
- project outbox summaries
- ChatGPT handoffs
- validation summaries

Include:

- what the agent is doing now
- why the action matters
- mission impact
- short changed files or components by name
- validation run and result
- Critical/High findings or blockers
- short GitHub branch/commit/PR status
- short deployment or production parity status
- next action

Avoid unless Ferosh explicitly asks:

- raw code blocks from implementation files
- raw unified diffs
- long command output
- pasted test logs
- large generated artifacts

When technical detail is needed, prefer:

- file references
- short excerpts only for the exact line or behavior under discussion
- `git diff --stat` or `git diff --name-only`
- targeted findings with file paths and line numbers
- links to commits or PRs

This rule does not mean code is irrelevant. It means code is implementation evidence. MDE completion is reported through mission progress, validation evidence, risk reduction, and deploy/submission state.
