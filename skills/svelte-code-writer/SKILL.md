---
name: svelte-code-writer
description: "Use whenever creating, editing, or analyzing Svelte `.svelte`, `.svelte.ts`, or `.svelte.js`; includes official docs lookup and autofixer workflow."
---

# Svelte Code Writer

## Capability

- Svelte/SvelteKit documentation lookup
- `svelte_autofixer` usage before finalizing Svelte code
- choosing the right tool inputs for file-based Svelte work

Load `svelte-core-bestpractices` alongside this skill when reactivity, event
handling, styling, state sharing, or other non-obvious framework choices matter.

## Tooling Contract

Prefer the built-in Svelte MCP tools in this environment:
- `mcp__svelte__list_sections`
- `mcp__svelte__get_documentation`
- `mcp__svelte__svelte_autofixer`
- `mcp__svelte__playground_link`

If you are operating outside the MCP-integrated flow, the equivalent CLI entrypoint is `npx @sveltejs/mcp`.

## Required Workflow

1. Start with `list_sections` and identify every section relevant to the requested change.
2. Fetch only the needed documentation sections.
3. Run `svelte_autofixer` on every Svelte component or module you create, edit, or analyze before you finalize the result.
4. When the change involves non-obvious framework choices, load `svelte-core-bestpractices` in the same turn instead of improvising local Svelte doctrine.
5. Ask about a playground link only when you are returning Svelte code directly rather than editing files in the repo.

## Required Use

- Run `svelte_autofixer` even for small changes.
- Fetch only documentation sections that match the requested feature or bug.
- Generate playground links only for returned snippets, not repo-file edits.
