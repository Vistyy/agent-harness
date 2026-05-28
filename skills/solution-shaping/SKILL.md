---
name: solution-shaping
description: "Shape non-trivial work before coding or review by preserving the full objective and choosing the simplest coherent end state and slices. Use when objective, scope, owner/interface, architecture, decomposition, cleanup, refactors, risk, or verification strategy could change the solution. Use this skill for solution shape only; it does not own durable memory, proof mechanics, or implementation."
---

# Solution Shaping

Owns the objective-preserving probe, shape, and slice loop before non-trivial
work and when new evidence invalidates a plan.

## Rule

Preserve the binding objective until the repo actually satisfies it, the user
accepts a reduction, or the work is blocked and visible. Do not replace a broad
objective with a convenient slice, note, plan, claim, test, or map item.

Research current repo reality before choosing the shape. Plans, maps, notes,
summaries, and parent conclusions are context only.

Ask one decision question at a time. If repo discovery can answer the question,
inspect the repo instead of asking the user. For broad investigation or
adaptation work, return a disposition ledger and proposed owner changes for
user signoff before implementation.

For non-trivial work, independently describe the expected finished repo state
before narrowing the work or accepting that the current implementation is close
to done. Derive that state from the user's objective and current repo reality,
not from branch history, backlog wording, PR status, previous completion
claims, or the files that happened to be mentioned. If the current repo falls
short, either include the gap in current scope, route it as future work or
accepted debt, reject it with evidence, or stop for a decision.

Concrete files, methods, tests, scripts, docs, and failures are evidence, not
automatically the work boundary. For non-trivial work, inspect the owning
workflow and adjacent peers enough to decide whether the issue is local or
points to wrong ownership, a missing boundary, obsolete residue,
over-abstraction, under-abstraction, weak proof, or stale documentation. Choose
a file-local fix only when the surrounding owner remains coherent.

When the area is unfamiliar, zoom out before drilling into edits: map relevant
owners, modules, callers, lifecycle/state paths, and proof surfaces using the
project vocabulary.

## Core Loop

Use one loop: probe, shape, slice, execute/review, close. This skill owns the
first three steps and the replan trigger. Large-change audit is a probe mode.
Atomic claims are the slice rule. Do not add separate gates for these concepts.

## Probe

Probe falsifies the assumption that work is local, simple, or already scoped.
Before treating work as trivial or implementation-ready, inspect enough repo
reality to identify the owner/interface, lifecycle/state path, production
trigger, failure behavior, proof surface, nearby peer patterns, and obvious
cleanup or simplification pressure.

For large branches, simplification passes, broad reviews, or multi-owner
requests, probe with mechanical diff facts first, then cluster by owner,
lifecycle, state authority, risk, and proof surface. First-found cleanup is not
a simplification pass.

For broad, ambiguous, or multi-owner work, keep a compact working model before
narrowing to tasks: objective, finished repo state, owners/boundaries,
knowns/unknowns/risks, finding routes, and plan-changing evidence. Files,
failures, notes, and visible symptoms are signals, not automatic scope.

## Shape

Choose the simplest coherent final solution, not the smallest diff. Include the
owner/interface, state and lifecycle ownership, production trigger, cleanup,
refactors, migrations, debt disposition, material risk, and verification
strategy needed for the solution to be correct.

Do not shape code that is more complex than the objective requires. Extra
concepts, branches, defensive checks, wrappers, states, public methods, tests,
or docs are defects unless a real product, runtime, data, security, or
maintenance reason justifies them.

Delete, collapse, reuse, and rewrite before adding new owners, wrappers, flags,
fallback paths, compatibility paths, process state, or documentation.
Tests protect required behavior, not accidental shape.

Before centralizing, extracting, or polishing duplicated complexity, prove the
underlying concept is still necessary and has a durable owner. If the likely
target architecture would obsolete it, route it as explicit future work or
accepted temporary debt instead of making the current shape nicer.

