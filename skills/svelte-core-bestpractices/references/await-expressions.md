## Await Expressions

Svelte `5.36+` allows `await` in three places:

- top-level component `<script>`
- inside `$derived(...)`
- inside markup

This is experimental. Enable `experimental.async` in Svelte config.

```js
export default {
	compilerOptions: {
		experimental: {
			async: true,
		},
	},
};
```

Expected future: flag goes away in Svelte `6`.

## Synchronized Updates

When `await` depends on state, Svelte holds visible UI update until async work
resolves so UI does not show inconsistent intermediate state.

Good mental model:

- state changes start async work
- visible update lands when awaited value for that state is ready
- fast later updates may overtake slower earlier updates

## Concurrency

Independent markup `await` expressions run in parallel.

```svelte
<p>{await one()}</p>
<p>{await two()}</p>
```

Sequential `await` in normal JS still behaves like normal JS.

Special case:

- independent `$derived(await ...)` values initialize sequentially once
- later updates run independently

If setup forms waterfall, expect `await_waterfall` warning.

## Loading State

Use `<svelte:boundary>` with `pending` snippet for first-load placeholder UI.

Use `$effect.pending()` for later async work after boundary has already
resolved once.

Use `settled()` when code must wait until current async-driven update finishes.

Use `tick()` when an immediate UI flag must render before later awaited work is
grouped in same update.

## Error Handling

Error in `await` expression bubbles to nearest error boundary.

## SSR

Async SSR is supported through `await render(...)`.

Rules:

- await result from `svelte/server` render API
- frameworks like SvelteKit do this for you
- boundary `pending` content may render during SSR while inner content waits
- awaited expressions outside pending boundary resolve before render returns

Streaming is future direction, not current assumption.

## Forking

`fork(...)` in `5.42+` lets framework or app start likely-near-future async
work early.

Good fit:

- preload on hover/focus intent
- menu/dialog/content expected to open soon

Pattern:

- create fork on intent
- `discard()` if user backs out
- `commit()` if user follows through

## Caveats

- feature is experimental
- exact semantics may still change before major release
- effect ordering changes when async mode is on
- block effects can run before `$effect.pre` / `beforeUpdate` in same component

Use this feature only when async-in-component model is clearer than explicit
loading state plumbing.
