---
name: testing-best-practices
description: "Use for persistent test work: adding, editing, deleting, reviewing, or deciding whether a behavior change needs durable executable proof."
---

# Testing Best Practices

Owns persistent-test admission, cleanup, layer choice, proof strength, and
meaningful persistent red evidence.

Does not own runtime verdicts, final completion claims, browser mechanics, or
mobile mechanics. Use `../runtime-proof/SKILL.md`,
`../verification-before-completion/SKILL.md`, `../webapp-testing/SKILL.md`, and
`../mobileapp-testing/SKILL.md` for those owners.

## Non-Negotiables

Persistent tests protect durable boundaries, not ceremony.

Rules:
- choose the cheapest honest persistent layer
- assert public behavior or a narrow durable contract
- add a persistent test only for a changed durable boundary with a named weaker
  implementation it rejects
- delete, shrink, or rewrite bad touched tests; they are not grandfathered
- do not fake red evidence to satisfy ritual
- runtime proof is not replaced by persistent tests

## Reference Gates

Read `references/persistent-test-contract.md` when adding, editing, deleting,
reviewing, or deciding whether to keep a persistent test.

## Changed-Test Loop

For each changed persistent test file:
1. Name regression it should catch.
2. Pick cheapest reliable layer.
3. Emit one row:
   `<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`.
4. If the changed cluster is too big for the slice, schedule follow-up now.

## Corpus Cleanup

Use only when the work owns a broader persistent-test suite slice, not for
ordinary touched-test edits.

For corpus cleanup:
- inventory and rank suspicious clusters
- take one coherent tranche: directory, route family, controller family, or
  provider family
- assign `keep | shrink | rewrite | delete` dispositions across the tranche
- finish the tranche before moving on
- refresh the inventory after each tranche

Do not hide repo-wide ballast behind "untouched files" once cleanup is the
owned work.

When cleanup spans product areas but the real problem is test quality, keep
follow-up owned by testing cleanup instead of scattering it across product
queues.

Suspicious by default: giant mixed-purpose suites, status/presence/snapshot
clusters, heavy mocks/waits with thin assertions, runner-heavy low-layer tests,
and expensive tests without an explicit retained contract.

Delete redundant expensive tests before optimizing them. Move behavior downward
before speeding up the wrong layer.

Helper:
- `scripts/test_suite_audit.py`: inventory and score suspicious test files and
  clusters before a corpus-wide cleanup tranche. It is an audit aid, not proof
  that a test should be kept or deleted.

## Output

One line per changed persistent test file:

`<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`
