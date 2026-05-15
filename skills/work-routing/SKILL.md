---
name: work-routing
description: "Use for every requested change to choose an explicit direct, planning, or wave execution route before editing, handoff, proof, or review; also use before promoting non-trivial planning to execution."
---

# Work Routing

Owns route selection and planning-readiness closure. Owner design, readiness,
proof, review, runtime, test, and durable-state doctrine stay with their
skills.

## Rule

Use the lightest route that can complete the binding objective through the
right owner/interface.

Every requested change gets an explicit route before editing, handoff, proof,
or review. `direct` is a route decision, not the absence of routing.

Do not replace a broad objective with a convenient slice. A slice is execution
scope, not an accepted reduction.

## Routes

- `direct`: small enough to complete in-thread without durable planning state.
- `planning`: non-trivial work whose objective, design, readiness claim, or
  execution state is not closed.
- `wave execution`: execute an `execution-ready` packet when state must survive
  queue tracking, handoff, interruption, resume, review, or multiple slices.

Use the heavier route when two competent implementers could choose materially
different owners, interfaces, proof paths, runtime behavior, state authority,
migration, compatibility, or public behavior.

## User Boundary

Ask or stop only for product intent, priority, credentials/access, accepted
reduction, accepted temporary debt, destructive/irreversible tradeoff, or
external dependency/cost/compatibility posture outside the current owner.

Implementation, design, architecture, test, cleanup, and proof choices inside
the routed objective are agent-owned.

## Stop

Stop or route to planning when route classification, objective continuity,
design integrity, readiness claim, required proof/review/runtime evidence, or
durable state is missing or stale.

## Planning Ready

Planning is ready only when execution can start without material discovery or
design discretion.

Close:

- Objective: original objective, accepted reductions, residual gaps.
- Design: owner/interface verdict from `../design-integrity/SKILL.md`.
- Readiness: exact claim and proof obligations from
  `../readiness-claim/SKILL.md`.
- State: direct execution or durable state under
  `../initiatives-workflow/SKILL.md`.

Do not promote while objective, design, readiness, current-scope blocker,
accepted temporary debt, discovery, or durable state is missing, stale, or
narrower than the binding objective without accepted reduction.

Non-trivial planning needs `planning_critic` and `quality_guard` approval before
execution readiness.

After routing, use the owner skill named by `AGENTS.md` or the project overlay.
