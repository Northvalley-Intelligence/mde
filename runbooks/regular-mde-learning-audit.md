# Regular MDE Learning Audit

Purpose: check whether MDE is actually learning while work happens in separate project repos.

This is manual until Ferosh wires automation later.

Process:

1. Read `portfolio/PROJECTS.yaml`.
2. Inspect accessible sibling repo `.mde/outbox` files.
3. Import central-worthy records without duplicating existing ledger entries.
4. Update central ledgers.
5. Update platform briefings.
6. Identify stale project sync status.
7. Identify repeated issues that should become patterns or validators.
8. Identify skill candidates ready for promotion.
9. Identify content seeds worth developing.
10. Recommend next central MDE improvement.

Optional helper scripts:

- `scripts/import_project_outboxes.py`
- `scripts/summarize_mde_learning.py`

Scripts are helpers, not replacements for human review.

