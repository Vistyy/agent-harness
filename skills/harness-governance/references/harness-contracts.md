# Harness Contracts

Load this reference when changing project-overlay contracts, global
`AGENTS.md`, repository posture, or reusable harness enforcement checks.

## Project Overlay Contract

A harness-managed project keeps its local instructions as an overlay. The
overlay owns:

- product and domain facts
- roadmap and initiative queue
- architecture maps
- runtime topology and environment wiring
- project-local skills
- local command recipe bodies
- safety invariants that are specific to the project

The overlay must point to global harness owners instead of copying reusable
policy after the global owner is installed and proven. Temporary duplicated
project docs are allowed during an extraction wave only when the active packet
names their retirement or pointerization wave.

## AGENTS.md Contract

`AGENTS.md` is the first-hop map for an agent working in a project. It should
contain:

- precedence rules
- compact repo map
- project-specific invariants
- pointers to global harness skills for reusable policy
- pointers to project owner docs for project truth

It should not become a second copy of reusable harness doctrine after the
global harness is installed and proven.

If an entrypoint is a skill, route by the skill frontmatter `description`
first. Read the skill body only for workflow mechanics and deeper owner links.

## Repository Structure

Harness-managed projects use this documentation layout:

- `docs-ai/docs/**` for durable project truth
- `docs-ai/current-work/**` for active execution state, queue state, evidence,
  blockers, and resume notes

Code, test, service, package, and runtime layout remains project-owned unless a
global skill explicitly owns a reusable convention.

## Repository Posture

Default posture when no user instruction or project owner doc overrides it:

- Treat a project as pre-release unless a durable owner marks a surface live or
  release-critical.
- Treat a project as single-developer unless a durable owner names other
  stakeholders.
- For internal-only surfaces, avoid compatibility shims, migration bridges,
  rollback ceremony, and approval choreography unless a real owner contract
  requires them.
- For released or externalized surfaces, assess compatibility, migration,
  rollout, and user impact explicitly. Shims or bridges still need an explicit
  durable owner requirement and removal condition; otherwise replace the old
  path and delete obsolete code in the same change.

Prefer the simplest operational path that honestly serves the current posture.

## Enforcement Checks

This skill owns `../scripts/harness_enforcement_checks.py`, a reusable
project-overlay check for markdown links in `AGENTS.md`, `docs-ai/docs/**`, and
`docs-ai/current-work/**`. It reports broken local or absolute markdown targets
and ignores external URLs, anchors, and template-like paths.

Use it from a harness-managed project when changing project overlay docs or
validating extraction/pointerization work:

```bash
python skills/harness-governance/scripts/harness_enforcement_checks.py .
```

Project-local harness checks should stay narrow, high-signal, and tied to owned
policy surfaces. Recurring reusable misses should move to global harness skills
rather than growing project overlays.
