---
name: testing-best-practices
description: Use when writing, reviewing, refactoring, or deleting tests to enforce the repo's high-signal testing doctrine, choose the right layer, and identify bad tests that should be shrunk, rewritten, or deleted.
---

# Testing Best Practices

Apply testing doctrine in real work. Owner policy lives in `references/testing-strategy.md`.

Related:
- red-to-green workflow: `../test-driven-development/SKILL.md`

## Non-Negotiables

1. Pick layer first.
2. Assert behavior or narrow durable contract.
3. Delete bad tests freely.
4. If test mostly protects implementation shape, treat it as bad.
5. If broad test catches real bug, move durable regression down when feasible.
6. Touched bad tests do not get grandfathered in.
7. Do not add a new persistent test unless it protects a changed durable
   boundary and rejects a concrete weaker implementation.
8. Corpus-wide cleanup is allowed to own whole suspicious tranches rather than
   only touched files.
9. When touching tests, emit one testing-strategy row per changed persistent
   test file; never `keep` a file with any invalid reason code.
10. Do not use mutable fake kwargs bags or broad `response.json()` dict/list
    casts as the main proof; use typed call records, typed adapters/models, or
    move the proof to the right layer.

## Fast Audit Loop

For each changed persistent test file:
1. Name regression it should catch.
2. Pick cheapest reliable layer.
3. Emit one row:
   `<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`.
4. If keeping high-layer test, state why smaller durable guard is not enough.
5. If adding a new persistent test, justify:
   - changed boundary
   - concrete regression rejected
   - why cheaper existing proof is insufficient
6. If cluster is too big for slice, schedule follow-up now.

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

## Exact String Rule

Valid only when string itself is contract:
- governed end-user copy
- stable CLI/help/diagnostic ABI
- schema keys or protocol literals

Usually bad:
- HTML fragments
- incidental error wording
- source or script text mirrors

## Output

One line per changed persistent test file:

`<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`
