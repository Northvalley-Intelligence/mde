# Summary-First Communication

MDE skill behavior should keep agent-to-user communication at summary level by default.

When output is reduced, preserve this priority order:

1. Ferosh's blocking ask or decision needed.
2. Current action and why it matters.
3. Mission impact.
4. Validation status and Critical/High findings.
5. Short GitHub/deploy status.
6. Short files or components touched.
7. Next action.

Items 5 and 6 should stay compact by default: use one-line commit/deploy/parity status and short touched-area names, then expand only when Ferosh asks.

Drop first: raw diffs, raw code, long logs, and line-by-line implementation narration.

Applies to:

- progress updates while work is happening
- command-result explanations
- final responses
- handoffs
- generation summaries
- validation summaries

Default shape:

- current action
- why it matters
- mission impact
- short files or components touched
- validation result
- Critical/High findings or blockers
- short GitHub submission and deployment status
- next action

Avoid unless Ferosh explicitly asks:

- raw implementation code
- raw diffs
- long command output
- pasted test logs

Use file references, short excerpts, commit SHAs, and validation evidence instead.
