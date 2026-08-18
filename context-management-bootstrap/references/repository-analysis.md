# Repository analysis

## Contents

- Resolve repository topology
- Read existing agent and engineering guidance
- Identify coarse repository areas
- Identify semantic project-map areas
- Select Start here locations
- Capture adjacency
- Capture repository-specific Rules and Notes
- Capture validation
- Detect validation baseline memory
- Refresh mode

## 1. Resolve repository topology

Inspect verified repository metadata and top-level structure.

Identify:

- repository root and active workspace
- top-level packages, applications, services, libraries, infrastructure, tooling, or other major workspaces
- language and build manifests
- test projects and test runners
- deployment/configuration surfaces
- generated-output and dependency locations
- large or noisy areas that should remain cold by default

Do not infer responsibility from folder names alone.

## 2. Read existing agent and engineering guidance

Inspect existing agent-facing instructions first, including root agent files and any repository-local guidance they reference.

Then inspect relevant repository documentation such as:

- root and package README files
- architecture or design documents
- ADRs or decision records
- contribution/development guides
- runbooks
- validation/test documentation
- deployment documentation

Treat documentation as evidence of intended structure. Verify current behavior and paths in source and tests before making them authoritative in generated context.

## 3. Identify coarse repository areas

Derive the small set of major work areas that meaningfully change what context should be hot or cold during normal agent work.

For each coarse area determine:

- hot context: source, tests, config, or docs normally needed first
- cold context: unrelated packages, generated output, large assets, deployment surfaces, or other areas that should not be loaded by default
- durable rules that belong in `AGENTS.md` only when they apply broadly to that coarse area

Do not duplicate fine semantic routing here.

## 4. Identify semantic project-map areas

Derive work areas from actual change intent and repository responsibility.

Use evidence such as:

- composition roots and registration points
- routes, handlers, controllers, commands, jobs, and schedulers
- core services and domain modules
- persistence models and migrations
- shared contracts and schemas
- UI composition and state boundaries
- build/deployment entrypoints
- integration adapters
- test suites organized around behavior
- existing docs that describe stable responsibility boundaries

A semantic area may cross directories or packages. A source path may participate in multiple areas.

## 5. Select `Start here` locations

Choose verified paths that give an agent the fastest reliable orientation for the mapped work intent.

Prefer paths that expose:

- ownership
- orchestration
- composition
- contract boundaries
- state transitions
- canonical extension points
- directly relevant tests

Use exact repository-relative paths or meaningful repository-relative globs.

Do not list files merely because they exist. Do not use stale paths from documentation without verifying them.

## 6. Capture adjacency

Add `Adjacent when needed` only when crossing a real boundary commonly requires the additional location.

Examples of qualifying relationships include:

- source plus shared contract
- runtime plus persistence model
- API surface plus consuming client
- implementation plus focused test suite
- deployment entrypoint plus runtime configuration

Do not use adjacency as an excuse for broad repository expansion.

## 7. Capture repository-specific Rules and Notes

Record a Rule or Note when verified repository evidence shows that future agents could otherwise take a plausible but incorrect path.

High-value material includes:

- authority boundaries
- ownership or responsibility boundaries
- compatibility-sensitive contracts
- established extension points
- files or data that must change together
- data flow or lifecycle ordering that is easy to misread
- generated versus authored ownership
- current migration/restore behavior that must be preserved
- explicit alternatives that the repository intentionally does not use

Do not add generic engineering principles unless they are already established repository rules and materially affect work in that area.

## 8. Capture validation

For each semantic area, identify the narrowest meaningful validation exposed by the repository.

Prefer:

- focused test commands
- package/project builds
- linters/type checks
- schema/content validators
- smoke scripts
- targeted integration checks

Add broader validation only when repository guidance or cross-boundary impact justifies it.

## 9. Detect validation baseline memory

Look for verified recurring failures or baseline caveats in existing context docs, test guidance, CI notes available in the workspace, or established repository documentation.

Do not run broad failing suites solely to manufacture a baseline file.

If stable recurring baseline knowledge exists, preserve it in the known-validation-failures artifact. If it does not, omit that artifact.

## 10. Refresh mode

When the context system already exists:

1. Read `AGENTS.md` and the current project map.
2. Treat every existing path, ownership claim, Rule, Note, and validation command as a candidate that must still match current repository reality.
3. Preserve detail that remains correct.
4. Repair moved/renamed paths and changed responsibility.
5. Remove obsolete semantic intents and add newly established important intents.
6. Re-check coarse hot/cold areas.
7. Re-check existing validation baseline entries.
8. Re-run the full validator.

Do not reset a mature map to a smaller generic map merely because the repository has accumulated detailed, still-valid routing knowledge.
