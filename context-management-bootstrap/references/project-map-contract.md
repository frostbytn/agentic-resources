# Project map contract

## Contents

- Required preamble
- Source-of-truth hierarchy
- Default agent routing
- Semantic area requirements
- Optional area subsections
- Rules and Notes
- Overlap
- Deeper documentation
- Validation placement
- Map maintenance

## Required preamble

Start with a repository-specific title ending in `Project Map`.

State directly that:

- the file is a routing index that tells agents where to start
- it is not the source of truth
- source files and tests are authoritative for current behavior
- `AGENTS.md` defines agent operating rules
- deeper architecture, runbook, migration, and other docs are reference material according to their scope
- if the map and source disagree, trust current source and update the map

## `## Source-of-truth hierarchy`

Describe the authority order without introducing competing policy.

At minimum preserve:

1. source files and tests are authoritative for current behavior
2. `AGENTS.md` defines agent operating behavior
3. the project map routes agents to likely source and validation surfaces
4. deeper docs are conditional reference material

## `## Default agent routing`

Before broad search require agents to:

- read `AGENTS.md`
- read the project map
- route from exact project-map paths first
- verify behavior in source before editing
- expand to adjacent areas or deeper docs only when current work requires it

Include an `Avoid by default:` list for globally noisy repository material that exists in the target repository.

## Semantic area requirements

Every normal mapped area must use an `##` heading and contain:

`Use for:`

- one or more concrete work intents, behaviors, responsibilities, or change surfaces

`Start here:`

- one or more verified repository-relative paths or meaningful globs

Do not use `Start here` as a general file inventory. Select entrypoints that expose ownership, orchestration, contract boundaries, canonical extension points, or focused tests.

## Optional area subsections

Use these only when they add routing value:

- `Adjacent when needed:`
- `Validation:`
- `Tests:`
- `Rules:`
- `Notes:`
- `Reference:`
- `References:`
- `Related docs:`
- `Avoid by default:`

Do not require every optional subsection in every area.

## Rules and Notes

Rules and Notes may be detailed when repository evidence justifies that detail.

Keep material that helps future agents understand:

- authority and ownership boundaries
- compatibility constraints
- established extension paths
- files or contracts that must change together
- important lifecycle or data-flow ordering
- generated-versus-authored ownership
- restore/migration behavior
- plausible but explicitly incorrect alternative paths

Do not replace verified high-value detail with vague summaries merely to make the map shorter.

Do not add generic design advice unrelated to the target repository.

## Overlap

Do not force mapped areas into mutually exclusive ownership buckets.

A path may appear in multiple areas when it is a legitimate starting point or adjacency for more than one work intent.

## Deeper documentation

Route to a deeper document only when the mapped work area genuinely benefits from it.

Do not require agents to traverse a documentation chain before reaching source.

Deeper docs remain reference material and do not override current source.

## Validation placement

Place focused validation in the mapped area when it helps an agent verify work in that area.

Prefer the narrowest repository-supported commands before broad suites.

If a known-validation-failures artifact exists, add a final `## Known validation caveats` section that routes agents to it before broad failure investigation.

## Map maintenance

The map is living routing state.

When current source reveals stale, misleading, or incomplete routing, repair the affected map area.

Update paths, intents, Rules, Notes, adjacency, and validation only where repository reality changed. Avoid unrelated map rewrites.
