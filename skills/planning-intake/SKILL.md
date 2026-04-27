---
name: planning-intake
description: "Use to turn vague work into a wave plan or harden an existing wave to execution-ready status by closing scope, decisions, proof allocation, and deferrals."
---

# Planning Intake

Discovery plus intake before wave execution.

Goal: close material decisions before execution starts.

## Outcome

Produce execution-ready wave planning only when scope, decisions, proof, and
deferrals are closed enough that implementation does not need discovery or
material design choices.

## Success Criteria

- user objective coverage is explicit
- material decisions are closed or routed to the user with a recommendation
- proof is allocated by owner layer, exact evidence, and counterfactual
- deferrals are persisted in repo state, not chat
- implementation handoff leaves no materially divergent plausible paths

## Constraints

- Be critical about scope, root cause, and proof.
- Start from the simplest honest solution; delete, collapse, or leave manual
  work manual unless a real constraint forces more.
- Default bounded local mechanics yourself.
- Persist important deferrals in repo state, not chat.

## Required Behavior

1. No silent material assumptions.
2. Blocking user questions are only for `user-owned decisions`.
3. Every blocking question includes recommendation and short reason.
4. `agent-defaultable decisions` are decided locally.
5. Push back on weak scope or transitional architecture.
6. Run omission-class sweep before promotion.
7. Important deferred work becomes durable wave/backlog/mobile-parity state in same session.
8. Discovery work does not leak into execution.

## Decision Taxonomy

User owns choices that set direction, visible semantics, taste, IA,
compatibility/rollout, vendor/platform/data-model/infrastructure direction,
release priority, or long-lived public/cross-owner contract.

Ask only when the unresolved choice materially changes product meaning,
strategy, reversibility, external promises, claim strength, runtime cost, or
delivery timing and no durable owner doc already closes the answer.

Agent defaults local execution mechanics: naming, placement, helper splitting,
bounded decomposition, packet wording, test-module layout, and scope reshaping
that keeps one wave coherent without changing user-owned commitments.

If deferred, persist adjacent interaction completeness, worthwhile cleanup,
migration/compatibility/operational follow-up, and stronger verification
follow-up.

## Mandatory Sweeps

Before promotion, check:
- user objective coverage
- security/trust boundaries
- failure and edge states
- migration, compatibility, and rollout
- interaction completeness
- worthwhile hotspot cleanup
- operational, observability, and idempotency posture
- proof ownership/allocation
- simplicity and necessity

Record how substantive user asks are handled, what can be deleted or collapsed,
and why any remaining complexity is necessary.

## Proof Allocation

Execution-ready planning must record in the wave brief or packet:
- proof class using
  `../verification-before-completion/references/runtime-proof-escalation.md`
  when runtime proof may matter
- owner layer
- success condition
- exact command/artifact or `not-required`
- one weaker implementation the proof must reject
- for typed-boundary or contract-tightening claims, each materially equivalent
  legacy path the proof must reject

Shape work around outcomes and proof, not command lists. A plan or task card
states the success condition, the proof that rejects a weaker implementation,
and then the expected command or artifact.

Packet proof-row schema is owned by
`../initiatives-workflow/references/wave-packet-contract.md`.

## Blocking Question Format

Use only for `user-owned decisions`.

```md
**Question:** <single decision question>

**Recommended:** Option A - <short reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |
| C | ... |

Reply with A/B/C, or say "yes" to accept recommendation.
```

## Continue Until

Continue intake until all four gate conditions are satisfied:

1. `scope closed`
2. `decisions closed`
3. `proof allocated`
4. `deferrals persisted`

If any fail, keep questioning or reshape the work.

## Stop Conditions

Do not promote to `execution-ready` while:
- any material implementation-shaping question remains open
- a substantive user ask was omitted, narrowed, or deferred without record
- the packet still contains discovery instead of implementation work
- two competent implementers could still choose materially different owner,
  proof, state-authority, runtime, compatibility, migration, or public behavior
- the plan is memory-only for non-trivial work

Non-trivial planning needs `planning_critic` before planning-gate
`quality_guard`. The critic is pressure, not approval. Record critic
provenance before requesting `quality_guard`.

## Doctrine Routing

- apply `../code-simplicity/SKILL.md` as the default shaping lens for
  non-trivial planning
- if work changes boundaries or ownership, load
  `../system-boundary-architecture/SKILL.md`
- structural slices need explicit `System-Boundary Architecture Disposition`
- workflow lifecycle is owned by
  `../initiatives-workflow/references/initiatives-workflow.md`
- packet schema is owned by
  `../initiatives-workflow/references/wave-packet-contract.md`
- delegation policy is owned by `../subagent-orchestration/SKILL.md`

## Anti-Misdirection Check

Before promotion, ask whether the plan treats a symptom as root cause, misses a
smaller fix, preserves old behavior through a surviving path, or moves
complexity instead of removing it.

If that exposes a `user-owned decision`, ask one blocking question. If a durable
owner doc already closes the better shape, decide locally and persist the
reshape.

For each substantive user ask, record whether planning keeps it, shrinks it,
rewrites the approach, or defers it.

## Output Shape

1. `docs-ai/current-work/delivery-map.md`
2. `docs-ai/docs/initiatives/waves/<wave-id>.md`
3. `docs-ai/current-work/<wave-id>/wave-execution.draft.md` when planning gate needs packet-shaped review
4. `docs-ai/current-work/<wave-id>/wave-execution.md` only after promotion
5. `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md` when deferral needs backlog state
6. `docs-ai/docs/roadmap.md` only when initiative/feature status changes materially
