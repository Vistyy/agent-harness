# Wave workflow-trim Execution Packet

## Scope And Execution Posture

- Original objective:
  - materially trim workflow harness ceremony while preserving hard gates
- Accepted reductions:
  - no role topology change
- Residual gaps:
  - none
- In-scope:
  - `workflow/trim`
- Out-of-scope:
  - `project overlays`
- Non-obvious constraints:
  - preserve validator-sensitive packet, role, and proof contracts
- System-boundary trigger:
  - `not-triggered`
- Implementer delegation posture:
  - `parent-only`
- Parent-only rationale:
  - `packet-declared-parent-only`
- Frozen decisions:
  - technical contracts remain in their current owners
- Planning Exceptions:
  - `none`

## Task Plan

| Task slug | State | Dependencies | Outcome summary | Proof rows |
| --- | --- | --- | --- | --- |
| `workflow/trim` |  | `none` | `Compact workflow owners and remove duplicate doctrine.` | `P1` |

Allowed states: blank, `done`, `blocked`.

### `workflow/trim`

- Outcome:
  - `Workflow docs are materially shorter and still preserve hard gates.`
- In scope:
  - `skills/work-routing/SKILL.md`
  - `skills/planning-intake/**`
  - `skills/initiatives-workflow/**`
  - `skills/subagent-orchestration/**`
  - `skills/code-review/references/review-governance.md`
  - `skills/verification-before-completion/**`
- Out of scope:
  - `project overlays`
- Owned files and surfaces:
  - `reusable workflow governance surface`
- Touched owner/component integrity:
  - `acceptable`
- Locked invariants:
  - `binding objective, full-work rule, planning_critic, quality_guard, final review, runtime evidence`
- Allowed local implementer decisions:
  - `wording and compaction that preserve listed contracts`
- Stop-and-handback triggers:
  - `validator-sensitive contract cannot be preserved`
- Proof rows:
  - `P1`
- Deferred follow-up:
  - `none`

## Proof Plan

```json
{
  "proof_plan": [
    {
      "proof_id": "P1",
      "task_slug": "workflow/trim",
      "anchor_ids": ["workflow-trim"],
      "claim": "Workflow harness surface was materially reduced without losing hard gates.",
      "material_variants": ["skills", "references", "assets", "adapter prompts"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "harness-validation",
      "exact_proof": ["just quality-fast", "agent-harness governance check --repo-root ."],
      "expected_evidence": ["52 tests passed", "harness validation passed"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Remove packet proof fields, allowed task states, or role table.",
        "failing_assertion_or_artifact": "quality_guard rejects or validate_harness fails"
      },
      "status": "planned"
    }
  ]
}
```

## Execution State

### Decisions And Blockers

| Type | Item | Action | Owner |
| --- | --- | --- | --- |
| `decision` | `none` | `none` | `agent` |

### Technical Debt And Deferred Follow-Up

- `none`
