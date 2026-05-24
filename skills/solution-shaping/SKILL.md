---
name: solution-shaping
description: "Shape non-trivial implementation before coding or review. Use when the objective, scope, owner/interface, architecture, decomposition, cleanup, refactors, risk, or verification strategy could change the final solution. Preserves the full user objective while choosing the simplest coherent end state and work slices."
---

# Solution Shaping

Owns objective-preserving shape and decomposition before non-trivial work.

## Rule

Preserve the binding objective until the repo actually satisfies it, the user
accepts a reduction, or the work is blocked and visible. Do not replace a broad
objective with a convenient slice, note, plan, claim, test, or map item.

Research current repo reality before choosing the shape. Plans, maps, notes,
summaries, and parent conclusions are context only.

Concrete files, methods, tests, scripts, docs, and failures are evidence, not
automatically the work boundary. For non-trivial work, inspect the owning
workflow and adjacent peers enough to decide whether the issue is local or
points to wrong ownership, a missing boundary, obsolete residue,
over-abstraction, under-abstraction, weak proof, or stale documentation. Choose
a file-local fix only when the surrounding owner remains coherent.

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

## Decomposition

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

When a finding is required for the binding objective, fold it into the required
slice list or current slice. When it invalidates the shape, re-enter shaping.
When it is separate future work, backlog the smallest owned problem and next
action. Current-scope work can move to accepted temporary debt only with
explicit user acceptance, owner, risk, removal condition, and backlog link.

Required slices are the accepted decomposition of the binding objective. Each
required slice names its objective contribution, owner/interface, expected
changed surface, evidence path, cleanup boundary, residual work, and stop
conditions. Every required slice must be completed, blocked, or removed by an
explicit user-accepted reduction before completion is claimed. Invalid slices
are blockers, not implementation challenges.

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
