# Wave harness-runtime-evidence-live-use-contract-1 Execution Packet Draft

## Scope And Execution Posture

- Original objective:
  - Make `runtime_evidence` clearly own independent live-use verification
    beyond tests, code review, quality gates, and final review.
- Accepted reductions:
  - none.
- Residual gaps:
  - UI product-grade design approval remains in
    `harness-ui-runtime-evidence-redesign-1`.
- In-scope:
  - `harness/runtime-proof/live-use-owner-contract`
  - `harness/runtime-evidence/adapter-role-prompts`
  - `harness/orchestration/runtime-evidence-routing`
  - `harness/testing/e2e-runtime-proof-relationship`
  - `harness/runtime-evidence/interrupted-edit-sweep`
  - `harness/validation/runtime-evidence-live-use-drift`
- Out-of-scope:
  - `design_judge` role implementation.
  - Product-grade UI design approval.
  - Broad e2e framework changes.
  - Project-specific runtime recipes.
- Non-obvious constraints:
  - Keep the role mission compact and repeated only as trigger/local
    consequence.
  - Do not make runtime evidence write tests or perform quality/design review.
  - Do not make e2e artifacts the default replacement for live-use proof.
- System-boundary trigger:
  - `triggered`
- Implementer delegation posture:
  - `implementer-eligible`
- Parent-only rationale:
  - `none`
- Frozen decisions:
  - `runtime_evidence` stays as a separate role.
  - Runtime evidence is independent live-use verification beyond tests and
    reviews.
  - Implementers write e2e tests when the approved plan requires them.
  - Runtime evidence may consume e2e artifacts only when they prove the same
    runtime claim through a faithful entrypoint and inspectable evidence.
  - `quality_guard` and `final_reviewer` verify gate coverage; they do not
    replace runtime evidence.
- Planning Exceptions:
  - none

## Required Gates

| Claim | Required gate | Owner | Proof/artifacts | Blocks when |
| --- | --- | --- | --- | --- |
| Runtime evidence mission is clear and isolated | planning review | `planning_critic`, `quality_guard` | wave brief, draft packet, role-boundary readback | role owns design/quality/test authoring, or trigger remains generic |
| Live-use contract is enforced | validation | harness validator | validator fixtures and affected prompt/skill docs | missing live-use/beyond-tests terms, advisory/non-blocking softening, or role-boundary drift |
| E2e relationship is bounded | review/readback | `testing-best-practices`, `runtime-proof` | docs readback and proof rows | tests replace runtime evidence without faithful entrypoint and inspectable artifacts |
| Interrupted draft edits are reconciled | readback | parent, `quality_guard` | git diff readback across touched prompt/docs/config files | unplanned runtime wording survives outside owned surfaces or non-runtime roles gain runtime_evidence authority |

## Task Plan

### harness/runtime-proof/live-use-owner-contract

- State:
  - `blank`
- Outcome:
  - `runtime-proof` owns runtime evidence as live-use verification beyond
    tests, code inspection, quality approval, and final review.
- In scope:
  - `skills/runtime-proof/SKILL.md`
  - `skills/runtime-proof/agents/openai.yaml`
- Out of scope:
  - Platform mechanics.
  - Project runtime recipes.
- Owned files and surfaces:
  - Runtime proof trigger, claim map, verdict, and live-use evidence contract.
- Touched owner/component integrity:
  - acceptable. Touched owner is `runtime-proof` runtime-evidence policy and
    verdict authority. Highest inspected scope is direct runtime-proof
    consumers in subagent routing, adapter prompts, testing, web, and mobile
    skills. Must-block signals: none planned. Accepted debt: none.
- Locked invariants:
  - Non-trivial runtime-visible claims require runtime evidence unless tiny,
    local, and no public-behavior or cross-boundary runtime risk.
  - Passing tests, review approval, or final signoff are not runtime proof.
  - `pass | reject | blocked` remain blocking verdicts.
- Allowed local implementer decisions:
  - Exact compact wording.
- Stop-and-handback triggers:
  - Need to change exemption semantics or runtime verdict vocabulary.
- Proof rows:
  - `P1`
- Deferred follow-up:
  - none

### harness/runtime-evidence/adapter-role-prompts

- State:
  - `blank`
- Outcome:
  - Adapter prompts make `runtime_evidence` use the app/service/API/operator
    path through a faithful entrypoint and reject proof by tests/reviews alone.
- In scope:
  - `agents/roles.md`
  - `adapters/codex/config.toml`
  - `adapters/codex/agents/runtime-evidence.toml`
  - `adapters/github-copilot/agents/runtime_evidence.agent.md`
- Out of scope:
  - Other role prompt redesigns except local pointers needed for boundary.
