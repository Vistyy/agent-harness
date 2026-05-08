---
name: planning-intake
description: "Use to turn vague work into a wave plan or harden an existing wave to execution-ready status by closing scope, decisions, proof allocation, and debt disposition."
---

# Planning Intake

Owns closing scope, owner, design, runtime, migration, proof, and wave-shaping
decisions before implementation.

Durable planning produces wave state. Non-trivial planning state must be
file-backed through `initiatives-workflow`.

## Outcome

Planning is ready only when durable wave state preserves the binding objective
and lets execution proceed without discovery or material design discretion.

Binding objective = original user objective plus explicitly accepted reductions.
Plans, packets, proof, and handoffs preserve it.

`../work-routing/SKILL.md` owns route selection and broad-objective semantics.
Do not promote shallow breadth plans that simulate coverage.

## Gate

Close or stop on owner-skill intake, scope, material decisions, adequacy,
touched owner/component integrity, proof allocation, and debt disposition.

For non-trivial work, durable planning must record the route, project
overlay/docs read, owner skills read, matched reference gates read, skipped
references with reason, and open owner gaps. `code-simplicity` is required.

Current-scope blockers are fixed or routed, not deferred. Discovered separate
debt uses `initiatives-workflow`; accepted temporary debt is user-owned and
requires owner, risk, removal condition, and backlog link.

## Decisions

Close decisions locally when the harness/project owner already gives a clear
default. Ask the user only for user-owned choices such as product intent,
priority, irreversible tradeoff, credential/tenant access, or acceptance of
temporary debt.

Blocking questions include a recommendation and reason.

## Touched Owner

Touched owner/component is the smallest owner whose contract, state, lifecycle,
design, workflow, or proof the change touches. Expand only to shared authority
required by the objective.

Assess whether the owner is coherent enough to complete the objective. Record
the before-implementation adequacy verdict. If the owner or selected scope is
inadequate, fix the owner now, reshape the plan, or stop for explicit accepted
debt.

## Omission Sweep

Check that the plan did not drop:
- original objective, breadth, quality bar, or runtime behavior
- public surfaces and entrypoints
- owner/state authority and migrations
- proof for each claimed surface
- cleanup of obsolete paths in touched scope
- current-scope blockers, discovered separate debt, and accepted temporary debt
  disposition

## Proof Allocation

For every material claim, name owner layer, exact proof, expected evidence, and
counterfactual regression probe.

Use initiatives workflow references only when shaping wave state or packet
schema.

## Stop Conditions

Do not promote while:
- a material implementation-shaping decision remains open
- the plan narrows requested breadth or quality without accepted reduction
- selected-slice promotion would not create durable wave state preserving
  objective continuity, route scope, proof/review gates, and stop conditions
- a broad objective is spread shallowly across multiple owners instead of
  following `work-routing` broad-objective semantics
- owner-skill intake is missing or stale
- before-implementation adequacy is missing, stale, or narrower than the
  binding objective
- touched-component integrity is `not assessed`
- unacceptable touched-component integrity relies on accepted temporary debt
  without explicit user acceptance and backlog link
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
- `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md` for
  discovered separate debt or accepted temporary debt
