# CV

The Markdown file is the source of truth:

```bash
python3 scripts/build_pdf.py
```

That writes:

```text
output/pdf/daan-rijpkema-cv.pdf
```

## Supported Markdown

The PDF builder intentionally supports only a small subset:

- `#`, `##`, and `###` headings
- paragraphs
- `-` or `*` bullets
- Markdown links
- bold and italic inline text

Visual styling lives in `scripts/build_pdf.py`; content and structure should stay in
`cv.md`.
