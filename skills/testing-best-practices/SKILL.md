---
name: testing-best-practices
description: "Use when writing, reviewing, refactoring, or deleting tests: choose the right layer, enforce high-signal doctrine, and shrink, rewrite, or delete bad tests."
---

# Testing Best Practices

Apply testing doctrine in real work. Start with `references/testing-strategy.md`
for the owner map.

Related:
- red-to-green workflow: `../test-driven-development/SKILL.md`

## Non-Negotiables

1. Pick layer first.
2. Assert behavior or narrow durable contract.
3. Delete bad tests freely.
4. Touched bad tests do not get grandfathered in.
5. Emit one row per changed persistent test file; never `keep` a file with any
   invalid reason code.
6. Do not add a persistent test unless it protects a changed durable boundary
   and rejects a concrete weaker implementation.

## Fast Audit Loop

For each changed persistent test file:
1. Name regression it should catch.
2. Pick cheapest reliable layer.
3. Emit one row:
   `<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`.
4. Load `references/touched-test-gate.md` for the row gate.
5. Load `references/proof-strength.md` for exact-string, private-shape, mock,
   weak-proof, or branch-coverage concerns.
6. Load `references/layer-selection.md` when layer, persistence lane, runtime
   handoff, CI lane, or workflow/infra proof is material.
7. If cluster is too big for slice, schedule follow-up now.

For corpus-wide audit work:
1. Inventory and score suspicious clusters first.
2. Take the next highest-value tranche.
3. Exhaust that tranche before moving on.
4. Refresh the inventory after each tranche.

Helper:
- `scripts/test_suite_audit.py`: inventory and score suspicious test files and
  clusters before a corpus-wide cleanup tranche. It is an audit aid, not proof
  that a test should be kept or deleted.

## Common Failure Modes

- wrong-layer coverage
- mock choreography
- source/implementation-shape assertions
- non-contract exact strings
- broad snapshots/goldens
- overscoped fixtures
- status-only or presence-only checks
- flaky, non-hermetic, or order-dependent tests
- giant mixed-purpose suites
- wait-heavy UI tests
- assertion-thin orchestration tests

## Output

One line per changed persistent test file:

`<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`
