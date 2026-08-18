#!/usr/bin/env python3
"""Validate a repository context-management bootstrap.

The validator is intentionally structural. It checks deterministic properties of
agent instructions, project-map routing, compatibility entrypoints, optional
validation-baseline memory, placeholders, and verified Start-here paths.

Architectural correctness remains a source-review responsibility for the agent.
"""

from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

AGENTS_PATH = Path("AGENTS.md")
CLAUDE_PATH = Path("CLAUDE.md")
CODEX_PATH = Path("CODEX.md")
MAP_PATH = Path("docs/agent-context/project-map.md")
VALIDATION_PATH = Path("docs/agent-context/known-validation-failures.md")

REQUIRED_AGENT_HEADINGS = [
    "## Default Behavior",
    "## Startup Context Order",
    "## Context Budget Rules",
    "## Subagent Policy",
    "## When to Spawn Exploratory Subagents",
    "## Repository Areas",
    "## Project Map Maintenance",
    "## Map Steward Review",
    "## Validation",
    "## Keeping These Instructions Current",
    "## Stop Conditions",
]

REQUIRED_MAP_HEADINGS = [
    "## Source-of-truth hierarchy",
    "## Default agent routing",
]

RESERVED_MAP_HEADINGS = {
    "Source-of-truth hierarchy",
    "Default agent routing",
    "Known validation caveats",
}

FORBIDDEN_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\?\?\?",
    r"<[^>]+>",
]

AGENT_TITLE = re.compile(r"^# (?:.+ )?Agent Instructions\s*$", re.MULTILINE)
MAP_TITLE = re.compile(r"^# (?:.+ )?Project Map\s*$", re.MULTILINE)
H2 = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
LIST_ITEM = re.compile(r"^-\s+(.+)$", re.MULTILINE)
BACKTICK = re.compile(r"`([^`]+)`")

errors: list[str] = []


def record(message: str) -> None:
    errors.append(message)


def read_required(root: Path, relative: Path) -> str:
    path = root / relative
    if not path.is_file():
        record(f"missing required file: {relative.as_posix()}")
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        record(f"required file is not valid UTF-8 text: {relative.as_posix()}")
        return ""


def read_optional(root: Path, relative: Path) -> str | None:
    path = root / relative
    if not path.exists():
        return None
    if not path.is_file():
        record(f"expected file path is not a file: {relative.as_posix()}")
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        record(f"optional context file is not valid UTF-8 text: {relative.as_posix()}")
        return ""


def extract_h2_sections(text: str) -> list[tuple[str, str]]:
    matches = list(H2.finditer(text))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), text[start:end]))
    return sections


def extract_label_block(section: str, label: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(label)}\s*$", re.MULTILINE)
    match = pattern.search(section)
    if not match:
        return None
    rest = section[match.end():]
    next_boundary = re.search(r"^(?:#{1,6} |[A-Z][A-Za-z /-]*:)\s*$", rest, re.MULTILINE)
    if next_boundary:
        return rest[: next_boundary.start()]
    return rest


def validate_placeholders(label: str, text: str) -> None:
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, text):
            record(f"{label} contains forbidden placeholder pattern: {pattern}")


def validate_authority(agents: str, project_map: str) -> None:
    lowered_agents = agents.lower()
    lowered_map = project_map.lower()

    if "agents.md" not in lowered_agents or not (
        "authoritative instruction" in lowered_agents or "source of truth" in lowered_agents
    ):
        record("AGENTS.md must identify itself as the authoritative operating instructions")

    if "project map" not in lowered_agents or "routing index" not in lowered_agents:
        record("AGENTS.md must identify the project map as a routing index")

    if "source files" not in lowered_agents or "authoritative" not in lowered_agents:
        record("AGENTS.md must preserve source authority for current behavior")

    if "not the source of truth" not in lowered_map:
        record("project map must state that it is not the source of truth")

    if "source files" not in lowered_map or "authoritative" not in lowered_map:
        record("project map must state that source files are authoritative")

    if "agents.md" not in lowered_map:
        record("project map must route operating behavior back to AGENTS.md")


def validate_agents(agents: str) -> None:
    if not agents:
        return

    if not AGENT_TITLE.search(agents):
        record("AGENTS.md title must end with 'Agent Instructions'")

    for heading in REQUIRED_AGENT_HEADINGS:
        if heading not in agents:
            record(f"AGENTS.md missing required heading: {heading}")

    if MAP_PATH.as_posix() not in agents:
        record(f"AGENTS.md must reference {MAP_PATH.as_posix()}")

    if "Cold by default:" not in agents:
        record("AGENTS.md must include a 'Cold by default:' context list")

    repo_areas = extract_label_block_for_h2(agents, "Repository Areas")
    if repo_areas is not None:
        if "Hot context:" not in repo_areas:
            record("AGENTS.md Repository Areas must include at least one 'Hot context:' block")
        if "Cold context:" not in repo_areas:
            record("AGENTS.md Repository Areas must include at least one 'Cold context:' block")

    if "Default maximum exploratory subagents: 3." not in agents:
        record("AGENTS.md must preserve the default maximum of 3 exploratory subagents")

    exploratory_contract = [
        "relevant files",
        "current behavior",
        "safest change points",
        "validation commands",
        "risks or unknowns",
        "500 words",
    ]
    lowered = agents.lower()
    for phrase in exploratory_contract:
        if phrase.lower() not in lowered:
            record(f"AGENTS.md missing exploratory subagent contract element: {phrase}")

    maintenance_terms = [
        "important files",
        "ownership or responsibility",
        "validation commands",
        "stale, misleading, or incomplete",
        "Project map updated: yes/no",
    ]
    for phrase in maintenance_terms:
        if phrase.lower() not in lowered:
            record(f"AGENTS.md missing project-map maintenance element: {phrase}")

    if "branch diff" not in lowered and "changed-file summary" not in lowered:
        record("AGENTS.md Map Steward Review must inspect the branch diff or changed-file summary")

    if "narrowest relevant validation first" not in lowered:
        record("AGENTS.md must require narrowest relevant validation first")

    if "do not continue into adjacent improvements" not in lowered:
        record("AGENTS.md must preserve the adjacent-improvement stop rule")


