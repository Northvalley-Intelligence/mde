# Codex Restart Handoff - Local Code Folder Move

Date: 2026-06-28

## Why This Exists

Ferosh is closing the current Codex session, moving the code root out of iCloud Drive, and restarting Codex from a local home-folder code directory.

Old MDE path:

```text
/Users/feroshjacob/Library/Mobile Documents/com~apple~CloudDocs/code/mde
```

Expected new root pattern:

```text
/Users/feroshjacob/code/mde
```

If the exact new path differs, use the new session `pwd` as truth and translate old sibling paths from the iCloud `code/` root to the new local `code/` root.

## Current MDE Repo State

The central MDE repo was clean and pushed before this handoff file was created.

Latest substantive MDE commits before this handoff file:

```text
e7faa09 Add client-facing content integrity validation
73bcbda Model third-person validation as a gate
6b0fcb8 Require third-person second validation review
b2d905b Add summary-first output and validation signal rules
22de13e Clarify Jacob Family status was read only
```

Expected `git status --short --branch` before move:

```text
## main...origin/main
```

After reopening from the new local folder, first verify:

```sh
pwd
git status --short --branch
git log -1 --oneline
git remote -v
```

Expected content-integrity commit in recent history:

```text
e7faa09 Add client-facing content integrity validation
```

The latest commit may be a newer handoff commit that adds this briefing.

## Most Recent Work Completed

The CJ Welding client-review lessons were promoted into central MDE as a reusable client-facing content integrity validation pattern.

Core lesson:

Generated client-facing material can look polished while still leaking internal process language, fake samples, placeholder testimonials, unsupported operational claims, or unresolved client inputs presented as fact. Websites, flyers, reports, proposals, and sales PDFs should validate content integrity before client review or publication.

Central MDE changes committed in `e7faa09`:

- Added `validators/client-facing-content/content-integrity.md`.
- Added `validators/client-facing-content/README.md`.
- Wired the validator into:
  - `validators/README.md`
  - `validators/website-build/README.md`
  - `validators/pdf/README.md`
  - `context-packs/client-website-build.md`
  - `context-packs/printable-artifacts.md`
  - `context-packs/pdf-generation.md`
  - `prompts/applicable-learning-check.prompt.md`
  - `prompts/new-client-website-skill-bootstrap.prompt.md`
  - `prompts/project-validation-strategy-generation0.prompt.md`
  - `runbooks/promote-project-learning.md`
  - `project-launches/client-website-build-brief-generator/validation-strategy.seed.json`
  - `skill-packages/mde-skill-next/*`
  - `MISSION_UPDATES.md`
- Added issue signatures:
  - `CLIENT_FACING_PROCESS_COPY_LEAK`
  - `PLACEHOLDER_OR_UNAPPROVED_PROOF_PUBLISHED`
  - `UNSUPPORTED_OPERATIONAL_CLAIM`
  - `VISUAL_PROOF_VARIETY_GAP`

Validation completed before push:

- `jq empty project-launches/client-website-build-brief-generator/validation-strategy.seed.json`
- `knowledge/issue-signatures.jsonl` parsed cleanly with 13 records.
- `git diff --check`
- Live skill frontmatter manual checks.

Known validation limitation:

- `/Users/feroshjacob/.codex/skills/.system/skill-creator/scripts/quick_validate.py` could not run because the Python environment was missing `PyYAML`.

## Live Skill Edits Outside This Repo

The installed skills under `~/.codex/skills` were also patched directly. These are outside the MDE git repo and should still exist after moving the code folder because they live under the home directory, not the iCloud code root.

Files patched:

```text
/Users/feroshjacob/.codex/skills/mission-driven-engineering/SKILL.md
/Users/feroshjacob/.codex/skills/northvalley-pdf-templates/SKILL.md
/Users/feroshjacob/.codex/skills/northvalley-pdf-templates/references/brand-guidelines.md
```

Live MDE skill addition:

- Public/client-facing artifacts such as websites, proposals, reports, flyers, and sales PDFs should include content integrity in the Validation Strategy.
- Reject visible implementation-process, AI-process, SEO-process, assessment-process, or template-explanation notes.
- Do not publish fake samples, placeholder proof, invented testimonials, unsupported operational claims, or unresolved client inputs as fact.
- Mark missing proof, photos, permissions, attribution, exact business facts, or client approvals as pending inputs.

Live Northvalley PDF skill addition:

- Client-facing flyers, reports, proposals, and sales PDFs require content integrity review before delivery.
- Validate claims against provided source material.
- Mark missing proof/details as pending instead of inventing.

## Important Operating Rules To Preserve

- One repo equals one writable Codex session.
- In an MDE session, read sibling repos only for context. Do not modify, format, install, commit, push, deploy, migrate, or reset sibling repos.
- Cross-project changes require an outbox/handoff record or a new Codex session opened in that target repo.
- Meaningful code/config/deploy changes should be committed and pushed to GitHub by session end, or the blocker must be recorded.
- Production-deployed projects must keep production code traceable to the submitted GitHub commit, and `main` must stay in sync with production deployment source unless an approved staged-release exception is documented.
- Agent communication should be summary-first: current action, mission impact, validation, short files/components, GitHub/deploy status, and next action. Avoid raw code/diff dumps unless Ferosh asks.

## Related Recent Decisions

- Phase readiness is now modeled as `Primary Validation Gate + Third-Person Validation Gate`.
- The Third-Person Validation Gate is a distinct reviewer-angle gate, not just a rerun.
- It should independently review usability, mission fit, role/workflow fit, edge cases, data shape, environment, or integration risk.
- It must record value added: new findings, decisions changed, coverage added, or no new findings.
- Same deterministic reruns belong inside a gate only when justified by nondeterminism, environment sensitivity, external dependency instability, concurrency/timing, or a known flaky path.

## Restart Instructions For The Next Codex Session

1. Open Codex with the new local MDE folder as the home/cwd.
2. Read `MISSION.md`, `MISSION_UPDATES.md`, and this handoff.
3. Run:

```sh
git status --short --branch
git log -1 --oneline
```

4. Confirm `e7faa09 Add client-facing content integrity validation` appears in recent history; the newest commit may be this handoff briefing.
5. If the user asks to continue MDE work, use the `mission-driven-engineering` skill.
6. If the user asks for Northvalley flyers/reports/proposals, use `northvalley-pdf-templates` and apply the content integrity checks above.

## No Pending MDE Work From This Session

There was no uncommitted central MDE repo work at the time this handoff was created.

Potential follow-up only if Ferosh asks:

- Re-run official skill validation after installing/repairing `PyYAML`.
- Promote the live installed skill edits into their source-of-truth skill repository if that repo is separate from central MDE.
- Sync existing open project sessions by restarting them so they reload the updated live skills.
