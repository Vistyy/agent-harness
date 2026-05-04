# Wave <wave-id> Execution Packet

## Scope And Execution Posture

- Original objective:
  - `<user objective>`
- Accepted reductions:
  - `<none | explicit>`
- Residual gaps:
  - `<none | explicit>`
- In-scope:
  - `<task-slug>`
- Out-of-scope:
  - `<none | unrelated/accepted reductions>`
- Non-obvious constraints:
  - `<constraint | none>`
- System-boundary trigger:
  - `not-triggered`
- Implementer delegation posture:
  - `implementer-eligible`
- Parent-only rationale:
  - `none`
- Frozen decisions:
  - `<closed decision | none>`
- Planning Exceptions:
  - `none`

## Required Gates

| Claim | Required gate | Owner | Proof/artifacts | Blocks when |
| --- | --- | --- | --- | --- |
| `<claim>` | `<gate>` | `<owner>` | `<proof/artifacts>` | `<missing/rejected/blocked/stale/narrower than claim>` |

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
