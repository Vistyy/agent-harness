# Wave <wave-id> Execution Packet

## Work Context

### Binding Objective

- original objective: `<user objective>`
- accepted reductions: `<none | explicit>`
- residual gaps: `<none | explicit>`
- newest-user-message checkpoint: `<date/context>`

### Owner Skill Intake

- route: `<direct | planning-intake | wave execution>`
- project overlay/docs read: `<paths | none>`
- owner skills read: `<skills>`
- matched reference gates read: `<references | none>`
- skipped references with reason: `<none | entries>`
- open owner gaps: `<none | entries>`

### Scope And Owners

- in scope: `<task-slug/surfaces>`
- out of scope: `<none | unrelated/accepted reductions>`
- touched owner/component: `<owner>`
- owned files/surfaces: `<paths/surfaces>`
- public entrypoints: `<entrypoints | none>`
- owner boundaries: `<boundaries>`

### Decisions And Assumptions

- closed decisions: `<decisions | none>`
- assumptions subagents may rely on: `<assumptions | none>`
- user-owned or blocked decisions: `<none | entries>`

### Adequacy Challenge

- before-implementation verdict: `<adequate | inadequate | blocked>`
- highest inspected scope: `<scope>`
- must-block signals: `<none | entries>`
- disposition: `<reshape | stop | accepted debt | adequate>`

### Required Gates

| Claim | Owner | Status | Blocks when | Proof rows | Role |
| --- | --- | --- | --- | --- | --- |
| `<claim>` | `<owner>` | `<planned | satisfied | blocked>` | `<condition>` | `P1` | `<role | none>` |

### Subagent Handoff Payload

- packet path: `docs-ai/current-work/<wave-id>/wave-execution.md`
- objective/reductions: `<summary>`
- task slice: `<task>`
- owned surfaces: `<surfaces>`
- assumptions: `<assumptions>`
- artifacts/proof rows: `<artifacts/proof rows>`
- risks: `<risks | none>`
- stop conditions: `<conditions>`

### Stop Conditions

- objective mismatch
- under-read owner skills
- inadequate touched owner
- proof drift
- unaccepted reduction/debt
- stale route
- context narrower than handoff/final claim

## Task Plan

### `<task/slug>`

- State:
  - `<blank | done | blocked>`
- Outcome:
  - `<complete outcome>`
- In scope:
  - `<paths/surfaces>`
- Out of scope:
  - `<none | unrelated/accepted reductions>`
- Owned files and surfaces:
  - `<path-or-surface>`
- Touched owner/component integrity:
  - `<acceptable | unacceptable with accepted-debt backlog link>`
- Locked invariants:
  - `<invariants>`
- Allowed local implementer decisions:
  - `<bounded choices | parent-only>`
- Stop-and-handback triggers:
  - `<objective mismatch | discovery leakage | proof drift | owner defect>`
- Proof rows:
  - `P1`
- Deferred follow-up:
  - `<none | backlog path>`

## Proof Plan

```json
{
  "proof_plan": [
    {
      "proof_id": "P1",
      "task_slug": "<task/slug>",
      "anchor_ids": ["A1"],
      "claim": "<claim proven by this row>",
      "material_variants": ["none"],
      "proof_classification": "<automated-suite-provable | runtime-provable | multi-proof-required | not-reliably-provable-with-current-harness>",
      "owner_layer": "<unit | contract | integration | static-check | runtime-web | runtime-mobile | ad-hoc-validation | doc-only>",
      "exact_proof": ["<command or runtime recipe with entrypoint/target/action/result/simulation boundary>"],
      "expected_evidence": ["<expected result tied to owner/user-visible surface>"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "<bad implementation or proof-shape substitution>",
        "failing_assertion_or_artifact": "<what would fail>"
      },
      "status": "<planned | blocked | satisfied | narrowed-claim | deferred>"
    }
  ]
}
```

## Execution State

### Decisions And Blockers

| Type | Item | Action | Owner |
| --- | --- | --- | --- |
| `decision` | `<decision needed | none>` | `<recommended action>` | `<user | agent>` |

### Technical Debt And Deferred Follow-Up

- `none`
- or `<backlog item with owner, affected files/surfaces, accepted must-block signals, risk, removal condition, and user acceptance>`

## System-Boundary Architecture Disposition (conditional)

Use only when `System-boundary trigger: triggered`.

- Why triggered: `<reason>`
- Planning disposition: `<closed decision>`
- Execution stop rule: `<when to return to planning>`
- Changed authorities or contracts: `<items>`
- Single owner after change: `<owner>`
- Public write paths: `<paths>`
- Read-repair paths: `<paths>`
- Forbidden bypass paths: `<paths>`
- Rejected alternatives: `<alternatives>`
- Why not artificially narrowed: `<reason>`
- Stable-to-extend expectation: `<reason>`