def extract_label_block_for_h2(text: str, heading_name: str) -> str | None:
    sections = dict(extract_h2_sections(text))
    return sections.get(heading_name)


def validate_compatibility_file(label: str, text: str | None) -> None:
    if text is None or text == "":
        return
    lowered = text.lower()
    if "agents.md" not in lowered:
        record(f"{label} must point directly to AGENTS.md")
    if "source of truth" not in lowered and "authoritative" not in lowered:
        record(f"{label} must identify AGENTS.md as the authority")


def path_matches(root: Path, raw: str) -> bool:
    normalized = raw.strip().replace("\\", "/")
    if not normalized:
        return False
    if normalized.startswith("/") or re.match(r"^[A-Za-z]:/", normalized):
        return False
    if normalized == ".." or normalized.startswith("../") or "/../" in normalized:
        return False

    if any(ch in normalized for ch in "*?["):
        pattern = str(root / normalized)
        return any(Path(match).exists() for match in glob.glob(pattern, recursive=True))

    return (root / normalized).exists()


def validate_map(root: Path, project_map: str, validation_exists: bool) -> None:
    if not project_map:
        return

    if not MAP_TITLE.search(project_map):
        record("project-map title must end with 'Project Map'")

    for heading in REQUIRED_MAP_HEADINGS:
        if heading not in project_map:
            record(f"project map missing required heading: {heading}")

    sections = extract_h2_sections(project_map)
    domain_sections = [(name, body) for name, body in sections if name not in RESERVED_MAP_HEADINGS]

    if not domain_sections:
        record("project map must contain at least one semantic mapped area")
        return

    names = [name for name, _ in domain_sections]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    for name in duplicates:
        record(f"duplicate project-map area heading: {name}")

    for name, body in domain_sections:
        use_for = extract_label_block(body, "Use for:")
        start_here = extract_label_block(body, "Start here:")

        if use_for is None:
            record(f"project-map area '{name}' missing 'Use for:'")
        elif not LIST_ITEM.search(use_for):
            record(f"project-map area '{name}' must list at least one use intent")

        if start_here is None:
            record(f"project-map area '{name}' missing 'Start here:'")
            continue

        items = LIST_ITEM.findall(start_here)
        if not items:
            record(f"project-map area '{name}' must list at least one Start-here path")
            continue

        for item in items:
            refs = BACKTICK.findall(item)
            if not refs:
                record(f"project-map area '{name}' Start-here item lacks a backticked path: {item}")
                continue
            for ref in refs:
                if not path_matches(root, ref):
                    record(f"project-map area '{name}' has missing Start-here path/glob: {ref}")

    has_validation_section = any(name == "Known validation caveats" for name, _ in sections)
    if validation_exists and not has_validation_section:
        record("project map must include '## Known validation caveats' when validation baseline memory exists")
    if has_validation_section and not validation_exists:
        record("project map routes to validation caveats but no validation baseline file exists")
    if validation_exists and VALIDATION_PATH.as_posix() not in project_map:
        record(f"project map must reference {VALIDATION_PATH.as_posix()} when it exists")


def validate_validation_memory(text: str | None) -> None:
    if text is None or text == "":
        return

    if "# Known Validation Failures" not in text:
        record("known-validation-failures.md missing required title")

    required = [
        "Command:",
        "Current expectation:",
        "Agent behavior:",
        "## Updating this file",
    ]
    for marker in required:
        if marker not in text:
            record(f"known-validation-failures.md missing required marker: {marker}")


def main() -> None:
    if len(sys.argv) != 2:
        print("ERROR: usage: validate_context_bootstrap.py <repository-root>")
        raise SystemExit(1)

    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"ERROR: repository root not found: {root}")
        raise SystemExit(1)

    agents = read_required(root, AGENTS_PATH)
    claude = read_required(root, CLAUDE_PATH)
    project_map = read_required(root, MAP_PATH)
    codex = read_optional(root, CODEX_PATH)
    validation = read_optional(root, VALIDATION_PATH)

    validate_agents(agents)
    validate_compatibility_file("CLAUDE.md", claude)
    validate_compatibility_file("CODEX.md", codex)
    validate_authority(agents, project_map)
    validate_map(root, project_map, validation is not None)
    validate_validation_memory(validation)

    for label, text in [
        (AGENTS_PATH.as_posix(), agents),
        (CLAUDE_PATH.as_posix(), claude),
        (MAP_PATH.as_posix(), project_map),
        (CODEX_PATH.as_posix(), codex or ""),
        (VALIDATION_PATH.as_posix(), validation or ""),
    ]:
        if text:
            validate_placeholders(label, text)
            if text.count("```") % 2 != 0:
                record(f"{label} contains unbalanced fenced code blocks")

    if errors:
        print(f"FAILED: {len(errors)} validation error(s)\n")
        for index, error in enumerate(errors, 1):
            print(f"  {index}. {error}")
        raise SystemExit(1)

    print("OK: repository context bootstrap passed validation")


if __name__ == "__main__":
    main()