- Owned files and surfaces:
  - Role mission, adapter description, runtime evidence prompt contract.
- Touched owner/component integrity:
  - acceptable. Touched component is runtime_evidence role mission across
    `agents/roles.md`, adapter config, and runtime_evidence prompts. Highest
    inspected scope includes adjacent role prompts only for boundary leakage.
    Must-block signals: duplicate role authority, product-grade design
    approval, e2e authoring, code-quality review. Accepted debt: none.
- Locked invariants:
  - Runtime evidence uses live behavior, not approval history.
  - Runtime evidence does not write tests by default.
  - Runtime evidence does not issue product-grade design approval.
- Allowed local implementer decisions:
  - Whether to use "live-use" or a clearer equivalent consistently.
- Stop-and-handback triggers:
  - Prompt needs project-specific recipes or UI design criteria.
- Proof rows:
  - `P2`
- Deferred follow-up:
  - none

### harness/orchestration/runtime-evidence-routing

- State:
  - `blank`
- Outcome:
  - Subagent routing tells the parent when and why to invoke
    `runtime_evidence`, and what inputs a valid handoff needs.
- In scope:
  - `skills/subagent-orchestration/SKILL.md`
  - `AGENTS.md` only if the global role map needs a compact pointer update.
- Out of scope:
  - Changing subagent preauthorization.
- Owned files and surfaces:
  - Delegation trigger and handoff input contract.
- Touched owner/component integrity:
  - acceptable. Touched owner is subagent handoff/routing in
    `subagent-orchestration`; highest inspected scope includes role map and
    runtime_evidence handoff inputs. Must-block signals: narrowed objective,
    shared runtime lifecycle transfer, missing accepted reductions. Accepted
    debt: none.
- Locked invariants:
  - Handoffs preserve binding objective and accepted reductions.
  - Runtime evidence receives exact runtime claim, entrypoint/recipe, state,
    data, role/device/browser, artifacts needed, and stop conditions.
- Allowed local implementer decisions:
  - Exact handoff field wording.
- Stop-and-handback triggers:
  - Delegation would narrow success or transfer shared runtime lifecycle.
- Proof rows:
  - `P3`
- Deferred follow-up:
  - none

### harness/testing/e2e-runtime-proof-relationship

- State:
  - `blank`
- Outcome:
  - Testing docs state implementers write e2e tests when planned, and runtime
    evidence may consume them only as faithful, inspectable proof artifacts.
- In scope:
  - `skills/testing-best-practices/SKILL.md`
  - `skills/webapp-testing/SKILL.md`
  - `skills/mobileapp-testing/SKILL.md`
- Out of scope:
  - Adding or changing an e2e framework.
- Owned files and surfaces:
  - Test ownership and runtime proof relationship.
- Touched owner/component integrity:
  - acceptable. Touched owner is testing/runtime-proof relationship across
    `testing-best-practices`, `runtime-proof`, `webapp-testing`, and
    `mobileapp-testing`. Must-block signals: tests replace runtime evidence by
    default, runtime evidence writes tests by default, platform mechanics own
    verdicts. Accepted debt: none.
- Locked invariants:
  - E2e authoring belongs to implementer-owned task cards.
  - E2e artifacts support runtime evidence only when they match the claim,
    faithful entrypoint, state/data/role/device/browser, and artifact needs.
- Allowed local implementer decisions:
  - Exact owner pointers.
- Stop-and-handback triggers:
  - Tests are proposed as universal replacement for runtime evidence.
- Proof rows:
  - `P4`
- Deferred follow-up:
  - none

### harness/runtime-evidence/interrupted-edit-sweep

- State:
  - `blank`
- Outcome:
  - All interrupted runtime-evidence-related edits are kept intentionally,
    revised under an owned task, or reverted; no stale draft authority remains.
- In scope:
  - `agents/roles.md`
  - `adapters/codex/config.toml`
  - `adapters/codex/agents/*.toml`
  - `adapters/github-copilot/agents/*.agent.md`
  - `skills/runtime-proof/SKILL.md`
  - `skills/runtime-proof/agents/openai.yaml`
  - `skills/subagent-orchestration/SKILL.md`
  - `skills/webapp-testing/SKILL.md`
  - `skills/mobileapp-testing/SKILL.md`
  - `skills/testing-best-practices/SKILL.md`
  - `skills/verification-before-completion/SKILL.md`
  - runtime/design wave state.
- Out of scope:
  - Reverting approved Wave 1 strict-validation changes.
- Owned files and surfaces:
  - Working-tree runtime-evidence role-boundary edits and adjacent prompt
    surfaces touched for boundary wording.
