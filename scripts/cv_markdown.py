"""Shared Markdown helpers for the CV builders."""

from __future__ import annotations

import html
import re
from typing import Iterable


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
STRONG_RE = re.compile(r"\*\*([^*]+)\*\*")
EM_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
TODO_RE = re.compile(r"^\s*(?:[-*]\s*)?(?:\[TODO:.*\]|TODO\b.*)$", re.IGNORECASE)


def strip_ignored_notes(markdown: str) -> str:
    """Remove drafting notes that should never appear in generated outputs."""
    without_comments = HTML_COMMENT_RE.sub("", markdown)
    return "\n".join(
        line for line in without_comments.splitlines() if not TODO_RE.match(line)
    )


def iter_blocks(markdown: str) -> Iterable[tuple[str, str | list[str]]]:
    paragraph: list[str] = []
    bullets: list[str] = []

    def flush_paragraph() -> tuple[str, str] | None:
        nonlocal paragraph
        if not paragraph:
            return None
        text = "\n".join(line.strip() for line in paragraph)
        paragraph = []
        return ("paragraph", text)

    def flush_bullets() -> tuple[str, list[str]] | None:
        nonlocal bullets
        if not bullets:
            return None
        items = bullets
        bullets = []
        return ("bullets", items)

    for raw_line in strip_ignored_notes(markdown).splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            block = flush_paragraph()
            if block:
                yield block
            block = flush_bullets()
            if block:
                yield block
            continue

        if stripped.startswith("#"):
            block = flush_paragraph()
            if block:
                yield block
            block = flush_bullets()
            if block:
                yield block
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip()
            yield (f"h{min(level, 3)}", text)
            continue

        if stripped.startswith(("- ", "* ")):
            block = flush_paragraph()
            if block:
                yield block
            bullets.append(stripped[2:].strip())
            continue

        block = flush_bullets()
        if block:
            yield block
        paragraph.append(stripped)

    block = flush_paragraph()
    if block:
        yield block
    block = flush_bullets()
    if block:
        yield block


def markdown_inline_to_html(text: str) -> str:
    """Convert the supported inline Markdown subset to HTML."""
    pieces: list[str] = []
    position = 0

    for match in LINK_RE.finditer(text):
        pieces.append(html.escape(text[position : match.start()]))
        label = html.escape(match.group(1))
        href = html.escape(match.group(2), quote=True)
        pieces.append(f'<a href="{href}">{label}</a>')
        position = match.end()

    pieces.append(html.escape(text[position:]))
    converted = "".join(pieces)
    converted = STRONG_RE.sub(r"<strong>\1</strong>", converted)
    converted = EM_RE.sub(r"<em>\1</em>", converted)
    return converted


def markdown_inline_to_reportlab(text: str) -> str:
    """Convert the supported inline Markdown subset to ReportLab XML."""
    converted = markdown_inline_to_html(text)
    return converted.replace("<strong>", "<b>").replace("</strong>", "</b>").replace(
        "<em>", "<i>"
    ).replace("</em>", "</i>").replace("<a href=", '<a color="#1f5f8b" href=')
