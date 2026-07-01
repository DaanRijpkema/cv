#!/usr/bin/env python3
"""Build a restrained, readable PDF CV from a small Markdown subset."""

from __future__ import annotations

import argparse
import sys

sys.dont_write_bytecode = True

from pathlib import Path

from cv_markdown import iter_blocks, markdown_inline_to_reportlab

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import (
        HRFlowable,
        ListFlowable,
        ListItem,
        Paragraph,
        SimpleDocTemplate,
    )
except ModuleNotFoundError as error:
    if error.name != "reportlab":
        raise
    print(
        "Missing Python dependency: reportlab\n\n"
        "Set up a local virtual environment once, then rerun the builder:\n\n"
        "  python3 -m venv .venv\n"
        "  source .venv/bin/activate\n"
        "  python -m pip install -r requirements.txt\n"
        "  python scripts/build_pdf.py\n",
        file=sys.stderr,
    )
    raise SystemExit(1) from error

def build_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    text_color = colors.HexColor("#1f2933")
    muted = colors.HexColor("#53616d")
    accent = colors.HexColor("#1f5f8b")

    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            alignment=TA_CENTER,
            textColor=text_color,
            spaceAfter=5,
        ),
        "intro": ParagraphStyle(
            "Intro",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            alignment=TA_CENTER,
            textColor=muted,
            spaceAfter=3,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=14,
            textColor=accent,
            spaceBefore=11,
            spaceAfter=5,
            keepWithNext=1,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=text_color,
            spaceBefore=7,
            spaceAfter=2,
            keepWithNext=1,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            alignment=TA_LEFT,
            textColor=text_color,
            spaceAfter=4,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            textColor=muted,
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.7,
            leading=11,
            leftIndent=0,
            firstLineIndent=0,
            textColor=text_color,
        ),
    }


def footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.HexColor("#7a8791"))
    canvas.drawRightString(
        A4[0] - doc.rightMargin,
        11 * mm,
        f"Daan Rijpkema - page {doc.page}",
    )
    canvas.restoreState()


def build_pdf(markdown_path: Path, output_path: Path) -> None:
    styles = build_styles()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=17 * mm,
        bottomMargin=18 * mm,
        title="Daan Rijpkema CV",
        author="Daan Rijpkema",
    )

    story = []
    seen_h1 = False
    before_first_section = True
    previous_block = ""

    for block_type, content in iter_blocks(markdown_path.read_text(encoding="utf-8")):
        if block_type == "h1":
            seen_h1 = True
            story.append(Paragraph(markdown_inline_to_reportlab(str(content)), styles["name"]))
            story.append(
                HRFlowable(
                    width="36%",
                    thickness=0.7,
                    color=colors.HexColor("#9fb2bf"),
                    spaceBefore=2,
                    spaceAfter=7,
                    hAlign="CENTER",
                )
            )
        elif block_type == "h2":
            before_first_section = False
            story.append(Paragraph(markdown_inline_to_reportlab(str(content)), styles["section"]))
        elif block_type == "h3":
            story.append(Paragraph(markdown_inline_to_reportlab(str(content)), styles["role"]))
        elif block_type == "bullets":
            items = [
                ListItem(Paragraph(markdown_inline_to_reportlab(item), styles["bullet"]))
                for item in content
            ]
            story.append(
                ListFlowable(
                    items,
                    bulletType="bullet",
                    bulletFontName="Helvetica",
                    bulletFontSize=6,
                    bulletColor=colors.HexColor("#1f5f8b"),
                    leftIndent=12,
                    bulletOffsetY=1,
                    spaceBefore=1,
                    spaceAfter=4,
                )
            )
        else:
            style_name = "intro" if seen_h1 and before_first_section else "body"
            if previous_block == "h3":
                style_name = "meta"
            text = str(content)
            if style_name == "intro":
                inline_content = "<br/>".join(
                    markdown_inline_to_reportlab(line) for line in text.splitlines()
                )
            else:
                inline_content = markdown_inline_to_reportlab(" ".join(text.splitlines()))
            story.append(
                Paragraph(inline_content, styles[style_name])
            )

        previous_block = block_type

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a polished PDF CV from a restrained Markdown file."
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
        "--output",
        type=Path,
        default=Path("output/daan-rijpkema-cv.pdf"),
        help="PDF output path. Defaults to output/daan-rijpkema-cv.pdf.",
    )
    args = parser.parse_args()

    build_pdf(args.source, args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