- Touched owner/component integrity:
  - acceptable. Touched component is current runtime-evidence-related diff
    hygiene across docs, prompts, config, and wave state. Must-block signals:
    unowned prompt edits, duplicate authority, stale design-scoring route,
    non-runtime role performing runtime_evidence job. Accepted debt: none.
- Locked invariants:
  - Non-runtime roles may verify required gate coverage only.
  - Runtime evidence wording may survive only in owned runtime-proof,
    runtime_evidence, orchestration, testing, web/mobile, or wave-state
    surfaces.
- Allowed local implementer decisions:
  - Keep, revise, or revert each interrupted edit only with readback rationale.
- Stop-and-handback triggers:
  - A stale edit needs a new owner or changes another role's responsibility.
- Proof rows:
  - `P5`
- Deferred follow-up:
  - none

### harness/validation/runtime-evidence-live-use-drift

- State:
  - `blank`
- Outcome:
  - Harness validation catches loss of core runtime-evidence live-use terms and
    obvious substitutions by tests/reviews alone.
- In scope:
  - harness validator
  - `tests/test_validate_harness.py`
- Out of scope:
  - Broad semantic prompt lint.
- Owned files and surfaces:
  - Static harness validation fixtures.
- Touched owner/component integrity:
  - acceptable. Touched owner is harness validator contract checks for runtime
    evidence. Highest inspected scope is existing runtime-proof/runtime_evidence
    validation plus new fixtures. Must-block signals: fuzzy semantic lint,
    prompt-style wording preferences, or unchecked core drift. Accepted debt:
    none.
- Locked invariants:
  - Validate only durable role-contract terms, not style or prose quality.
  - Existing advisory/non-blocking checks remain blocking.
- Allowed local implementer decisions:
  - Exact helper/function names and fixture layout.
- Stop-and-handback triggers:
  - The check needs fuzzy interpretation of intent.
- Proof rows:
  - `P6`
- Deferred follow-up:
  - none

## Proof Plan

