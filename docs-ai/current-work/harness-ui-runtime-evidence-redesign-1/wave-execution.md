# Wave harness-ui-runtime-evidence-redesign-1 Execution Packet

## Scope And Execution Posture

- Original objective:
  - Redesign the reusable harness flow for UI runtime evidence so broad UI work
    cannot be approved by checklist fulfillment alone. UI approval must require
    screenshot-led critical design judgment, constructive findings, and an
    explicit ship-quality verdict.
- Accepted reductions:
  - none.
- Residual gaps:
  - none.
- In-scope:
  - `harness/runtime-evidence/ui-design-gate-boundary-contract`
  - `harness/runtime-evidence/screenshot-artifact-sufficiency-gate`
  - `harness/review/final-ui-closeout-screenshot-inspection-contract`
  - `harness/evals/regression-case-bad-ui-must-reject`
- Out-of-scope:
  - Project-specific redesign implementation.
  - Replacing project design truth with generic harness taste.
  - Backend/runtime correctness proof unrelated to UI quality.
- Non-obvious constraints:
  - Runtime evidence must not be allowed to approve broad UI design quality
    through numeric design-fidelity scoring alone.
  - Design approval must remain anchored in `user-apps-design` and project
    design anchors, not hidden inside browser/mobile proof mechanics.
  - Reports must stay compact but must include concrete visual findings when
    blocking or approving with issues.
  - Depends on `harness-strict-validation-governance-1` for blocking gate
    semantics and packet `Required Gates` schema; that dependency is done.
  - `design_judge` must be present on pre-selection routing and authorization
    surfaces, not only inside agent prompt bodies.
  - Prompt/config files alone do not prove callability. If the active adapter
    cannot expose `design_judge` as an invocable role, stop and record the
    adapter/runtime blocker instead of claiming the gate exists.
- System-boundary trigger:
  - `triggered`
- Implementer delegation posture:
  - `implementer-eligible`
- Parent-only rationale:
  - `none`
- Frozen decisions:
  - UI runtime proof and UI design approval are separate gates.
  - `runtime-proof` owns runtime claim maps, entrypoint fidelity, screenshot
    artifact sufficiency, and `pass | reject | blocked` completion impact.
  - `user-apps-design` owns product-grade visual quality criteria and hard
    design blockers.
  - `webapp-testing` and `mobileapp-testing` own screenshot/contact-sheet
    capture mechanics only.
  - `code-review`/`final_reviewer` must verify runtime evidence and
    `design_judge` cover the screenshots/contact sheets that support the final
    claim.
  - Add a dedicated `design_judge` role for screenshot-led product UI design
    approval. It owns visual verdicts and uses `user-apps-design`.
  - `quality_guard` remains the implementation quality gate. It verifies that
    required `runtime_evidence` and `design_judge` gates exist and cover the
    claim; it does not perform runtime proof or visual design judgment.
  - `runtime_evidence` proves live behavior and artifact sufficiency for
    design handoff; it does not approve product-grade visual quality.
  - Design verdicts are `pass`, `reject`, and `blocked`.
  - Broad UI readiness remains blocked unless `design_judge` returns `pass`.
  - The old `20/20`-style design-fidelity score cannot be sufficient for
    approval and should be removed or demoted to non-authoritative observations.
- Planning Exceptions:
  - none.

## Required Gates

| Claim | Required gate | Owner | Proof/artifacts | Blocks when |
| --- | --- | --- | --- | --- |
| Live UI behavior and artifact sufficiency are proven | runtime proof | `runtime_evidence` | command/run id, route/screen/state, viewport/device, logs, screenshot/contact-sheet paths; durable e2e artifacts are valid only when they exercise the same claim through a faithful entrypoint | missing, rejected, blocked, stale, not real-entrypoint/equivalent, or narrower than claim |
| Product-facing UI design is shippable | design approval | `design_judge` | screenshots/contact sheets, design anchors, visible findings | missing anchors/artifacts, reject, blocked, score-only, selector-only, finding-free, or narrower than claim |
| Implementation satisfies owner quality and gate coverage | implementation review | `quality_guard` | diff, tests, proof rows, runtime/design gate reports | owner defect, proof gap, missing required gate, rejected/blocked/stale gate |
| Final UI readiness claim is supportable | final closeout review | `final_reviewer` and `verification-before-completion` | all required gate reports and final proof summary | claim exceeds proof/review/gate coverage |

