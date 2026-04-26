---
name: tailwind-design-system
description: Use when implementing or refactoring Tailwind CSS v4 styles to enforce non-obvious, stable conventions (CSS-first configuration, class detection, variants, theming, and maintainable component patterns) across the web app.
---

# Tailwind Design System

Use for Tailwind v4 implementation mechanics after design direction is already decided.

Prerequisite for end-user surfaces:
- apply `user-apps-design` first

Do not use this skill to re-decide product design direction.

## Scope

In scope:
- Tailwind v4 configuration and source detection
- tokens and theming conventions
- component and variant authoring patterns
- utility/custom CSS integration

Out of scope:
- app UX policy and language constraints
- browser runtime behavior claims

## Tailwind v4 Invariants

1. CSS-first config
   - define theme tokens with `@theme`
   - use `@config` only for legacy JS config migration
2. explicit source detection
   - dynamic class interpolation is unsafe
   - map props to complete class strings present in source
   - in multi-package repos, use `@source`
3. safelisting via `@source inline()`
   - do not rely on old `safelist`
4. v4 variant semantics
   - stack variants left to right
   - `important` is suffix style like `bg-red-500!`
   - prefixes behave like variants when configured
5. prefer CSS variables over `theme()`
6. use `@apply` sparingly
   - prefer utilities in markup
   - in CSS modules or Svelte/Vue style blocks, import context via `@reference` before `@apply`
7. do not stack Tailwind with Sass/Less/Stylus
8. respect v4 browser baseline
   - Safari `16.4+`
   - Chrome `111+`
   - Firefox `128+`

## Repo Locks

- prefer semantic token aliases over raw palette classes in product components
- document arbitrary values briefly in review context when they matter
- keep variant APIs explicit and type-safe in shared UI primitives

## Checklist

- [ ] config is CSS-first
- [ ] no unsafe dynamic class construction
- [ ] variants and modifiers follow v4 syntax
- [ ] `@apply` usage is minimal and context-aware
- [ ] source detection/safelisting uses v4 directives
- [ ] repo conventions are respected or explicitly waived

## References

- https://tailwindcss.com/docs/functions-and-directives
- https://tailwindcss.com/docs/detecting-classes-in-source-files
- https://tailwindcss.com/docs/upgrade-guide
- https://tailwindcss.com/docs/compatibility

## Related Skills

- `user-apps-design`
- `webapp-testing`
