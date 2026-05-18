---
name: readiness-claim
description: "Use before proof, review, runtime evidence, handoff, or completion for non-trivial behavior/readiness/fix claims; owns claim completeness and proof admissibility."
---

# Readiness Claim

Owns what can honestly be claimed and how final delivery is explained.

## Contract

A claim is admissible only when it names the interface being claimed and the
proof crosses that interface. Otherwise the claim is blocked or explicitly
narrowed.

The final claim cannot exceed:

- binding objective and accepted reductions
- simplest correct end state and design interface selected by
  `../design-integrity/SKILL.md`
- proof that crossed that interface
- runtime, design, and review verdicts for the same claim
- stated exclusions and residual risks
- delivery brief support for non-trivial work

Non-trivial runtime-visible behavior needs runtime evidence unless the claim is
tiny, local, and has no public-behavior or cross-boundary runtime risk.

## Claimed Interface

For a workflow claim, name entrypoint/actor, inputs and producer path,
observable output, durable state changes, external side effects,
cleanup/release/rollback behavior, user/operator status projection, failure,
retry, restart, downtime behavior, and exclusions.

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

## Delivery Brief

For non-trivial completion, produce a delivery brief a non-code owner can trust
without reading the diff. It is not a new approval gate; it is the final claim
mapped to evidence and reviewer judgment.

Inline is the default. Use `assets/delivery-brief.md` only when a durable
artifact is useful for active durable work; place it next to the active context
at `docs-ai/current-work/<wave-id>/delivery-brief.md`.

The brief states:

- objective and accepted reductions
- outcome in product/system terms
- end-state shape: what was deleted, collapsed, reused, avoided, or added and
  why this is the simplest correct shape
- plan coverage: delivered, changed with reason, not delivered with accepted
  reduction or blocker
- evidence mapped by claim, including what each item does not prove
- reviewer verdicts for strategy, implementation shape, and final merge
  readiness
- residual risks, accepted debt, separate backlog, or `none`
- context closeout: durable notes removed, superseded, extracted, or still
  intentionally active

Durable delivery briefs follow the same lifecycle as active durable context.
At closeout, extract retained facts to the owning durable surface or backlog,
then remove, supersede, or leave the brief intentionally active with a reason.

A delivery brief is invalid when it only narrates work done, cites passing
checks without claim mapping, hides a narrowed objective, or omits reviewer
judgment for non-trivial work.

## Reference Gates

- Read `references/material-risk-lenses.md` before non-trivial planning,
  handoff, proof, runtime evidence, review, or completion claims when material
  non-correctness risks can affect the binding objective, touched
  owner/interface, proof path, runtime behavior, operator workflow, or approval
  boundary.

## Gate

Before proof, review, runtime evidence, handoff, or completion:

1. state the exact claim
2. state the claimed interface
3. list material obligations and exclusions
4. apply any matched reference gate and record material-risk disposition
5. map proof/evidence to those obligations
6. block or narrow any unproved obligation
7. for non-trivial completion, assemble delivery-brief support
8. report residual risks or `none`

## Escaped Defects

If live behavior contradicts a passed proof or completed claim, the next route
must identify the missed interface obligation or invalid proof precondition.
Fixing only the product defect is incomplete when the proof gap belongs to the
current objective or touched owner.
