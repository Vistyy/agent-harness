# Migration Guardrails Lifecycle

Define which checks are durable quality gates versus temporary migration
guardrails.

## Classification

Use these categories:

- **Durable behavior checks**: verify user-visible, API-visible, or stable
  operator contracts such as auth behavior, response shape, data integrity, and
  business rules.
- **Temporary migration guardrails**: enforce transitional structure during
  refactors, such as exact route ownership, exact file or module location,
  forbidden path globs, and static allowlists tied to one migration.

If a check mainly asserts where code, routes, or modules live rather than what
the system does, classify it as a temporary migration guardrail.

## Policy

- Temporary migration guardrails are allowed only while a migration is active.
- Temporary migration guardrails must not be required in persistent project
  quality gates.
- Temporary migration guardrails must not be part of canonical runtime smoke
  commands.
- Durable behavior checks remain in persistent quality and smoke gates.

## Placement

- Durable checks: keep under normal service or application test and smoke
  locations.
- Temporary migration guardrails: keep in active execution state with explicit
  run instructions in the governing artifact.

## Exit Criteria

Every temporary migration guardrail must include:

- owner work item,
- reason for existence,
- removal trigger,
- planned removal step.

Before marking a migration task or wave done, remove or archive temporary
migration guardrails.

## Examples

Temporary migration guardrails:

- exact endpoint ownership matrices while a split is in flight,
- API allowlist boundary scripts tied to one edge-routing snapshot,
- tests that scan for forbidden module or file paths only to enforce a
  transitional package split.

Durable checks:

- session minting works,
- protected routes reject missing or invalid credentials,
- query endpoints return valid contract payloads for authorized requests,
- mutation endpoints preserve auth and outcome behavior.
