---
name: implementation-plan-renderer
description: generate a deterministic repository-aware markdown implementation plan for the feature under discussion. use when working in the currently opened repository and you need a concrete execution plan for a feature, refactor, migration, architectural change, or cross-cutting delivery effort with exact file targets, workstreams, test coverage, and a saved plan artifact.
---

# Implementation Plan Renderer

Generate one comprehensive markdown implementation plan for the feature under discussion, optimized for agentic coding work in the currently opened repository.

## Core Contract

- Generate exactly one primary plan artifact named `<feature-slug>-implementation-plan.md`.
- Return the plan as a saved markdown file inside the repository when file writing is available. Only fall back to inline markdown if file creation is unavailable.
- Preserve valid markdown at all times. Use only standard markdown constructs.
- Replace every placeholder before finalizing. The final plan must contain no unresolved markers, no template tokens, and no note-to-self language.
- Do not include questions, options lists, brainstorming, or uncertainty language anywhere in the final plan.
- Base the plan on verified conversation context plus verified repository context. Never invent file paths, symbols, tests, modules, or architecture.
- Optimize the plan for implementation by coding agents. Every workstream and checkbox task must be executable without interpretation drift.

## Required Resources

Load these files before drafting the plan:

- `references/plan-template.md`
- `references/quality-rules.md`
- `references/repository-contract.md`

Use `scripts/validate_plan_markdown.py` before returning the plan artifact.

## Execution Workflow

### 1. Lock The Feature Definition

- Extract the implementation target, scope boundary, constraints, affected surfaces, guardrails, success criteria, and non-goals from the current conversation.
- Convert abstract discussion into a single concrete implementation direction.
- Prefer existing repository patterns already verified in repository files.
- Keep the plan deterministic. Do not insert follow-up questions into the plan.

### 2. Inspect The Repository Surface

Inspect the actual repository before naming files, symbols, workstreams, or tests.

Always verify, when relevant:

- entry points, routes, pages, handlers, background processes, schedulers, services, and jobs
- models, DTOs, contracts, serializers, validators, schemas, registries, and asset catalogs
- UI components, hooks, stores, view models, registries, and interaction flows
- config files, deployment surfaces, feature flags, environment contracts, permissions, and observability seams
- existing tests, fixtures, smoke scripts, manual verification helpers, and test commands
- existing `docs/implementation-notes/` and `docs/plans/` conventions, or the nearest equivalent documentation structure

For every area that matters, capture:

- exact file path
- exact symbol, function, component, test suite, command, or route when available
- why the area is involved
- whether it must be created, modified, extended, or validated only

### 3. Resolve Repository Identity And Publication Paths

Resolve the active repository context before writing the plan.

Always verify, when available:

- repository root
- repository name from git remote metadata or workspace folder name
- current branch name
- whether `docs/` already exists

Use these defaults unless a stronger verified repository convention already exists:

- plan publication root: `docs/plans/`
- collaboration-notes root: `docs/implementation-notes/`
- commit message: `docs(plans): add <feature-slug> implementation plan`

Publish the validated plan to:

- `docs/plans/<feature-slug>/<utc-timestamp>-<feature-slug>-implementation-plan.md`

### 4. Build The Workstream Map

Split the feature into concern-aligned workstreams. Workstreams must reflect real boundaries such as UI, API, backend logic, data contracts, persistence, configuration, observability, deployment, and test coverage.

For every workstream:

- name it precisely
- state the objective in one direct sentence
- list exact files to modify and exact files to create
- include checkbox implementation tasks in execution order
- include checkbox test tasks tied to real suites or commands
- include explicit exit criteria

### 5. Draft The Plan

- Use the exact section structure from `references/plan-template.md`.
- Keep all major headings from the template.
- Populate each section with concrete repository-aware content.
- Apply every rule from `references/quality-rules.md`.

### 6. Add Collaboration Paths

For non-trivial work, plan collaboration notes under the verified repository convention:

- `docs/implementation-notes/<feature-slug>/README.md`
- `docs/implementation-notes/<feature-slug>/decision-log.md`
- `docs/implementation-notes/<feature-slug>/test-notes.md`
- `docs/implementation-notes/<feature-slug>/handoff-summary.md`

Reference those paths directly in the plan where cross-agent coordination is needed.

### 7. Validate The Markdown Artifact

- Save the finished plan as `<feature-slug>-implementation-plan.md` during drafting, then place the final copy under `docs/plans/<feature-slug>/`.
- Run `python scripts/validate_plan_markdown.py <path-to-markdown-file>`.
- If validation fails, fix the plan and validate again.
- Do not return the plan until validation passes.

### 8. Publish The Same Plan To The Current Repository

After validation, publish the identical markdown content into the currently opened repository.

Use this exact publication contract:

- repository: resolved current repository name or workspace repository label
- branch: resolved current branch when available
- path: `docs/plans/<feature-slug>/<utc-timestamp>-<feature-slug>-implementation-plan.md`
- commit message: `docs(plans): add <feature-slug> implementation plan`

Publication rules:

- Create the scoped feature directory under `docs/plans/` as part of the file path.
- Publish the exact same markdown body that was returned as the saved plan artifact.
- Prefer direct file creation in the current workspace when the path is new.
- If publication fails because file write access is unavailable, state that clearly in the final response and still return the validated markdown artifact.
- Never skip publication silently.

## Evidence Rules

- Reference only verified files and verified symbols.
- Prefer exact file paths over directory-level references.
- Prefer exact symbol names over vague component descriptions.
- When introducing a new file, place it under a verified existing directory whenever possible.
- When introducing a new directory, justify it and keep it aligned with existing repository structure.
- Name the exact tests to update or create.
- Name the exact commands to run for relevant validation work.

## Mandatory Plan Content

The final plan must include all of the following:

- executive summary
- objectives, outcomes, strategy, and guardrails
- scope definition with in-scope, out-of-scope, and non-goals
- verified system context and code impact map
- user stories and negative user stories
- developer stories and negative developer stories
- segmented workstreams with checkbox subtasks
- testing stories that map to unit, integration, regression, and manual verification work
- manual testing guidance that tells the developer exactly what to test and what areas were impacted
- repository publication section with the final `docs/plans/...` target path
- running changelog / decision log for the implementing agent
- implementation report contract with the exact sections the implementing agent must use when reporting back

## Output Quality Gates

Reject and rewrite the plan before returning it if any of the following are true:

- any placeholder text remains
- any section asks a question or leaves an open decision
- any task lacks a concrete file or behavior target
- any workstream mixes unrelated concerns without clear sequencing
- any testing section is generic or disconnected from the feature stories
- any markdown section is malformed
- any publication path does not target `docs/plans/`
- the plan differs from the markdown content published to the repository

## Final Response Contract

Return a short response that includes:

- the saved markdown file path
- the repository publication path used for the committed or written copy
- a brief note when publication could not be completed

Do not echo the full plan body into chat after the artifact is created.
