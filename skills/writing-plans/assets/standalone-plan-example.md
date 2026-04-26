# Example Standalone Plan — Tighten Review-Report Copy Contract

## Goal

Make one small doc-only change that tightens review-report wording without
reopening routing or workflow topology.

## Architecture Summary

`review-governance.md` stays policy owner. This plan only updates one durable
owner doc plus one directly consuming skill surface.

## Decision Closure Check

- behavior/runtime/migration/proof decisions closed: `yes`
- remaining material planning questions: `none`
- rationale: owned scope is doc-only and fully bounded to one wording contract

## Scope Coverage Plan

| Surface | Owner | Why in scope |
| --- | --- | --- |
| `skills/code-review/references/review-governance.md` | review-governance | policy wording owner |
| `skills/code-review/SKILL.md` | code-review skill | consumer wording must align to owner |

## Implementation Tasks

### 1. `tighten-owner-wording`

- Exact paths:
  - `skills/code-review/references/review-governance.md`
- Changes:
  - replace stale completion wording with owner-approved stricter phrasing
- Verification:
  - `uv run python scripts/harness_enforcement_checks.py`
- Expected evidence:
  - passing harness check output

### 2. `align-skill-consumer`

- Exact paths:
  - `skills/code-review/SKILL.md`
- Changes:
  - trim duplicated wording and link back to owner doc
- Verification:
  - `just quality`
- Expected evidence:
  - passing quality output

## Required Doc/Backlog Follow-Up

- `none`

## Approval Record

```json
{
  "planning_critic": {
    "review_mode": "planning_critic",
    "disposition": "APPROVE",
    "recorded_at": "2026-04-17",
    "summary": "Planning critic confirmed the slice is closed enough for execution."
  },
  "plan_approval": {
    "review_mode": "quality_guard",
    "disposition": "APPROVE",
    "recorded_at": "2026-04-12",
    "summary": "Doc-only scope is fully bounded, exact paths and proof are named, and execution can proceed without reopening planning."
  }
}
```
