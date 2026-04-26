---
name: svelte-core-bestpractices
description: Broad companion guidance for writing fast, robust, modern Svelte code. Use alongside `svelte-code-writer` whenever non-obvious framework choices, reactivity, styling, or integration patterns matter.
---

# Svelte Core Best Practices

## Ownership

- `svelte-code-writer` owns doc lookup, autofixer use, tooling-entry workflow
- this skill owns durable Svelte framework guidance and anti-pattern avoidance
- `user-apps-design` owns product-facing UI direction, parity, copy rules
- `system-boundary-architecture` owns frontend layer ownership, import
  direction, public-surface hygiene, route-shell boundaries, state authority,
  and facade/screen-model boundaries

## `$state`

Use `$state` only for variables that must drive template output, `$effect`, or
`$derived`.

Rules:

- objects and arrays in `$state(...)` become deeply reactive proxies
- that proxying has overhead
- if large object is only reassigned, prefer `$state.raw`
- API responses are common `$state.raw` candidate

## `$derived`

Compute from state with `$derived`, not `$effect`.

```js
let square = $derived(num * num);
```

If expression is too complex, use `$derived.by`.

Rules:

- `$derived` takes expression, not function
- derived values are writable
- object or array returned from `$derived` is not made deeply reactive
- if rare deep reactivity is needed inside `$derived.by`, use `$state` there

## `$effect`

Effects are escape hatch. Avoid when better model exists. Especially avoid state
updates inside effects.

Use instead:

- `{@attach ...}` for external library sync like D3
- direct event handler or function binding for interaction-driven logic
- `$inspect` for logging and debugging
- `createSubscriber` for observing external signals

Never wrap effect body in `if (browser)`. Effects do not run on server.

## `$props`

Treat props as changing values.

Use `$derived` for values computed from props.

```js
let { type } = $props();
let color = $derived(type === 'danger' ? 'red' : 'green');
```

Do not compute once from prop and assume it stays current.

## `$inspect.trace`

Use `$inspect.trace(label)` as first line of `$effect`, `$derived.by`, or helper
they call when debugging reactivity.

Use it to see dependencies and which one triggered update.

## Events

Any element attribute starting with `on` is event listener.

Use:

- `onclick={...}` on elements
- `<svelte:window>` for `window`
- `<svelte:document>` for `document`

Avoid `onMount` or `$effect` for listener setup.

## Snippets

Use [snippets](references/snippet.md) for reusable template chunks rendered with
`{@render ...}` or passed as props.

Rules:

- declare snippets in template
- top-level snippets are visible in `<script>`
- state-free top-level snippets can be exported from `<script module>`

## Each Blocks

Prefer keyed each blocks.

Rules:

- key must uniquely identify item
- never use index as key
- avoid destructuring when item must be mutated with bindings

## JS Values In CSS

If JS value is needed in CSS, set CSS custom property with `style:`.

```svelte
<div style:--columns={columns}>...</div>
```

Then use `var(--columns)` in `<style>`.

## Styling Child Components

Scoped CSS means parent usually should style child through CSS custom
properties.

Prefer CSS variables first.
Use `:global` only when child cannot be controlled normally, like third-party
component.

## Context

Prefer context over shared module state when state should be scoped to part of
app.

Reasons:

- avoids SSR cross-user leakage
- keeps state local to surface that needs it

Use `createContext` instead of `setContext` and `getContext` when possible.

For web route work:

- prefer feature-local state and facade boundaries over shared module state
- do not let route component or shared singleton become hidden workflow owner
  just because it already holds nearby data

## Async Svelte

On Svelte `5.36+`, await expressions and hydratable flow are available if
`experimental.async` is enabled in `svelte.config.js`.

Treat them as usable, but not fully stable.

See:

- [await expressions](references/await-expressions.md)
- [hydratable](references/hydratable.md)

## Avoid Legacy Features

For new code:

- use runes mode
- use `$state` instead of implicit reactivity
- use `$derived` and `$effect` instead of `$:`
- use `$props` instead of `export let`, `$$props`, `$$restProps`
- use `onclick={...}` instead of `on:click={...}`
- use `{#snippet ...}` and `{@render ...}` instead of slots, `$$slots`,
  `<svelte:fragment>`
- use `<DynamicComponent>` instead of `<svelte:component this={...}>`
- use imported self component instead of `<svelte:self>`
- use classes with `$state` fields instead of stores when sharing reactivity
  between components
- use `{@attach ...}` instead of `use:action`
- use clsx-style arrays and objects in `class`, not `class:`
