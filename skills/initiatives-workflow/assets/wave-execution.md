# Wave <wave-id> Execution Packet

Use this template in one of two states:

- planning-gate draft:
  `docs-ai/current-work/<wave-id>/wave-execution.draft.md`
  while durable brief is `**Status:** discovery-required`
- canonical execution packet:
  `docs-ai/current-work/<wave-id>/wave-execution.md`
  only after durable brief is `**Status:** execution-ready`

Linked durable brief:

- `docs-ai/docs/initiatives/waves/<wave-id>.md`

Field semantics are owned by
`skills/initiatives-workflow/references/wave-packet-contract.md`.

One packet layout only. Vary depth, not shape.

## Scope And Execution Posture

- In-scope:
  - `<task-slug-1>`
  - `<task-slug-2>`
- Out-of-scope:
  - `<explicitly deferred scope>`
- Non-obvious constraints:
  - `<constraint>`
- System-boundary trigger:
  - `not-triggered`
  - or `triggered`
- Implementer delegation posture:
  - `parent-only`
  - or `implementer-eligible`
- Parent-only rationale:
  - `none`
  - or `packet-declared-parent-only`
  - or `repeated-implementer-handback`
  - or `tool-or-runtime-limit`
  - or `shared-file-churn`
  - or `tiny-local-followup`
- Frozen decisions:
  - `<planning decision execution must not reopen>`
  - or `none`
- Planning Exceptions:
  - `none`
  - or `<expectation skipped/narrowed> | <why safe> | <owner> | <review/removal condition>`

Rules:

- `implementer-eligible` is the preferred default for structured wave execution
- `parent-only` requires an explicit reason in this packet
- `implementer-eligible` requires each delegable task card to carry one bounded
  autonomy envelope
- required task-card boundary fields are owned files/surfaces, locked
  invariants, allowed local implementer decisions, stop-and-handback triggers,
  proof rows, and deferred follow-up disposition
- starting files/symbols, existing patterns, and implementation notes are
  optional hints; include only when useful for bounded execution
- do not use `implementer-eligible` to hide unresolved discovery or strategic
  product/boundary/proof decisions
- `System-boundary trigger: triggered` requires
  `## System-Boundary Architecture Disposition`
- `System-boundary trigger: not-triggered` allows the section to stay absent
- the durable brief must already carry planning-review provenance in
  `planning_gate.planning_critic`; this packet never substitutes memory for planning
- proof rows assigned to a task define the implementer's task-local verification
  obligations; handback should leave those checks green or return an explicit
  blocker
- do not restate generic repo completion policy here

## Task Plan

| Task slug | State | Dependencies | Outcome summary | Proof rows |
| --- | --- | --- | --- | --- |
| `<initiative/feature/task-1>` |  | `none` | `<1-line expected result>` | `P1, P2` |
| `<initiative/feature/task-2>` |  | `<task-1>` | `<1-line expected result>` | `P3` |

Allowed states:

- blank
- `done`
- `blocked`

### `<initiative/feature/task-1>`

- Outcome:
  - `<1-2 lines of user-visible or contract-visible result>`
- In scope:
  - `<what this task includes>`
- Out of scope:
  - `<what this task explicitly does not include>`
- Owned files and surfaces:
  - `<files/components/routes this task may change>`
- Starting files and symbols (optional):
  - `<path + symbol or entrypoint>`
- Existing patterns to follow (optional):
  - `<path or feature pattern>`
  - or `none`
- Locked invariants:
  - `<decision that must not drift during execution>`
  - or `none`
- Allowed local implementer decisions:
  - `<small code-shape / helper / test-placement choices allowed locally>`
  - or `parent-only`
- Stop-and-handback triggers:
  - `<when implementer must stop instead of deciding locally>`
  - or `parent-only`
- Implementation notes (optional):
  - `<non-obvious constraints, ordering notes, or edge posture>`
- Proof rows:
  - `P1`
  - `P2`
- Deferred follow-up:
  - `none`
  - or `<backlog-slug / mobile-parity item / follow-up wave>`

### `<initiative/feature/task-2>`

- Outcome:
  - `<1-2 lines>`
- In scope:
  - `<...>`
- Out of scope:
  - `<...>`
- Owned files and surfaces:
  - `<...>`
- Locked invariants:
  - `<...>`
  - or `none`
- Allowed local implementer decisions:
  - `<...>`
  - or `parent-only`
- Stop-and-handback triggers:
  - `<...>`
  - or `parent-only`
- Proof rows:
  - `P3`
- Deferred follow-up:
  - `none`
  - or `<...>`

## Proof Plan

Wave-local proof allocation matrix. Keep proof ownership here instead of
splitting it across checklist/command/evidence sections.

If durable brief already has `Proof-Gap Disposition Registry`, mirror those
closed dispositions here. Do not invent new proof posture during execution.

```json
{
  "proof_plan": [
    {
      "proof_id": "P1",
      "task_slug": "<initiative/feature/task-1>",
      "anchor_ids": ["A1"],
      "claim": "<short claim summary>",
      "material_variants": [
        "<guest-local | authenticated-server | capability-denied | none>"
      ],
      "proof_classification": "<automated-suite-provable | runtime-provable | multi-proof-required | not-reliably-provable-with-current-harness>",
      "owner_layer": "<unit | contract | integration | static-check | runtime-web | runtime-mobile | ad-hoc-validation | doc-only>",
      "exact_proof": [
        "<exact command / artifact recipe / explicit not-required marker>"
      ],
      "expected_evidence": [
        "<report path / runtime artifact path / log id / diff ref>"
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "<realistic wrong implementation or proof-shape substitution>",
        "failing_assertion_or_artifact": "<what exact proof would fail>"
      },
      "status": "<planned | blocked | satisfied | narrowed-claim | deferred>"
    }
  ]
}
```

## System-Boundary Architecture Disposition (conditional)

Use this section only when `System-boundary trigger: triggered`.

- Trigger status:
  - `triggered`
- Why triggered:
  - `<why structural/boundary doctrine applies>`
- Planning disposition:
  - `<how planning closed the structural decision>`
- Execution rule:
  - `<stop-and-return-to-planning rule if a new unresolved structural decision appears>`
- Changed authorities or contracts:
  - `<state/contract owner changes>`
- Single owner after change:
  - `<one explicit owner>`
- Public write paths:
  - `<all public mutation paths that must route through owner>`
- Read-repair paths:
  - `<all repair/reconciliation reads that can persist or heal state>`
- Forbidden bypass paths:
  - `<old direct APIs/call-site patterns now disallowed>`
- Rejected alternatives:
  - `<material alternatives rejected in planning>`
- Why not artificially narrowed:
  - `<why wave includes full owner/path coverage instead of tactical subset>`
- Stable-to-extend expectation:
  - `<why next work should extend without first refactoring owner shape>`

## Execution State

### Decisions And Blockers

| Type | Item | Action | Owner |
| --- | --- | --- | --- |
| `decision` | `<decision needed>` | `<recommended option>` | `user` |
| `blocker` | `<blocking issue>` | `<next action>` | `agent` |

### Technical Debt And Deferred Follow-Up

- `none`
- or `<backlog item / follow-up wave / parity item with short reason>`
