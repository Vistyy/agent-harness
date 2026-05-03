---
name: svelte-core-bestpractices
description: "Use with Svelte code work when reactivity, route state, styling boundaries, SSR-safe state, or code-shape posture matters."
---

# Svelte Core Best Practices

## Durable Posture

- Use modern Svelte/runes patterns for new code.
- Treat props as changing values; derive from them instead of computing once.
- Prefer `$derived` for computed values and reserve `$effect` for external
  synchronization.
- Keep route components thin; route state authority belongs behind local
  facades or screen models when behavior grows.
- Prefer scoped state/context over shared module state when SSR or per-surface
  ownership matters.
- Prefer keyed each blocks and stable semantic keys.
- Use CSS custom properties for JS-to-CSS values and component theming.
- Avoid legacy syntax in new code unless the surrounding file is intentionally
  legacy and migration is out of scope.

Use official Svelte docs for version-sensitive API details.

## Reference Map

Load only the reference needed for the current choice:
- reactivity, runes, and state ownership: `references/svelte-reactivity.md`
- snippets and render tags: `references/snippet.md`,
  `references/@render.md`
- external library synchronization: `references/@attach.md`
- binding edge cases: `references/bind.md`
- keyed list behavior: `references/each.md`
- debugging reactive dependencies: `references/$inspect.md`

If a local reference conflicts with official docs, follow official docs and
update or ignore the stale local reference.

## Anti-Patterns

- state updates inside `$effect` when `$derived`, event handlers, or function
  bindings model the behavior
- shared module state as hidden workflow owner
- route files parsing, normalizing, and owning nested transport/domain payloads
- index keys for mutable lists
- `:global` styling when CSS custom properties or component API can express
  the contract
- local framework docs copied into this skill instead of looked up through
  official docs