Use the deletion test before adding, preserving, or polishing an abstraction:
if deleting it removes complexity instead of concentrating necessary behavior
behind a clearer owner/interface, it is probably shallow. For broad
architecture cleanup, present candidate directions with confidence and wait for
the user to choose before editing.

### Fix-Now Disposition

Current-scope findings must be dispositioned immediately. A finding is
`fix now` only when all are true:

- it is exposed by the current work or lies on the touched owner path
- it affects owner coherence, lifecycle consistency, proof validity, cleanup,
  or the simplicity of the current target shape
- the repair uses an established peer pattern already present in the repo
- the repair reduces or unifies structure instead of adding capability, public
  surface, optional behavior, compatibility path, or speculative abstraction
- the repair can be proved inside the current atomic claim or a directly
  adjacent atomic claim

Queue the smallest owned problem or stop for a decision when the finding adds
product/runtime capability, introduces a new abstraction or pattern, requires
broad migration outside the touched owner path, has multiple valid target
patterns, or cannot be proved within the current or directly adjacent atomic
claim.

## Slice

Decompose only after the final shape is understood. A slice may narrow the
implementation surface; it must not narrow the objective or final claim unless
the user accepts that reduction.

Discovery findings are not decomposition. Before a finding becomes work, route
it as one of:

- required for the binding objective
- invalidates the current shape or slice order
- slice-local implementation detail
- blocker or user decision
- separate future work
- accepted temporary debt
- rejected or no-change

End investigation by routing each material finding with owner, reason,
confidence, and next evidence path. Required findings enter the slice list or
current slice; invalidating findings re-enter shaping; future work gets the
smallest owned backlog problem; current-scope debt needs explicit user
acceptance, owner, risk, removal condition, and backlog link. Do not leave
"investigated" as the final state.

Required slices are atomic repo claims. Use this shape:

`For <owner/interface>, <behavior/state/contract> changes from <current> to
<target> through <entrypoint/lifecycle>, proved by <proof>.`

Each slice includes every changed path needed to make that one claim true end
to end, and nothing whose correctness is a separate claim. It names its
contribution to the expected finished state, owner/interface, expected changed
surface, evidence path, cleanup boundary, residual work, and stop conditions.

Split a proposed slice when it has more than one primary owner, state
authority, production trigger, failure policy, independent proof path, or
cleanup disposition. Merge a proposed slice when it cannot prove a behavior or
owner-visible claim alone, such as "models only", "tests only", or "docs only"
work that leaves the real lifecycle unproved.

Every required claim must be completed, blocked, or removed by an explicit
user-accepted reduction before completion is claimed. Invalid claims are
blockers, not implementation challenges.

## Replan

Plan acceptance is not a lock. Re-enter shaping when discovery,
implementation, review, or proof evidence invalidates owner/interface, target
shape, slice order, proof strategy, current-scope boundary, or accepted
complexity. Stop rather than reward-hack a stale plan.

## Escape Hatch

When shaping or slicing cannot honestly preserve the objective, stop or analyze
a valid alternate route. Report the original objective, inspected evidence, the
contradiction or missing decision, why continuing would risk wrong work or fake
proof, and the smallest decision or revised shape needed.

## Review And Proof

Use `../subagent-handoff/SKILL.md` for planning critic, quality guard, or final
reviewer handoffs when risk warrants. Use `../verify-work/SKILL.md` to select
proof that would fail if the shaped claim were false.

## References

- Read `references/web-boundaries.md` when a browser route, page, shared UI
  module, facade, or screen model is the touched owner.
- Read `references/mobile-client-boundaries.md` when a mobile client/backend
  contract is the touched owner.
- Read `references/python-service-boundaries.md` when a Python service, unit of
  work, repository, handler, or dynamic input boundary is the touched owner.
- Read `references/review-lenses.md` before non-trivial planning, review,
  evidence design, or closeout.
