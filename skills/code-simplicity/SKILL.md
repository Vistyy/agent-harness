---
name: code-simplicity
description: "Default simplicity gate for planning, design, architecture, implementation, tests, workflow, and review; requires touched-component integrity for non-trivial work."
---

# Code Simplicity

Use by default for planning, design, architecture, implementation, tests,
workflow, and review.

## Rule

Choose the least complex complete correction.

Simple does not mean smallest diff, easiest proof, safest review slice, or
fastest approvable patch. Simple means the smallest shape that satisfies the
binding user objective and leaves the touched owner/component coherent.

If the current objective touches a wrong owner, bad boundary, stale path,
duplicated authority, patch-over workaround, or unnecessary ceremony, fixing
that owner is in scope. Defer only unrelated nearby debt or explicitly accepted
temporary debt with owner, risk, and removal condition.

Prefer, in order:
1. delete
2. collapse
3. demote to manual or breakglass
4. reuse an existing owner
5. add only the structure a real constraint requires

## Owner-Correct Work

Do not patch symptoms. If the defect, feedback, failed proof, or requested
change belongs to the current objective or touched owner, fix that owner now.

Defer only:
- unrelated nearby debt
- explicitly accepted temporary debt with owner, risk, and removal condition

If fixing the owner is too large, risky, or blocked, stop and name the blocker.
Do not apply a smaller patch that preserves the reason the work is wrong.

Block or reshape when the plan:
- treats a symptom as the root problem
- preserves the wrong owner or duplicated authority
- patches around a defect that affects the current objective
- moves complexity instead of removing it
- keeps optional workflow, proof, adapter, flag, or compatibility ceremony
- narrows breadth, quality, runtime behavior, or review surface without
  accepted reduction
- defers debt that belongs to the current objective or touched owner

## Local Shape

Local structure must make ownership and behavior easier to see.

Rules:
- repeated branching, mutation stages, or adapter choreography means hotspot
  pressure
- helpers must clarify ownership and behavior, not hide the same hotspot behind
  another name
- keep mutation paths visible: initialization, change, and cleanup should be
  easy to find
- publish semantic state at the authority boundary instead of making consumers
  recompute readiness, phase, ownership, or permission from low-level flags
- do not hide major path differences behind loose booleans, nullable parameter
  combinations, or option fields that cannot affect valid output
- production boundary modules must not branch to test-only or
  missing-framework fallback behavior
- test seams should fall out of good design, not be bolted on after tests hurt

## Required References

- Read `references/touched-component-integrity-gate.md` for non-trivial work,
  reviews, implementation handbacks, or possible must-block signals.

## Non-Negotiables

- Completion is measured against the binding objective, not the diff.
- Delete, collapse, demote, or reuse before adding.
- Diff-only review is invalid for non-trivial work.
- Existing bad shape is not grandfathered when the work touches, depends on,
  preserves, extends, or proves it.
- `not assessed` touched-component integrity is never approvable.
- Accepted debt requires explicit user acceptance and a backlog link.
