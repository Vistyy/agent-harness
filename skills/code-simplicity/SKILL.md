---
name: code-simplicity
description: "Default simplicity gate for planning, design, architecture, implementation, tests, workflow, and review; requires touched-component integrity for non-trivial work."
---

# Code Simplicity

This is the canonical simplicity gate. Use it by default for all planning,
design, architecture, implementation, tests, workflow, and review.

Default: choose the simplest honest solution. Delete, collapse, demote, reuse,
or leave work manual before adding structure. Complexity is allowed only when a
real constraint requires it.

Hard rule: for non-trivial work, evaluate the touched owner/component, not just
the diff or immediate request. If that owner has unacceptable
touched-component integrity, reshape or block unless the user explicitly
accepts the debt and a backlog item records it before approval or closeout.

Passing behavior, passing tests, narrow scope, and "already existing" code do
not make unacceptable integrity acceptable.

Deleted files, fewer owners, passing tests, matching the packet, or moving
behavior into one place are not proof of simplicity by themselves. The final
touched owner/component must be acceptable directly.

## Required References

Read `references/default-simplicity-posture.md` when planning or shaping any
solution, design, architecture, workflow, test strategy, or implementation.

Read `references/touched-component-integrity-gate.md` for all non-trivial work,
all reviews, all implementation handbacks, and any time a must-block signal may
exist.

Do not stop at this file when either reference applies.

## Non-Negotiables

- Simplicity is the default, not a preference.
- Push back before executing when requested scope, tooling, architecture,
  rollout, or process adds complexity without a proved constraint. User
  preference overrides this only when the exception is explicit and any accepted
  debt is recorded.
- Diff-only review is invalid for non-trivial work.
- Existing bad shape is not grandfathered when the work touches, depends on,
  preserves, extends, or proves it.
- Accepted debt requires explicit user acceptance and a backlog link.
- `not assessed` touched-component integrity is never approvable.
