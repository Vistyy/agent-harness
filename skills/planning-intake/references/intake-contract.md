# Planning Intake Contract

Load this reference when planning has unresolved scope, decision ownership,
proof allocation, deferral, or blocking-question shape.

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
- touched owner/component integrity

Record how substantive user asks are handled, what can be deleted or collapsed,
the smallest owner/component whose contract, state, lifecycle, design,
workflow, or proof is touched, and why any remaining complexity is necessary.

## Proof Allocation

Execution-ready planning must record in the wave brief or packet:
- proof class using
  `../../verification-before-completion/references/runtime-proof-escalation.md`
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
`../../initiatives-workflow/references/wave-packet-contract.md`.

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

## Anti-Misdirection Check

Before promotion, ask whether the plan treats a symptom as root cause, misses a
smaller fix, preserves old behavior through a surviving path, or moves
complexity instead of removing it.

If that exposes a `user-owned decision`, ask one blocking question. If a durable
owner doc already closes the better shape, decide locally and persist the
reshape.

For each substantive user ask, record whether planning keeps it, shrinks it,
rewrites the approach, or defers it.

## Touched Owner Integrity

For non-trivial work, planning must record:
- touched owner/component
- highest expected scope to inspect
- touched-component integrity: `acceptable`, `unacceptable`, or `not assessed`
- must-block `code-simplicity` signals, or `none`
- accepted-debt backlog link, or `none`

Select the smallest owner/component whose contract, state, lifecycle, design,
workflow, or proof the change touches. Expand only to shared authority required
by the change.

`not assessed` cannot promote to execution-ready. Unacceptable integrity cannot
promote unless the user explicitly accepted the presented blocker and a backlog
item with owner, risk, and removal condition is linked.
