# MDE Mission

Mission-Driven Engineering is the platform discipline for building personalized software economically.

MDE now includes portfolio memory, incremental migration, cross-repo coordination, dependency tracking, existing session bridging, learning triage, content seed capture, and Codex/ChatGPT handoff discipline.

The platform uses durable files first. Repositories stay separate. The `mde` repo is shared memory and operating discipline, not a monorepo.

MDE enforces repository ownership boundaries. A Codex session may read related project repositories for context, but it may write only inside the repository that is the session home. Cross-project changes must be requested through a separate Codex session opened in the target project root. Central `mde` imports project outboxes; it does not silently patch project repos.

MDE requires GitHub submission and production parity discipline. After meaningful code changes or validation readiness, work should be committed and pushed, or an explicit blocker must be recorded. For production-deployed projects, the deployed production code must be traceable to the submitted GitHub commit, and `main` must stay in sync with the production deployment source unless an approved staged-release exception is documented.

MDE agent-to-user communication is summary-first. Code changes are implementation evidence, not the primary artifact. While working and when finishing, agents should summarize what they are doing, why it matters, validation, risks, files changed, commits, and next actions; they should not paste raw code, raw diffs, or long command output unless Ferosh explicitly asks for that level of detail.

When output must be reduced, MDE keeps this priority order: Ferosh's blocking ask or decision needed; current action and why it matters; mission impact; validation status and Critical/High findings; short GitHub/deploy status; short files or components touched; next action. GitHub/deploy and files/components entries should be terse by default so Ferosh can ask for more detail when needed. Raw diffs, raw code, long logs, and line-by-line implementation narration are lowest priority and should be omitted unless explicitly requested.

MDE now distinguishes session routing cases, including projects that already use MDE with open Codex windows.

MDE supports just-in-time reusable learning through context packs and issue signatures. Reusable lessons apply when future work touches matching artifact profiles, not by automatically rewriting every repo.

MDE requires project-specific Validation Strategy during Generation 0 for new projects or during the first safe validation update for existing projects.

Quality Gate is deprecated as a standalone concept. Phase readiness is based on validation gates, not rerun counts. Meaningful user-facing or mission-critical work uses a Primary Validation Gate plus a Third-Person Validation Gate. The Primary Validation Gate proves the implementation works functionally and technically. The Third-Person Validation Gate independently reviews the result from a user, mission-fit, role, workflow, edge-case, data-shape, environment, usability, or integration perspective. Same-test reruns belong inside a gate only when the risk is nondeterminism, environment sensitivity, external dependency instability, concurrency/timing behavior, or a known flaky path, and the reason must be recorded. Every Third-Person Validation Gate records outcome and value added: new findings, decisions changed, coverage added, or no new findings. Reevaluate and tune the third-person gate when repeated reviews add no signal.

MDE now includes skill-driven bootstrap, regular learning audits, project outbox sync, planned project launch packs, client website bootstrap support, skill update packages, and content/book note capture.

New client websites should get their own repos and run MDE skill Generation 0. Do not rely on static website templates as the primary bootstrap mechanism while MDE is still evolving.
