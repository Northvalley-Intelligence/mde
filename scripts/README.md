# Scripts

Optional helpers for central MDE audits.

These scripts do not replace human review. They read file-based MDE artifacts and fail gracefully when paths are missing or records cannot be parsed.

Scripts:

- `import_project_outboxes.py`: inspect sibling project outboxes and import central-worthy JSONL records without duplicating IDs.
- `summarize_mde_learning.py`: summarize central ledgers, issue signatures, skill candidates, and launch status.

