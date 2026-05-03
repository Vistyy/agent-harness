---
name: systematic-debugging
description: Use when a bug, failing check, build failure, performance issue, or unexpected behavior appears during work; find root cause before fixes.
---

# Systematic Debugging

Root cause first. No guess-fixing.

## Iron Law

No fix before root-cause investigation.

## Loop

1. Read the full error or symptom.
2. Reproduce or gather enough evidence to explain why reproduction is blocked.
3. Find the immediate cause, then trace backward through callers, data, state,
   config, and boundaries until the original trigger is known.
4. Compare with a working in-repo pattern.
5. State one hypothesis and test one variable.
6. Fix the source, not the symptom.
7. Add bounded guards or proof only where supported paths can still bypass the
   source fix.
8. Verify the fix and surrounding checks.

For multi-component failures, record what enters and leaves each boundary until
the failing layer is known.

## Handoffs

- After root cause is known, apply `../code-simplicity/SKILL.md` for
  owner-correct repair.
- Read `../testing-best-practices/references/condition-based-waiting.md` when
  tests rely on arbitrary sleeps or fixed waits.
- If the root cause is unresolved ownership, authority, contract, state,
  storage, or interface boundary, use
  `../system-boundary-architecture/SKILL.md`.
- If feedback caused the investigation, use `../feedback-address/SKILL.md` for
  disposition first.

## Stop

- no symptom fix first
- no bundled cleanup during investigation
- no pretending to understand an unreproduced issue
- after three failed fixes, stop and reopen diagnosis

## Reference Gate

- Read `references/diagnostics.md` when structured diagnostic evidence,
  correlation IDs, or bounded runtime context matters.
