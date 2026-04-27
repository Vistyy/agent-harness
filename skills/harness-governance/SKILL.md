---
name: harness-governance
description: Use when creating, installing, validating, or reviewing the reusable agent-harness repository itself, Codex adapter install behavior, global AGENTS.md/project-overlay contracts, skill architecture, harness repo posture, or reusable harness enforcement checks.
---

# Harness Governance

Use this skill for the reusable agent-harness repository and for
harness-managed project overlay contracts. Do not use it for ordinary project
implementation work or for choosing `just` recipes; use `just-recipe-routing`
for command selection.

## Operating Model

The global agent harness owns reusable agent workflow policy, skills, role
adapters, templates, prompts, and validation. Harness-managed projects own
product facts, architecture, roadmap, runtime topology, local command bodies,
active execution state, and project-only exceptions.

Codex is one adapter. The harness identity is generic.

Global reusable policy lives in this harness repository. Project overlays may
narrow or extend global policy only for project facts, local runtime shape, or
explicit documented exceptions. Reusable global truth must not live in a
project active-work directory.

Harness changes are reviewed and committed in the harness repository.
Project-overlay changes are reviewed in the project repository. Closeout
reports must state both repository statuses when a task touches both.

Any task that touches the agent-harness repository must route the proposed
harness change through `planning_critic` before further harness edits or
closeout when subagent delegation is available and authorized. If delegation is
unavailable, perform the same hostile planning review in-thread and report that
constraint.

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
  rollout, and user impact explicitly.

Prefer the simplest operational path that honestly serves the current posture.

## Skill Architecture

Reusable skill guidance belongs in focused skill directories.

- `SKILL.md` owns trigger description and workflow mechanics.
- Reference material should be split out only when the content is too large or
  specialized to keep in the skill body.
- Asset folders own templates copied or consumed by the skill.
- Script folders own helper scripts used by the skill.
- Agent-adapter folders own platform-specific hints.

Keep project facts out of reusable skills. Keep skill frontmatter concise and
route by description. Move reusable supporting material with the owning skill instead of
leaving it in a project documentation tree. Do not duplicate the same durable
rule in multiple skills; link to the owner. Keep examples generic unless the
skill is explicitly project-local.

## Enforcement Checks

This skill owns `scripts/harness_enforcement_checks.py`, a reusable
project-overlay check for markdown links in `AGENTS.md`, `docs-ai/docs/**`, and
`docs-ai/current-work/**`. It reports broken local or absolute markdown targets
and ignores external URLs, anchors, and template-like paths.

Use it from a harness-managed project when changing project overlay docs or
validating extraction/pointerization work:

```bash
python /home/syzom/projects/agent-harness/skills/harness-governance/scripts/harness_enforcement_checks.py .
```

Project-local harness checks should stay narrow, high-signal, and tied to owned
policy surfaces. Recurring reusable misses should move to global harness skills
rather than growing project overlays.
