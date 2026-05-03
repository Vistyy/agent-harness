---
name: feedback-address
description: Use before changing code, docs, plans, or workflow because of feedback/review findings, or when workflow friction, recurring agent/process issues, or review patterns are not fixed immediately.
---

# Feedback Address

Classify feedback before editing. Feedback is evidence, not an implementation
plan.

## Gate

Before editing:
1. verify, disprove, or mark the claim unverifiable
2. name the touched owner/component
3. classify the path

## Paths

- `surface fix`: owner contract is coherent; defect is local.
- `owner fix`: feedback exposes ambiguous defaults, wrong owner, duplicate
  authority, stale path, hidden coupling, or current-objective patch-over.
- `debt plus fix`: only unrelated nearby debt or explicitly accepted temporary
  debt with owner, risk, and removal condition.
- `no change`: stale, invalid, already addressed, or intentionally by design.

Apply `../code-simplicity/SKILL.md` for owner-correct repair. Use
`../planning-intake/SKILL.md` when feedback opens non-trivial scope, owner,
proof, public behavior, state authority, migration, or wave shape.

## Workflow Feedback

Use the ledger only for workflow friction not fixed in the current change.
Current-objective defects are fixed now, not parked here.

Project observations go in `docs-ai/current-work/workflow-feedback-ledger.md`.
If missing, create from `assets/workflow-feedback-ledger.md`.

Each entry includes date, reporter/context, observed issue, affected surface,
suggested disposition, and status. Promote reusable harness policy through
`../harness-governance/SKILL.md`.