## Task Plan

### harness/runtime-evidence/ui-design-gate-boundary-contract

- State:
  - `blocked`
- Outcome:
  - Harness docs and agent instructions separate live runtime proof from
    product-grade UI design approval, while preserving blocking completion
    semantics for both gates.
- In scope:
  - `skills/runtime-proof/SKILL.md`
  - `skills/user-apps-design/SKILL.md`
  - `skills/user-apps-design/references/design-quality-rubric.md`
  - `skills/verification-before-completion/SKILL.md`
  - `skills/code-review/references/review-governance.md`
  - `agents/roles.md`
  - `skills/subagent-orchestration/SKILL.md`
  - `skills/subagent-orchestration/agents/openai.yaml`
  - `AGENTS.md`
  - `adapters/codex/config.toml`
  - `adapters/codex/agents/design-judge.toml`
  - `adapters/codex/agents/runtime-evidence.toml`
  - `adapters/codex/agents/quality-guard.toml`
  - `adapters/github-copilot/agents/design_judge.agent.md`
  - `adapters/github-copilot/agents/runtime_evidence.agent.md`
  - `adapters/github-copilot/agents/quality_guard.agent.md`
- Out of scope:
  - Changing existing role responsibilities beyond isolating their gate
    coverage obligations.
- Owned files and surfaces:
  - Runtime proof policy, design-quality ownership, runtime-evidence prompt
    contracts, subagent role routing, and adapter authorization surfaces.
- Touched owner/component integrity:
  - acceptable; the existing owner split from `harness-ui-design-quality` and
    `harness-runtime-proof-design-refactor` remains coherent if runtime proof
    consumes design anchors but cannot be sole design approver.
- Locked invariants:
  - Functional assertions, selector checks, logs, DOM order, snapshots, and
    numeric design scores cannot approve a UI-quality claim without artifact
    inspection and design-gate verdict.
  - Runtime evidence may reject obvious runtime-visible contradictions or block
    missing/stale artifacts, but product-grade visual approval belongs to
    `design_judge`.
  - `design_judge` must reject broad UI claims supported only by selectors,
    text, numeric score, or screenshot path without visible findings.
  - `quality_guard` must block when required `runtime_evidence` or
    `design_judge` gates are missing, rejected, blocked, stale, or narrower
    than the implementation claim.
  - `design_judge` trigger and authorization must live in pre-selection
    surfaces: `AGENTS.md`, `agents/roles.md`, adapter role registry/config, and
    `subagent-orchestration`.
- Allowed local implementer decisions:
  - Exact wording and section placement.
  - Whether to remove numeric scoring entirely or demote it to optional
    non-authoritative notes.
  - Exact wording for the `design_judge` report fields, provided verdict,
    artifact paths, visible findings, and completion impact remain explicit.
- Stop-and-handback triggers:
  - Any change that makes `runtime_evidence` the only owner of broad design
    approval.
  - Any need to make an existing role perform `design_judge` responsibility
    instead of adding the dedicated role.
  - Any unresolved conflict between project design truth and generic harness
    visual blockers.
  - Any implementation path that folds visual design judgment back into
    `runtime_evidence`, `quality_guard`, or `final_reviewer`.
  - Adapter/runtime support cannot expose `design_judge` as an invocable role.
- Proof rows:
  - `P1`
- Deferred follow-up:
  - none

### harness/runtime-evidence/screenshot-artifact-sufficiency-gate

- State:
  - `done`
- Outcome:
  - UI-quality runtime handoffs and reports require screenshots/contact sheets
    for every claimed route/state/viewport/device and block when artifacts are
    missing, stale, cropped away from the claimed surface, or not tied to the
    runtime claim. Product-grade visual judgment belongs to `design_judge`.
