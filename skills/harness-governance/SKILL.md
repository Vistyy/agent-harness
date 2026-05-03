---
name: harness-governance
description: "Use for reusable agent-harness governance: skill architecture, global AGENTS/project overlays, adapter install behavior, project-overlay contracts, and checks."
---

# Harness Governance

Owns reusable harness posture, project-overlay contracts, adapter posture,
skill architecture, and harness checks.

## Contract

The harness is a contract, not a playbook. It owns reusable agent-facing policy
and tooling; projects own product facts, runtime shape, local command bodies,
roadmap, queue state, active execution state, and project-only exceptions.

Keep harness policy adapter-neutral unless it lives in an adapter file. Codex is
one adapter.

Write harness policy under `documentation-stewardship`: shortest enforceable
rule that preserves owner, outcome, forbidden workaround, and proof or stop
condition when needed. Avoid inherited process stacks.

## Rules

- Keep `AGENTS.md` and skill bodies as maps/contracts, not manuals.
- Frontmatter `description` owns ordinary trigger/routing text.
- Skill bodies are post-selection contracts.
- Reference rows are mandatory purpose gates; matched gates must be read, and
  unmatched references must not be loaded speculatively.
- Keep one durable rule in one owner; point to the owner instead of copying.
- Delete, collapse, demote, or reuse before adding harness structure.
- Exceptions need an owner, protected surface, and removal condition.

Non-trivial harness changes touch `AGENTS.md`, reusable skills or metadata,
adapter prompts/config, validation checks, workflow policy, project-overlay
contracts, or reusable policy ownership.

Harness closeout names changed reusable owners, removed obsolete routes, changed
routing triggers, harness repo status, and project repo status when overlays
also changed.

## Reference Gates

- Read `references/harness-contracts.md` before changing project overlays,
  `AGENTS.md`, project-overlay documentation layout, or governance check
  semantics.
- Read `references/skill-architecture.md` before changing skill authoring,
  splitting, installing, metadata, reference rows, templates, helper commands,
  validation, skill eval posture, or split proposals.

## Check

```bash
agent-harness governance check --repo-root .
```

When this skill changes, validation plus readback must prove owner boundary,
non-trivial classification, closeout obligations, and reference gates survive.
