---
name: svelte-code-writer
description: "Create, edit, or analyze Svelte `.svelte`, `.svelte.ts`, and `.svelte.js` files with official docs lookup, autofixer workflow, and core Svelte posture. Use whenever Svelte source changes or Svelte-specific analysis is needed. Use this skill for Svelte mechanics only; it does not own product design, Tailwind policy, or runtime proof."
---

# Svelte Code Writer

Owns Svelte file work, official docs lookup, autofixer use, and core Svelte
posture. Do not maintain copied local framework docs here.

## Tooling

Prefer the built-in Svelte MCP tools in this environment:
- `mcp__svelte__list_sections`
- `mcp__svelte__get_documentation`
- `mcp__svelte__svelte_autofixer`
- `mcp__svelte__playground_link`

If operating outside the MCP-integrated flow, the equivalent CLI entrypoint is
`npx @sveltejs/mcp`.

## Required Workflow

1. Start with `list_sections` and identify sections relevant to the requested
   change.
2. Fetch only the needed documentation sections.
3. Run `svelte_autofixer` on every Svelte component or module you create, edit,
   or analyze before finalizing.
4. Ask about a playground link only when returning Svelte code directly rather
   than editing repo files.

Use official Svelte docs for version-sensitive API details.

## Svelte Posture

- Use modern Svelte/runes patterns for new code.
- Treat props as changing values; derive from them instead of computing once.
- Prefer `$derived` for computed values.
- Reserve `$effect` for external synchronization.
- Keep route components thin; route state authority belongs behind local
  facades or screen models when behavior grows.
- Prefer scoped state/context over shared module state when SSR or per-surface
  ownership matters.
- Prefer keyed each blocks and stable semantic keys.
- Use CSS custom properties for JS-to-CSS values and component theming.
- Avoid legacy syntax in new code unless the surrounding file is intentionally
  legacy and migration is out of scope.

## Anti-Patterns

- state updates inside `$effect` when `$derived`, event handlers, or function
  bindings model the behavior
- shared module state as hidden workflow owner
- route files parsing, normalizing, and owning nested transport or domain
  payloads
- index keys for mutable lists
- `:global` styling when component API or CSS custom properties can express the
  contract
- local framework docs copied into this skill instead of looked up through
  official docs