- In scope:
  - `skills/runtime-proof/SKILL.md`
  - `skills/webapp-testing/references/browser-runtime-proof-workflow.md`
  - `skills/mobileapp-testing/references/mobile-runtime-proof-workflow.md`
  - `adapters/codex/agents/runtime-evidence.toml`
  - `adapters/github-copilot/agents/runtime_evidence.agent.md`
- Out of scope:
  - Playwright or emulator implementation changes unless required by existing
    tests.
- Owned files and surfaces:
  - Runtime claim map artifact requirements, browser/mobile evidence mechanics,
    runtime-evidence report contract.
- Touched owner/component integrity:
  - acceptable; platform skills own capture mechanics, while runtime-proof owns
    verdict impact and design gate handoff requirements.
- Locked invariants:
  - A UI runtime `pass` must list artifact paths, viewport/device, inspected
    state, and whether artifacts are sufficient for `design_judge` handoff.
  - Missing, stale, or mis-scoped screenshots for a UI-quality claim yields
    `blocked`.
  - Runtime evidence may reject runtime-visible layout contradictions, but it
    does not approve or reject product-grade visual design quality.
  - `behavioral verdict: pass` is not a UI-ready pass when `design_judge` is
    missing, rejected, blocked, stale, or narrower than the UI claim.
- Allowed local implementer decisions:
  - Contact-sheet naming and exact report field names.
  - How many screenshots are required for responsive coverage, provided every
    claimed viewport/device/state is inspectable.
- Stop-and-handback triggers:
  - Report contract requires runtime evidence to decide visual ship quality.
  - Existing tests or validation encode the old numeric score as authoritative.
- Proof rows:
  - `P2`
- Deferred follow-up:
  - none

### harness/review/final-ui-closeout-screenshot-inspection-contract

- State:
  - `done`
- Outcome:
  - Final closeout review blocks UI redesign completion unless runtime evidence
    and `design_judge` both cover the final claim.
- In scope:
  - `skills/code-review/SKILL.md`
  - `skills/code-review/references/review-governance.md`
  - `skills/verification-before-completion/SKILL.md`
  - `adapters/codex/agents/final-reviewer.toml`
  - `adapters/github-copilot/agents/final_reviewer.agent.md`
- Out of scope:
  - Changing final reviewer role identity.
- Owned files and surfaces:
  - Final review output contract and completion-claim gate.
- Touched owner/component integrity:
  - acceptable; final review already owns approval scope, and this adds a
    UI-specific evidence requirement without changing runtime verdict terms.
- Locked invariants:
  - Final reviewer verifies runtime and design gate coverage; it does not
    replace `runtime_evidence` or `design_judge`.
  - Final reviewer must block if runtime/design proof is missing, rejected,
    blocked, stale, too narrow, or not tied to the final claim.
  - Verification-before-completion cannot claim UI design readiness without
    matching runtime evidence and `design_judge` pass.
- Allowed local implementer decisions:
  - Exact report field name and placement.
- Stop-and-handback triggers:
  - Any proposal that lets final review replace runtime proof or design
    judgment instead of verifying those gate reports.
- Proof rows:
  - `P3`
- Deferred follow-up:
  - none

### harness/evals/regression-case-bad-ui-must-reject

- State:
  - `done`
- Outcome:
  - Harness validation includes a regression case proving a functional
    selector-passing but visibly poor UI cannot receive UI design approval.
- In scope:
  - `tests/**`
  - harness validator
  - A `design_judge` eval fixture under the existing test/fixture structure or
    a new lightweight fixture path owned by validation.
- Out of scope:
  - Full screenshot computer-vision scoring.
  - Project-specific runtime reproduction.
- Owned files and surfaces:
  - Harness validation tests, prompt/report contract checks, and design_judge
    eval fixture artifacts.
- Touched owner/component integrity:
  - acceptable; validation should test the contract and hard blockers, not
    attempt subjective automated beauty scoring.
