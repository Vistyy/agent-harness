# Condition-Based Waiting

Owns the test rule for replacing guessed sleeps with real readiness checks.

Use when tests rely on `sleep`, `setTimeout`, `time.sleep`, fixed waits, or
wait-heavy retries before assertions.

Do not use when timing itself is the behavior under test, such as debounce,
throttle, expiry, or timeout contracts.

## Rule

Wait for the condition the assertion needs:
- event arrived
- state ready
- count reached
- file exists
- UI element/action available
- async operation settled

Every wait helper needs:
- bounded timeout
- modest polling interval
- fresh condition evaluation inside the loop
- failure message naming the condition that timed out

If a fixed timeout is truly contract-backed, first wait for the trigger
condition, then document why the fixed delay is the behavior under test.

Guessed sleeps are invalid persistent-test proof.
