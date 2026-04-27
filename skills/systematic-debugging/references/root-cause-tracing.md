# Root Cause Tracing

Bug often explodes deep in stack. Fixing explosion point fixes symptom, not
cause.

Core rule: trace backward through call chain until original trigger is found.
Fix there. Then add defense-in-depth where useful.

## Use When

- error appears deep in execution
- stack trace is long
- bad data arrived from unknown caller
- failing test exists but polluter/trigger is unclear

## Process

1. Observe symptom.
2. Find immediate direct cause.
3. Ask who called that.
4. Trace passed values upward.
5. Stop only when original trigger is found.

Do not stop at first place where crash is visible.

## Instrumentation

When manual tracing is unclear, log before dangerous operation.

Good debug payload:

- current argument values
- `process.cwd()` or similar ambient state
- relevant env vars
- timestamp if ordering matters
- `new Error().stack`

In tests, prefer `console.error()` over app logger if logger may be suppressed.

## Polluter Hunting

If tests pollute filesystem or shared state and culprit is unknown, use
the npm-specific example helper `../examples/find-polluter.sh` to bisect first
polluting test.

## Real Example Pattern

Symptom:

- dangerous operation runs in wrong directory

Trace:

1. operation used empty directory value
2. empty directory resolved to process cwd
3. caller passed empty string
4. test read setup value before `beforeEach`
5. setup helper returned placeholder empty value before initialization

Root cause:

- invalid early access, not bad `git init` call

Fix:

- make getter throw if accessed before setup

Defense-in-depth after source fix:

- validate at API entry
- validate again at manager/service layer
- add environment guard for dangerous operation
- add temporary stack logging if needed

## Principles

- never fix only symptom point if source is traceable
- if you can trace one level higher, keep going
- after fixing source, add bounded validation layers that make bug harder to
  repeat
- source fix plus guardrails beats guardrails alone

## Stack Trace Tips

- log before dangerous operation, not after it fails
- capture full stack with `new Error().stack`
- include enough context to distinguish caller patterns
- look for test names, file paths, and parameter shape

## Success Condition

You know root cause is found when:

- original bad value/state trigger is identified
- symptom disappears with source fix
- weaker symptom-only fix is no longer needed
- regression can be blocked by smaller validation or better test
