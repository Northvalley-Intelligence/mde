# Existing MDE Open Session Sync Prompt

You are in an existing Codex session for a repository that already uses MDE.

Do not re-adopt MDE.
Do not restart the mission.
Do not rewrite `MISSION.md` unless the mission actually changed.
Do not rebuild the `.mde` folder from scratch.
Do not discard existing generations, validation runs, findings, or mission updates.

Your job is to bridge this already-MDE project into the central MDE portfolio memory and just-in-time learning discipline.

Before continuing work:

1. Read this repo's `MISSION.md` if available.
2. Read this repo's `MISSION_UPDATES.md` if available.
3. Read this repo's `.mde/project.json` if available.
4. Read this repo's `.mde/state.json`, `.mde/generations`, `.mde/validation-runs`, or equivalent if available.
5. Read `../mde/briefings/current-platform-brief.md` if available.
6. Read `../mde/portfolio/PROJECTS.yaml` if available.
7. Read `../mde/portfolio/DEPENDENCIES.yaml` if available.
8. Read `../mde/context-packs/README.md` and any context packs that match this project or current task.
9. Read `../mde/knowledge/issue-signatures.jsonl` if available.

Then create or update only the missing sync files:

```text
.mde/outbox/portfolio-sync.json
.mde/outbox/events.jsonl
.mde/outbox/lessons.jsonl
.mde/outbox/impacts.jsonl
.mde/outbox/content-seeds.jsonl
.mde/outbox/skill-update-candidates.jsonl
```

If `.mde/project.json` exists, preserve it and only add missing fields such as:

- `artifact_profiles`
- `central_mde_sync_status`
- `context_packs`
- `validation_strategy_status`
- `downstream_dependencies`
- `upstream_dependencies`

Do not make broad unrelated changes.

Before implementation, perform Applicable Learning Check:

- What artifact type is being touched?
- Which context packs apply?
- Which prior issue signatures apply?
- Which validators or checks should be included in this generation?
- Which downstream repos could be affected?

At the end of the session, perform Learning Triage and Sync:

1. What changed?
2. What validation ran?
3. What reusable issue signatures were discovered?
4. What context packs should be updated?
5. What validator candidates were discovered?
6. What central MDE skill update candidates were discovered?
7. What content, blog, or book seeds were discovered?
8. What downstream projects are affected?
9. What outbox records were written?
10. What should be imported into central `mde`?

Do not dump code. Summarize in mission language.

