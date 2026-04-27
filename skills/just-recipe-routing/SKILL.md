---
name: just-recipe-routing
description: Use when choosing `just` commands in a harness-managed repo, including namespace discovery, stack-local vs root quality gates, `quality-fast`/`quality`/`quality-full` selection, and avoiding raw tool commands when a project-owned recipe exists.
---

# Just Recipe Routing

Harness-managed repositories expose workflow commands through `just`. Use this
skill whenever you are selecting development, formatting, linting, testing,
runtime, diagnostics, or quality-gate commands.

## Router Model

The root `justfile` is a command router. Start with the smallest useful
discovery scope:

- `just` or `just help` for top-level namespaces and root rollups.
- `just <namespace>` for a namespace recipe list.
- `just <namespace> <recipe> ...` for stack- or service-specific work.

Project overlays own concrete namespace names, aliases, runtime targets, recipe
bodies, and service-specific helpers. If the project docs do not name the
right namespace, inspect `just help` and then the relevant namespace list.

## Selection Rules

Use namespace recipes for day-to-day work inside one surface. Prefer the
matching namespace for development, probes, formatting, linting, typechecking,
testing, OpenAPI checks, runtime helpers, diagnostics, and stack-local quality.

Use root rollups only when the work is cross-stack, the user explicitly asks
for a repo-wide gate, or you are making a broad completion claim.

Do not default to raw technology commands when a `just` namespace owns the
workflow. Raw commands are acceptable for tiny local probes, missing-recipe
gaps, or when a skill explicitly requires a lower-level tool.

## Gate Rules

- In-progress or stack-local work: use the narrowest honest namespace recipe.
- Final stack-local gate: use that stack's `quality`.
- Final cross-stack gate: use root `just quality`.
- `quality-fast` is the cheap implementation and CI baseline.
- `quality` is the default completion gate.
- `quality-full` is the explicit expanded-confidence gate when the user, owner
  doc, reviewer, or risk profile calls for it.

Standard harness-managed projects expose these root recipes:

- `just quality-fast`
- `just quality`
- `just quality-full`
- `just test`
- `just fmt`
- `just agent profile .`
- `just agent up <target> .`
- `just agent verify .`
- `just agent down <target>`
- `just agent logs <service>`

## Navigation Rule

Start from the namespace that owns the files or runtime surface you touched.
Only widen to root rollups when the change or claim crosses stacks.

When service namespaces exist, use them for service-specific helpers. Do not
switch to a service namespace for generic language lint, typecheck, or test
work unless the project overlay explicitly says that service owns that gate.
