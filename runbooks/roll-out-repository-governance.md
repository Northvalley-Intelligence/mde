# Roll Out Repository Governance

Use this from central `mde` when Ferosh wants the repository ownership, GitHub submission, and production parity rules applied across projects.

## Central Rollout

1. Finish the central `mde` rule update.
2. Commit and push the central `mde` change to GitHub.
3. Open a separate Codex session in the `codex-skills` repo.
4. Use `prompts/skill-update-promotion.prompt.md` to promote `skill-packages/mde-skill-next`.
5. Do not edit `codex-skills` from the central `mde` session.

## Per-Project Rollout

For each active MDE project:

1. Open Codex with that project as the home folder.
2. Run `../mde/prompts/project-repository-governance-sync.prompt.md`.
3. Let that project session update only project-local MDE/status/deploy artifacts.
4. If code changed, commit and push from that project session.
5. If production-deployed, record the deployed commit/source and verify `main` parity.

For projects with already-open Codex windows, paste this bridge instruction into that existing window:

```text
Read ../mde/prompts/project-repository-governance-sync.prompt.md and ../mde/runbooks/repository-governance.md, then apply the rules to this project only. Do not modify sibling repos. From now on, after meaningful code changes or two clean Validation Gate passes, submit this project's code to GitHub or record the blocker. If this project is production-deployed, verify main is in sync with deployed production code or record the approved exception/blocker.
```

This refreshes the session behavior without pretending the already-open window has reloaded the MDE skill.

Suggested priority:

1. Production-deployed client or public projects.
2. Projects with automated deploys from GitHub.
3. Active internal apps.
4. Planned or paused projects.

## GitHub Settings

Where GitHub settings allow it, configure production repos with:

- protected `main`
- required status checks before merge
- no force pushes
- no branch deletion
- PR review for high-risk public/client repos
- deployment workflow from `main` or a documented `prod` branch

MDE can enforce the session discipline in artifacts and handoffs. GitHub branch protection enforces it at the repository host.