```json
{
  "proof_plan": [
    {
      "proof_id": "P1",
      "task_slug": "harness/runtime-proof/live-use-owner-contract",
      "anchor_ids": ["A1"],
      "claim": "runtime-proof owns runtime evidence as live-use verification beyond tests and reviews without absorbing platform mechanics or design approval.",
      "material_variants": ["UI", "API", "service", "integration", "mobile", "browser"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-contract",
      "exact_proof": ["readback of runtime-proof owner contract and direct consumers"],
      "expected_evidence": ["one owner rule; consumers use compact pointers and local consequences"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Runtime evidence is described only as artifact review or generic proof review.",
        "failing_assertion_or_artifact": "readback finds no live-use beyond-tests mission"
      },
      "status": "planned"
    },
    {
      "proof_id": "P2",
      "task_slug": "harness/runtime-evidence/adapter-role-prompts",
      "anchor_ids": ["A2"],
      "claim": "runtime_evidence prompts require faithful live-use verification and reject tests, code review, or approval history as substitutes.",
      "material_variants": ["Codex adapter", "Copilot adapter", "role list", "adapter config"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-contract/static-check",
      "exact_proof": ["readback of role prompts and harness validator"],
      "expected_evidence": ["prompts name live-use path, faithful entrypoint, pass/reject/blocked, and role exclusions"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Runtime evidence may pass because tests and reviews passed.",
        "failing_assertion_or_artifact": "validator fixture or readback rejects prompt"
      },
      "status": "planned"
    },
    {
      "proof_id": "P3",
      "task_slug": "harness/orchestration/runtime-evidence-routing",
      "anchor_ids": ["A3"],
      "claim": "subagent orchestration invokes runtime_evidence when live-use runtime-visible claims need proof beyond tests and reviews.",
      "material_variants": ["parent handoff", "runtime evidence handoff", "shared runtime lifecycle"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-contract",
      "exact_proof": ["readback of subagent-orchestration and roles.md"],
      "expected_evidence": ["routing preserves binding objective and names live-use proof inputs"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Parent sends only a narrow task summary or test result as runtime evidence.",
        "failing_assertion_or_artifact": "readback finds handoff contract blocks it"
      },
      "status": "planned"
    },
    {
      "proof_id": "P4",
      "task_slug": "harness/testing/e2e-runtime-proof-relationship",
      "anchor_ids": ["A4"],
      "claim": "e2e tests support runtime evidence only when implementer-owned and faithful to the runtime claim.",
      "material_variants": ["web", "mobile", "service", "durable test artifact", "manual live-use proof"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-contract",
      "exact_proof": ["readback of testing, webapp, mobileapp, and runtime-proof docs"],
      "expected_evidence": ["docs keep e2e authoring with implementation and runtime verdict with runtime-proof"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Any passing e2e suite replaces runtime evidence regardless of entrypoint or artifacts.",
        "failing_assertion_or_artifact": "readback finds explicit block"
      },
      "status": "planned"
    },
    {
      "proof_id": "P5",
      "task_slug": "harness/runtime-evidence/interrupted-edit-sweep",
      "anchor_ids": ["A5"],
      "claim": "interrupted runtime-evidence-related edits are explicitly reconciled and do not leak stale authority into unrelated roles.",
      "material_variants": ["runtime prompts", "non-runtime prompts", "role list", "config", "skills", "wave state"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-contract/static-check",
      "exact_proof": ["git diff readback of runtime-evidence-related surfaces", "uv run python scripts/validate_harness.py"],
      "expected_evidence": ["every runtime-evidence-related diff is owned by a task or removed"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "A stale prompt edit leaves quality_guard, final_reviewer, or runtime_evidence with duplicate authority.",
        "failing_assertion_or_artifact": "readback or validation blocks closeout"
      },
      "status": "planned"
    },
    {
      "proof_id": "P6",
      "task_slug": "harness/validation/runtime-evidence-live-use-drift",
      "anchor_ids": ["A6"],
      "claim": "validation catches concrete drift away from live-use runtime evidence and required gate blocking.",
      "material_variants": ["missing live-use mission", "tests-as-substitute", "review-as-substitute", "role-boundary drift"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check/test",
      "exact_proof": ["uv run pytest tests/test_validate_harness.py -q", "uv run python scripts/validate_harness.py", "just quality-fast"],
      "expected_evidence": ["fixtures fail weak runtime evidence prompt/skill variants"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Runtime evidence prompt omits live-use beyond-tests contract or treats tests/reviews as proof.",
        "failing_assertion_or_artifact": "validator test fails"
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
| `decision` | Runtime evidence mission | Closed: independent live-use verification beyond tests/reviews. | agent |
| `decision` | E2e ownership | Closed: implementers write e2e tests when planned; runtime evidence consumes qualifying artifacts. | agent |
| `decision` | Validator checked files | Closed: runtime-proof skill, runtime_evidence adapter prompts, role/config routing, and fixtures. | agent |
| `decision` | Validator required terms | Closed: live-use/app-service-API-operator path, beyond tests/reviews, faithful entrypoint, pass/reject/blocked, not code quality, not product-grade design approval. | agent |
| `decision` | Validator negative fixtures | Closed: tests/reviews as proof substitute, missing live-use mission, runtime_evidence writing e2e tests by default, runtime_evidence owning design approval. | agent |
| `blocker` | Planning review | Required before execution-ready promotion. | planning_critic |

### Technical Debt And Deferred Follow-Up

- none

## System-Boundary Architecture Disposition

- Why triggered:
  - The wave changes reusable runtime-evidence role authority, routing, prompt
    contracts, and validator checks.
- Planning disposition:
  - Keep one runtime-proof owner; update consumers with compact local trigger
    and handoff consequences.
- Execution stop rule:
  - Stop if runtime evidence absorbs design approval, implementation quality
    review, e2e authoring, or project-specific recipes.
- Changed authorities or contracts:
  - `runtime-proof`: live-use runtime evidence mission and verdict policy.
  - `subagent-orchestration`: invocation and handoff inputs.
  - adapter prompts/config: role trigger and output contract.
  - testing/web/mobile skills: e2e and platform-mechanic relationship.
  - harness validator: concrete drift checks.
- Single owner after change:
  - Runtime evidence policy and verdicts: `runtime-proof`.
  - Subagent invocation and handoff: `subagent-orchestration`.
  - E2e authoring policy: `testing-best-practices`.
  - Platform mechanics: `webapp-testing`, `mobileapp-testing`.
- Public write paths:
  - Skills, adapter prompts/config, role list, validation tests, wave state.
- Read-repair paths:
  - Failing runtime gate repairs the runtime behavior, supplies missing live
    evidence, or narrows the claim only by explicit accepted reduction.
- Forbidden bypass paths:
  - Passing tests as runtime proof without matching claim/entrypoint/artifacts.
  - Quality or final review replacing runtime evidence.
  - Runtime evidence replacing design approval.
  - Runtime evidence writing e2e tests by default.
- Rejected alternatives:
  - Delete `runtime_evidence`: rejected because tests and reviews can pass while
    the real app/service fails.
  - Make e2e tests the default runtime gate: rejected because many runtime
    failures require live-use inspection or current environment evidence.
  - Fold into `quality_guard`: rejected because it muddles implementation
    review with live runtime proof.
- Why not artificially narrowed:
  - The problem applies to UI, API, service, integration, browser, mobile, and
    live-state claims.
- Stable-to-extend expectation:
  - The dependent UI/design wave consumes this live-use contract and adds
    `design_judge` without redefining runtime evidence.
