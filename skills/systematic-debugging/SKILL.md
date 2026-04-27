---
name: systematic-debugging
description: Use for bugs, test failures, build failures, performance issues, or unexpected runtime behavior; find root cause before proposing or applying fixes.
---

# Systematic Debugging

Root cause first. No guess-fixing.

## Iron Law

`NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST`

If Phase 1 is incomplete, do not propose fix.

## Use When

- test failure
- bug
- unexpected behavior
- performance issue
- build failure
- integration break

Use it especially when pressure is high or "quick fix" feels obvious.

## Process

### 1. Root Cause Investigation

- read errors fully
- reproduce consistently
- check recent changes
- gather evidence across component boundaries
- trace bad data backward to source

For multi-component systems:
- log what enters and leaves each boundary
- verify config and env propagation
- identify exact failing layer before changing code

### 2. Pattern Analysis

- find working example in same codebase
- read reference pattern completely
- list concrete differences
- understand required dependencies and assumptions
- after second confirmed defect in same surface, ask whether one shared owner or
  authority mistake explains both failures
- if yes, stop stacking symptom patches and route through structural diagnosis

### 3. Hypothesis And Test

- state one hypothesis clearly
- make smallest possible change to test it
- test one variable at a time
- if it fails, form new hypothesis instead of stacking fixes

### 4. Implementation

- create failing test or repro first
- implement one fix for root cause
- verify fix and surrounding checks

If 3 fixes failed:
- stop
- question architecture
- discuss before more fixes

If 2+ valid findings share same controller/store/service:
- stop incremental patching
- write boundary diagnosis first
- prefer common-cause refactor over third local fix

## Guardrails

- no symptom fix first
- no bundled "while here" cleanup during root-cause step
- no pretending to understand what you do not understand
- if issue is not reproducible, gather more evidence instead of guessing

## Optional References

- `root-cause-tracing.md`: use when the symptom appears deep in a call stack or
  the original trigger is unclear.
- `condition-based-waiting.md`: use when tests rely on arbitrary sleeps.
- `examples/condition-based-waiting-example.ts`: illustrative example only; do
  not copy project-shaped imports directly.
- `defense-in-depth.md`: use after root cause is known and supported paths need
  layered validation.
- `references/diagnostics.md`: use when structured logs, correlation IDs, or
  runtime diagnostic fields matter.
- `examples/find-polluter.sh`: npm-specific example helper for finding a test
  that creates unwanted files or shared state.

Evaluation-only files:
- `evaluations/test-academic.md`
- `evaluations/test-pressure-1.md`
- `evaluations/test-pressure-2.md`
- `evaluations/test-pressure-3.md`
