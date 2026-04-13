# repository contract

Use this file for the currently opened repository.

## Repository identity

- Resolve the repository root from the active workspace or git metadata.
- Resolve the repository name from git remote metadata when available.
- If git remote metadata is unavailable, use the workspace repository label or folder name.
- Resolve the current branch name when available.
- Do not assume a specific repository, owner, or branch.

## Required publication pattern

Publish the final validated plan to:

- `docs/plans/<feature-slug>/<utc-timestamp>-<feature-slug>-implementation-plan.md`

Use this commit message format:

- `docs(plans): add <feature-slug> implementation plan`

## Verified notes convention

Use this collaboration-notes convention unless a stronger verified repository convention already exists:

- `docs/implementation-notes/<feature-slug>/README.md`
- `docs/implementation-notes/<feature-slug>/decision-log.md`
- `docs/implementation-notes/<feature-slug>/test-notes.md`
- `docs/implementation-notes/<feature-slug>/handoff-summary.md`

Prefer that pattern when the feature is large enough to justify cross-agent coordination.

## Planning behavior inside the current repository

- Prefer verified file paths inside existing top-level packages before planning new top-level directories.
- Keep UI, backend, persistence, deployment, configuration, observability, and docs workstreams separated unless the feature genuinely spans them.
- Name commands explicitly inside the testing strategy when the repository exposes them.
- Keep docs publication separate from implementation notes.
- Do not treat this reference as a substitute for repository inspection. Verify exact files and symbols during each run.
