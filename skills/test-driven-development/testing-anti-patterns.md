# Testing Anti-Patterns

Use when writing/changing tests, adding mocks, or feeling tempted to add test-only production APIs.

## Iron Rules

1. Never test mock existence instead of behavior.
2. Never add test-only methods to production code.
3. Never mock without understanding real dependency behavior.
4. Never use partial mocks for structures downstream code consumes.
5. Never treat testing as follow-up after implementation.

## Anti-Patterns

### Mock Existence Tests

Bad:
- asserting rendered `*-mock` node exists

Why bad:
- proves mock works, not product behavior

Fix:
- test real behavior,
- or keep mock but assert caller behavior, not mock presence

Gate:
- ask "am I testing real behavior or mock existence?"

### Test-Only Production Methods

Bad:
- `destroy()`, `reset()`, or similar method added only for tests

Why bad:
- pollutes production API
- confuses lifecycle ownership

Fix:
- move cleanup to test utilities
- keep production class focused on real responsibilities

Gate:
- ask "is this method only for tests?"

### Mocking Without Understanding

Bad:
- mock high-level method that test logic actually depends on

Why bad:
- removes side effects test needs
- creates false failure or false pass

Fix:
- run with real implementation first
- identify real slow/external boundary
- mock lower layer only

Gate:
- what side effects does real method have?
- does test depend on them?

### Partial Mocks

Bad:
- mocking only fields current assertion touches

Why bad:
- hides structural assumptions
- downstream code may need omitted fields

Fix:
- mirror complete real response/schema shape

Gate:
- compare mock against real documented/example structure

### Testing As Afterthought

Bad:
- implementation done, tests later

Fix:
- red -> green -> refactor

## Warning Signs

- mock setup longer than test logic
- test breaks when mock changes, not when behavior changes
- test needs production-only helper added for convenience
- broad source-text assertions replace executable proof

When signs appear, shrink, rewrite, or delete test.
