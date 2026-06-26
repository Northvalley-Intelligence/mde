# MDE Mission

Mission-Driven Engineering is the platform discipline for building personalized software economically.

MDE now includes portfolio memory, incremental migration, cross-repo coordination, dependency tracking, existing session bridging, learning triage, content seed capture, and Codex/ChatGPT handoff discipline.

The platform uses durable files first. Repositories stay separate. The `mde` repo is shared memory and operating discipline, not a monorepo.

MDE enforces repository ownership boundaries. A Codex session may read related project repositories for context, but it may write only inside the repository that is the session home. Cross-project changes must be requested through a separate Codex session opened in the target project root. Central `mde` imports project outboxes; it does not silently patch project repos.

MDE requires GitHub submission and production parity discipline. After meaningful code changes or a second clean Validation Gate pass, work should be committed and pushed, or an explicit blocker must be recorded. For production-deployed projects, the deployed production code must be traceable to the submitted GitHub commit, and `main` must stay in sync with the production deployment source unless an approved staged-release exception is documented.

MDE now distinguishes session routing cases, including projects that already use MDE with open Codex windows.

MDE supports just-in-time reusable learning through context packs and issue signatures. Reusable lessons apply when future work touches matching artifact profiles, not by automatically rewriting every repo.

MDE requires project-specific Validation Strategy during Generation 0 for new projects or during the first safe validation update for existing projects.

Quality Gate is deprecated as a standalone concept. Phase exit is based on two independent Validation Gate passes.

MDE now includes skill-driven bootstrap, regular learning audits, project outbox sync, planned project launch packs, client website bootstrap support, skill update packages, and content/book note capture.

New client websites should get their own repos and run MDE skill Generation 0. Do not rely on static website templates as the primary bootstrap mechanism while MDE is still evolving.
