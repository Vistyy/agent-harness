---
name: user-apps-design
description: "Use for end-user web/mobile UI direction: parity, composition, hierarchy, density, UX state, and copy posture; route mechanics and runtime proof to owners."
---

# User Apps Design

Use for end-user visible UI changes in web or mobile apps.

Owns product-facing UI direction, parity decisions, composition quality, and
copy posture. Project strategy, language policy, app paths, and delivery timing
stay in the project overlay.

## Routing

Start here, then add only what matches:

- `tailwind-design-system` for web implementation mechanics
- `mobile-design` for mobile platform constraints, accessibility, touch, runtime
  validation
- `flutter-expert` for Flutter implementation mechanics

Do not create parallel design decision tracks downstream.

## Read First

- project overlay docs for surface discovery, product language, delivery
  timing, design archetypes, and design-fidelity governance when present
- `references/parity-dimensions.md`
- `references/atomic-design.md`
- `references/text-constraints.md`

Do not continue until you can restate the relevant invariants.

## Scope

In:

- screen, layout, component styling and composition
- shell or nav hierarchy and density
- empty, loading, error state UX
- end-user copy and microcopy
- cross-client parity decisions for UX behavior and interaction posture
- web-first handoff readiness and mobile follow-up assumptions

Out:

- API contracts, backend semantics, auth/session internals
- framework mechanics once direction is set
- mobile platform mechanics after direction is set

## Quality Bar

- Reject any surface matching project design-fidelity anti-patterns.
- Reject monolithic single-scroll editing surfaces when stateful sectioning is
  needed.
- Reject inconsistent nav semantics between web and mobile.
- Reject browser-native confirm/prompt patterns in end-user web flows when
  in-app patterns exist.
- Reject hardcoded UX placeholders like fixed recent-search tags.
- Accept only when hierarchy is intentional, density fits the target, parity is
  explicit, reusable composition beats route-local one-offs, and relevant IA
  patterns have `adopt` or `reject` rationale.

## Taste-Pressure Lens

Use taste pressure as a bounded design-quality lens, not a second skill or
scorecard.

- Route visual ambition through the approved archetype, surface brief,
  accessibility, parity, product scope, performance, and runtime proof.
- Prefer clarity, density, accessibility, and consistency on transactional
  app surfaces when cinematic novelty would weaken the task.
- Use aggressive or high-variance composition only when the approved archetype
  and surface brief explicitly call for it.
- When archetype and brief leave visual density, motion intensity, or
  composition variance open, require those dials to be named before editing.
- Use the project design-fidelity governance reference for scoring and anti-pattern names.

## Required Loop

1. Satisfy the project-owned discovery gate when UI quality or product direction is in scope. If required context is missing, stop.
2. Read the project design-implementation posture when the change needs an
   implementation loop or handoff posture.
3. Choose one approved archetype or record a justified exception before
   editing.
4. Write parity matrix before editing: must-match behavior, state, copy, and
   component semantics; allowed divergence is layout/navigation structure. For
   staged cross-client delivery, record follower-surface match points and avoid
   browser-only assumptions.
5. Map route-level work to atomic layers and identify reuse/new reusable blocks.
6. Run density/layout pass before polish: remove oversized shell chrome and
   improve scanability/spacing rhythm.
7. For IA-affecting changes, evaluate relevant established patterns and record
   `adopt` or `reject` in planning artifacts.
8. When claiming hierarchy, density, shell, or UI quality, define `3-7`
   design-intent anchors per the project surface-discovery contract.
9. Use existing project tokens, components, patterns, and design-system
   contracts. No ad hoc styling values.
10. For runtime UI proof, route to `webapp-testing` or `mobileapp-testing` and
    use the project design-fidelity governance terms for verdicts.
11. For web route ownership changes, route to `system-boundary-architecture`;
    this skill does not own route/state authority doctrine.

## Cross-Skill Routing

- `tailwind-design-system`: shared web Tailwind components and tokens
- `mobile-design`: iOS/Android constraints, accessibility, touch, mobile
  validation
- `flutter-expert`: Flutter/Dart implementation mechanics
- `webapp-testing` or `mobileapp-testing`: runtime UI behavior claims
- `system-boundary-architecture`: route/state authority, shared frontend
  boundaries, and ownership changes

## If Source Of Truth Is Missing

Do not invent local workaround.

If missing truth is app main draw, shell ownership, or core loop, stop bounded
surface work and route into foundation-reset discovery per
the project surface-discovery contract.

1. Record exact missing or contradictory rule.
2. Point to closest doc that should own it.
3. Propose smallest source-of-truth update.
4. Wait for confirmation before changing UI behavior.
