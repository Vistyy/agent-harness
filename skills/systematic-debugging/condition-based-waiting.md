# Condition-Based Waiting

Arbitrary sleeps make tests flaky. Wait for real condition, not guessed time.

## Use

Use when:
- test uses arbitrary delay like `setTimeout`, `sleep`, `time.sleep`
- test passes locally and flakes under load or CI
- async work must finish before assertion

Do not use when:
- testing real timing behavior like debounce or throttle
- timeout itself is part of contract

If arbitrary timeout is correct, document why.

## Core Pattern

```typescript
// Bad: guessed timing
await new Promise(r => setTimeout(r, 50));
expect(getResult()).toBeDefined();

// Good: real condition
await waitFor(() => getResult() !== undefined, "result");
expect(getResult()).toBeDefined();
```

## Common Conditions

| Need | Pattern |
| --- | --- |
| event arrived | `waitFor(() => events.find(e => e.type === "DONE"), "DONE event")` |
| state ready | `waitFor(() => machine.state === "ready", "ready state")` |
| count reached | `waitFor(() => items.length >= 5, "5 items")` |
| file exists | `waitFor(() => fs.existsSync(path), "file creation")` |
| compound state | `waitFor(() => obj.ready && obj.value > 10, "ready value")` |

## Implementation Rules

- poll at modest interval like `10ms`, not `1ms`
- always include timeout
- error must say what condition timed out
- compute condition inside loop; do not cache stale state

Generic shape:

```typescript
async function waitFor<T>(
  condition: () => T | undefined | null | false,
  description: string,
  timeoutMs = 5000
): Promise<T> {
  const start = Date.now();

  while (true) {
    const result = condition();
    if (result) return result;

    if (Date.now() - start > timeoutMs) {
      throw new Error(`Timeout waiting for ${description} after ${timeoutMs}ms`);
    }

    await new Promise((r) => setTimeout(r, 10));
  }
}
```

Full implementation and helper variants live in `condition-based-waiting-example.ts`.

## When Timeout Is Correct

Use timeout only after trigger condition is real and timing is contract-backed.

Example:

```typescript
await waitForEvent(manager, "TOOL_STARTED");
await new Promise((r) => setTimeout(r, 200));
```

Requirements:
1. first wait for trigger condition
2. timeout matches known timing, not guess
3. comment explains why

## Rule

Replace guessed sleeps with condition waits unless time itself is behavior under test.
