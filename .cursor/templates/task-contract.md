# TASK CONTRACT

## Objective

State exactly what is being changed or proven.

## Allowed Scope

List files, directories, modules, or behaviors the task may touch.

## Out of Scope

List nearby areas that must not be changed.

## Known Facts

Only repository-proven or directly observed facts.

## Open Unknowns

Only unknowns that actually block the task.

## Evidence Required

For each blocking unknown:

- exact question
- preferred source
- one decisive observation that would resolve it

## Acceptance Criteria

List concrete conditions for completion.

## Safety Constraints

Examples:

- no network unless explicitly authorized
- no database mutation unless explicitly authorized
- no unrelated refactors
- no dependency changes unless required
- preserve existing public behavior unless the task says otherwise

## Stop Conditions

Stop and report if:

- the requested behavior cannot be defined from available evidence
- a required dependency or source is unavailable
- the task requires out-of-scope changes
- a contradiction invalidates the task assumptions

## Completion Report

At completion, report only:

- files changed
- tests run
- result
- unresolved issues
- whether scope was exceeded
