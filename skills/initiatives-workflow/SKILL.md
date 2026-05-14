---
name: initiatives-workflow
description: "Use for full wave execution or durable wave/backlog state: delivery-map structure, packet schema, backlog entries, and closeout cleanup."
---

# Initiatives Workflow

Owns durable wave, packet, delivery-map, and backlog state. It stores decisions;
other skills own design, readiness, review, delegation, proof, and runtime
doctrine.

Use a wave only when state must survive queue tracking, handoff, interruption,
resume, review, or multiple execution slices.

## Reference

Read `references/wave-packet-contract.md` when creating or validating a packet.

## State

- map: `docs-ai/current-work/delivery-map.md`
- brief: `docs-ai/docs/initiatives/waves/<wave-id>.md` when queue-visible
  status is needed
- packet: `docs-ai/current-work/<wave-id>/wave-execution.md`
- draft packet: `docs-ai/current-work/<wave-id>/wave-execution.draft.md`
- backlog: `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md`

Statuses: `discovery-required`, `execution-ready`, `done`, `retired`.

Only `execution-ready` waves execute from canonical packets. Draft packets
preserve planning state only.

## Execute

Before execution:

- packet satisfies the packet contract
- objective, design integrity, execution slices, and readiness claim are closed
- `planning_critic` and `quality_guard` approved non-trivial planning

During execution:

- execute slices in dependency order
- update blockers, decisions, evidence, and follow-up in the packet
- use `quality_guard` after each non-trivial implementation chunk

Stop on objective drift, stale packet state, missing design/readiness state,
discovery leakage, or current-scope owner defects not fixed/routed/accepted.

## Closeout

Close only after verification, final review, and `readiness-claim` support the
final claim.

Extract retained value to the owning durable surface or valid backlog. Then
remove delivery-map state, packet state, and disposable briefs.

## Assets

- discovery brief: `assets/wave-brief-discovery-required.md`
- execution-ready brief: `assets/wave-brief-execution-ready.md`
- packet: `assets/wave-execution.md`
- backlog item: `assets/backlog-entry.md`
