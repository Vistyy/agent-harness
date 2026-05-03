---
name: initiatives-workflow
description: "Use for full wave execution or durable wave/backlog state: delivery-map structure, packet schema, backlog entries, and closeout cleanup."
---

# Initiatives Workflow

Owns durable wave, packet, delivery-map, backlog state, and full wave
execution. It does not own planning, review, delegation, or verification
doctrine.

A wave may be one task. It is the single durable execution artifact for
non-trivial work.

## References

- Read `references/wave-packet-contract.md` when packet, task-card, proof-row,
  or execution-state schema matters.

## Owned Work

- backlog to wave promotion
- delivery-map updates
- wave brief and packet maintenance
- backlog/mobile-parity follow-up state
- wave closeout cleanup
- full execution of one `execution-ready` wave

## State Rules

- map: `docs-ai/current-work/delivery-map.md`
- brief: `docs-ai/docs/initiatives/waves/<wave-id>.md`
- draft packet: `docs-ai/current-work/<wave-id>/wave-execution.draft.md`
- canonical packet: `docs-ai/current-work/<wave-id>/wave-execution.md`
- backlog: `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md`
- `discovery-required` waves may have `wave-execution.draft.md`.
- Only `execution-ready` waves keep canonical `wave-execution.md`.
- Closeout removes delivery-map state and packet only after final review and
  verification approve the binding objective.
- Backlog entries are for valid deferrals only: unrelated nearby debt or
  explicitly accepted temporary debt with owner, risk, and removal condition.

Statuses:
- `discovery-required`: decisions still open; no canonical packet.
- `execution-ready`: planning gate approved; canonical packet exists.
- `done`: verified and final-reviewed; current-work packet can be cleaned.
- `retired`: intentionally closed without execution.

## Execute A Wave

Before execution:
- wave brief status is `execution-ready`
- canonical `wave-execution.md` exists
- packet satisfies the wave packet contract
- durable brief and packet preserve original objective plus accepted reductions
- planning gate records real `planning_critic` and `quality_guard` approval

During execution:
- execute task cards in dependency order
- use `subagent-orchestration` for implementer handoffs when useful
- pass original objective, accepted reductions, residual gaps, exact task,
  proof rows, risks, and stop triggers in every handoff
- stop on discovery leakage, objective mismatch, owner defect outside accepted
  debt, or materially stale packet assumptions
- run required proof and `quality_guard` after meaningful chunks

Before closeout:
- run wave-level verification and final isolated review
- ensure final claim does not exceed proof, runtime fidelity, or accepted scope
- update delivery map, brief, packet, backlog, and roadmap state consistently
- remove packet state only after closeout is actually approved

## Assets

- discovery brief: `assets/wave-brief-discovery-required.md`
- execution-ready brief: `assets/wave-brief-execution-ready.md`
- packet: `assets/wave-execution.md`
- backlog item: `assets/backlog-entry.md`

## CLI

```bash
agent-harness wave bootstrap --repo-root <project-root> --wave <wave-id> --title "<title>"
agent-harness wave refs --repo-root <project-root> --wave <wave-id>
agent-harness wave cleanup --repo-root <project-root> --wave <wave-id>
```
