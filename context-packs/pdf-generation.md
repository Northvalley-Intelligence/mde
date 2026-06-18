# PDF Generation Context Pack

Applicable artifact profiles:

- `pdf_generation`
- `print_layout`
- `client_facing_document`
- `report_generation`

Known issue signatures:

- `PDF_TEXT_OVERFLOW_MARGIN`
- `PDF_CONTENT_CLIPPED`
- `PDF_HEADER_FOOTER_OVERLAP`
- `PDF_BAD_PAGE_BREAK`
- `PDF_TABLE_OVERFLOW`

Checks:

- Long text wraps or truncates intentionally.
- Text stays inside safe margins.
- Tables do not exceed page width.
- Headers and footers do not overlap body content.
- Page breaks do not split important content awkwardly.
- Generated PDF is validated in PDF/print mode, not only browser view.

