---
name: user-apps-design
description: Primary design-implementation skill for end-user web/mobile UI work; use to turn references/contracts into a high-quality, non-amateur UI outcome with explicit parity decisions.
---

# User Apps Design

Use for end-user visible UI changes in web or mobile applications.

Project-specific product strategy, language policy, app paths, and delivery timing stay in the project overlay.

Owns product-facing UI direction, parity decisions, composition bar, and
copy/contract posture.

## Routing

Start here, then add only what matches:

- `tailwind-design-system` for web implementation mechanics
- `mobile-design` for mobile platform constraints, accessibility, touch, runtime
  validation
- `flutter-expert` for Flutter implementation mechanics

Do not create parallel design decision tracks in downstream skills.

## Read First

- project overlay docs for surface discovery, product language, delivery timing, design archetypes, and design-fidelity governance when the project provides them
- `references/parity-dimensions.md`
- `references/atomic-design.md`
- `references/text-constraints.md`
- `../system-boundary-architecture/references/web-frontend-boundaries.md`
  when shared web layer ownership, import direction, or public-surface hygiene
  changes in web app code
- `../system-boundary-architecture/references/web-route-and-state-boundary-doctrine.md`
  when route shells, screen-facing state authority, or facade/screen-model
  boundaries change in web app code

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

Reject:

- any surface matching fixed anti-pattern families from
  `the project design-fidelity governance reference`
- monolithic single-scroll editing surfaces when stateful sectioning is needed
- inconsistent nav semantics between web and mobile
- browser-native confirm or prompt patterns in end-user web flows when in-app
  patterns exist
- hardcoded UX placeholders like fixed recent-search tags

Accept only when:

- hierarchy is intentional and scannable
- component density matches desktop, tablet, or mobile target
- parity matrix is explicit
- reusable atoms, molecules, patterns beat route-local one-offs
- relevant IA patterns were evaluated with explicit `adopt` or `reject`
  rationale

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

## Non-Negotiable Rules

1. No ad hoc styling values.
2. Use existing project tokens, components, and patterns from the project UI entrypoint.
3. End-user copy follows the project-owned language policy.
4. Preserve declared UX invariants unless spec changes them.
5. Choose one approved archetype from
   the project design-fidelity archetype reference or record a justified exception
   before design-shaping execution.
6. Consume the scorecard and anti-pattern taxonomy from
   the project design-fidelity governance reference; do not restate them as local source of
   truth.
7. Follow `references/parity-dimensions.md` for parity semantics. Do not restate it here.
8. Follow `references/atomic-design.md` for composition semantics. Do not
   restate it here.
9. Follow `references/text-constraints.md` for length, overflow, truncation,
   and inline-highlight posture. Do not restate it here.
10. Follow
   the project end-user copy governance reference
   for explanatory-text posture. Do not restate it here.

## Required Loop

1. Satisfy the project-owned discovery gate when UI quality or product direction is in scope. If required context is missing, stop.
2. Read the project design-implementation posture when the change needs an
   implementation loop, reviewed runtime screenshot set, or handoff posture.
3. Choose one approved archetype or record a justified exception before
   editing.
4. Write parity matrix before editing:
   - must-match: behavior, state, copy, component semantics
   - allowed divergence: layout and navigation structure
   - for staged cross-client delivery, note what the follower surface must later match
5. Map route-level work to atomic layers:
   - what is reused
   - what new reusable blocks are needed
6. Run density and layout pass before polish:
   - remove oversized shell chrome
   - improve scanability and spacing rhythm
7. For IA-affecting change, evaluate relevant established patterns and record
   `adopt` or `reject` in planning artifacts.
8. When claiming hierarchy, density, shell, or UI quality, define `3-7`
   design-intent anchors per the project surface-discovery contract.
9. Apply styling only through existing design-system contracts.
10. Validate in runtime before claiming UI quality. When claims need reviewed
    proof, use the targeted runtime screenshot set from
    the project design-implementation posture. If evidence fails, use the remediation
    handback fields from the owner doc and the dimension/anti-pattern names
    from the project design-fidelity governance reference.
11. For web route work, keep route a thin shell. If route becomes workflow
    owner, stop and apply web route/state doctrine.

## Cross-Skill Routing

- `tailwind-design-system`: shared web Tailwind components and tokens
- `mobile-design`: iOS/Android constraints, accessibility, touch, mobile
  validation
- `flutter-expert`: Flutter/Dart implementation mechanics
- `webapp-testing` or `mobileapp-testing`: runtime UI behavior claims

## Pre-Change Checklist

- [ ] required docs read
- [ ] discovery gate satisfied
- [ ] implementation posture read when implementation evidence is in scope
- [ ] approved archetype chosen or exception justified
- [ ] parity matrix written or confirmed
- [ ] staged cross-client obligations are explicit and not built on browser-only
      assumptions
- [ ] route-level composition is not monolithic box stack
- [ ] fixed anti-pattern families are not present
- [ ] IA pattern evaluation recorded when IA scope changes
- [ ] design-intent anchors exist for UI-quality claims
- [ ] no ad hoc style values
- [ ] user-facing strings follow the project language policy
- [ ] parity requirements satisfied
- [ ] atomic composition requirements satisfied
- [ ] remediation handback response path understood for failed evidence
- [ ] verification path exists

## If Source Of Truth Is Missing

Do not invent local workaround.

If missing truth is app main draw, shell ownership, or core loop, stop bounded
surface work and route into foundation-reset discovery per
the project surface-discovery contract.

1. Record exact missing or contradictory rule.
2. Point to closest doc that should own it.
3. Propose smallest source-of-truth update.
4. Wait for confirmation before changing UI behavior.
