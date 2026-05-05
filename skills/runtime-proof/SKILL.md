---
name: runtime-proof
description: "Use when a non-trivial runtime-visible claim needs live-use proof beyond tests/reviews; owns claim maps, entrypoint fidelity, verdicts, and blocking runtime findings."
---

# Runtime Proof

Owns runtime evidence policy. Browser and mobile skills own platform mechanics.
`../verification-before-completion/SKILL.md` owns final completion claim
gating.

## Rule

Runtime evidence is live-use validation. It uses the app, service, API, or
operator path through a faithful entrypoint and verifies the claimed behavior
actually works beyond code inspection, tests, and review approval.

Runtime evidence proves the binding objective plus accepted reductions. A
handoff for a smaller claim without accepted reduction is mis-scoped and
returns `blocked`.

Runtime evidence is required for non-trivial runtime-visible claims unless the
claim is tiny, local, and has no public-behavior or cross-boundary runtime risk.
Durable e2e tests may supply runtime artifacts only when they exercise the same
claim through a faithful entrypoint and leave inspectable evidence.

Runtime evidence is blocking, not advisory. `reject`, `blocked`, incomplete,
or mis-scoped proof blocks broad completion until fixed and re-proven or
explicitly narrowed by the user.

For UI-quality claims, runtime evidence proves live behavior and screenshot
artifact sufficiency for design handoff. Product-grade UI design approval
requires `design_judge` `pass`.

For broad UI claims, runtime evidence reports anti-generic report artifact
sufficiency for `design_judge`; it does not decide design quality.

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
`real-entrypoint` unless the claim is explicitly narrowed. Simulated or
adjacent proof names the unproved boundary.

## Verdicts

- `pass`: observed runtime behavior satisfies the runtime claim map.
- `reject`: observed behavior contradicts the runtime claim, design anchors,
  public behavior, or accepted quality bar.
- `blocked`: recipe, data, environment, missing anchors, or mis-scoped handoff
  prevents proof.

## Evidence

Evidence must be small enough to inspect and complete enough to prove the
claim. Artifact minimalism never justifies claim shrinking.

Report claim boundary, entrypoint fidelity, recipe, actions, artifact paths,
material logs/traces or `none observed`, verdict, block impact, and
screenshot-backed checks for UI quality claims.

UI runtime reports name screenshot/contact-sheet paths, screen/state,
viewport/device, freshness/scope, and whether artifacts are sufficient for
`design_judge` handoff. Missing, stale, cropped, or claim-mismatched UI
artifacts return `blocked`.

When required, UI runtime reports name the anti-generic source, artifact, and
handoff sufficiency. Missing or detector-only design approval evidence is
insufficient for broad UI design readiness.

## Platform Owners

- Use `../webapp-testing/SKILL.md` for browser proof mechanics, Playwright
  vehicles, browser sessions, screenshots, and console/network handling.
- Use `../mobileapp-testing/SKILL.md` for emulator/device mechanics, Dart MCP,
  adb, widget trees, logs, screenshots, and device lifecycle.
- Use `../testing-best-practices/SKILL.md` when deciding whether runtime proof
  should become a durable persistent test.