- Locked invariants:
  - The fixture must model the triggering failure: a shopping-list UI that
    passes functional assertions while visible composition, hierarchy, density,
    and product fit are unacceptable.
  - The test must fail if a runtime/design report can pass from selectors or
    numeric score alone.
  - The eval input is a bad-shopping-list screenshot/contact-sheet artifact
    plus metadata: screen/state, viewport/device, design anchors, and a
    functional behavior pass from runtime proof.
  - The eval expected output is a `design_judge` `reject` with visible findings
    for oversized low-information rows, detached search/action grouping, weak
    hierarchy, scaffold-like material, and non-shippable composition.
  - A schema/report test may validate output shape, but the required regression
    proof must include an executable `design_judge` fixture invocation that
    reads the bad-UI artifact path, design anchors, runtime functional pass,
    and expected `reject` verdict with visible findings.
  - The wave cannot claim the bad-UI judgment proof from manual notes,
    schema-only validation, score-only output, or prompt readback.
- Allowed local implementer decisions:
  - Exact fixture path and script name, provided the command is executable and
    asserts the expected `reject` plus visible findings.
- Stop-and-handback triggers:
  - Proving the gate requires unavailable screenshot analysis infrastructure.
  - Existing validation architecture cannot host the regression without a
    broader test harness redesign.
- Proof rows:
  - `P4`
- Deferred follow-up:
  - none

## Proof Plan

