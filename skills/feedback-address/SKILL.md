---
name: feedback-address
description: Use before changing code, docs, plans, or workflow because of feedback/review findings, or when workflow friction, recurring agent/process issues, or review patterns are not fixed immediately.
---

# Feedback Address

Classify feedback before editing. Feedback is evidence, not an implementation
plan.

## Gate

Before editing in any direct, planning, or wave route:
1. verify, disprove, or mark the claim unverifiable
2. name the touched owner/interface
3. classify the path

## Paths

- `surface fix`: owner contract is coherent; defect is local.
- `owner fix`: feedback exposes ambiguous defaults, wrong owner, duplicate
  authority, stale path, hidden coupling, or current-objective patch-over.
- `track separate debt`: concrete issue outside the current approval boundary
  that is too large, risky, or separately owned for the current route.
- `accepted temporary debt`: user-owned exception inside the current approval
  boundary with owner, risk, removal condition, and backlog link.
- `no change`: stale, invalid, already addressed, or intentionally by design.

Apply `../design-integrity/SKILL.md` for owner-correct repair. Use
`../work-routing/SKILL.md` when feedback opens non-trivial scope, owner, proof,
public behavior, state authority, migration, or wave shape.

When feedback changes objective, design, readiness, proof, execution slices, or
durable state, amend the route, plan, or durable context before code changes. A
local surface fix may stay in the current route only when that route remains
valid.

Use `../systematic-debugging/SKILL.md` for root-cause diagnosis. This skill
owns disposition of feedback after the claim is understood; it does not replace
debugging.

If live behavior contradicts a passed proof or completed claim, apply
`../readiness-claim/SKILL.md` to identify the proof/interface gap before or
alongside product repair.

## Workflow Feedback

Use the ledger only for workflow friction not fixed in the current change.
Current-objective defects are fixed or routed, not parked here.

Project observations go in `docs-ai/current-work/workflow-feedback-ledger.md`.
If missing, create from `assets/workflow-feedback-ledger.md`.

Each entry includes date, reporter/context, observed issue, affected surface,
suggested disposition, and status. Promote reusable harness policy through
`../harness-governance/SKILL.md`.
