# Wave harness-thin-design-judge-contract-1 Execution Packet

## Scope And Execution Posture

- Original objective:
  - Slim the reusable harness UI/design workflow so the harness exposes only a
    thin blocking `design_judge` visual-quality gate, while projects own design
    method, taste, mockup requirements, before/after comparison, preservation
    language, and generated-image workflow choices.
- Accepted reductions:
  - none
- Residual gaps:
  - none intended after execution; completed UI wave brief deletion remains
    separate unless this wave proves a specific brief has a full successor.
- In-scope:
  - `thin-ui-design-owner-contract`
  - `thin-role-adapter-contracts`
  - `thin-validation-and-review-coverage`
- Out-of-scope:
  - Defining project-specific design taste or workflow.
  - Requiring `imagegen`, generated mockups, before/after comparisons, visual
    inventories, critique loops, Impeccable, Figma, or any other project-local
    design method globally.
  - Removing `runtime_evidence` for non-trivial live behavior claims.
  - Deleting completed UI wave briefs without successor review.
- Non-obvious constraints:
  - The harness may require the handoff to include whatever artifacts the
    project design source requires; it must not decide which design method every
    project uses.
  - Adapter prompts should carry role-local instructions and consequences, not
    route selection doctrine or another owner's design criteria.
  - Validation should protect exact high-risk thin-contract terms, not
    project-specific or preservation-specific doctrine.
- System-boundary trigger:
  - `triggered`
- Implementer delegation posture:
  - `implementer-eligible`
- Parent-only rationale:
  - `none`
- Frozen decisions:
  - `design_judge` is a blocking visual-quality gate for broad product UI
    claims.
  - `runtime_evidence` proves live behavior when required; it does not approve
    visual quality.
  - Projects own when generated mockups, before/after comparison, visual
    inventories, critique loops, preservation anchors, or replacement approval
    rules are required.
- Planning Exceptions:
  - `none`

## Required Gates

| Claim | Required gate | Owner | Proof/artifacts | Blocks when |
| --- | --- | --- | --- | --- |
| The reusable UI design contract is thin and project-owned for method/taste. | Successor owner review | `documentation-stewardship` / `user-apps-design` | Diff readback plus review | Harness prescribes mockups, before/after comparison, generated images, preservation taxonomy, or project taste |
| `design_judge` adapters contain only role-local visual gate instructions. | Adapter boundary review | `harness-governance` / `subagent-orchestration` | Codex/Copilot adapter diff and validator tests | Adapter prompt performs routing, runtime proof, code review, debugging, app execution, or project design method ownership |
| Review and completion gates require `design_judge` coverage without duplicating design method. | Review/verification coverage review | `code-review` / `verification-before-completion` | Skills/adapters diff and focused validator tests | Final review or completion can approve broad UI without required visual gate coverage, or they decide visual quality themselves |
| Runtime evidence remains a live behavior verifier, not a default visual gate. | Runtime boundary review | `runtime-proof` | Runtime skill/adapter readback and validation | Runtime evidence is required for visual-only UI readiness or allowed to approve product-grade design |
| Validation protects thin-contract drift. | Static proof | `harness-governance` | `uv run pytest tests/test_validate_harness.py -k 'design_judge or final_reviewer or ui_approval or runtime_evidence_ui_default'` and `uv run python ./scripts/validate_harness.py` | Protected terms still require preservation-specific doctrine or miss thin role boundaries |

## Task Plan

### `thin-ui-design-owner-contract`

- State:
  - `blank`
- Outcome:
  - `user-apps-design` states only the reusable UI completion contract:
    project design source or narrowed claim, screenshot/contact-sheet artifacts,
    `design_judge` pass, and project ownership of design method/taste.
- In scope:
  - `skills/user-apps-design/SKILL.md`
  - direct consumers that must point to the owner without copying method
- Out of scope:
  - Project-specific workflows and required mockup/comparison choices.
- Owned files and surfaces:
  - Reusable UI design completion contract.
- Touched owner/component integrity:
  - Acceptable only if one owner remains for the thin visual gate and
    project-local method ownership is explicit.
- Locked invariants:
  - Broad UI visual quality cannot be approved by tests, selectors, logs,
    runtime evidence, code review, or final review alone.
  - Project design sources own mockups, image generation, before/after
    comparison, preservation, replacement approval, and taste.
  - Missing, contradictory, stale, or narrower project design-source coverage
    blocks broad visual approval.
