# Validation Gate

Quality Gate is not a standalone phase gate.

Phase exit requires two independent Validation Gate passes. BDD is part of Functional Validation, not the whole gate.

The second pass is risk-based and must rerun critical, failed, affected, high-risk, and non-deterministic validations.

After the second clean pass, run Repository Governance checks before claiming the phase is complete:

- meaningful code/config/deploy changes committed and pushed, or blocker recorded
- current session did not modify sibling repositories
- for production-deployed projects, deployed production commit/source is recorded
- `main` is synchronized with production deployment source, or an approved staged-release exception is documented
