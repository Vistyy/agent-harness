---
name: feedback-address
description: Use before changing code, docs, plans, or workflow because of feedback/review findings, or when workflow friction, recurring agent/process issues, or review patterns are not fixed immediately.
---

# Feedback Address

Use feedback as evidence. Fix the cause, not the comment.

## Gate

Before editing:
1. verify, disprove, or mark the claim unverifiable
2. name the touched owner/component
3. classify the path

## Paths

- `surface fix`: owner contract is coherent; the defect is local.
- `owner fix`: feedback exposes ambiguous defaults, wrong owner, duplicate
  authority, stale path, hidden coupling, or patch-over behavior in the current
  objective.
- `debt plus fix`: only for unrelated nearby debt or explicitly accepted
  temporary debt with owner, risk, and removal condition.
- `no change`: stale, invalid, already addressed, or intentionally by design.

## Rule

If the defect affects the current objective or touched owner, fix that owner
now. Do not appease feedback with a smaller patch that preserves the reason the
feedback was valid.

Use `planning-intake` when feedback opens non-trivial implementation-shaping
scope, owner boundaries, proof, public behavior, state authority, migration, or
wave/plan scope.

## Workflow Feedback

Use the ledger only for workflow friction not fixed in the current change.
Current-objective defects are fixed in the active workflow, not parked here.

Project-specific observations go in
`docs-ai/current-work/workflow-feedback-ledger.md`. If missing, create from
`assets/workflow-feedback-ledger.md`.

Each entry includes date, reporter/context, observed issue, affected surface,
suggested disposition, and status. Promote reusable harness policy through
`../harness-governance/SKILL.md`.