- Allowed local implementer decisions:
  - Exact compact wording.
- Stop-and-handback triggers:
  - Need to prescribe a global design method.
  - Need to keep preservation-specific global terms as canonical doctrine.
- Proof rows:
  - `P1`
- Deferred follow-up:
  - `none`

### `thin-role-adapter-contracts`

- State:
  - `blank`
- Outcome:
  - Codex and Copilot role adapters state only local role boundaries and outputs
    for `design_judge`, `runtime_evidence`, `quality_guard`, and
    `final_reviewer` where touched.
- In scope:
  - `adapters/codex/agents/design-judge.toml`
  - `adapters/github-copilot/agents/design_judge.agent.md`
  - final reviewer / quality guard / runtime evidence adapters only if needed
    to align with the thin owner contract
- Out of scope:
  - Role selection doctrine beyond local "do not perform other role" boundaries.
- Owned files and surfaces:
  - Adapter-local role instructions.
- Touched owner/component integrity:
  - Acceptable only if adapters repeat local consequences without becoming the
    source of design method or runtime proof doctrine.
- Locked invariants:
  - `design_judge` inspects supplied visual artifacts and declared project
    design source only.
  - It does not run the app, review code, debug, prove runtime behavior, or
    invent design criteria.
  - It returns `pass`, `reject`, or `blocked` for visual quality only.
- Allowed local implementer decisions:
  - Exact compact role wording and output labels.
- Stop-and-handback triggers:
  - Adapter wording needs project design methodology.
  - Adapter wording makes `design_judge` responsible for runtime behavior or
    code quality.
- Proof rows:
  - `P2`
- Deferred follow-up:
  - `none`

### `thin-validation-and-review-coverage`

- State:
  - `blank`
- Outcome:
  - Validation and review/completion owners protect the thin contract without
    hard-coding preservation-specific global doctrine.
- In scope:
  - `./scripts/validate_harness.py`
  - `tests/test_validate_harness.py`
  - `skills/code-review/references/review-governance.md`
  - `skills/verification-before-completion/SKILL.md`
  - `skills/subagent-orchestration/SKILL.md`
  - runtime proof / runtime evidence surfaces only if drift appears
- Out of scope:
  - Subjective semantic lint or design taste validation.
- Owned files and surfaces:
  - Thin-contract validation and review coverage gates.
- Touched owner/component integrity:
  - Acceptable only if validation protects one-owner boundaries with exact
    high-risk terms and does not preserve obsolete detailed doctrine.
- Locked invariants:
  - Required visual gate coverage remains blocking.
  - Final review and completion verify coverage; they do not decide visual
    quality.
  - Runtime evidence remains live behavior proof and not visual approval.
- Allowed local implementer decisions:
  - Exact protected term strings.
- Stop-and-handback triggers:
  - Required proof would need subjective visual-quality lint.
  - Review/verification surfaces become duplicate design judges.
- Proof rows:
  - `P3`
- Deferred follow-up:
  - `none`

## Proof Plan

