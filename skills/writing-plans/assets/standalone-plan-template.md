# <Plan Title>

## Goal

<1-2 lines of exact outcome>

## Architecture Summary

<short owner/boundary summary>

## Decision Closure Check

- behavior/runtime/migration/proof decisions closed: `yes`
- remaining material planning questions: `none`
- if not `none`, stop and return to planning

## Scope Coverage Plan

| Surface | Owner | Why in scope |
| --- | --- | --- |
| `<path-or-surface-1>` | `<owner>` | `<reason>` |
| `<path-or-surface-2>` | `<owner>` | `<reason>` |

## Implementation Tasks

### 1. `<task-name>`

- Exact paths:
  - `<path-1>`
  - `<path-2>`
- Changes:
  - `<exact change>`
- Verification:
  - `<exact command>`
- Expected evidence:
  - `<artifact or output>`

### 2. `<task-name>`

- Exact paths:
  - `<path>`
- Changes:
  - `<exact change>`
- Verification:
  - `<exact command>`
- Expected evidence:
  - `<artifact or output>`

## Required Doc/Backlog Follow-Up

- `none`
- or `<durable follow-up artifact>`

## Approval Record

```json
{
  "planning_critic": {
    "review_mode": "planning_critic",
    "disposition": "APPROVE",
    "recorded_at": "YYYY-MM-DD",
    "summary": "<1-line critic rationale>"
  },
  "plan_approval": {
    "review_mode": "quality_guard",
    "disposition": "APPROVE",
    "recorded_at": "YYYY-MM-DD",
    "summary": "<1-line approval rationale>"
  }
}
```
