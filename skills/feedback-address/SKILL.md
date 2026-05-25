---
name: feedback-address
description: "Classify feedback or review findings before edits by deciding whether they are a surface fix, owner fix, separate backlog work, accepted temporary debt, or no-change. Use when comments, review findings, PR feedback, or user concerns need disposition before implementation. Use this skill for feedback disposition only; it does not replace root-cause debugging, solution shaping, or code repair."
---

# Feedback Address

Classify feedback before editing. Feedback is evidence, not authority or an
implementation plan.

## Rule

Before feedback-caused edits:
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

Apply `../solution-shaping/SKILL.md` when feedback opens non-trivial scope,
owner, proof, public behavior, state authority, migration, or work shape.

When feedback changes objective, target shape, proof, implementation slices, or
durable memory, amend the active note before code changes. A local surface fix
may stay local only when the objective remains valid.

Use `../systematic-debugging/SKILL.md` for root-cause diagnosis. This skill
owns disposition of feedback after the claim is understood; it does not replace
debugging.

If live behavior contradicts a passed proof or completed claim, apply
`../solution-shaping/SKILL.md` to identify the proof/interface gap before or
alongside product repair.

## Workflow Ledger

Use the ledger only for recurring process observations that are not fixed in
the current change. Current-objective defects are fixed or routed, not parked.

Project observations go in `docs-ai/current-work/workflow-feedback-ledger.md`.
If missing, create from `assets/workflow-feedback-ledger.md`.

Each entry includes date, reporter/context, observed issue, affected surface,
suggested disposition, and status. Promote reusable overlay policy through
`../overlay-governance/SKILL.md`.
