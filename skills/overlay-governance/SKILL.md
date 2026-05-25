---
name: overlay-governance
description: "Govern reusable workflow overlay changes: skills, AGENTS overlays, adapters, role/prompt contracts, validation checks, and reusable agent-policy ownership. Use when changing overlay structure or deciding where agent workflow policy belongs. Use this skill for overlay contracts only; it does not own project facts, product architecture, runtime commands, active work, or project-only exceptions."
---

# Overlay Governance

Owns reusable workflow overlay posture, project-overlay contracts, adapter
posture, skill architecture, and overlay checks.

## Contract

This repository is a reusable workflow overlay: skills, role adapters, prompt
inputs, templates, helper commands, and checks that fit agent work to local
practice.

The overlay is a contract, not a project playbook. It owns reusable
agent-facing workflow policy and tooling; projects own product facts, runtime
shape, local command bodies, roadmap, queue state, active execution state, and
project-only exceptions.

Keep overlay policy adapter-neutral unless it lives in an adapter file. Adapter
files may name runtime-specific mechanics.

Write overlay policy under `documentation-stewardship`: shortest enforceable
rule that preserves owner, outcome, forbidden workaround, and proof or stop
condition when needed. Avoid inherited process stacks.
Apply its density rule to skills, adapter prompts, examples, validation docs,
and project-overlay contracts.

## Rules

- Required overlay gates are blocking. Use `pass`, `reject`, `blocked`, or
  `not-applicable`; do not make required rule, proof, review, runtime,
  architecture, solution-shaping, or validation failures advisory.
- `NON-BLOCKING` is an observation category, not a code-review verdict. It is
  valid only outside the binding objective or for explicitly accepted temporary
  debt with owner, risk, and removal condition.
- Keep `AGENTS.md` and skill bodies as maps/contracts, not manuals.
- Frontmatter `description` owns ordinary trigger/routing text: purpose,
  positive triggers, and likely exclusions.
- Skill bodies are post-selection contracts.
- Reference rows are mandatory purpose gates; matched gates must be read, and
  unmatched references must not be loaded speculatively.
- Follow `documentation-stewardship` for one-owner durable concepts. Overlay
  skills, adapters, and bootstrap docs may repeat only compressed owner
  pointers plus local load, input, output, or stop consequences.
- Closed work notes are not durable doctrine. After extraction to the real
  owner or valid backlog, durable docs must not depend on closed work notes.
- Treat duplicate doctrine as a review concern. Do not add exact-phrase
  validators for documentation ownership; use positive current structure and
  reviewer judgment instead.
- Delete, collapse, demote, or reuse before adding overlay structure.
- Exceptions need an owner, protected surface, and removal condition.

Non-trivial overlay changes touch `AGENTS.md`, reusable skills or metadata,
adapter prompts/config, validation checks, workflow policy, project-overlay
contracts, or reusable policy ownership.

Overlay closeout names changed reusable owners, removed obsolete routes, changed
routing triggers, overlay repo status, and project repo status when overlays
also changed.

## Reference Gates

- Read `references/overlay-contracts.md` before changing project overlays,
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
