---
name: implementation-decision-ledger
description: Use during implementation for minor pre-authorized local decisions and traceability; keep a run-scoped, ephemeral decision ledger for post-run human review without using it as a substitute for unresolved planning.
---

# Implementation Decision Ledger

Use for minor execution-local decisions only. Not a planning escape hatch.

If execution uncovers material behavior, scope, migration, or verification gap, stop and return to planning.

## Artifacts

- directory: `.artifacts/agent-decisions/`
- log: `.artifacts/agent-decisions/<run-id>.jsonl`
- summary: `.artifacts/agent-decisions/<run-id>-review.md`

Keep artifacts run-scoped and ephemeral.

## Required Event Fields

- `timestamp`
- `run_id`
- `agent`
- `scope`
- `entry_type`
- `summary`
- `rationale`
- `confidence`
- `impact`
- `durability`
- `needs_review`
- `resolved`

Value constraints:
- `timestamp`: UTC ISO-8601
- `entry_type`: `meta | decision | assumption`
- `confidence`: `1..5`
- `impact`: `low | medium | high`
- `durability`: `ephemeral | restart-safe | multi-instance-safe`
- `needs_review`: `true | false`
- `resolved`: `true | false`

Durability values:
- `ephemeral`
- `restart-safe`
- `multi-instance-safe`

## Log When

1. start-of-run metadata
2. minor bounded local decision allowed by plan/packet
3. implementation-local assumption that does not change approved behavior
4. unresolved high-impact assumption found during verification/review
5. durability-sensitive assumption

## Utility

Use:
- `scripts/agent_decision_log.py`

Flow:
1. append entries during implementation
2. generate review summary at end
3. surface unresolved high-impact entries in final reporting

## Final Report

Include:
- `log_path`
- `review_path`
- unresolved entries that still need review
