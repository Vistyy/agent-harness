# `hydratable`

Use `hydratable` when server already computed async or unstable value and hydration must reuse it instead of recomputing it.

## Problem

Plain top-level `await` runs on server, then runs again during hydration.
That blocks hydration and can repeat expensive or unstable work.

```svelte
<script>
	import { getUser } from 'my-database-library';

	const user = await getUser();
</script>

<h1>{user.name}</h1>
```

## Fix

Wrap value in `hydratable`.

```svelte
<script>
	import { hydratable } from 'svelte';
	import { getUser } from 'my-database-library';

	const user = await hydratable('user', () => getUser());
</script>

<h1>{user.name}</h1>
```

Behavior:
- server runs function and serializes result
- hydration reuses serialized value instead of rerunning function
- later client calls run function normally

Typical uses:
- server-fetched data
- random values that must stay stable across hydration
- time-based values that must not jump during hydration

Library authors should prefix keys to avoid conflicts.

## Serialization

Return value must be serializable by Svelte's serializer.
This includes more than JSON, for example `Map`, `Set`, `URL`, `BigInt`, and promises.

```svelte
<script>
	import { hydratable } from 'svelte';

	const values = hydratable('random', () => ({
		one: Promise.resolve(1),
		two: Promise.resolve(2),
	}));
</script>

{await values.one}
{await values.two}
```

## CSP

`hydratable` injects inline `<script>` into rendered `head`.

For dynamic SSR, provide `nonce` to `render` and use same nonce in CSP header.

For static HTML, use CSP hashes instead.

Rule:
- prefer `nonce` when dynamic per-response rendering is available
- use hashes for static generation
