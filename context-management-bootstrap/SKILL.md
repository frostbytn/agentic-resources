---
name: context-management-bootstrap
description: bootstrap or refresh repository-local agent context management for the currently opened repository. use when a repository needs coherent agent operating instructions, deterministic startup routing, hot/cold context boundaries, a semantic project map, project-map maintenance rules, bounded subagent behavior, validation guidance, and thin vendor compatibility entrypoints derived from verified repository source, tests, docs, and existing agent instructions.
---

# Context Management Bootstrap

Bootstrap or refresh the repository-local context system used by coding agents. Infer repository-specific content from the current repository, install one authoritative operating-instruction source, install a semantic project map, and wire supported agent entrypoints to that authority.

This skill reproduces a fixed context-management operating model. Adapt repository content to the target repository, but do not invent new context-management mechanisms.

## Core Contract

- Operate on the currently opened repository.
- Treat source files and tests as authoritative for current behavior.
- Treat existing repository documentation and agent instructions as evidence that must be checked against current source before reuse.
- Generate or refresh one authoritative root `AGENTS.md`.
- Generate or refresh `docs/agent-context/project-map.md` as the repository routing index.
- Generate or refresh a thin root `CLAUDE.md` that defers to `AGENTS.md` rather than establishing independent policy.
- If a root `CODEX.md` already exists, normalize it into a thin compatibility pointer to `AGENTS.md`; do not create it solely for this skill.
- Create `docs/agent-context/known-validation-failures.md` only when verified recurring validation baseline knowledge exists or that file already exists with still-relevant baseline knowledge.
- Re-running the skill must refresh the existing context system against current repository reality. Preserve still-valid detail; repair stale routing, paths, rules, context boundaries, and validation guidance.
- Never require an implementation-planning, task-notes, or other task-artifact system for this context system to function.
- Never copy terminology, domain names, file paths, product rules, or examples from any repository used to derive this skill. Generated repository content must come from the target repository.

## Required Resources

Load all of these references before writing repository files:

- `references/operating-model.md`
- `references/repository-analysis.md`
- `references/agent-instructions-contract.md`
- `references/project-map-contract.md`
- `references/quality-rules.md`

Run `scripts/validate_context_bootstrap.py <repository-root>` before completing the bootstrap or refresh.

## Execution Workflow

### 1. Resolve Repository Identity And Existing Context

Resolve and verify:

- repository root
- current repository structure
- root package/workspace/project manifests
- existing `AGENTS.md`
- existing `CLAUDE.md`
- existing `CODEX.md` when present
- existing agent-facing instruction files and repository guidance
- existing `docs/agent-context/` files
- existing project maps, architecture references, runbooks, contribution guides, and validation documentation

If the context system already exists, treat its contents as a routing hypothesis to verify, not as implementation truth.

### 2. Inspect The Repository

Follow `references/repository-analysis.md`.

Build an evidence-backed model of:

- major repository/workspace boundaries
- semantic work areas and capabilities
- authoritative components and important responsibility boundaries
- high-information source entrypoints
- directly adjacent files or packages that commonly participate in the same change
- established extension paths and cross-boundary flows
- repository-specific invariants that prevent incorrect change paths
- validation commands and test surfaces
- context that should remain cold by default
- existing documentation that should be consulted only for specific domains
- recurring validation failures or baseline caveats, when verified

Do not infer architecture from directory names alone. Verify important claims in source and tests.

### 3. Normalize Existing Agent Instructions

Use `references/agent-instructions-contract.md`.

When existing agent instructions contain still-valid repository-specific guidance:

- preserve durable operating rules in `AGENTS.md`
- move routing-specific detail into the project map when that is its actual purpose
- keep deeper architecture or runbook material as conditional references rather than duplicating it
- remove duplicated or conflicting authority only after verifying which guidance matches current source
- keep vendor-specific entrypoints subordinate to `AGENTS.md`

Do not add generic software-engineering doctrine merely because it sounds useful. Repository-specific rules must be supported by the target repository or its established guidance.

### 4. Generate Or Refresh `AGENTS.md`