```json
{
  "proof_plan": [
    {
      "proof_id": "P1",
      "task_slug": "harness/runtime-evidence/ui-design-gate-boundary-contract",
      "anchor_ids": ["A1", "A2"],
      "claim": "Runtime evidence cannot be the sole approval path for broad UI design quality; product-grade visual approval is a separate design_judge gate with blocking completion impact.",
      "material_variants": ["web UI", "mobile UI", "internal/admin UI without design claim", "quality_guard gate-coverage review", "final_reviewer closeout coverage"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-contract/role-registry/adapter-routing",
      "exact_proof": [
        "Readback of updated runtime-proof, user-apps-design, review-governance, verification-before-completion, AGENTS.md, agents/roles.md, adapter role registry/config, subagent-orchestration, runtime-evidence prompt, design_judge prompt, quality_guard prompt, and final_reviewer prompt contracts showing isolated responsibilities, pre-selection design_judge routing, and no authoritative numeric design score path.",
        "uv run python scripts/validate_harness.py",
        "uv run python adapters/codex/assert_prompt_input_agents.py docs-ai/current-work/harness-ui-runtime-evidence-redesign-1/artifacts/design-judge-prompt-input.json design_judge",
        "rg -n \"20/20|design-fidelity score|per-dimension scores|numeric design\" skills adapters docs-ai"
      ],
      "expected_evidence": [
        "Docs state runtime evidence must block missing artifacts and cannot approve UI design by selector checks or numeric score alone.",
        "design_judge instructions own screenshot-led product UI approval and reject selector-only, score-only, and finding-free screenshot approval.",
        "AGENTS.md, agents/roles.md, adapter config, and subagent-orchestration expose design_judge before prompt selection.",
        "Fresh Codex prompt-input registry proof shows design_judge is exposed to the adapter runtime.",
        "Harness validation rejects missing design_judge role registration, authorization, or required prompt/report contract terms.",
        "quality_guard instructions verify required gate coverage without performing runtime proof or visual design judgment.",
        "Search output shows no remaining authoritative numeric scoring contract for UI approval."
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Runtime evidence keeps a numeric design-fidelity score as sufficient approval for broad UI redesign, quality_guard/final_reviewer performs visual design judgment instead of verifying design_judge, or design_judge exists only in docs/prompts without pre-selection adapter exposure.",
        "failing_assertion_or_artifact": "Readback, rg, validation, or assert_prompt_input_agents.py fails on score-based approval language, mixed-role design judgment, missing design_judge registration/authorization, or absent fresh prompt-input role exposure."
      },
      "status": "blocked"
    },
    {
      "proof_id": "P2",
      "task_slug": "harness/runtime-evidence/screenshot-artifact-sufficiency-gate",
      "anchor_ids": ["A3"],
      "claim": "UI runtime evidence requires screenshot/contact-sheet artifacts sufficient for design_judge handoff and does not approve product-grade visual design quality.",
      "material_variants": ["desktop viewport", "mobile viewport/device", "reachable loading/empty/error states when claimed"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "runtime-web/runtime-mobile/doc-contract",
      "exact_proof": [
        "Readback of updated runtime-proof plus browser/mobile runtime workflow docs proving screenshot/contact-sheet requirements for UI-quality claims.",
        "uv run pytest tests/test_validate_harness.py -q"
      ],
      "expected_evidence": [
        "Runtime report contract requires artifact path, screen/state, viewport/device, artifact freshness/scope, and design_judge handoff sufficiency.",
        "Tests pass with contract validation for required screenshot-backed runtime evidence fields."
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "A UI runtime report can pass with selectors, DOM assertions, or snapshots and no screenshots/contact sheets, or claims visual design approval itself.",
        "failing_assertion_or_artifact": "Validator or tests reject missing artifact-inspection fields and reject runtime-evidence design approval language."
      },
      "status": "done"
    },
    {
      "proof_id": "P3",
      "task_slug": "harness/review/final-ui-closeout-screenshot-inspection-contract",
      "anchor_ids": ["A4"],
      "claim": "Final UI closeout cannot approve broad UI design readiness without runtime_evidence and design_judge reports that match the final claim.",
      "material_variants": ["final_reviewer", "verification-before-completion"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "review/verification/doc-contract",
      "exact_proof": [
        "Readback of updated code-review, review-governance, verification-before-completion, and final-reviewer prompt contracts.",
        "uv run python scripts/validate_harness.py"
      ],
      "expected_evidence": [
        "Final review output contract verifies runtime_evidence and design_judge coverage or blocks closeout.",
        "Verification gate rejects UI readiness claims when runtime/design gate evidence is missing or narrower than the final claim."
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Final reviewer approves UI closeout by replacing runtime_evidence or design_judge with its own unsupported judgment.",
        "failing_assertion_or_artifact": "Contract readback or validation catches missing runtime/design gate coverage requirement."
      },
      "status": "done"
    },
    {
      "proof_id": "P4",
      "task_slug": "harness/evals/regression-case-bad-ui-must-reject",
      "anchor_ids": ["A5"],
      "claim": "A functional but ugly/scaffold-like shopping-list UI cannot receive UI design approval and cannot pass via selector-only, score-only, or finding-free screenshot evidence.",
      "material_variants": ["selector-passing bad UI", "missing screenshot", "score-only approval", "design_judge eval artifact"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "test/ad-hoc-validation",
      "exact_proof": [
        "uv run pytest tests/test_validate_harness.py -q",
        "uv run python scripts/validate_harness.py",
        "uv run python scripts/eval_design_judge_fixture.py tests/fixtures/design_judge/bad-shopping-list.json",
        "just quality-fast"
      ],
      "expected_evidence": [
        "Regression fixture includes a shopping-list screenshot/contact-sheet artifact, functional pass evidence, design anchors, and design_judge rejection evidence.",
        "Contract tests reject selector-only pass, score-only approval, and screenshot-without-findings report variants.",
        "Quality-fast passes after docs, prompts, and validation are consistent.",
        "The executable design_judge fixture command asserts expected reject, screenshot artifact path, functional-pass context, design anchors, and concrete visible findings for oversized rows, detached search/action grouping, weak hierarchy, scaffold-like material, and non-shippable composition."
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "A report marks a generic, low-density, visually incoherent shopping-list UI as pass because selectors and console checks pass, or claims judgment proof from schema tests alone.",
        "failing_assertion_or_artifact": "Contract tests fail weak report shape, and the executable design_judge fixture command fails when reject verdict, artifact path, anchors, or visible findings are missing."
      },
      "status": "done"
    }
  ]
}
```

## Execution State

### Decisions And Blockers

