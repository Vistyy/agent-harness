---
name: verification-before-completion
description: "Use before any completion or fix claim to gather fresh proof, run required just quality gates, and route runtime evidence when the claim needs it."
---

# Verification Before Completion

Use before claiming work is fixed, done, ready, or approved.

## Rule

Prove the exact claim against the binding objective and accepted reductions.
Do not finish on stale proof, narrower proof, or proof for a smaller invented
objective.

## Required References

- `references/quality-gate-selection.md`: choose static/test quality gate.
- `references/verification-evidence.md`: evidence shape.
- `references/runtime-proof-escalation.md`: when runtime proof is needed.
- `references/runtime-evidence-contract.md`: runtime-evidence verdict shape.

## Gate

Before completion:
1. name the exact claim
2. name the binding objective and accepted reductions
3. run the right fresh proof
4. map runtime-visible claims to entrypoint fidelity and runtime evidence
5. check touched owner/component integrity for non-trivial work
6. ensure review approvals match the claim

## Stop

Stop or narrow the claim when:
- proof is stale, missing, indirect, or narrower than the claim
- runtime-visible behavior lacks required runtime evidence
- entrypoint fidelity is adjacent/component-only for a broad user-flow claim
- final review or quality guard rejected or did not cover the claim
- residual gaps belong to the current objective

## Completion Note

Report verification command/artifact, runtime evidence when applicable, review
status, touched owner/component integrity, and residual risks or `none`.