```json
{
  "proof_plan": [
    {
      "proof_id": "P1",
      "task_slug": "thin-ui-design-owner-contract",
      "anchor_ids": ["A1"],
      "claim": "The harness UI design owner is thin and leaves design method/taste to project-local sources.",
      "material_variants": ["imagegen mockups", "before/after comparison", "preservation language", "project design source coverage"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-only",
      "exact_proof": ["manual readback of skills/user-apps-design/SKILL.md during quality_guard and final_reviewer", "rg -n \"imagegen|before/after|preservation anchors|visual-language replacement|generic replacement\" skills adapters scripts tests docs-ai/docs/initiatives/waves/harness-thin-design-judge-contract-1.md"],
      "expected_evidence": ["The owner names project-local ownership for design methods and keeps only the visual gate contract; residual detailed terms are either removed, project-owned examples, or active wave state."],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Keep global requirements for generated mockups, before/after comparison, or preservation anchors.",
        "failing_assertion_or_artifact": "Review blocks duplicate project-design-method ownership."
      },
      "status": "planned"
    },
    {
      "proof_id": "P2",
      "task_slug": "thin-role-adapter-contracts",
      "anchor_ids": ["A2"],
      "claim": "Design judge adapters contain only thin visual-gate instructions and local role boundaries.",
      "material_variants": ["Codex adapter", "GitHub Copilot adapter"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": ["uv run pytest tests/test_validate_harness.py -k design_judge", "uv run python scripts/validate_harness.py"],
      "expected_evidence": ["Focused tests and validator protect artifact inspection, declared project design source coverage, visual-quality-only verdict, and no cross-role substitution."],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Adapter requires preservation anchors or generated mockups as global design method.",
        "failing_assertion_or_artifact": "Review blocks duplicate owner doctrine or validator rejects stale protected terms."
      },
      "status": "planned"
    },
    {
      "proof_id": "P3",
      "task_slug": "thin-validation-and-review-coverage",
      "anchor_ids": ["A3"],
      "claim": "Review, completion, runtime, and validation surfaces protect thin visual gate coverage without deciding design method.",
      "material_variants": ["final review", "verification before completion", "quality guard", "runtime evidence boundary", "validator terms"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "static-check",
      "exact_proof": ["uv run pytest tests/test_validate_harness.py -k 'final_reviewer or review_governance or ui_approval or runtime_evidence_ui_default'", "uv run python scripts/validate_harness.py", "agent-harness governance check --repo-root .", "just quality-fast"],
      "expected_evidence": ["Focused tests, validator, governance check, and quality-fast pass after preserving blocking design_judge coverage and runtime-evidence separation."],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Final review, completion, or runtime evidence can approve broad visual quality without design_judge coverage.",
        "failing_assertion_or_artifact": "Validator/test failure or review blocker."
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
| `decision` | Design method ownership | Projects own generated mockups, before/after comparison, preservation language, replacement approval, and taste. | agent |
| `decision` | Harness visual gate | Harness keeps a thin `design_judge` blocking gate over supplied artifacts and declared project design source. | agent |
| `decision` | Runtime evidence boundary | Runtime evidence remains live behavior proof and does not approve visual quality. | agent |

### Technical Debt And Deferred Follow-Up

- `none`

## System-Boundary Architecture Disposition

- Why triggered:
  - The wave changes reusable UI/design approval ownership, role adapter
    contracts, review/completion coverage, and validator terms.
- Planning disposition:
  - `user-apps-design` owns the thin visual completion contract. Projects own
    design method and taste. `design_judge` owns visual-quality verdicts over
    supplied artifacts. Review/completion owners verify coverage only.
    `runtime-proof` owns live behavior proof.
- Execution stop rule:
  - Stop if the change needs global design methodology, project-specific taste,
    subjective semantic lint, or removal of blocking visual gate coverage.
- Changed authorities or contracts:
  - UI design owner contract.
  - `design_judge` adapter role boundary.
  - Review/completion coverage wording.
  - Runtime evidence visual-approval boundary if touched.
  - Validator protected terms.
- Single owner after change:
  - Harness owns only the thin visual gate contract; project overlays own design
    method/taste; runtime-proof owns behavior proof.
- Public write paths:
  - `skills/user-apps-design/SKILL.md`
  - `skills/verification-before-completion/SKILL.md`
  - `skills/code-review/references/review-governance.md`
  - `skills/subagent-orchestration/SKILL.md`
  - `skills/runtime-proof/SKILL.md`
  - `adapters/**/agents/*design*`
  - `adapters/**/agents/*reviewer*`
  - `adapters/**/agents/*quality_guard*`
  - `adapters/**/agents/*runtime_evidence*`
  - `./scripts/validate_harness.py`
  - `tests/test_validate_harness.py`
- Read-repair paths:
  - Remaining completed UI wave briefs only for successor review; do not patch
    them as living doctrine.
- Forbidden bypass paths:
  - Treating `imagegen`, before/after comparison, or preservation anchors as
    global harness requirements.
  - Letting runtime evidence, tests, selectors, code review, quality guard, or
    final review approve visual quality.
  - Letting `design_judge` run the app, debug, review code, or invent design
    criteria.
- Rejected alternatives:
  - Keep current preservation-specific global terms: rejected as too much
    project-method doctrine.
  - Remove `design_judge`: rejected because broad UI visual quality still needs
    a blocking visual gate.
  - Make runtime evidence the UI gate: rejected because it proves behavior, not
    design quality.
- Why not artificially narrowed:
  - The scope includes the owner skill, role adapters, review/completion
    coverage, runtime boundary, and validation surfaces needed to keep the thin
    contract coherent.
- Stable-to-extend expectation:
  - Projects can adopt generated mockups, before/after comparisons,
    preservation anchors, Impeccable, or bespoke design workflows without
    changing the global harness contract.
