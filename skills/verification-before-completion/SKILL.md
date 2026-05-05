---
name: verification-before-completion
description: "Use before any completion or fix claim to bind the final claim to fresh proof, required runtime evidence, review coverage, and residual risk."
---

# Verification Before Completion

Owns final completion claim gating. Review approval scope, runtime verdicts,
and platform mechanics stay with their owner skills.

Completion claims require fresh proof against the binding objective before
saying work is fixed, done, ready, or approved.

## Rule

The final claim cannot exceed the binding objective, accepted reductions, fresh
proof, runtime evidence, and review coverage.

Broad product-facing UI design readiness also requires `design_judge` `pass`
covering the same screenshots/contact sheets, design anchors, states,
viewports, and devices as the final claim.

Compare completion to the original objective plus accepted reductions, not to
the implemented slice, diff summary, reviewer prompt, or handoff wording.

## Required References

- Read `../runtime-proof/SKILL.md` when the claim is runtime-visible, uses
  runtime evidence, or needs entrypoint fidelity.
- Read `../just-recipe-routing/SKILL.md` when choosing quality or proof
  commands.
- Read `../code-review/SKILL.md` when review coverage or approval scope matters.
- Read `../user-apps-design/SKILL.md` when product UI design readiness is part
  of the claim.

## Gate

Before completion:
1. name the binding objective and accepted reductions
2. name the exact final claim
3. run fresh owner-selected proof
4. include runtime evidence when runtime-visible behavior is claimed
5. include `design_judge` `pass` when broad product UI design is claimed
6. confirm required review covers the same claim
7. report residual risks or `none`

## Stop

Stop or narrow the claim when:
- proof is stale, missing, indirect, or narrower than the claim
- runtime evidence is required but missing, rejected, blocked, incomplete, or
  mis-scoped
- broad product UI design readiness is claimed but `design_judge` is missing,
  rejected, blocked, stale, or narrower than the claim
- tests, code review, or approval history are offered as substitutes for
  required runtime evidence
- review rejected or did not cover the binding objective
- residual gaps belong to the current objective

## Completion Note

Report proof command or artifact, runtime verdict when applicable, review
status when required, and residual risks or `none`.
