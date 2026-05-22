---
name: testing-best-practices
description: "Use when adding, changing, deleting, reviewing, or relying on persistent tests, or when choosing whether a test is the right proof layer. Covers test layer, admission, durability, fake red evidence, and cleanup."
---

# Testing Best Practices

Owns persistent-test admission, cleanup, layer choice, test strength, and
meaningful persistent red evidence.

Does not own delivery claims, final scope, proof selection, browser mechanics,
or mobile mechanics. Use `../solution-shaping/SKILL.md` for final shape and
`../verify-work/SKILL.md` for proof selection.

## Non-Negotiables

Persistent tests protect durable boundaries, not ceremony.

Rules:
- this skill is mandatory whenever persistent tests are added, changed,
  deleted, reviewed, or used as proof
- choose the cheapest honest persistent layer
- assert public behavior or a narrow durable contract
- assert current positive behavior or structure; negative assertions are valid
  only for current closed sets, schemas, manifests, or public API contracts
- require changed durable boundary plus named weaker implementation
- delete, shrink, or rewrite bad touched tests
- never fake red evidence
- never replace required live-use proof with persistent tests
- for migration/runtime failures, prefer the real failed path or faithful
  integration/smoke proof before mocked persistent tests
- e2e tests are written by implementers when an approved task owns them; they
  support verification only when they exercise the same claim through a
  faithful entrypoint and leave inspectable artifacts

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

For corpus cleanup, inventory suspicious clusters, take one coherent tranche,
assign `keep | shrink | rewrite | delete`, finish it, then refresh inventory.

Do not hide repo-wide ballast behind "untouched files" once cleanup is the
owned work.

When cleanup spans product areas but the real problem is test quality, keep
follow-up owned by testing cleanup instead of scattering it across product
queues.

Suspicious by default: giant mixed-purpose suites, status/presence/snapshot
clusters, heavy mocks/waits with thin assertions, runner-heavy low-layer tests,
and expensive tests without explicit retained contract.

Delete redundant expensive tests before optimizing them. Move behavior downward
before speeding up the wrong layer.

Helper:
- `scripts/test_suite_audit.py`: inventory and score suspicious test files and
  clusters before a corpus-wide cleanup tranche. It is an audit aid, not proof
  that a test should be kept or deleted.

## Output

One line per changed persistent test file:

`<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`
