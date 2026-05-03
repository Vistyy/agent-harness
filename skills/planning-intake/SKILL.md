---
name: planning-intake
description: "Use to turn vague work into a wave plan or harden an existing wave to execution-ready status by closing scope, decisions, proof allocation, and deferrals."
---

# Planning Intake

Owns closing scope, owner, design, runtime, migration, proof, and wave-shaping
decisions before implementation.

Durable planning produces wave state. Direct in-thread briefs are owned by
`../work-routing/SKILL.md`.

## Outcome

Planning is ready only when durable wave state lets an implementer complete the
binding objective without discovery or material design discretion.

Binding objective = original user objective plus explicitly accepted reductions.
Plans, packets, proof, and handoffs preserve it.

`../work-routing/SKILL.md` owns broad-objective routing and full-work
semantics. Planning preserves the original objective when routing selects an
execution owner/problem, and promotion is blocked while that routing decision
is unresolved.

Do not promote shallow breadth plans that touch many areas lightly to simulate
coverage.

## Gate

Close or stop on:
1. scope and non-goals
2. material decisions
3. touched owner/component integrity
4. proof allocation
5. deferrals

Deferrals are valid only when unrelated to the current objective or explicitly
accepted temporary debt with owner, risk, and removal condition.

## Decisions

Close decisions locally when the harness/project owner already gives a clear
default. Ask the user only for user-owned choices such as product intent,
priority, irreversible tradeoff, credential/tenant access, or acceptance of
temporary debt.

Every blocking question includes a recommendation and the reason.

## Touched Owner

Touched owner/component is the smallest owner whose contract, state, lifecycle,
design, workflow, or proof the change touches. Expand only to shared authority
required by the objective.

Assess whether the owner is coherent enough to complete the objective. If it is
not, fix the owner now or stop for explicit accepted debt.

## Omission Sweep

Check that the plan did not drop:
- original objective, breadth, quality bar, or runtime behavior
- public surfaces and entrypoints
- owner/state authority and migrations
- proof for each claimed surface
- cleanup of obsolete paths in touched scope
- valid deferrals and their durable home

## Proof Allocation

For every material claim, name owner layer, exact proof command or artifact,
expected evidence, and counterfactual regression probe.

Use initiatives workflow references only when shaping wave state or packet
schema.

## Stop Conditions

Do not promote while:
- a material implementation-shaping decision remains open
- the plan narrows requested breadth or quality without accepted reduction
- a broad objective is spread shallowly across multiple owners instead of
  following `work-routing` broad-objective semantics
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
