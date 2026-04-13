# quality rules

Apply these rules before returning and publishing the plan.

## Mandatory rules

- Keep markdown structurally valid.
- Keep headings in title case after the first heading.
- Keep workstreams ordered in execution order.
- Keep tasks concrete, checkable, and repository-aware.
- Keep stories behavior-oriented.
- Keep tests mapped to stories and blast radius.
- Keep changelog entries short and evidence-oriented.
- Keep the repository-published markdown byte-for-byte equivalent to the saved plan artifact.

## Forbidden content

Do not include any of the following in the final plan:

- Questions
- `TODO`
- `TBD`
- `???`
- `Open Questions`
- `Future Investigation`
- `Maybe`
- `Might`
- `Could`
- `Should we`
- `Consider whether`
- `Figure out`
- `FIXME`
- placeholder angle-bracket tokens such as `<feature-name>`

## File pointer rules

- Prefer exact file paths over directory names.
- Prefer exact symbols over broad component descriptions.
- Pair each file pointer with a concrete reason.
- When a new file is planned, locate it under a verified existing directory when possible.
- Name exact test files, commands, and validation surfaces.

## Publication rules

- Publish under `docs/plans/<feature-slug>/` only.
- Use a UTC timestamp in the filename.
- Keep the feature slug in both the filename and the directory.
- Use the commit message `docs(plans): add <feature-slug> implementation plan`.
- Never claim publication succeeded without actually writing the file to the current repository.

## Testing rules

- Do not add tests that only restate implementation details without validating behavior.
- Do not create tiny isolated tests when an existing suite already covers the behavior boundary.
- Do not omit manual verification for behavior that affects workflows, runtime behavior, operations, or integration seams.
- Prefer updating existing suites before creating fragmented new suites.

## Final check

Before returning the markdown file, confirm that:

- every major heading from the template is present
- every workstream has implementation tasks, test tasks, and exit criteria
- every test section names real files, suites, commands, or behaviors
- every change target is tied to a verified file or a justified new file
- the repository publication section names the resolved current repository
- the published path targets `docs/plans/`
