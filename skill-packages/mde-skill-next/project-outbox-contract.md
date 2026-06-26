# Project Outbox Contract

Every MDE-enabled project should write cross-project events, reusable lessons, impacts, content seeds, skill candidates, and portfolio sync metadata to `.mde/outbox`.

Central `mde` imports records selectively. Project-only noise stays local.

Project outboxes are the safe cross-repo modification path. A source-project session records downstream impact; it does not edit the downstream repository directly.
