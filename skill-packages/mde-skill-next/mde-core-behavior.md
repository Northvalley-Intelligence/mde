# MDE Core Behavior

MDE is mission-first, validation-driven, and file-backed.

Repos stay separate. Central `mde` stores shared platform memory, reusable lessons, context packs, validators, skill candidates, launch packs, and handoff material.

Default daily work model: one repo equals one Codex window.

Writable scope is the session home repository only. A Codex session may read sibling repos for context, but it must not edit, format, install, commit, push, deploy, migrate, or reset sibling repos. Cross-project changes require a handoff/outbox record and a Codex session opened in the target repo.

Meaningful code/config/deploy changes must be submitted to GitHub by session end or after validation readiness. If submission cannot happen, record the blocker.

For production-deployed projects, deployed production code must be traceable to the submitted GitHub commit. `main` must stay in sync with production deployment source unless a documented staged-release exception is approved.

Agent-to-user communication should be summary-first. During work and in final responses, summarize current action, why it matters, mission impact, validation, findings, short files/components, short commit/deploy status, and next action. Do not paste raw code, raw diffs, or long command output unless Ferosh explicitly asks.

When output is constrained, keep blockers/decisions, current action, mission impact, validation, short GitHub/deploy status, short files/components, and next action before implementation detail. Keep GitHub/deploy and files/components terse by default; expand only when Ferosh asks.
