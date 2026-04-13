#!/usr/bin/env python3
"""Validate a generated repository-aware implementation markdown plan.

This validator is intentionally strict. It checks for:
- required headings and publication sections
- forbidden placeholder and uncertainty tokens
- missing workstream subsections (including architecture alignment)
- workstream execution sequence table
- missing report contract sections
- basic markdown structural issues
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Required top-level headings
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# Required sub-headings under specific sections
# ---------------------------------------------------------------------------

REQUIRED_SYSTEM_CONTEXT_SUBHEADINGS = [
    "### Architecture alignment",
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

# ---------------------------------------------------------------------------
# Forbidden content patterns
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# Structural patterns
# ---------------------------------------------------------------------------

WORKSTREAM_HEADING = re.compile(r"^### Workstream \d+: .+", re.MULTILINE)
WORKSTREAM_NUMBER = re.compile(r"^### Workstream (\d+): .+", re.MULTILINE)
CHECKBOX_PATTERN = re.compile(r"^- \[(?: |x|X)\] ", re.MULTILINE)
PUBLISHED_PATH_PATTERN = re.compile(
    r"docs/plans/[a-z0-9-]+/[0-9]{8}-[0-9]{6}-[a-z0-9-]+-implementation-plan\.md"
)

# The execution sequence table must appear inside the Workstream plan section.
# It requires a header row with at minimum: Order, Workstream, Depends on.
SEQUENCE_TABLE_HEADER = re.compile(
    r"^\|[^\n]*Order[^\n]*\|[^\n]*Workstream[^\n]*\|[^\n]*Depends on[^\n]*\|",
    re.MULTILINE | re.IGNORECASE,
)
SEQUENCE_TABLE_ROW = re.compile(
    r"^\|\s*\d+\s*\|", re.MULTILINE
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

errors: list[str] = []


def record(message: str) -> None:
    """Record a validation error without exiting immediately."""
    errors.append(message)


def extract_workstream_block(text: str, heading: str, all_headings: list[str]) -> str:
    """Return the text block for a single workstream heading."""
    start = text.index(heading)
    # Find the next workstream heading or the next ## heading
    rest = text[start + len(heading):]
    next_ws = re.search(r"^### Workstream \d+: .+", rest, re.MULTILINE)
    next_h2 = re.search(r"^## ", rest, re.MULTILINE)
    candidates = []
    if next_ws:
        candidates.append(start + len(heading) + next_ws.start())
    if next_h2:
        candidates.append(start + len(heading) + next_h2.start())
    end = min(candidates) if candidates else len(text)
    return text[start:end]


def extract_section(text: str, heading: str) -> str | None:
    """Return the text from *heading* until the next heading of equal or higher level."""
    level_match = re.match(r"^(#+)", heading)
    if not level_match:
        return None
    level = len(level_match.group(1))
    pattern = re.compile(rf"^{re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return None
    start = match.start()
    rest = text[match.end():]
    # Match next heading of equal or higher level (fewer or equal #)
    next_heading = re.search(rf"^#{{1,{level}}} ", rest, re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading else len(text)
    return text[start:end]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    if len(sys.argv) != 2:
        print("ERROR: usage: validate_plan_markdown.py <path-to-markdown-file>")
        raise SystemExit(1)

    path = Path(sys.argv[1])
    if not path.exists() or not path.is_file():
        print(f"ERROR: file not found: {path}")
        raise SystemExit(1)
    if path.suffix.lower() != ".md":
        print("ERROR: target file must have a .md extension")
        raise SystemExit(1)

    text = path.read_text(encoding="utf-8")

    # -----------------------------------------------------------------------
    # Structural markdown checks
    # -----------------------------------------------------------------------

    if text.count("```") % 2 != 0:
        record("unbalanced fenced code blocks detected")

    # -----------------------------------------------------------------------
    # Required headings
    # -----------------------------------------------------------------------

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            record(f"missing required heading: {heading}")

    for heading in REQUIRED_SYSTEM_CONTEXT_SUBHEADINGS:
        if heading not in text:
            record(f"missing required system-context subheading: {heading}")

    for heading in REQUIRED_PUBLICATION_SUBHEADINGS:
        if heading not in text:
            record(f"missing required publication subheading: {heading}")

    for heading in REQUIRED_REPORT_SUBHEADINGS:
        if heading not in text:
            record(f"missing required implementation report subheading: {heading}")

    # -----------------------------------------------------------------------
    # Workstream headings
    # -----------------------------------------------------------------------

    workstreams = WORKSTREAM_HEADING.findall(text)
    if not workstreams:
        record("at least one workstream heading is required")

    if not CHECKBOX_PATTERN.search(text):
        record("at least one checkbox task is required")

    # -----------------------------------------------------------------------
    # Workstream execution sequence
    # -----------------------------------------------------------------------

    workstream_section = extract_section(text, "## Workstream plan")
    if workstream_section:
        if not SEQUENCE_TABLE_HEADER.search(workstream_section):
            record(
                "missing workstream execution sequence table inside '## Workstream plan' "
                "(must contain a table with columns: Order, Workstream, Depends on)"
            )
        else:
            # Verify the table has at least as many data rows as workstreams
            sequence_rows = SEQUENCE_TABLE_ROW.findall(workstream_section)
            if len(sequence_rows) < len(workstreams):
                record(
                    f"workstream execution sequence table has {len(sequence_rows)} "
                    f"row(s) but {len(workstreams)} workstream(s) exist — every "
                    f"workstream must appear in the sequence table"
                )
    elif workstreams:
        record(
            "could not locate '## Workstream plan' section to validate execution sequence"
        )

    # Verify workstream numbers are sequential starting from 1
    ws_numbers = [int(m) for m in WORKSTREAM_NUMBER.findall(text)]
    if ws_numbers and ws_numbers != list(range(1, len(ws_numbers) + 1)):
        record(
            f"workstream numbers must be sequential starting from 1, "
            f"found: {ws_numbers}"
        )

    # -----------------------------------------------------------------------
    # Publication path
    # -----------------------------------------------------------------------

    if not PUBLISHED_PATH_PATTERN.search(text):
        record(
            "published path must match "
            "docs/plans/<feature-slug>/<utc-timestamp>-<feature-slug>-implementation-plan.md"
        )

    # -----------------------------------------------------------------------
    # Forbidden content
    # -----------------------------------------------------------------------

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, text):
            record(f"forbidden content matched pattern: {pattern}")

    for line_number, line in enumerate(text.splitlines(), start=1):
        if FORBIDDEN_LINE_ENDING.search(line):
            record(f"question-form line detected at line {line_number}: {line.strip()}")

    # -----------------------------------------------------------------------
    # Per-workstream block validation
    # -----------------------------------------------------------------------

    for workstream in workstreams:
        block = extract_workstream_block(text, workstream, workstreams)

        required_labels = [
            "**Objective**",
            "**Files and code pointers**",
            "**Existing patterns and abstractions to reuse**",
            "**Implementation tasks**",
            "**Test tasks**",
            "**Exit criteria**",
        ]
        for label in required_labels:
            if label not in block:
                record(f"missing '{label}' inside workstream block: {workstream}")

        # Each workstream must have at least one checkbox task
        if not CHECKBOX_PATTERN.search(block):
            record(f"no checkbox tasks found inside workstream block: {workstream}")

    # -----------------------------------------------------------------------
    # Architecture alignment in verified system context
    # -----------------------------------------------------------------------

    arch_section = extract_section(text, "### Architecture alignment")
    if arch_section:
        # Must have substantive content (more than just the heading)
        content_lines = [
            line.strip()
            for line in arch_section.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
        if not content_lines:
            record(
                "'### Architecture alignment' section exists but has no content — "
                "document the patterns, conventions, and abstractions discovered "
                "during codebase analysis"
            )

    # -----------------------------------------------------------------------
    # Guardrails must mention architecture (light heuristic)
    # -----------------------------------------------------------------------

    guardrails_section = extract_section(text, "## Guardrails")
    if guardrails_section:
        arch_keywords = re.compile(
            r"architect|pattern|convention|abstraction|invariant|layer|reuse|existing",
            re.IGNORECASE,
        )
        if not arch_keywords.search(guardrails_section):
            record(
                "'## Guardrails' section should include architectural invariants "
                "discovered during codebase analysis (no architecture-related "
                "language detected)"
            )

    # -----------------------------------------------------------------------
    # Report
    # -----------------------------------------------------------------------

    if errors:
        print(f"FAILED: {len(errors)} validation error(s)\n")
        for i, err in enumerate(errors, 1):
            print(f"  {i}. {err}")
        raise SystemExit(1)

    print("OK: markdown plan passed validation")


if __name__ == "__main__":
    main()
