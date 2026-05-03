---
name: testing-best-practices
description: "Use for test work or behavior changes needing failing executable evidence; choose the right layer and reject test ceremony."
---

# Testing Best Practices

Owns persistent-test doctrine, test value, test cleanup, and red-evidence
workflow when behavior changes need executable failing proof.

## Non-Negotiables

1. Pick layer first.
2. Assert behavior or narrow durable contract.
3. Delete bad tests freely.
4. Touched bad tests do not get grandfathered in.
5. Emit one row per changed persistent test file; never `keep` a file with any
   invalid reason code.
6. Do not add a persistent test unless it protects a changed durable boundary
   and rejects a concrete weaker implementation.

## Red Evidence

For behavior changes that need failing executable evidence, RED happens before
implementation. Testing is not follow-up after implementation.

Valid RED evidence:
- existing failing test at the right boundary
- new failing test at the right boundary
- failing static or contract check for non-runtime behavior

If no meaningful failing check can be produced, stop, clarify, or narrow the
claim. Do not fake a test to satisfy ritual.

Before adding any test, answer:
1. What production regression does it catch?
2. What concrete future change would make it fail?
3. Why is this the cheapest reliable protection?

Weak answer means do not add the test.

## Reference Gates

- Read `references/touched-test-gate.md` when changing a persistent test file,
  adding a persistent test, assigning keep/shrink/rewrite/delete disposition,
  or using invalid reason codes.
- Read `references/proof-strength.md` when proof sufficiency, exact strings,
  source/private shape, mocks, weakly provable claims, branch coverage, or
  multi-proof persistent-test legs matter.
- Read `references/layer-selection.md` when choosing layer, persistence lane,
  runtime handoff, workflow/infra proof, CI posture, or practical add/keep
  checks.
- Read `references/condition-based-waiting.md` when tests use sleeps, fixed
  delays, or wait-heavy retries before assertions.
- Read `references/corpus-audit.md` when running corpus-wide cleanup,
  suspicious-cluster audit, test cost cleanup, or harness-level testing
  follow-up.

## Changed-Test Loop

For each changed persistent test file:
1. Name regression it should catch.
2. Pick cheapest reliable layer.
3. Emit one row:
   `<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`.
4. Load the matched reference gates.
5. If cluster is too big for slice, schedule follow-up now.

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
- mock existence checks instead of behavior
- test-only production APIs
- partial mocks that omit downstream-consumed structure
- testing source text, private shape, or implementation wiring instead of
  public behavior or durable contracts

## Output

One line per changed persistent test file:

`<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`
