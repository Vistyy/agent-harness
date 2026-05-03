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

## Required References

- Read `references/default-simplicity-posture.md` when shaping any solution.
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
