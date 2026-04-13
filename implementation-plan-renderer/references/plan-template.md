# feature implementation plan: <replace-with-feature-name>

## Executive summary

Provide a direct summary of the feature, the implementation intent, the affected surfaces, and the outcome this work must produce.

## Objectives

- State measurable feature objectives.
- State expected outcomes for users, developers, and system behavior.

## Strategy

- State the implementation strategy as an execution approach, not a discussion.
- State the rollout shape when relevant.

## Guardrails

- State behaviors that must remain unchanged.
- State architectural, performance, security, compatibility, maintainability, and deployment constraints.

## Scope definition

### In scope

- List the exact feature behaviors and surfaces to implement.

### Out of scope

- List adjacent items that must not be pulled into this change.

### Non-goals

- State what this plan intentionally does not attempt to solve.

## Verified system context

### Repositories, modules, and entry points

- List exact repositories, projects, packages, modules, routes, handlers, entry points, pages, jobs, or services involved.

### Data, contracts, and persistence

- List exact models, DTOs, API contracts, schemas, migrations, repositories, queries, registries, queues, cache surfaces, or event shapes involved.

### UI and interaction surface

- List exact components, views, forms, hooks, stores, or presentation layers involved.

### Configuration, permissions, and operations

- List exact config files, flags, dependency injection registrations, environment settings, permissions, logging, metrics, alerts, smoke scripts, or deployment surfaces involved.

### Architecture alignment

- List the architectural patterns, layering conventions, and cross-cutting abstractions discovered in the codebase that this plan must follow.
- List shared utilities, base classes, wrappers, or modules that existing features use and that this plan must reuse.
- List any architectural documentation files read and the key conventions extracted from them.
- When no documentation or clear conventions exist, state which default architecture principles apply.

## Code impact map

### Existing files to modify

- `path/to/file.ext` — reason this file must change

### New files to create

- `path/to/new-file.ext` — reason this file must be created

### Existing tests to update

- `path/to/existing-test.ext` — reason this test must change

### New tests to create

- `path/to/new-test.ext` — reason this test must be created

## Stories

### User stories

- As a user, ...

### Negative user stories

- As a user, I expect ... not to ...

### Developer stories

- As a developer, ...

### Negative developer stories

- As a developer, I expect ... not to ...

## Workstream plan

### Workstream execution sequence

| Order | Workstream | Depends on | Rationale |
| --- | --- | --- | --- |
| 1 | Workstream 1: name | — | Why this runs first |
| 2 | Workstream 2: name | Workstream 1 | Why this depends on Workstream 1 |

Execute workstreams in the order listed above. A workstream must not begin until all workstreams listed in its "Depends on" column are complete. Independent workstreams with no dependencies may execute in parallel.

### Workstream 1: <replace-with-concrete-workstream-name>

**Objective**

State the workstream objective.

**Files and code pointers**

- `path/to/file.ext` — `SymbolName` — exact reason
- `path/to/another-file.ext` — `functionName` — exact reason

**Existing patterns and abstractions to reuse**

- Name the existing cross-cutting pattern, shared abstraction, utility, or convention that this workstream must follow.
- When a new composable primitive must be created, name it here and explain why no existing abstraction covers the need.

**Implementation tasks**

- [ ] Task with an exact file target and behavior target
- [ ] Task with an exact file target and behavior target
- [ ] Task with an exact file target and behavior target

**Test tasks**

- [ ] Update or add a test with an exact suite or file target
- [ ] Update or add a test with an exact suite or file target

**Exit criteria**

- Observable condition that confirms this workstream is complete
- Observable condition that confirms this workstream is complete

### Workstream 2: <replace-with-concrete-workstream-name>

Repeat the exact same sub-structure for each additional workstream. Add as many workstreams as needed to cover the feature completely.

## Testing strategy

### Testing stories

- Story-driven behavior that must be validated by tests.
- Regression-sensitive behavior that must remain unchanged.

### Unit coverage

- Exact units, validators, registries, hooks, components, or helper behaviors to test.

### Integration coverage

- Exact boundaries, flows, endpoints, persistence interactions, authoring/runtime seams, or orchestration seams to test.

### Regression coverage

- Exact existing flows or areas that could break and must be covered.

### Manual verification

- Exact user flows, roles, environments, edge cases, and impacted surfaces to test manually.
- Explicitly state the blast radius.

## Repository publication

### Target repository

- `resolved-current-repository-name`

### Published path

- `docs/plans/<feature-slug>/<utc-timestamp>-<feature-slug>-implementation-plan.md`

### Commit contract

- Commit message: `docs(plans): add <feature-slug> implementation plan`
- Published markdown must exactly match the saved plan artifact.

## Agent collaboration notes

### Notes directory

- `docs/implementation-notes/<feature-slug>/README.md`
- `docs/implementation-notes/<feature-slug>/decision-log.md`
- `docs/implementation-notes/<feature-slug>/test-notes.md`
- `docs/implementation-notes/<feature-slug>/handoff-summary.md`

### Usage rules

- Use the notes directory for decisions, execution sequencing, verification evidence, and cross-agent handoff details.
- Keep the plan and the notes directory aligned.

## Running changelog / decision log

| Date | Change or decision | Why | Evidence | Owner |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Initial plan created | Establish deterministic execution path | Conversation and repository inspection | Planning agent |

## Implementation report contract

Require the implementing agent to report back with these sections after execution:

### What changed

### Why it changed

### Files added

### Files modified

### Tests added or updated

### Manual test checklist

### Assumptions applied

### Follow-up hardening steps
