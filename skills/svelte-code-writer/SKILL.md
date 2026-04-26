---
name: svelte-code-writer
description: Tooling-entry skill for Svelte documentation lookup and autofixer workflow. MUST be used whenever creating, editing, or analyzing any Svelte component (.svelte) or Svelte module (.svelte.ts/.svelte.js).
---

# Svelte Code Writer

## Ownership Boundary

This skill owns:
- Svelte/SvelteKit documentation lookup
- `svelte_autofixer` usage before finalizing Svelte code
- choosing the right tool inputs for file-based Svelte work

This skill does not own the repo's broad Svelte framework guidance. Load `svelte-core-bestpractices` alongside this skill when reactivity, event handling, styling, state sharing, or other non-obvious framework choices matter.

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

## Guardrails

- Do not treat this skill as the owner of broad Svelte best-practice doctrine.
- Do not skip `svelte_autofixer` because the change looks small.
- Do not fetch documentation blindly; choose the sections that match the requested feature or bug.
- Do not generate playground links for code that was already written into repo files.

## Related Skills

- `svelte-core-bestpractices` for the broad Svelte guidance this skill deliberately does not duplicate
- `user-apps-design` for end-user UI direction and copy rules when the Svelte work is user-facing
- `webapp-testing` for browser runtime evidence
