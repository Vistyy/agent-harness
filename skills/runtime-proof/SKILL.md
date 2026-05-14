---
name: runtime-proof
description: "Use for live-use runtime evidence mechanics, entrypoint fidelity, artifacts, and pass/reject/blocked verdicts after readiness-claim names the claim."
---

# Runtime Proof

Owns live-use validation mechanics. `../readiness-claim/SKILL.md` owns claim
completeness and final scope. Browser and mobile skills own platform mechanics.

## Rule

Runtime evidence uses the app, service, API, or operator path through a
faithful entrypoint and reports whether observed behavior supports the handed
readiness claim beyond code inspection, tests, and review approval.

This skill does not decide when runtime evidence is required. That requirement
comes from `../readiness-claim/SKILL.md`, project overlays, or the active route.

Runtime evidence is blocking when required. Return `reject`, `blocked`,
incomplete, or mis-scoped evidence to `readiness-claim`; completion waits for
fixed/re-proven evidence or an explicitly narrowed claim.

Visual-only UI design readiness does not require runtime evidence by default;
`design_judge` owns product-grade visual approval.

## Handoff

Name:

- binding objective and accepted reductions
- readiness claim and obligations checked
- entrypoint or recipe
- affected states, roles, data, devices, browsers, or viewports
- UI behavior risks, if claimed
- unproved boundaries, or `none`

Missing or narrower handoff returns `blocked`.

## Entrypoint Fidelity

- `real-entrypoint`: actual user/operator path
- `scripted-entrypoint`: project-supported command exercising the same boundary
- `adjacent-component`: nearby component or mocked boundary only
- `artifact-only`: screenshot, build output, or static artifact without live
  behavior

Broad readiness and user-flow claims need `real-entrypoint` unless
`readiness-claim` explicitly narrows the claim.

## Output

Report claim boundary, entrypoint fidelity, recipe, actions, artifact paths,
material logs/traces or `none observed`, verdict `pass | reject | blocked`,
and block impact.

Use `../webapp-testing/SKILL.md`, `../mobileapp-testing/SKILL.md`, or
`../testing-best-practices/SKILL.md` for browser, mobile, or persistent-test
mechanics.
