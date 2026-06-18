# Applicable Learning Check Prompt

Before implementation, check whether central MDE contains lessons relevant to this generation.

Inputs:

- current task
- project `artifact_profiles`
- files or artifacts likely to be changed
- central context packs
- central issue signatures
- project validation strategy

Ask:

1. What artifact type is this generation touching?
2. Which project artifact profiles apply?
3. Which context packs apply?
4. Which known issue signatures apply?
5. Which validators or checks should be added to this generation?
6. Are any downstream projects affected?
7. Should this generation update local validation strategy?

Do not apply unrelated lessons.
Do not automatically modify other repos.
Do not run portfolio-wide remediation unless explicitly requested.

Example: if a prior invoice repo generation discovered PDF text overflow into margins and recorded `PDF_TEXT_OVERFLOW_MARGIN`, then a future proposal repo generation that touches PDF generation should load the PDF generation context pack and include PDF margin safety checks. It should not automatically regenerate every proposal PDF at the time the invoice bug is fixed.

