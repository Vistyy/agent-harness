# Wave sample-proof-allocation-1 Execution Packet

Ephemeral example. Create only after durable wave brief is
`**Status:** execution-ready`.

Linked durable brief:

- `docs-ai/docs/initiatives/waves/sample-proof-allocation-1.md`

One packet layout only. Vary depth, not shape.

## Scope And Execution Posture

- In-scope:
  - `engineering-harness/internal-harness-baseline/packet-shape-alignment`
  - `engineering-harness/internal-harness-baseline/proof-plan-adoption`
- Out-of-scope:
  - `engineering-harness/testing-cleanup/expanded-testing-skill`
- Non-obvious constraints:
  - `Keep one packet layout; do not introduce compact/standard/proof-heavy variants.`
- System-boundary trigger:
  - `not-triggered`
- Implementer delegation posture:
  - `implementer-eligible`
- Parent-only rationale:
  - `none`
- Frozen decisions:
  - `Proof allocation lives in one packet-local Proof Plan instead of separate checklist and command sections.`
- Planning Exceptions:
  - `none`

Rules:

- `implementer-eligible` is the preferred default for structured wave execution.
- `parent-only` requires an explicit reason in this packet.
- Task cards require material handoff boundaries and proof rows; starting
  files, existing patterns, and implementation notes are optional hints.
- the durable brief must already carry planning-review provenance in
  `planning_gate.planning_critic`; this packet never substitutes memory for
  planning.
- this packet never substitutes memory for planning.

## Task Plan

| Task slug | State | Dependencies | Outcome summary | Proof rows |
| --- | --- | --- | --- | --- |
| `engineering-harness/internal-harness-baseline/packet-shape-alignment` |  | `none` | `Owner doc and packet template align on one elastic packet shape.` | `P1` |
| `engineering-harness/internal-harness-baseline/proof-plan-adoption` |  | `engineering-harness/internal-harness-baseline/packet-shape-alignment` | `Planning and review consume one proof allocation structure.` | `P2` |

### `engineering-harness/internal-harness-baseline/packet-shape-alignment`

- Outcome:
  - `Packet owner doc and template describe same section shape and handoff fields.`
- In scope:
  - `workflow owner-doc edits`
  - `packet template edits`
- Out of scope:
  - `execution/runtime product behavior changes`
- Owned files and surfaces:
  - `skills/initiatives-workflow/references/initiatives-workflow.md`
  - `skills/initiatives-workflow/assets/wave-execution.md`
- Touched owner/component integrity:
  - `acceptable; task touches one workflow owner and aligns owner doc, packet template, and proof rows.`
- Starting files and symbols (optional):
  - `skills/initiatives-workflow/references/initiatives-workflow.md`
  - `skills/initiatives-workflow/assets/wave-execution.md`
- Existing patterns to follow (optional):
  - `skills/initiatives-workflow/assets/wave-brief.example.md`
- Locked invariants:
  - `execution-ready packets remain implementation-only`
  - `System-Boundary Architecture Disposition stays absent when not triggered`
- Allowed local implementer decisions:
  - `section wording and local example density`
  - `small template factoring choices that do not change packet shape`
- Stop-and-handback triggers:
  - `need for a second packet shape`
  - `need to reopen execution-ready gate semantics outside this owner doc change`
- Implementation notes (optional):
  - `Prefer denser sections over more section count.`
- Proof rows:
  - `P1`
- Deferred follow-up:
  - `none`

### `engineering-harness/internal-harness-baseline/proof-plan-adoption`

- Outcome:
  - `Planning/review surfaces require owner layer, exact proof, and counterfactual regression probes.`
- In scope:
  - `planning-intake`
  - `review-governance`
  - `planning_critic` routing triplet
- Out of scope:
  - `new testing skill creation`
- Owned files and surfaces:
  - `skills/planning-intake/SKILL.md`
  - `skills/code-review/references/review-governance.md`
  - `adapters/codex/agents/planning-critic.toml`
- Touched owner/component integrity:
  - `acceptable; task touches planning/review governance surfaces and keeps proof allocation owned by the packet contract.`
- Starting files and symbols (optional):
  - `skills/planning-intake/SKILL.md`
  - `skills/code-review/references/review-governance.md`
  - `adapters/codex/agents/planning-critic.toml`
- Existing patterns to follow (optional):
  - `skills/initiatives-workflow/assets/wave-execution.md`
- Locked invariants:
  - `planning_critic remains critic only, not final approver`
- Allowed local implementer decisions:
  - `exact wording for plan-pressure guidance`
  - `which existing sentences to tighten vs delete`
- Stop-and-handback triggers:
  - `need to reopen review-mode topology`
  - `need for a new durable worker role`
- Implementation notes (optional):
  - `Prefer reject criteria that attack underfed implementer handoff and weak proof posture.`
- Proof rows:
  - `P2`
- Deferred follow-up:
  - `engineering-harness/testing-cleanup/expanded-testing-skill`

## Proof Plan

```json
{
  "proof_plan": [
    {
      "proof_id": "P1",
      "task_slug": "engineering-harness/internal-harness-baseline/packet-shape-alignment",
      "anchor_ids": ["A1"],
      "claim": "The workflow owner doc and packet template now share one elastic packet layout with explicit implementer handoff fields.",
      "material_variants": ["owner-doc", "packet-template"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "doc-only",
      "exact_proof": [
        "Inspect the initiatives-workflow owner doc and the wave-execution template diff",
        "Run `just quality`"
      ],
      "expected_evidence": [
        "workflow-owner-diff",
        "packet-template-diff",
        "just quality"
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "The owner doc and template keep different section layouts or omit implementer handoff fields.",
        "failing_assertion_or_artifact": "Doc/template diff review would show drift; final review would reject owner-template mismatch."
      },
      "status": "planned"
    },
    {
      "proof_id": "P2",
      "task_slug": "engineering-harness/internal-harness-baseline/proof-plan-adoption",
      "anchor_ids": ["A2"],
      "claim": "Important wave claims now allocate proof through a single packet-local proof plan instead of scattered checklist and command sections.",
      "material_variants": ["planning-skill", "review-owner", "role-wrapper"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "doc-only",
      "exact_proof": [
        "Inspect planning-intake, review-governance, and planning_critic diff",
        "Run `just quality`"
      ],
      "expected_evidence": [
        "proof-plan-diff",
        "review-governance-diff",
        "planning-critic-routing-diff",
        "just quality"
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Proof classification exists in prose, but the packet still scatters owner layer, exact proof, and counterfactuals across multiple sections.",
        "failing_assertion_or_artifact": "Proof-plan review would show missing owner layer or exact proof rows, and planning-gate review would reject under-specified proof allocation."
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

- `engineering-harness/testing-cleanup/expanded-testing-skill` after packet/proof-plan changes are exercised in real planning work

### Contradiction Sweep

```json
{
  "contradiction_sweep": [
    {
      "scope": "P1",
      "brief_alignment": "aligned",
      "durable_doc_alignment": "aligned",
      "packet_alignment": "aligned",
      "notes": "none"
    },
    {
      "scope": "P2",
      "brief_alignment": "aligned",
      "durable_doc_alignment": "aligned",
      "packet_alignment": "aligned",
      "notes": "none"
    }
  ]
}
```

### Resume Cursor

- Next task: `engineering-harness/internal-harness-baseline/packet-shape-alignment`
- Rationale: `It establishes packet owner/template contract before planning/review surfaces consume it.`
