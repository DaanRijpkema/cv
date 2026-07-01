# CV

The Markdown file is the source of truth:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Then build the PDF:

```bash
python scripts/build_pdf.py
```

That writes:

```text
output/daan-rijpkema-cv.pdf
```

## Supported Markdown

The PDF builder intentionally supports only a small subset:

- `#`, `##`, and `###` headings
- paragraphs
- `-` or `*` bullets
- Markdown links
- bold and italic inline text

Drafting notes are ignored when building the PDF:

- HTML comments, including multi-line `<!-- ... -->` comments
- lines that start with `TODO`
- bullet lines like `- [TODO: add metric]`

Visual styling lives in `scripts/build_pdf.py`; content and structure should stay in
`cv.md`.
