---
name: initiatives-workflow
description: "Use for wave/backlog workflow maintenance, delivery-map structure, packet schema upkeep, and closeout state cleanup."
---

# Initiatives Workflow

Thin maintenance wrapper for wave/backlog state.

Owner doc:
- `references/initiatives-workflow.md`

Packet contract:
- `references/wave-packet-contract.md`

Use this skill for:
- backlog -> wave promotion,
- `discovery-required` -> `execution-ready` promotion after planning closes,
- packet maintenance,
- backlog/mobile-parity entry maintenance,
- wave closeout state cleanup.

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

Helpers:
- Preferred installed CLI:
  `agent-harness wave bootstrap --repo-root <project-root> --wave <wave-id> --title "<title>"`
  scaffolds a `discovery-required` wave brief.
- Preferred installed CLI:
  `agent-harness wave refs --repo-root <project-root> --wave <wave-id>`
  lists exact references to one wave brief path during closeout.
- Preferred installed CLI:
  `agent-harness wave cleanup --repo-root <project-root> --wave <wave-id>`
  dry-runs closed current-work wave directory cleanup; add `--execute` after
  closeout prerequisites are satisfied.

## Guardrails

- keep policy changes in owner docs
- keep this skill thin; link owner policy rather than restating it
- when queue, packet, and backlog all move, update all in same change
