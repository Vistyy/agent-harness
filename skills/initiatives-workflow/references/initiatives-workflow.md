# Initiatives Workflow

Owns reusable wave and backlog state. A wave may be one task and is the single
durable execution artifact for non-trivial work.

## State Files

- map: `docs-ai/current-work/delivery-map.md`
- brief: `docs-ai/docs/initiatives/waves/<wave-id>.md`
- draft packet: `docs-ai/current-work/<wave-id>/wave-execution.draft.md`
- canonical packet: `docs-ai/current-work/<wave-id>/wave-execution.md`
- backlog: `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md`

## Statuses

- `discovery-required`: decisions still open; no canonical packet.
- `execution-ready`: planning gate approved; canonical packet exists.
- `done`: verified and final-reviewed; current-work packet can be cleaned.
- `retired`: intentionally closed without execution.

## Lifecycle

1. Create or update the brief and delivery-map entry.
2. Use `planning-intake` to close scope, decisions, proof, and deferrals.
3. Use a draft packet only when packet-shaped review is needed.
4. Promote to `execution-ready` only after `planning_critic` and
   `quality_guard` approve execution readiness.
5. Execute via `initiatives-workflow`.
6. Close only after fresh verification and final isolated review approve the
   binding objective.
7. Remove map state and packet state only after closeout is true.

## Deferrals

Backlog is not a place to hide current-objective work. Add backlog only for:
- unrelated nearby debt
- explicitly accepted temporary debt with owner, risk, and removal condition
- follow-up outside the approved completion claim

When queue, packet, and backlog state all move, update them in the same change.
