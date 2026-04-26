## Snippets

Use snippets for reusable markup chunks inside one component.
Render them with `{@render ...}` or pass them to child components.

Basic shape:

```svelte
{#snippet name()}...{/snippet}
{#snippet name(param1, param2)}...{/snippet}
```

Good fit:

- repeated markup with small parameter changes
- component content props
- `children`-style composition without old slot API

Snippets can use default parameters and destructuring.
They cannot use rest parameters.

## Scope

Snippets may be declared anywhere in component template.

Rules:

- snippet can read values from outer lexical scope
- snippet is visible to siblings and nested children in same lexical scope
- snippet is not visible outside that lexical scope
- snippets may call themselves or each other recursively when scope allows it

## Passing Snippets To Components

### Explicit Props

Snippet is a normal value, so pass it like any other prop.

```svelte
<Table data={fruits} {header} {row} />
```

### Implicit Props

Snippet declared directly inside component tags becomes prop on that component.

```svelte
<Table data={fruits}>
	{#snippet header()}...{/snippet}
	{#snippet row(d)}...{/snippet}
</Table>
```

### Implicit `children`

Content inside component tags that is not snippet declaration becomes
`children` snippet.

Use:

```svelte
<Button>click me</Button>
```

Rendered inside component with:

```svelte
<button>{@render children?.()}</button>
```

Avoid regular prop named `children` when component also receives inline content.

### Optional Snippet Props

Use optional chaining for no-op render:

```svelte
{@render children?.()}
```

Or `#if` for fallback UI:

```svelte
{#if children}
	{@render children()}
{:else}
	fallback content
{/if}
```

## Typing

Import `Snippet` from `svelte`.

Rules:

- generic form is `Snippet<[Param1, Param2]>`
- type argument is tuple because snippet may take multiple parameters
- use generics when snippet parameter type should match another prop like
  `data: T[]`

## Exporting

Top-level snippets in `.svelte` file may be exported from `<script module>` if
they do not depend on non-module `<script>` state, directly or indirectly.

## When Not To Use

Do not use snippet when:

- markup should become standalone component
- logic/state boundary matters more than markup reuse
- reuse must cross many unrelated components

Use snippet when reuse is local and markup-heavy.
