#!/usr/bin/env python3
"""Validate a generated repository-aware implementation markdown plan.

This validator is intentionally strict. It checks for:
- required headings and publication sections
- forbidden placeholder and uncertainty tokens
- missing workstream subsections
- missing report contract sections
- basic markdown structural issues
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "## Executive summary",
    "## Objectives",
    "## Strategy",
    "## Guardrails",
    "## Scope definition",
    "## Verified system context",
    "## Code impact map",
    "## Stories",
    "## Workstream plan",
    "## Testing strategy",
    "## Repository publication",
    "## Agent collaboration notes",
    "## Running changelog / decision log",
    "## Implementation report contract",
]

REQUIRED_PUBLICATION_SUBHEADINGS = [
    "### Target repository",
    "### Published path",
    "### Commit contract",
]

REQUIRED_REPORT_SUBHEADINGS = [
    "### What changed",
    "### Why it changed",
    "### Files added",
    "### Files modified",
    "### Tests added or updated",
    "### Manual test checklist",
    "### Assumptions applied",
    "### Follow-up hardening steps",
]

FORBIDDEN_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\?\?\?",
    r"\bOpen Questions\b",
    r"\bFuture Investigation\b",
    r"\bMaybe\b",
    r"\bMight\b",
    r"\bCould\b",
    r"\bShould we\b",
    r"\bConsider whether\b",
    r"\bFigure out\b",
    r"\bFIXME\b",
    r"<[^>]+>",
]

FORBIDDEN_LINE_ENDING = re.compile(r"\?\s*$")
WORKSTREAM_HEADING = re.compile(r"^### Workstream \d+: .+", re.MULTILINE)
CHECKBOX_PATTERN = re.compile(r"^- \[(?: |x|X)\] ", re.MULTILINE)
PUBLISHED_PATH_PATTERN = re.compile(
    r"docs/plans/[a-z0-9-]+/[0-9]{8}-[0-9]{6}-[a-z0-9-]+-implementation-plan\.md"
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_plan_markdown.py <path-to-markdown-file>")

    path = Path(sys.argv[1])
    if not path.exists() or not path.is_file():
        fail(f"file not found: {path}")
    if path.suffix.lower() != ".md":
        fail("target file must have a .md extension")

    text = path.read_text(encoding="utf-8")

    if text.count("```") % 2 != 0:
        fail("unbalanced fenced code blocks detected")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            fail(f"missing required heading: {heading}")

    for heading in REQUIRED_PUBLICATION_SUBHEADINGS:
        if heading not in text:
            fail(f"missing required publication subheading: {heading}")

    for heading in REQUIRED_REPORT_SUBHEADINGS:
        if heading not in text:
            fail(f"missing required implementation report subheading: {heading}")

    workstreams = WORKSTREAM_HEADING.findall(text)
    if not workstreams:
        fail("at least one workstream heading is required")

    if not CHECKBOX_PATTERN.search(text):
        fail("at least one checkbox task is required")

    if not PUBLISHED_PATH_PATTERN.search(text):
        fail("published path must match docs/plans/<feature-slug>/<utc-timestamp>-<feature-slug>-implementation-plan.md")

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, text):
            fail(f"forbidden content matched pattern: {pattern}")

    for line_number, line in enumerate(text.splitlines(), start=1):
        if FORBIDDEN_LINE_ENDING.search(line):
            fail(f"question-form line detected at line {line_number}: {line.strip()}")

    for workstream in workstreams:
        start = text.index(workstream)
        next_heading_match = re.search(r"^### Workstream \d+: .+", text[start + len(workstream):], re.MULTILINE)
        end = start + len(workstream) + next_heading_match.start() if next_heading_match else len(text)
        block = text[start:end]
        for label in [
            "**Objective**",
            "**Files and code pointers**",
            "**Implementation tasks**",
            "**Test tasks**",
            "**Exit criteria**",
        ]:
            if label not in block:
                fail(f"missing '{label}' inside workstream block: {workstream}")

    print("OK: markdown plan passed validation")


if __name__ == "__main__":
    main()
