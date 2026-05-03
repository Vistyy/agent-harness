---
name: runtime-proof
description: "Use for runtime-visible claim maps, runtime evidence handoffs, entrypoint fidelity, pass/reject/blocked verdict semantics, and blocking runtime findings."
---

# Runtime Proof

Owns runtime evidence policy. Browser and mobile skills own platform mechanics.

## Rule

Runtime evidence proves the binding objective plus accepted reductions. A
parent handoff that asks for a smaller claim is mis-scoped and must return
`blocked`.

Use runtime proof when the completion claim is user-visible, API-visible,
service-visible, integration-visible, or depends on live state.

Use `runtime_evidence` for non-trivial runtime-visible claims unless the claim
is tiny, local, and has no public-behavior or cross-boundary runtime risk.

Runtime evidence is blocking, not advisory. `reject`, `blocked`, incomplete, or
mis-scoped proof blocks broad completion unless the issue is fixed and
re-proven or the user explicitly accepts the narrowed claim.

## Runtime Claim Map

Every runtime handoff names:
- binding objective
- accepted reductions
- exact runtime claim
- target entrypoint or recipe
- affected surfaces, states, roles, data, devices, browsers, or viewports
- design anchors when UI quality is claimed
- unproved boundaries, or `none`

## Entrypoint Fidelity

- `real-entrypoint`: actual user/operator path.
- `scripted-entrypoint`: project-supported command that exercises the same
  boundary.
- `adjacent-component`: nearby component or mocked boundary only.
- `artifact-only`: screenshot, build output, or static artifact without live
  behavior.

Broad readiness, end-to-end, redesign, or user-flow claims require
`real-entrypoint` or an accepted narrower claim. Simulated or adjacent proof
must name the unproved boundary.

## Verdicts

- `pass`: observed runtime behavior satisfies the runtime claim map.
- `reject`: observed behavior contradicts the runtime claim, design anchors,
  public behavior, or accepted quality bar.
- `blocked`: recipe, data, environment, missing anchors, or mis-scoped handoff
  prevents proof.

## Evidence

Reviewed evidence must be small enough to inspect and complete enough to prove
the claim. Artifact minimalism never justifies claim shrinking.

Runtime evidence reports:
- claim boundary covered
- entrypoint fidelity
- runtime recipe used
- actions executed
- evidence artifact paths
- material logs/traces or `none observed`
- verdict and block impact
- screenshot-backed checks for UI quality claims

## Platform Owners

- Use `../webapp-testing/SKILL.md` for browser proof mechanics, Playwright
  vehicles, browser sessions, screenshots, and console/network handling.
- Use `../mobileapp-testing/SKILL.md` for emulator/device mechanics, Dart MCP,
  adb, widget trees, logs, screenshots, and device lifecycle.
- Use `../testing-best-practices/SKILL.md` when deciding whether runtime proof
  should become a durable persistent test.
