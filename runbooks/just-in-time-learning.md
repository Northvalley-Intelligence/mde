# Just-In-Time Learning

Reusable lessons should usually apply when future work touches matching artifacts, not by automatically modifying every related repo immediately.

## Inputs

- Current task
- Project `artifact_profiles`
- Files or artifacts likely to be changed
- Central context packs
- Central issue signatures
- Project validation strategy

## Process

1. Identify the artifact type this generation touches.
2. Match project artifact profiles.
3. Load relevant context packs.
4. Check known issue signatures.
5. Add relevant validators or checks to the generation.
6. Identify downstream projects affected by the change.
7. Decide whether the local validation strategy needs a safe update.

Do not apply unrelated lessons.
Do not automatically modify other repos.
Do not run portfolio-wide remediation unless explicitly requested.

## PDF Example

If a prior invoice repo generation discovered PDF text overflow into margins, record issue signature `PDF_TEXT_OVERFLOW_MARGIN`.

When a future proposal repo generation touches PDF generation, MDE should automatically load `context-packs/pdf-generation.md` and include PDF margin safety checks.

MDE should not automatically regenerate all proposal PDFs at the time the invoice bug is fixed.

