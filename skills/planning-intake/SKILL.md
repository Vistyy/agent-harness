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
- non-trivial plans name the touched owner/component and its integrity posture
- implementation handoff leaves no materially divergent plausible paths

## Constraints

- Be critical about scope, root cause, and proof.
- Apply the `code-simplicity` gate; delete, collapse, or leave manual work
  manual unless a real constraint forces more.
- Default bounded local mechanics yourself.
- Persist important deferrals in repo state, not chat.

## Required Behavior

1. No silent material assumptions.
2. Blocking user questions are only for `user-owned decisions`.
3. Every blocking question includes recommendation and short reason.
4. `agent-defaultable decisions` are decided locally.
5. Push back on weak scope or transitional architecture.
6. Run omission-class sweep before promotion.
7. Run touched owner/component integrity check for non-trivial work.
8. Important deferred work becomes durable wave/backlog/mobile-parity state in same session.
9. Discovery work does not leak into execution.

## Reference Loading

Load `references/intake-contract.md` when you need the detailed decision
taxonomy, omission sweeps, proof allocation fields, blocking-question format, or
anti-misdirection check. Do not load it for already-closed tiny/local work.

## Continue Until

Continue intake until all five gate conditions are satisfied:

1. `scope closed`
2. `decisions closed`
3. `proof allocated`
4. `deferrals persisted`
5. `touched-component integrity assessed`

If any fail, keep questioning or reshape the work.

## Stop Conditions

Do not promote to `execution-ready` while:
- any material implementation-shaping question remains open
- touched-component integrity is `not assessed` for non-trivial work
- unacceptable touched-component integrity lacks explicit accepted debt and a
  backlog link
- a substantive user ask was omitted, narrowed, or deferred without record
- the packet still contains discovery instead of implementation work
- two competent implementers could still choose materially different owner,
  proof, state-authority, runtime, compatibility, migration, or public behavior
- the plan is memory-only for non-trivial work

Non-trivial planning needs `planning_critic` before planning-gate
`quality_guard`. The critic is pressure, not approval. Record critic
provenance before requesting `quality_guard`.

## Direct Inputs

- apply the `code-simplicity` gate while shaping non-trivial planning
- plans name the smallest owner/component whose contract, state, lifecycle,
  design, workflow, or proof is touched; expand only to required shared
  authority
- accepted touched-component debt requires a concrete blocker presentation,
  explicit user acceptance, and backlog state before approval
- close structural ownership and boundary choices before promotion
- structural slices need explicit `System-Boundary Architecture Disposition`
- use `../initiatives-workflow/references/initiatives-workflow.md` for wave
  lifecycle states
- use `../initiatives-workflow/references/wave-packet-contract.md` for packet
  schema

## Output Shape

1. `docs-ai/current-work/delivery-map.md`
2. `docs-ai/docs/initiatives/waves/<wave-id>.md`
3. `docs-ai/current-work/<wave-id>/wave-execution.draft.md` when planning gate needs packet-shaped review
4. `docs-ai/current-work/<wave-id>/wave-execution.md` only after promotion
5. `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md` when deferral needs backlog state
6. `docs-ai/docs/roadmap.md` only when initiative/feature status changes materially
