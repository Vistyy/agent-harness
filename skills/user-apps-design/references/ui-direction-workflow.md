# UI Direction Workflow

Use before planning or editing end-user UI. This reference owns scope, quality
bar, taste pressure, required loop, and missing-source-of-truth handling.

## Scope

In:
- screen, layout, component styling, and composition
- shell or nav hierarchy and density
- empty, loading, error state UX
- end-user copy and microcopy
- `DESIGN.md` or equivalent project design-contract use when present
- cross-client parity decisions for UX behavior and interaction posture
- web-first handoff readiness and mobile follow-up assumptions

Out:
- API contracts, backend semantics, and auth/session internals
- framework mechanics before UI direction is set
- mobile platform mechanics before cross-platform UI direction is set
- browser/mobile runtime proof mechanics and evidence reports

## Quality Bar

For user-facing products, functional correctness is not enough. End-user UI must
feel intentionally designed for the project's domain, audience, and product
posture: visually composed, interaction-coherent, and rewarding to return to in
repeated use. Treat visual quality, interaction feel, and repeated-use delight as
product quality, not optional polish.

The global harness owns that requirement only. Each project owns the observable
meaning through design anchors, archetypes, scorecards, runtime proof
expectations, and anti-patterns. If a user-facing UI change lacks those anchors,
stop and request the smallest project-owned source-of-truth update instead of
accepting generic functional UI.

Reject:
- project design-fidelity anti-patterns
- user-facing UI that is only technically correct or generic, with no
  project-owned design anchors proving intentional hierarchy, interaction feel,
  visual character, and repeated-use quality
- monolithic single-scroll editing surfaces when stateful sectioning is needed
- inconsistent nav semantics between web and mobile
- browser-native confirm/prompt patterns in end-user web flows when in-app
  patterns exist
- hardcoded UX placeholders like fixed recent-search tags

Accept only when hierarchy is intentional, density fits the target, parity is
explicit, reusable composition beats route-local one-offs, and relevant IA
patterns have `adopt` or `reject` rationale.

## Taste Pressure

Route visual ambition through approved archetype, surface brief, accessibility,
parity, product scope, performance, and runtime proof.

Prefer clarity, density, accessibility, and consistency on transactional app
surfaces when cinematic novelty would weaken the task.

Use aggressive or high-variance composition only when approved archetype and
surface brief explicitly call for it.

When archetype and brief leave density, motion, or variance open, name those
dials before editing.

## Required Loop

1. Satisfy project-owned discovery gate when UI quality or product direction is
   in scope. Stop if required context is missing.
2. Read project `DESIGN.md` or equivalent design contract when present, then
   project design-implementation posture when the change needs an
   implementation loop or handoff posture.
3. Choose one approved archetype or record a justified exception before editing.
4. Write parity matrix before editing: must-match behavior, state, copy, and
   component semantics; allowed divergence is layout/navigation structure.
5. Map route work to atomic layers and identify reuse/new reusable blocks.
6. For non-trivial visual redesigns or new end-user surfaces, use an approved
   or inspected whole-screen composition, prototype, or reference before
   product-code implementation. Inspect it as a complete screen against project
   design anchors. Component, token, or rule compliance alone is insufficient.
   If the whole-screen composition fails, implementation is blocked; do not
   iterate in product code from a bad composition.
7. Run density/layout pass before polish: remove oversized shell chrome and
   improve scanability/spacing rhythm.
8. For IA-affecting changes, evaluate established patterns and record `adopt`
   or `reject` in planning artifacts.
9. When claiming hierarchy, density, shell, or UI quality, define `3-7`
   design-intent anchors per project surface-discovery contract.
10. Use existing project tokens, components, patterns, and design-system
   contracts. No ad hoc styling values.
11. Runtime UI proof must use project design-fidelity governance verdict terms.
12. Web route ownership changes must close route/state authority before editing.

## Missing Source Of Truth

If missing truth is app main draw, shell ownership, or core loop, stop bounded
surface work and route into foundation-reset discovery.

1. Record the missing or contradictory rule.
2. Point to the closest doc that should own it.
3. Propose the smallest source-of-truth update.
4. Wait for confirmation before changing UI behavior.
