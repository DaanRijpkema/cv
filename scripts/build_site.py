#!/usr/bin/env python3
"""Build the GitHub Pages source folder from the CV Markdown."""

from __future__ import annotations

import argparse
import shutil
import sys

sys.dont_write_bytecode = True

from pathlib import Path

from cv_markdown import strip_ignored_notes


def build_site(
    markdown_path: Path,
    output_dir: Path,
    pdf_path: Path,
    site_pdf_name: str,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    markdown = strip_ignored_notes(markdown_path.read_text(encoding="utf-8")).strip()
    index = "\n".join(
        [
            "---",
            "layout: default",
            "title: Daan Rijpkema CV",
            "---",
            "",
            f"[Download PDF]({site_pdf_name})",
            "",
            markdown,
            "",
        ]
    )
    (output_dir / "index.md").write_text(index, encoding="utf-8")

    if pdf_path.exists():
        shutil.copyfile(pdf_path, output_dir / site_pdf_name)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate the GitHub Pages source folder from the CV."
    )
    parser.add_argument(
        "source",
        nargs="?",
        type=Path,
        default=Path("cv.md"),
        help="Markdown source file. Defaults to cv.md.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("docs"),
        help="GitHub Pages output directory. Defaults to docs.",
    )
    parser.add_argument(
        "--pdf",
        type=Path,
        default=Path("output/daan-rijpkema-cv.pdf"),
        help="PDF to copy into the site folder when present.",
    )
    parser.add_argument(
        "--site-pdf-name",
        default="daan-rijpkema-cv.pdf",
        help="Filename for the PDF copy in the site folder.",
    )
    args = parser.parse_args()

    build_site(args.source, args.output_dir, args.pdf, args.site_pdf_name)
    print(f"Wrote {args.output_dir / 'index.md'}")
    if args.pdf.exists():
        print(f"Copied {args.pdf} to {args.output_dir / args.site_pdf_name}")
    else:
        print(f"Skipped PDF copy because {args.pdf} does not exist")


if __name__ == "__main__":
    main()
