# architecture principles

Apply these principles when analyzing the codebase and structuring the implementation plan.

## Phased architecture analysis

Complete the following phases in order before drafting any workstream or implementation task.

### Phase 1: Read existing architectural documentation

Before creating the plan, search for and read all architectural and code-structure documentation in the repository.

Look for:

- `ARCHITECTURE.md`, `DESIGN.md`, `CONTRIBUTING.md`, `DEVELOPMENT.md`, or equivalents at the repository root or under `docs/`
- inline architecture decision records under `docs/adr/`, `docs/decisions/`, `docs/architecture/`, or similar directories
- README files in top-level packages, modules, or service directories that describe structure or conventions
- code style guides, linting configurations, and formatter configurations that encode structural preferences
- dependency injection registrations, module bootstrapping files, or composition roots that reveal wiring conventions
- any `.instructions.md`, `.copilot-instructions.md`, or similar agent guidance files that encode project conventions

When architectural documentation exists, treat it as authoritative. Follow the conventions, patterns, layering, naming, and structural rules it defines throughout every workstream in the plan.

### Phase 2: Decompose the codebase into architectural components

When documentation is absent or incomplete, inspect the codebase directly to extract its structural patterns.

Identify and document:

- **Layering and module boundaries** — how the codebase separates concerns (e.g., controllers / services / repositories, handlers / domain / persistence, routes / middleware / models)
- **Cross-cutting patterns** — how the codebase handles authentication, authorization, HTTP clients, logging, error handling, configuration access, caching, retries, and observability
- **Shared abstractions and utilities** — base classes, shared libraries, helper modules, common middleware, reusable hooks, or shared UI primitives that multiple features depend on
- **Data flow and contract patterns** — how data enters the system, transforms, persists, and exits; which serialization, validation, and mapping patterns are standard
- **Test organization** — how tests are structured, where fixtures live, which test runners and assertion libraries are used, and how test utilities are shared

For each pattern identified, capture:

- the exact files and symbols that implement the pattern
- whether the pattern is consistently applied or has known deviations
- how the planned feature must interact with or extend the pattern

**Critical rule:** When the codebase already handles a concern in a standard way, the plan must reuse that existing approach. Do not introduce new patterns, libraries, wrappers, or abstractions for concerns the codebase already solves. Code reuse is mandatory when an existing path exists.

### Phase 3: Apply default architecture principles

When the codebase lacks both documentation and clear structural conventions, or when the plan introduces a genuinely new concern with no existing pattern to follow, apply these default principles:

#### Readability and maintainability first

- Structure code for clarity over cleverness. Prefer explicit, readable implementations over compact or technically impressive alternatives.
- Name files, modules, functions, types, and variables to communicate intent without requiring additional context.
- Keep functions and methods focused on a single responsibility with a clear input-output contract.

#### Idempotent execution

- Design operations to produce the same result when executed multiple times.
- Expect that executing logic may retry, re-run, or re-enter any code path. State mutations must be safe to repeat.
- Guard creation and mutation operations with existence checks, upsert semantics, or idempotency keys as appropriate to the domain.

#### DRY, SOLID, and abstraction discipline

- Do not duplicate logic. Extract shared behavior into well-named, well-located abstractions.
- Follow single-responsibility, open-closed, Liskov substitution, interface segregation, and dependency inversion principles where the language and framework support them.
- Prefer composition over inheritance. Prefer small, focused interfaces over broad ones.
- Locate abstractions where they are discoverable — near their consumers or in a shared module that the codebase already uses for that purpose.

#### Composable primitives design

- When a feature requires a generalized concept (e.g., a retry mechanism, a permission check, a data transformer, a validation pipeline), build that concept as a standalone, reusable primitive first.
- Layer the feature-specific behavior on top of the composable primitive.
- Do not embed generalized logic directly inside feature-specific code paths.
- Do not proliferate small, single-use code paths that technically satisfy the feature but prevent reuse.
- Ask: "If another feature needed this same capability tomorrow, would it be able to import and use what we built?" If the answer is no, restructure.

## How to apply in the plan

- In the **Verified system context** section, document the architectural patterns, cross-cutting conventions, and shared abstractions discovered during analysis.
- In each **Workstream**, explicitly state which existing patterns, abstractions, or utilities the implementation must reuse.
- In each **Workstream**, explicitly call out when a new composable primitive must be created before feature-specific work begins. Sequence the primitive creation task before the tasks that depend on it.
- In the **Guardrails** section, list the architectural invariants that must not be violated (e.g., "all HTTP calls must go through the existing `HttpClient` wrapper", "all auth checks must use the existing middleware pipeline").
- In the **Exit criteria** for each workstream, include a check that the implementation follows the established or documented patterns and does not introduce redundant abstractions.
