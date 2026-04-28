# Standalone Plans

Owner for standalone implementation plans under `docs/plans/**`.

## Scope

This file owns:
- when work should use a standalone plan instead of a wave
- what makes a standalone plan execution-ready
- required approval record for plan execution
- touched owner/component integrity requirements for standalone planning
- how `executing-plans` and `implementer` may trust an approved standalone plan

This file does not own:
- wave workflow or packet lifecycle
- generic review doctrine
- generic worker topology beyond the standalone-plan entry condition

## Source Of Truth

- normative policy: this file
- authoring mechanics: `../SKILL.md`
- execution mechanics: `../../executing-plans/SKILL.md`
- review/approval doctrine: `../../code-review/references/review-governance.md`
- wave lifecycle: `../../initiatives-workflow/references/initiatives-workflow.md`

## Use Standalone Plan When

Use `docs/plans/**` only when all are true:
- work is real implementation, not discovery
- scope is closed enough that execution should not reopen design/proof/runtime
  decisions
- work does not belong to an active or better-shaped wave
- one approved plan can bound the execution slice without queue/packet state

If work is still shaping architecture, discovery, rollout, migration, or proof
posture, use wave planning instead.

## Output Path

- `docs/plans/YYYY-MM-DD-<feature-name>.md`

`docs/plans/**` is execution surface for concrete approved plans only.
Do not store examples, templates, scratch planning, or policy docs there.

## Execution-Ready Contract

A standalone plan is execution-ready only when it closes:
- scope and owned surfaces
- touched owner/component integrity for non-trivial work
- material behavior, migration, runtime, and verification decisions
- exact files or paths to change
- ordered implementation tasks
- proof obligations per task
- required doc/backlog follow-up

If two competent executors could still choose materially different behavior,
runtime posture, migration posture, or proof shape, the plan is not approved.

Non-trivial standalone work needs a durable planning artifact before material implementation starts. Memory-only planning is not enough.

## Required Plan Sections

Each standalone plan must include:
- short goal
- short architecture summary
- `Decision Closure Check`
- `Scope Coverage Plan`
- `Touched Owner Integrity`
- ordered implementation tasks with exact paths
- verification commands and expected evidence per task
- required doc/backlog follow-up
- `## Approval Record`

Templates and examples for this contract live under
`../assets/`.

## Touched Owner Integrity

Non-trivial standalone plans must name:
- touched owner/component
- highest expected scope to inspect
- touched-component integrity: `acceptable`, `unacceptable`, or `not assessed`
- must-block `code-simplicity` signals, or `none`
- accepted-debt backlog link, or `none`

Select the smallest owner/component whose contract, state, lifecycle, design,
workflow, or proof the change touches. Expand only to shared authority required
by the change.

`not assessed` means the plan is unapproved. Unacceptable integrity requires
explicit user acceptance after the blocker presentation plus a backlog item with
owner, risk, and removal condition before approval.

## Approval Record

Approved standalone plans must carry one JSON fenced block under
`## Approval Record` with exact shape:

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

Rules:
- missing `## Approval Record` means the plan is unapproved
- any disposition other than `APPROVE` means execution must stop and return to
  planning
- an approval record is invalid when touched-component integrity is
  `not assessed` or when accepted touched-component debt lacks a backlog link
- `executing-plans` may trust only `plan_approval`; the same `## Approval Record`
  block must also carry `planning_critic` provenance at top level
- approval must not be inferred from surrounding prose or from a separate
  record object

## Execution Trust Boundary

- `writing-plans` may author plans and templates inside this contract
- `executing-plans` may execute only approved plans that satisfy this contract
- `implementer` may be used only when routing surfaces also confirm the narrow
  approved-standalone-plan exception and the plan satisfies this contract
- missing/invalid approval data must stop execution; do not repair or rewrite
  plan approval in place during execution

## Deferral Rule

If execution or review exposes missing in-scope surfaces, unresolved planning,
or broader architecture than one standalone plan should own:
1. stop execution
2. return to planning or wave shaping
3. persist durable follow-up state in same session when needed
