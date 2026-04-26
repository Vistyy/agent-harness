# Wave <wave-id>

**Status:** execution-ready

## User objective

<one plain-language statement of the concrete user or operator outcome this wave closes>

## Problem

<why this wave exists>

## Objective

<what changes when wave succeeds>

## In Scope

- `<task-slug-1>`
- `<task-slug-2>`

## Out Of Scope

- `<explicit defer>`

## Constraints

- `<constraint>`

## Risks

- `<risk or dependency>`

## Execution Tasks

- `<task-slug-1>`
- `<task-slug-2>`

## Acceptance Anchors

```json
{
  "acceptance_anchors": [
    {
      "anchor_id": "A1",
      "critical": "yes",
      "claim": "<short claim summary>",
      "proof_classification": "<automated-suite-provable | runtime-provable | multi-proof-required | not-reliably-provable-with-current-harness>",
      "expected_evidence_path": ["<diff-or-artifact-ref>", "<command-or-proof-ref>"]
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
      "recorded_at": "<YYYY-MM-DD>",
      "summary": "<planning gate summary>",
      "planning_critic": {
        "review_mode": "planning_critic",
        "disposition": "APPROVE",
        "recorded_at": "<YYYY-MM-DD>",
        "summary": "<planning critic summary>"
      }
    },
    "acceptance_audits": [
      {
        "anchor_id": "A1",
        "status": "not-audited-yet",
        "review_proof_posture": "execution-ready planning approved; implementation and proof pending",
        "scheduled_follow_up": "covered by active wave packet"
      }
    ]
  }
}
```

## References

- `<owner doc / prior wave / key code path>`
