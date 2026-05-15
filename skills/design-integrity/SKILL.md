---
name: design-integrity
description: "Use when work needs design or architecture judgment: owner/interface choice, module depth, state authority, lifecycle, seams/adapters, interface adequacy, or simplification."
---

# Design Integrity

Owns whether the work is shaped around the right owner and interface, including
solution correctness.

## Contract

Make the binding objective true through the smallest coherent interface.

Correct implementation of an avoidably wrong solution shape is not approvable.

Small means no unnecessary owners, wrappers, gates, adapters, flags, or
compatibility paths. Coherent means callers, tests, runtime proof, and future
changes know which owner owns the state, lifecycle, policy, and side effects.

For non-trivial owner/interface work, deletion, collapse, rewrite, or
replacement is the default design move. Adding code, wrappers, compatibility
paths, flags, or parallel systems requires justification against the simpler
delete/rewrite option.

Large additive plans must prove the smallest deep owner, the simpler shape that
was rejected, and why existing tools or contracts cannot absorb generic
behavior.

## Design Test

For non-trivial work, answer:

1. What owner/module/interface is supposed to make the objective true?
2. What must callers know to use that interface correctly?
3. Does the interface hide meaningful behavior, or does it mostly mirror its
   implementation?
4. If this owner were deleted, would complexity disappear or spread into
   callers?
5. Can tests and readiness proof use the same public interface as callers?

If the answers expose shallow ceremony, duplicate authority, hidden lifecycle,
or proof that reaches behind the interface, reshape before execution.

If implementation materially differs from the accepted design source, revise
the implementation, revise the design source, or block. Do not silently approve
a different shape.

## Interface Rules

- An interface includes types, invariants, ordering, error modes, config,
  lifecycle, side effects, and performance expectations.
- The interface is the test surface.
- Prefer depth: more useful behavior behind less caller knowledge.
- Prefer locality: change, bugs, knowledge, and proof concentrated in one
  owner.
- Add a seam or adapter only when behavior genuinely varies across it.
- Delete, collapse, or deepen shallow modules before adding another layer.

## Integrity Verdict

Report:

- binding objective and accepted reductions
- touched owner/interface
- highest inspected scope
- verdict: `acceptable`, `unacceptable`, or `blocked`
- must-block signals or `none`
- accepted temporary debt backlog link or `none`

`not assessed` is never approvable for non-trivial work.

## Must-Block Signals

- wrong or ambiguous owner
- duplicate authority for state, lifecycle, policy, proof, or normalization
- wrapper/seam/adapter that hides rather than simplifies
- interface that leaks raw or weak contract shapes across owners
- test or proof path that must use private state/choreography
- compatibility path without owner, protected surface, and removal condition
- local patch that preserves the reason the owner is wrong
- additive change that bypasses a simpler delete/rewrite option
- implementation shape that differs from accepted design without revised
  authority

Stop or route when design integrity is unacceptable and the user has not
explicitly accepted temporary debt.

## References

- Read `references/web-boundaries.md` when a browser boundary is the touched
  owner.
- Read `references/mobile-client-boundaries.md` when a mobile client/backend
  boundary is the touched owner.
- Read `references/python-service-boundaries.md` when a Python service boundary
  is the touched owner.