| Type | Item | Action | Owner |
| --- | --- | --- | --- |
| `decision` | Runtime evidence versus design approval ownership | Closed: separate gates; runtime evidence proves live behavior and artifact sufficiency, `design_judge` owns product-grade visual approval, and `quality_guard` verifies gate coverage only. | agent |
| `decision` | Separate subagent role | Closed: add `design_judge` role for screenshot-led product UI approval. | agent |
| `decision` | Artifact required for UI approval | Closed: inspected screenshot/contact sheet tied to claimed surface/state/viewport/device. | agent |
| `decision` | Design verdicts and impact | Closed: `design_judge` returns `pass`, `reject`, or `blocked`; only `pass` can support broad UI completion. | agent |
| `decision` | Regression shape | Closed: bad-but-functional shopping-list UI must reject/block despite passing selectors. | agent |
| `blocker` | Active adapter callability proof | Repo registration, validation, and prompt contracts are implemented, but this session's live `spawn_agent` schema does not expose `design_judge`; P1 cannot close without fresh prompt-input proof or adapter/runtime exposure. | adapter/runtime |

### Technical Debt And Deferred Follow-Up

- none

## System-Boundary Architecture Disposition

- Why triggered:
  - The wave changes approval authority and handoff contracts between runtime
    proof, design quality, platform mechanics, review, verification, and agent
    prompts.
- Planning disposition:
  - Keep existing owner split and add an explicit UI design approval gate.
    Runtime evidence remains the live validation guard, not the sole design
    critic.
- Execution stop rule:
  - Stop if the adapter/runtime cannot expose the new authorized
    `design_judge` role, moves design ownership into platform mechanics, or
    lets runtime evidence approve broad UI design by score/checklist alone.
- Changed authorities or contracts:
  - `runtime-proof`: UI runtime reports must include screenshot-backed artifact
    sufficiency for design handoff, not product-grade design approval.
  - `design_judge`: screenshot-led product UI design approval gate.
  - `user-apps-design`: hard visual blockers and design rubric consumed by
    `design_judge`.
  - `webapp-testing`/`mobileapp-testing`: screenshot/contact-sheet capture
    mechanics and viewport/device evidence.
  - `code-review`/`final_reviewer`: final UI closeout verifies runtime and
    design gate coverage.
  - `quality_guard`: in-thread implementation review verifies required gates
    exist and cover the claim; it does not perform those gates.
  - `verification-before-completion`: final claim cannot exceed runtime,
    design_judge, and review evidence.
- Single owner after change:
  - Runtime verdict semantics: `runtime-proof`.
  - Product UI design approval: `design_judge`.
  - Product UI design rubric: `user-apps-design`.
  - In-thread implementation gate: `quality_guard`.
  - Final review approval scope: `code-review`.
  - Completion claim assembly: `verification-before-completion`.
- Public write paths:
  - Skill docs, global/subagent authorization surfaces, role registry, adapter
    role registry/config, provider routing docs/prompts, role prompt files,
    validation/tests, executable eval fixture/script, prompt-input proof
    artifact, and wave state only.
- Read-repair paths:
  - A failed `design_judge` gate returns concrete visible findings to the
    implementer; repair occurs in the target project, then runtime/design proof
    reruns on fresh screenshots.
- Forbidden bypass paths:
  - Selector-only UI approval.
  - DOM/snapshot-only UI approval.
  - Numeric score-only UI approval.
  - Final review approval without artifact inspection.
  - Treating generic harness taste as a substitute for project design anchors.
- Rejected alternatives:
  - Make `runtime_evidence` a full design critic: rejected because it recreates
    the current failure mode by mixing live proof with aesthetic approval.
  - Make `quality_guard` the visual design gate: rejected because it muddles
    implementation quality review with product UI design approval.
  - Rely on automated screenshot scoring: rejected because the required failure
    is judgmental and artifact-led, not reliably solved by image metrics.
- Why not artificially narrowed:
  - The packet covers runtime proof, design gate, final review, verification,
    and regression proof required by the original harness failure.
- Stable-to-extend expectation:
  - A future dedicated `design_critic` role can wrap the same gate contract
    without moving ownership or weakening runtime proof semantics.
