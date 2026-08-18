# Agent instructions contract

## Contents

- Required title and authority
- Default Behavior
- Startup Context Order
- Context Budget Rules
- Subagent Policy
- When to Spawn Exploratory Subagents
- Repository Areas
- Project Map Maintenance
- Map Steward Review
- Validation
- Keeping These Instructions Current
- Stop Conditions
- Compatibility entrypoints

## Required title and authority

Use a title ending in `Agent Instructions`.

Immediately establish that:

- `AGENTS.md` is the authoritative instruction file for coding-agent work in the repository
- other agent-facing entrypoints and docs must not override it
- source files and tests are authoritative for current behavior
- the project map is a routing index, not implementation truth
- if map and source disagree, trust current source and update the map

## `## Default Behavior`

Require agents to:

- keep work aligned to the requested scope
- route through the project map before broad exploration
- verify behavior in source before editing
- avoid unrelated refactors
- avoid expanding scope into adjacent improvements

Do not make this section depend on a task-planning artifact.

## `## Startup Context Order`

Before broad repository exploration require this sequence:

1. read `AGENTS.md`
2. read `docs/agent-context/project-map.md`
3. use the project map as the routing guide
4. verify current behavior in source before editing
5. consult deeper docs only when the mapped area or current task requires them
6. consult recorded validation baseline caveats before chasing broad failures when the baseline file exists

Restate that source files and tests are authoritative.

## `## Context Budget Rules`

Require targeted exploration and a `Cold by default:` list.

Include globally cold categories that actually exist in the repository, such as:

- dependency trees
- generated output
- build artifacts
- logs
- screenshots
- large unrelated assets
- lockfiles unless dependency work is in scope
- historical or archived docs when they are not relevant to current work

Do not create context tiers beyond hot and cold.

## `## Subagent Policy`

Preserve the bounded, non-overlapping delegation policy from the operating model.

Include:

- good uses
- prohibited uses
- map-first behavior for subagents
- targeted-read preference
- no nested delegation unless explicitly requested
- concise exploratory output contract: relevant files, current behavior, safest change points, validation commands, risks or unknowns
- exploratory output under 500 words

## `## When to Spawn Exploratory Subagents`

Preserve the conservative spawn behavior.

Allow exploratory subagents when at least two of these are true:

- work touches more than one major mapped area
- work crosses a meaningful package, process, runtime, or contract boundary
- durable state, compatibility-sensitive contracts, security-sensitive behavior, or other cross-boundary consistency is involved
- relevant files are not already identified by the project map
- validation failures may originate from multiple independent areas

If exact files are already known and the task is localized, do not spawn exploratory subagents.

Include exactly:

`Default maximum exploratory subagents: 3.`

Use more only when explicitly requested or scopes are clearly independent.

## `## Repository Areas`

Generate repository-specific coarse areas.

For each area use a `###` heading and include:

`Hot context:`

and

`Cold context:`

Add broadly applicable area Rules only when verified and durable.

Keep fine semantic routing in the project map.

## `## Project Map Maintenance`

Require project-map consideration after any meaningful code change.

Require map updates when a change:

- adds, removes, renames, or moves important files
- changes ownership or responsibility
- changes a major runtime, data, UI, integration, deployment, or validation flow
- changes which files future agents should inspect first
- changes validation commands or known expectations
- reveals that the map is stale, misleading, or incomplete

State that trivial implementation-only edits do not require map churn when routing, ownership, flow, commands, and important files are unchanged.

Require every final change report to include:

- `Project map updated: yes/no`
- when no, why no update was needed

## `## Map Steward Review`

For work touching more than one major mapped area, require a final routing-document review.

The review must:

- inspect the branch diff or changed-file summary
- update the project map and relevant agent instructions only if routing or durable operating behavior changed
- avoid speculative architecture notes
- avoid unrelated source edits

## `## Validation`

Require:

- narrowest relevant validation first
- baseline validation caveats before broad repair loops when available
- broader validation only when established guidance requires it, changed files cross meaningful boundaries, narrow failures indicate integration risk, or the user explicitly requests it
- unrelated verified baseline failures to be reported rather than repaired opportunistically

## `## Keeping These Instructions Current`

Update `AGENTS.md` only when durable operating context changes, including repository structure, package/workspace boundaries, validation commands, project-map conventions, subagent conventions, or major agent-facing workflows.

Do not update it for feature-specific behavior, temporary workarounds, one-off details, or routing detail that belongs in the project map.

Require:

- general and reusable instructions
- stale paths/commands removed when replaced
- conservative context-budget rules
- no duplicated project-map routing

## `## Stop Conditions`

Require agents to stop and report when:

- the requested work is complete
- relevant validation has run or a blocking issue is identified
- project-map impact has been considered and applied when needed
- agent guidance conflicts with current repository state
- the requested work would require unrequested broad architectural change

End with a direct prohibition on continuing into adjacent improvements after the requested work is complete.

## Compatibility entrypoints

Generate root `CLAUDE.md` as a thin compatibility pointer.

It should state that:

- `AGENTS.md` is the source of truth for repository operating behavior
- agents should follow `AGENTS.md` and its project-map routing
- conflicts are resolved in favor of `AGENTS.md`

Do not duplicate the full operating policy into `CLAUDE.md`.

If root `CODEX.md` already exists, normalize it using the same pointer behavior. Do not create it solely for this bootstrap.
