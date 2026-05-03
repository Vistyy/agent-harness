---
name: planning-intake
description: "Use to turn vague work into a wave plan or harden an existing wave to execution-ready status by closing scope, decisions, proof allocation, and deferrals."
---

# Planning Intake

Use when implementation would otherwise begin with open scope, owner, design,
runtime, migration, proof, or wave-shaping decisions.

Non-trivial durable work becomes a wave, even when it is only one task. There
is no separate standalone-plan path.

## Outcome

Planning is ready only when durable wave state lets an implementer complete the
binding objective without discovery or material design discretion.

Binding objective = original user objective plus explicitly accepted reductions.
Plans, packets, proof, and handoffs preserve it.

## Gate

Close or stop on:
1. scope and non-goals
2. material decisions
3. touched owner/component integrity
4. proof allocation
5. deferrals

Deferrals are valid only when unrelated to the current objective or explicitly
accepted temporary debt with owner, risk, and removal condition.

## Required Reference

Read `references/intake-contract.md` for non-trivial planning, omission sweeps,
proof allocation, or blocking questions. Use initiatives workflow references
only when shaping wave state or packet schema.

## Stop Conditions

Do not promote while:
- a material implementation-shaping decision remains open
- the plan narrows requested breadth or quality without accepted reduction
- touched-component integrity is `not assessed`
- unacceptable touched-component integrity lacks accepted debt and backlog link
- discovery work leaks into execution
- two competent implementers could choose materially different owners, proof,
  state authority, runtime, migration, compatibility, or public behavior

Non-trivial planning needs `planning_critic` before execution readiness and
`quality_guard` before promotion.

## Outputs

- `docs-ai/current-work/delivery-map.md`
- `docs-ai/docs/initiatives/waves/<wave-id>.md`
- `docs-ai/current-work/<wave-id>/wave-execution.draft.md` for review
- `docs-ai/current-work/<wave-id>/wave-execution.md` only after promotion
- `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md` for valid
  deferrals