Render the authoritative operating instructions using the exact behavior defined by `references/agent-instructions-contract.md`.

The file must include:

- a clear authority statement
- default scoped behavior
- deterministic startup context order
- global context-budget and cold-by-default rules
- bounded subagent policy and spawn guidance
- repository-specific coarse hot/cold areas
- project-map maintenance triggers
- the multi-domain map-steward review
- narrow-first validation behavior
- instruction-maintenance rules
- stop conditions

Keep routing detail in the project map rather than duplicating it into `AGENTS.md`.

### 5. Generate Or Refresh The Project Map

Render `docs/agent-context/project-map.md` using `references/project-map-contract.md`.

Map the repository by semantic work area, not by filesystem inventory.

For each mapped area:

- describe the work intents it is used for
- identify verified source locations where an agent should start
- include adjacent locations only when they are commonly needed to cross a real boundary
- include validation or tests when they materially guide work in that area
- include Rules or Notes when verified repository-specific invariants, ownership, established flows, or known wrong paths materially change how future agents should work
- include references or avoid-by-default context only when useful

Do not force optional subsections into every area. Do not force areas to be mutually exclusive. A source path may legitimately appear in more than one semantic area.

### 6. Handle Validation Baseline Memory

If verified recurring broad-validation failures or stable baseline caveats exist, generate or refresh:

- `docs/agent-context/known-validation-failures.md`

For each recorded validation surface include:

- command
- current expectation
- verified recurring examples when available
- required agent behavior

Include update rules explaining when the baseline file itself changes.

If no such baseline knowledge is verified and the file does not already contain still-valid knowledge, do not create an empty baseline artifact.

### 7. Wire Compatibility Entrypoints

Generate or refresh root `CLAUDE.md` as a thin pointer to `AGENTS.md`.

It must:

- identify `AGENTS.md` as the authoritative repository operating instructions
- direct the agent to the project map through the canonical instructions
- avoid creating a second independent instruction source

If root `CODEX.md` already exists, apply the same compatibility-pointer behavior.

Do not create chains of agent instruction files that point through one another before reaching the authority.

### 8. Reflect Against Source

Before validation, perform the evidence review defined in `references/quality-rules.md`.

Re-read the generated files and attempt to falsify their non-obvious claims against current source, tests, and established repository guidance.

Repair:

- stale paths
- unsupported ownership or authority claims
- incorrect hot/cold classifications
- overbroad or missing semantic routing
- invalid validation commands
- duplicated authority
- rules or notes that are not backed by the repository
- missing routing-critical invariants that are clearly established in the repository

This reflection is generation quality assurance. Do not use it to introduce new context-management mechanisms.

### 9. Validate Deterministically

Run:

```bash
python scripts/validate_context_bootstrap.py <repository-root>
```

If validation fails:

- fix every reported issue
- run the validator again
- do not complete until it passes

### 10. Report The Bootstrap

Return a concise report containing:

- whether the run was an initial bootstrap or refresh
- files created
- files updated
- project-map location
- whether validation-baseline memory was created, refreshed, preserved, or not needed
- validator result

Do not dump the full generated context files into chat when repository file writing is available.

## Evidence Rules

- Verify every `Start here` path in the project map against the current repository.
- Verify every repository-specific Rule or Note against source, tests, or established repository guidance.
- Prefer source and tests when documentation and current behavior disagree.
- Preserve existing high-value detail when it remains correct.
- Remove stale routing rather than carrying it forward for historical completeness.
- Route to deep documentation only when a mapped work area actually needs it.
- Do not manufacture repository architecture, validation behavior, or ownership semantics.

## Refresh Rules

On repeat invocation:

- read the current context files first
- verify their paths and claims against the current repository
- preserve still-valid semantic areas and detailed invariants
- add newly established important areas or entrypoints
- remove or repair stale paths, ownership, flows, and validation guidance
- re-evaluate coarse hot/cold repository areas
- re-evaluate known validation baseline knowledge
- keep the same authority hierarchy and maintenance behavior
- validate the entire refreshed context system

Do not blindly regenerate the context system from a generic template.
