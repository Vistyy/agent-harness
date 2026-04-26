# Wave sample-proof-allocation-1

**Status:** execution-ready

## User objective

Give implementers one plain-language statement of the actual user or operator outcome this wave must close.

## Problem

Packets said proof/review mattered, but still scattered commands, checklists, and evidence prose. Implementers had to reconstruct proof plan by hand.

## Objective

Land one compact packet shape that still makes:
- implementer starting point
- proof allocation
- contradiction checks

explicit.

## In Scope

- `engineering-harness/internal-harness-baseline/packet-shape-alignment`
- `engineering-harness/internal-harness-baseline/proof-plan-adoption`

## Out Of Scope

- new testing skill
- final-review topology redesign

## Constraints

- keep one packet layout
- do not add separate planning artifact

## Risks

- review docs and templates must stay aligned in same change

## Execution Tasks

- `engineering-harness/internal-harness-baseline/packet-shape-alignment`
- `engineering-harness/internal-harness-baseline/proof-plan-adoption`

## Acceptance Anchors

```json
{
  "acceptance_anchors": [
    {
      "anchor_id": "A1",
      "critical": "yes",
      "claim": "The workflow owner doc and packet template now share one elastic packet layout with explicit implementer handoff fields.",
      "proof_classification": "automated-suite-provable",
      "expected_evidence_path": ["workflow-owner-diff", "packet-template-diff", "just quality"]
    },
    {
      "anchor_id": "A2",
      "critical": "yes",
      "claim": "Important wave claims now allocate proof through a single packet-local proof plan instead of scattered checklist and command sections.",
      "proof_classification": "automated-suite-provable",
      "expected_evidence_path": ["proof-plan-diff", "review-governance-diff", "just quality"]
    }
  ]
}
```

## Durable Audit Record

```json
{
  "wave_audit_record": {
    "overall_disposition": "execution-ready",
    "planning_gate": {
      "review_mode": "quality_guard",
      "disposition": "APPROVE",
      "recorded_at": "2026-04-09",
      "summary": "Planning approved after packet shape, proof allocation, and implementer autonomy envelopes were made explicit enough for bounded delegation without reopening strategic decisions.",
      "planning_critic": {
        "review_mode": "planning_critic",
        "disposition": "APPROVE",
        "recorded_at": "2026-04-09",
        "summary": "Example critic provenance."
      }
    },
    "acceptance_audits": [
      {
        "anchor_id": "A1",
        "status": "not-audited-yet",
        "review_proof_posture": "Template and owner alignment approved; execution and final proof pending.",
        "scheduled_follow_up": "covered by active wave packet"
      },
      {
        "anchor_id": "A2",
        "status": "not-audited-yet",
        "review_proof_posture": "Proof-plan adoption approved in planning; execution and final proof pending.",
        "scheduled_follow_up": "covered by active wave packet"
      }
    ]
  }
}
```

## References

- `skills/initiatives-workflow/references/initiatives-workflow.md`
- `skills/initiatives-workflow/assets/wave-execution.md`
- `skills/code-review/references/review-governance.md`
