# PDF Margin Safety Validator Candidate

Goal:
Prevent generated PDFs from overflowing into unsafe margins, clipping content, or hiding important text.

Applies to:

- `pdf_generation`
- `print_layout`
- `client_facing_document`
- `report_generation`

Suggested checks:

- Generate sample PDFs with realistic and adversarial long text.
- Inspect rendered PDF or extracted text bounding boxes.
- Fail if content crosses safe margin boundaries.
- Fail if table, image, or content is clipped.
- Fail if header/footer overlaps body content.

Run policy:

- When PDF templates change.
- When PDF data schema changes.
- When client-facing PDF is generated or regenerated.
- Before phase or release validation.

Default severity:
High. Critical if client-facing, legal, or financial artifact.

