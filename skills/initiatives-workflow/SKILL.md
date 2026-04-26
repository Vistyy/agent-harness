---
name: initiatives-workflow
description: "Use when the task is workflow maintenance (delivery-map structure, wave execution packet conventions, or wave/backlog workflow policy), not when actively shaping scope or executing a wave."
---

# Initiatives Workflow

Thin maintenance wrapper for wave/backlog state.

Owner doc:
- `references/initiatives-workflow.md`

Use this skill for:
- backlog -> wave promotion,
- `discovery-required` -> `execution-ready` promotion after planning closes,
- packet maintenance,
- backlog/mobile-parity entry maintenance,
- wave closeout state cleanup.

Do not use it for scope shaping or wave execution.

## Working Rules

- durable intent stays in `docs-ai/docs/**`
- queue, packet, evidence pointers stay in `docs-ai/current-work/**`
- only `execution-ready` waves keep canonical `wave-execution.md`
- planning gate may use `wave-execution.draft.md`
- closeout removes wave from map, deletes packet, and then deletes or slims
  the closed brief per the owner doc's closed-wave rule
- mobile parity items and backlog items are lightweight follow-up state only

## Templates

- discovery-required brief:
  `assets/wave-brief-discovery-required.md`
- execution-ready brief:
  `assets/wave-brief-execution-ready.md`
- packet:
  `assets/wave-execution.md`
- backlog detail:
  `assets/backlog-entry.md`

Examples:
- `assets/wave-brief.example.md`
- `assets/wave-execution.example.md`

Bootstrap helper:
- `scripts/bootstrap_wave_docs.py`

## Guardrails

- keep policy changes in owner doc, not here
- do not restate owner policy
- when queue, packet, and backlog all move, update all in same change
