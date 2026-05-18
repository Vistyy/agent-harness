---
name: work-routing
description: "Use for every requested change to choose an explicit direct, planning, or wave execution route before editing, handoff, proof, or review; also use before promoting non-trivial planning to execution."
---

# Work Routing

Owns route choice. It does not own design, proof, review, runtime, test, or
durable context doctrine.

## Rule

Use for every requested change. Route to the simplest correct end state for the
binding objective, not to the smallest local diff.

Every requested change gets an explicit route before editing, handoff, proof, or
review. `direct` is a route decision, not the absence of routing.

Do not replace a broad objective with a convenient slice. A slice is execution
scope, not an accepted reduction.

## Routes

- `direct`: use when the simplest correct end state is clear enough to execute
  and review in-thread.
- `planning`: use when the end state, owner/interface, ordering, material risks,
  required evidence, or hidden design discretion must be decided before
  execution.
- `wave execution`: use only when durable context must survive queue tracking,
  handoff, interruption, resume, review, or multiple slices.

Use the heavier route when the lighter route would bias the work toward
patching around the defect, preserving the wrong owner, or hiding a material
decision in implementation.

## User Boundary

Ask or stop only for product intent, priority, credentials/access, accepted
reduction, accepted temporary debt, destructive/irreversible tradeoff, or
external dependency/cost/compatibility posture outside the current owner.

Implementation, design, architecture, test, cleanup, and proof choices inside
the routed objective are agent-owned.

## Stop

Stop or route to planning when route classification, objective continuity, the
simplest correct end state, design integrity, readiness claim, required
proof/review/runtime evidence, or durable context is missing or stale.

## Planning Ready

Planning is ready only when execution can start without material discovery,
hidden design discretion, or a likely simpler end state left unexplored.

Close:

- Objective: original objective, accepted reductions, residual gaps.
- End state: the simplest correct final shape and rejected simpler/alternate
  paths.
- Design: owner/interface verdict from `../design-integrity/SKILL.md`.
- Readiness: exact claim and proof obligations from
  `../readiness-claim/SKILL.md`.
- Material risk: matched `../readiness-claim/SKILL.md` material risks are
  identified, required evidence is named, blockers/debt are disposed, and no
  hidden design discretion remains; final claims use the readiness-owned
  disposition labels.
- State: direct execution or durable context under
  `../initiatives-workflow/SKILL.md` when context must survive.

Do not promote while objective, end state, design, readiness, current-scope
blocker, accepted temporary debt, discovery, or durable context is missing,
stale, or narrower than the binding objective without accepted reduction.

Non-trivial planning needs `planning_critic` and `quality_guard` challenge
before execution readiness.
