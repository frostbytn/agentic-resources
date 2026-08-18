# Operating model

## Contents

- Authority model
- Startup and context acquisition
- Hot and cold context
- Two routing resolutions
- Semantic project-map behavior
- Bounded subagent behavior
- Validation behavior
- Validation baseline memory
- Project-map maintenance
- Map-steward review
- Instruction maintenance
- Stop behavior
- Non-innovation invariant

## Authority model

1. Keep one authoritative repository operating-instruction source.
2. Use root `AGENTS.md` as that authority.
3. Keep vendor-specific entrypoints subordinate to `AGENTS.md` rather than creating competing policy.
4. Treat the project map as a routing index, not as implementation truth.
5. Treat source files and tests as authoritative for current behavior.
6. When the project map and source disagree, trust current source and repair the map.

## Startup and context acquisition

1. Read the authoritative agent instructions before broad repository exploration.
2. Read the project map before broad repository exploration.
3. Route from the project map to likely source entrypoints.
4. Verify current behavior in source before editing.
5. Expand context only when the current task, an imported dependency, a contract boundary, a test boundary, or a validation failure justifies it.
6. Avoid broad repository scans when targeted routing is sufficient.

## Hot and cold context

Use exactly the hot/cold model.

- Hot context is the normal starting context for a specific coarse work area.
- Cold context is not prohibited. It is context that should not be loaded by default and becomes relevant only when the current work justifies it.

Keep globally noisy material cold by default when present, including dependency trees, generated output, build artifacts, logs, screenshots, large unrelated assets, and lockfiles unless dependency work is in scope.

Infer repository-specific hot/cold boundaries from the target repository. Do not create additional context tiers, scoring systems, or priority models.

## Two routing resolutions

Preserve the division between coarse operating context and fine semantic routing.

- `AGENTS.md` carries coarse repository/workspace hot/cold areas and durable operating behavior.
- The project map carries fine semantic routing for work intents, source entrypoints, adjacency, local invariants, tests, validation, and conditional references.

Do not duplicate fine project-map routing into `AGENTS.md`.

## Semantic project-map behavior

1. Organize mapped areas around work intents, capabilities, responsibilities, and change surfaces rather than mirroring the directory tree.
2. Every mapped area must answer `Use for` and `Start here`.
3. Add `Adjacent when needed`, `Validation`, `Tests`, `Rules`, `Notes`, `Reference`, `Related docs`, or `Avoid by default` only when they improve future routing or prevent a known wrong path.
4. Allow mapped areas to overlap when the same source location is a legitimate entrypoint for multiple kinds of work.
5. Keep verified repository-specific Rules and Notes when they materially encode authority, ownership, compatibility, established extension paths, files that change together, or alternatives that should not be introduced.
6. Do not reduce the map to a filesystem index.
7. Do not turn the map into generic architecture documentation unrelated to agent routing.

## Bounded subagent behavior

Use subagents only when work naturally splits into bounded, non-overlapping scopes.

Good uses:

- read-only exploration across separate repository domains
- independent validation of separate areas
- completed-diff review for correctness, scope creep, or stale context docs
- map-steward review after multi-domain changes

Do not use subagents for:

- small single-file or single-domain changes
- broad repository exploration
- duplicate investigation of the same files
- speculative architecture work
- unassigned implementation work

Exploratory subagents must:

- read the project map first
- stay within their assigned scope
- prefer search and targeted reads over broad scans
- avoid editing unless explicitly assigned
- avoid nested delegation unless explicitly requested
- return concise findings

Exploratory findings must cover:

- relevant files
- current behavior
- safest change points
- validation commands
- risks or unknowns

Keep exploratory output under 500 words.

Default maximum exploratory subagents: 3.

Use more than 3 only when explicitly requested or when clearly independent scopes require it.

## Validation behavior

1. Run the narrowest relevant validation first.
2. Read recorded baseline validation caveats before chasing broad failures when such a baseline exists.
3. Broaden validation when changed files cross meaningful boundaries, narrow validation indicates integration risk, established repository guidance requires it, or the user explicitly requests it.
4. Do not spend repair loops on verified unrelated baseline failures.
5. Investigate failures caused by the current change.

## Validation baseline memory

Use a known-validation-failures artifact only when verified recurring baseline knowledge exists.

Each validation entry records:

- command
- current expectation
- recurring examples when known
- required agent behavior

Update it when a known broad failure is fixed, changes shape, a new recurring unrelated baseline issue is verified, or expected validation commands change.

Do not use it for one-off task-specific failures.

## Project-map maintenance

After any meaningful code change, consider whether the project map needs an update.

Update the map when a change:

- adds, removes, renames, or moves important files
- changes ownership or responsibility of a module or area
- changes a major runtime, data, UI, integration, deployment, or validation flow
- changes which files future agents should inspect first for a work area
- changes validation commands or known expectations
- reveals that the map is stale, misleading, or incomplete

Do not update the map for trivial implementation-only edits that do not affect routing, ownership, flow, commands, or important files.

Every final change report must state whether the project map was updated and, when it was not, why no update was needed.

## Map-steward review

For changes touching more than one major mapped area, run a final routing-document review before stopping.

The review must:

- inspect the branch diff or changed-file summary
- update the project map and relevant agent instructions only when routing or durable operating behavior changed
- avoid speculative architecture notes
- avoid unrelated source edits

## Instruction maintenance

Update `AGENTS.md` only when durable repository operating context changes, such as:

- repository structure
- package or workspace boundaries
- validation commands
- project-map conventions
- subagent conventions
- major agent-facing workflows

Do not update it for feature-specific behavior, temporary workarounds, one-off details, or routing detail that belongs in the project map.

When updating it:

- keep instructions reusable across future work
- prefer area-level rules over feature-specific rules
- remove stale paths or commands when replacing them
- keep context-budget rules conservative
- do not duplicate project-map routing

## Stop behavior

Stop and report when the requested work is complete, relevant validation has run or a blocker is identified, the project-map impact has been considered, or the work would require unrequested broad architectural change.

Do not continue into adjacent improvements after the requested work is complete.

## Non-innovation invariant

Do not introduce new context-management mechanisms while applying this skill.

In particular, do not add:

- context states beyond hot and cold
- context scoring or confidence models
- new routing layers or nested map hierarchies
- agent-memory systems
- generated architecture encyclopedias
- mandatory task-planning systems
- new delegation topologies
- arbitrary map-size, domain-count, or entry-count budgets
- rigid requirements for optional map subsections

Repository-specific content may be rich. The operating model must remain fixed.
