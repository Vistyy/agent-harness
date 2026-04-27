---
name: test-driven-development
description: Use before implementing any behavior change to establish failing executable evidence first and drive work through red to green.
---

# Test-Driven Development

Use TDD as proof workflow, not test-count ritual.

Related:
- testing doctrine: `../testing-best-practices/SKILL.md`
- test anti-pattern details:
  `references/testing-anti-patterns.md`

## Non-Negotiables

1. Start with RED evidence.
2. Add tests only if they are cheapest reliable protection.
3. Reject low-value tests even if they satisfy ceremony.
4. Prefer public-boundary outcomes over internals.
5. Pick layer first and justify it in one line.
6. For workflow/infra/runtime wiring, prefer executable integration or smoke proof over source/implementation-shape assertions.
7. ABI-only unit tests are acceptable when workflow/script unit tests are unavoidable.

## Valid RED Evidence

- existing failing test at right boundary
- new failing test at right boundary
- existing failing static/contract check for non-runtime behavior

If no meaningful failing check can be produced, stop and clarify scope.

## Value Gate

Before adding test, answer:
1. What production regression does it catch?
2. What concrete future change would make it fail?
3. Why is this cheapest reliable protection?

Weak answer = do not add test.

## Preferred Order

1. Reuse existing failing test.
2. Contract/boundary test.
3. Small unit test for real invariant.
4. Integration test when cross-boundary behavior is actual invariant.

## Do Not Add

- implementation-detail assertions
- mock-centric call-order tests
- framework behavior tests
- trivial getter/default/no-crash tests
- snapshots without contract meaning
- slow tests with tiny risk reduction
- source/implementation-shape assertions; use the testing-strategy owner for
  exception rules

## Workflow

### Red

- create or find failing evidence
- run narrowest command that proves failure

### Green

- implement minimal fix
- rerun same narrow check

### Refactor

- improve structure with checks still green
- run smallest relevant confidence suite

## Commands

Use repo wrappers:

```bash
just <stack> test tests/path/to/test_file.py::test_name
just <stack> tests unit sum
just <stack> quality-fast
just <stack> quality
```

## Done

- RED happened before implementation
- final checks are green
- new tests passed value gate
- no low-value tests introduced
