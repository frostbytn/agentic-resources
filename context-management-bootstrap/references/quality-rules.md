# Quality rules

## Contents

- Fixed operating-model rules
- Repository-evidence rules
- Existing-instruction rules
- Project-map rules
- Context-budget rules
- Validation rules
- Adversarial source review
- Refresh review
- Forbidden output state

## Fixed operating-model rules

- Preserve the operating model in `references/operating-model.md`.
- Do not add new context-management layers, tiers, scoring systems, routing hierarchies, memory mechanisms, or delegation patterns.
- Use only hot and cold context classifications.
- Keep one authoritative operating-instruction source.
- Keep the project map a routing index rather than implementation truth.
- Keep source files and tests authoritative for current behavior.
- Keep map maintenance and map-steward behavior in the generated operating instructions.
- Keep the default exploratory subagent maximum at 3.
- Do not require task-planning artifacts for the context system to work.

## Repository-evidence rules

- Every `Start here` path must exist in the current repository or be a meaningful glob that matches current repository content.
- Every repository-specific Rule or Note must be supported by source, tests, or established repository guidance that still matches current source.
- Do not infer ownership from directory names alone.
- Do not copy stale paths from existing docs.
- Do not manufacture validation commands.
- Do not manufacture known baseline failures.
- Do not copy terminology, domain language, examples, paths, or product rules from any repository used as a design reference for this skill.

## Existing-instruction rules

When existing agent instructions are present:

- preserve still-valid durable repository guidance
- resolve duplicated or conflicting authority into `AGENTS.md`
- move fine routing detail into the project map when that is its actual purpose
- keep deeper architecture/runbook material as conditional references
- do not silently discard a still-valid repository-specific invariant
- do not preserve stale guidance merely because it was previously documented

## Project-map rules

- Map semantic work intent rather than mirroring the filesystem.
- Require `Use for` and `Start here` for normal mapped areas.
- Allow optional subsections only when useful.
- Allow overlapping areas when repository behavior overlaps.
- Keep detailed Rules and Notes when they prevent a plausible wrong implementation path.
- Do not impose arbitrary map size, domain count, file count, or section length limits.
- Do not thin a mature, correct map into a generic index on refresh.
- Do not turn the map into a generic architecture encyclopedia.

## Context-budget rules

- Keep broad exploration discouraged.
- Keep globally noisy repository material cold by default when present.
- Infer coarse repository hot/cold areas from actual repository boundaries.
- Do not introduce a third context state.

## Validation rules

- Prefer focused validation.
- Use broad validation only when justified by established repository guidance, cross-boundary changes, narrower failure evidence, or explicit user request.
- Preserve known recurring baseline failures only when verified.
- Do not encourage agents to repair unrelated baseline failures.

## Adversarial source review

Before running the Python validator, re-read the generated files and challenge every non-obvious claim.

For each project-map area verify:

1. Do the `Use for` intents reflect real repository behavior?
2. Do all `Start here` paths exist and still provide useful orientation?
3. Are adjacent paths actually adjacent to the mapped responsibility?
4. Are Rules and Notes supported by current source or established guidance?
5. Are validation commands real and appropriately scoped?
6. Is any important current routing knowledge missing because an older map or doc was stale?
7. Is any detail present only because it came from a design reference rather than this repository?

For `AGENTS.md` verify:

1. Is there exactly one operating authority?
2. Is startup deterministic and map-first?
3. Are hot/cold areas repository-specific and current?
4. Is subagent behavior bounded and non-overlapping?
5. Is map maintenance required after meaningful code changes?
6. Is the multi-domain map-steward review present?
7. Is narrow-first validation preserved?
8. Are stop conditions preventing adjacent scope expansion?
9. Did generic engineering doctrine appear without repository evidence?

For compatibility files verify:

1. Do they defer to `AGENTS.md`?
2. Did they accidentally become an independent policy source?
3. Do they point directly to the authority rather than through an instruction chain?

## Refresh review

On repeat invocation:

- preserve verified mature detail
- repair stale details surgically
- re-check every existing `Start here` path
- re-check map Rules and Notes that describe ownership or cross-boundary flow
- re-check coarse hot/cold areas
- re-check validation baseline entries
- update authority files only where current repository reality requires it

## Forbidden output state

Reject and repair the generated context system if:

- placeholders remain
- required context files are missing
- compatibility entrypoints establish competing authority
- a `Start here` path is stale or invented
- source authority is ambiguous
- project-map maintenance behavior is missing
- map-steward review is missing
- subagent routing bypasses the project map
- a new context-management mechanism has been introduced
- repository-specific terminology cannot be traced to the target repository
