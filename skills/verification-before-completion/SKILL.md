---
name: verification-before-completion
description: "Use before any completion or fix claim to gather fresh proof, run required just quality gates, and route runtime evidence when the claim needs it."
---

# Verification Before Completion

Completion claims require fresh proof before saying work is fixed, done, ready,
or approved.

## Rule

Prove the exact claim against the binding objective and accepted reductions.
Do not finish on stale proof, narrower proof, or proof for a smaller invented
objective.

## Required References

- Read `references/verification-evidence.md` when evidence shape, artifact
  placement, or completion-note proof rows matter.
- Read `references/runtime-proof-escalation.md` when deciding whether runtime
  proof is required.
- Read `references/runtime-evidence-contract.md` when producing or reviewing a
  runtime-evidence verdict.

## Quality Gate Selection

Choose the smallest gate that proves the claim:
- harness/workflow changes: `just quality-fast` plus
  `agent-harness governance check --repo-root .`
- project code changes: project `just ... quality*` owner command when present
- test-only changes: affected tests and any test-doctrine validation
- docs-only changes: validation that checks those docs
- runtime-visible changes: static checks plus runtime evidence

Do not substitute a cheaper gate when the claim depends on broader behavior.

## Temporary Structural Checks

Path, import, location, or allowlist checks used during refactors are temporary
structural checks unless they verify durable behavior.

Rules:
- keep temporary structural checks out of persistent quality and runtime smoke
  gates
- store them in active execution state with owner, reason, removal trigger, and
  planned removal
- remove or archive them before closeout
- durable behavior checks stay in persistent quality and smoke gates

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
