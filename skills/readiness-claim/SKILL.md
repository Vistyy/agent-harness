---
name: readiness-claim
description: "Use before proof, review, runtime evidence, handoff, or completion for non-trivial behavior/readiness/fix claims; owns claim completeness and proof admissibility."
---

# Readiness Claim

Owns what can honestly be claimed.

## Contract

A claim is admissible only when it names the interface being claimed and the
proof crosses that interface. Otherwise the claim is blocked or explicitly
narrowed.

The final claim cannot exceed:

- binding objective and accepted reductions
- design interface selected by `../design-integrity/SKILL.md`
- proof that crossed that interface
- runtime, design, and review verdicts for the same claim
- stated exclusions and residual risks

Non-trivial runtime-visible behavior needs runtime evidence unless the claim is
tiny, local, and has no public-behavior or cross-boundary runtime risk.

## Claimed Interface

For a workflow claim, name:

- entrypoint and actor
- inputs and producer path
- observable output
- durable state changes
- external side effects
- cleanup/release/rollback behavior
- user/operator status projection
- failure, retry, restart, and downtime behavior
- exclusions, or `none`

For a module claim, name the public interface, invariants, ordering, error
modes, state authority, side effects, and exclusions.

## Proof Rule

Proof counts only for the interface obligations it actually exercises.

Hand-built state, mocks, stale fixtures, or impossible preconditions do not
prove workflow readiness unless the production producer path that creates that
state is also proven.

Tests, review, screenshots, static inspection, and runtime evidence are not
substitutes for one another. They may support the same claim only when they
cover the same claimed interface.

Use:

- `../runtime-proof/SKILL.md` for live-use mechanics
- `../testing-best-practices/SKILL.md` for persistent tests
- `../code-review/SKILL.md` for isolated review
- the relevant design owner and `design_judge` when product UI design readiness
  is claimed

## Gate

Before proof, review, runtime evidence, handoff, or completion:

1. state the exact claim
2. state the claimed interface
3. list material obligations and exclusions
4. map proof/evidence to those obligations
5. block or narrow any unproved obligation
6. report residual risks or `none`

## Escaped Defects

If live behavior contradicts a passed proof or completed claim, the next route
must identify the missed interface obligation or invalid proof precondition.
Fixing only the product defect is incomplete when the proof gap belongs to the
current objective or touched owner.
