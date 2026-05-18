---
name: design-integrity
description: "Use when work needs design or architecture judgment: owner/interface choice, module depth, state authority, lifecycle, seams/adapters, interface adequacy, or simplification."
---

# Design Integrity

Owns whether the chosen end state and owner/interface make the binding
objective true, including solution correctness.

## Contract

Optimize for the simplest correct end state, not the smallest local change.
Make that end state true through the smallest coherent interface.

Correct implementation of an avoidably wrong final shape is not approvable.

Small means no unnecessary owners, wrappers, gates, adapters, flags,
compatibility paths, generated artifacts, tests, docs, durable notes, or process
surfaces. Coherent means callers, tests, runtime proof, and future changes know
which owner owns state, lifecycle, policy, side effects, and failure modes.

For non-trivial owner/interface work, including new functionality, deletion,
collapse, rewrite, or replacement is the default design move. Reuse is equally
preferred when an existing owner already fits. Adding code, wrappers,
compatibility paths, flags, documents, tests, durable state, or parallel systems
requires justification against the simpler delete/rewrite option and against
reuse or collapse when those are available.

## Challenge

Before execution or review of non-trivial work, answer:

1. What simplest correct end state satisfies the binding objective?
2. What owner/interface makes that end state true?
3. What existing owner, tool, behavior, or contract can be reused, deleted,
   collapsed, or deepened?
4. What is being added, and why is it cheaper for the final system than the
   non-additive path?
5. Can callers, tests, readiness proof, and future work use the same public
   interface?

If the answer exposes shallow ceremony, duplicate authority, hidden lifecycle,
proof that reaches behind the interface, or additive work that mostly preserves
the old shape, reshape before execution.

If implementation materially differs from the accepted design source, revise
the implementation, revise the design source, or block. Do not silently approve
a different shape.

## Must-Block Signals

- wrong or ambiguous owner
- duplicate authority for state, lifecycle, policy, proof, or normalization
- wrapper/seam/adapter that hides rather than simplifies
- interface that leaks raw or weak contract shapes across owners
- test or proof path that must use private state/choreography
- compatibility path without owner, protected surface, and removal condition
- local patch that preserves the reason the owner is wrong
- additive change that bypasses a simpler delete/rewrite option
- additive feature work that skips reuse/collapse pressure because the request
  asks for new behavior
- implementation shape that differs from accepted design without revised
  authority

Stop or route when design integrity is unacceptable and the user has not
explicitly accepted temporary debt.

## Verdict

Report:

- binding objective and accepted reductions
- simplest correct end state
- touched owner/interface
- highest inspected scope
- verdict: `acceptable`, `unacceptable`, or `blocked`
- must-block signals or `none`
- accepted temporary debt backlog link or `none`

`not assessed` is never approvable for non-trivial work.

## References

- Read `references/web-boundaries.md` when a browser boundary is the touched
  owner.
- Read `references/mobile-client-boundaries.md` when a mobile client/backend
  boundary is the touched owner.
- Read `references/python-service-boundaries.md` when a Python service boundary
  is the touched owner.
