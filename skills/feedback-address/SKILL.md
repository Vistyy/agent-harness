---
name: feedback-address
description: Use before changing code, docs, plans, or workflow because of feedback or review findings.
---

# Feedback Address

Use feedback as evidence. Fix the cause, not the comment.

## Required Gate

Do not edit until all three are true:

1. The claim is verified, disproved, or explicitly marked unverifiable.
2. The touched owner/component is named.
3. The path is classified as surface fix, owner fix, debt plus fix, or no
   change.

One valid finding is enough to expose bad owner shape. Multiple related
findings are only extra evidence.

## Classification

Use surface fix only when the owner contract is coherent and the defect is a
local mistake inside that contract.

Use owner fix when the defect is enabled by ambiguous defaults, duplicate
authority, wrong ownership, misleading helper names, hidden coupling, unclear
state lifecycle, or repeated caller-specific interpretation.

Use debt plus fix only after presenting the blocker, risk, recommended
reshape, and backlog path, and only after explicit user acceptance. Then make
the necessary immediate fix and record backlog with owner, risk, and removal
condition.

Use no change only when the feedback is stale, invalid, already addressed, or
intentionally by design.

## Handoff

Use `planning-intake` before implementation when feedback opens non-trivial
implementation-shaping scope, owner boundaries, proof, public behavior, state
authority, migration, or wave/plan scope.

Verify with proof matched to the touched owner.

## Guardrails

- Feedback suggestions are hypotheses, not binding implementation plans.
- Push back on requests that preserve wrong ownership, add wrappers around bad
  shape, or weaken the user objective.
- Use a numbered disposition ledger only when the user asks for triage or when
  several feedback items must be tracked explicitly.
