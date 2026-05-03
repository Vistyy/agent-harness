# Wave harness-workflow-followthrough Execution Packet

## Scope And Execution Posture

- Original objective:
  - Finish the remaining harness cleanup queue at depth instead of from thread memory.
- Accepted reductions:
  - none
- Residual gaps:
  - none; this packet is the successor state for the queue.
- In-scope:
  - `workflow/slice-state`
  - `adapters/prompt-drift`
  - `reviewers/split`
  - `runtime/adapter-alignment`
  - `examples/assets-cleanup`
  - `governance/one-owner-validation`
  - `skills/compactness-pass`
  - `agents/instructions-review`
- Out-of-scope:
  - product runtime changes outside harness docs, adapters, validators, tests,
    examples, assets, and agent instructions.
- Non-obvious constraints:
  - no new planning document type
  - no rule duplication between owners unless a local consequence differs
  - no thread-only state for non-trivial narrowed work
- System-boundary trigger:
  - `triggered`
- Implementer delegation posture:
  - `implementer-eligible`
- Parent-only rationale:
  - `none`
- Frozen decisions:
  - existing wave state is the durable path, including one-task waves
  - task cards own state; task summary tables are optional
- Planning Exceptions:
  - `none`

## Task Plan

### `workflow/slice-state`

- State:
  - `done`
- Outcome:
  - Broad-objective slices require execution-ready wave state, and one-task
    packet state is compact enough to use.
- In scope:
  - `skills/work-routing/SKILL.md`
  - `skills/planning-intake/SKILL.md`
  - `skills/initiatives-workflow/**`
  - harness validator
  - harness validator tests
- Out of scope:
  - remaining cleanup queue
- Owned files and surfaces:
  - workflow route state
  - wave packet task-card schema
  - harness validator
- Touched owner/component integrity:
  - acceptable
- Locked invariants:
  - execution only from `execution-ready` brief plus canonical packet
  - draft packets are planning-only
  - task states are `blank`, `done`, or `blocked`
- Allowed local implementer decisions:
  - wording and validator structure
- Stop-and-handback triggers:
  - planning state requires a new artifact type
  - task state loses validator coverage
- Proof rows:
  - `P1`
- Deferred follow-up:
  - `none`

### `adapters/prompt-drift`

- State:
  - `done`
- Outcome:
  - Provider install/config prompts preserve current harness owner rules and
    cannot drift into stale workflow names or advisory gates.
- In scope:
  - `adapters/codex/README.md`
  - `adapters/codex/config.toml`
  - `adapters/codex/install-scope.md`
  - `adapters/codex/install.sh`
  - `adapters/github-copilot/README.md`
  - provider install/config prompts
  - validator checks for provider prompt invariants
- Out of scope:
  - provider-specific features unrelated to harness governance
  - `adapters/*/agents/**`
  - AGENTS/instruction-template routing
- Owned files and surfaces:
  - provider adapter prompts
  - prompt validation
- Touched owner/component integrity:
  - acceptable if each reusable rule points to one owner
- Locked invariants:
  - adapter prompts route to owner skills instead of restating doctrine
  - stale skill names and advisory proof language are rejected
- Allowed local implementer decisions:
  - exact validation strings and compact prompt wording
- Stop-and-handback triggers:
  - provider prompt needs contradictory behavior
  - validation would encode a duplicate doctrine owner
- Proof rows:
  - `P2`
- Deferred follow-up:
  - `none`

### `reviewers/split`

- State:
  - `done`
- Outcome:
  - `quality_guard` and `final_reviewer` have distinct, compact responsibilities
    and cannot approve a minimized slice against a minimized prompt.
- In scope:
  - reviewer role prompts
  - `skills/code-review/**`
  - `skills/verification-before-completion/**`
  - validator checks for review-scope invariants
- Out of scope:
  - runtime proof mechanics
- Owned files and surfaces:
  - review role contracts
  - final claim/review coverage wording
- Touched owner/component integrity:
  - acceptable if implementation-loop review and isolated closeout remain
    separate owners
- Locked invariants:
  - review checks binding objective plus accepted reductions
  - quality approvals do not substitute for final isolated review
- Allowed local implementer decisions:
  - whether duplicate lines are deleted or replaced by owner pointers
- Stop-and-handback triggers:
  - same approval authority is assigned to both reviewers
- Proof rows:
  - `P3`
- Deferred follow-up:
  - `none`

### `runtime/adapter-alignment`

- State:
  - `done`
- Outcome:
  - Runtime evidence adapters and prompts treat runtime findings as binding
    verdicts, not advisory notes, and route platform mechanics to their owners.
- In scope:
  - `adapters/**runtime*`
  - runtime-evidence role prompts
  - `skills/runtime-proof/**`
  - `skills/webapp-testing/**`
  - `skills/mobileapp-testing/**`
  - validator checks for runtime wording
- Out of scope:
  - project-specific browser or emulator flows
- Owned files and surfaces:
  - runtime proof policy
  - runtime evidence role handoff
  - platform mechanics references
- Touched owner/component integrity:
  - acceptable if verdict policy and platform mechanics remain separate
- Locked invariants:
  - `reject`, `blocked`, and incomplete runtime verdicts block or narrow claims
  - browser mechanics stay in `webapp-testing`
  - mobile mechanics stay in `mobileapp-testing`
- Allowed local implementer decisions:
  - compact wording and validation target selection
- Stop-and-handback triggers:
  - runtime role becomes a general review approver
  - adapter cannot express binding verdict semantics
- Proof rows:
  - `P4`
- Deferred follow-up:
  - `none`

### `examples/assets-cleanup`

- State:
  - `done`
- Outcome:
  - Harness examples and assets remain current, compact, and owned; stale
    examples cannot teach removed workflow paths.
- In scope:
  - `skills/**/assets/**`
  - `skills/**/examples/**`
  - stale reference validation where useful
- Out of scope:
  - project-local examples outside reusable harness
- Owned files and surfaces:
  - skill assets
  - examples
  - removed-path validation
- Touched owner/component integrity:
  - acceptable if every retained asset is used by an owner skill
- Locked invariants:
  - examples are executable or explicitly illustrative
  - deleted references have successor readback
- Allowed local implementer decisions:
  - delete, compact, or move assets to the owning skill
- Stop-and-handback triggers:
  - asset encodes policy not present in an owner skill
- Proof rows:
  - `P5`
- Deferred follow-up:
  - `none`

### `governance/one-owner-validation`

- State:
  - `blank`
- Outcome:
  - Reusable concepts have one owner, and validation catches high-risk duplicate
    doctrine across skills, adapters, and AGENTS instructions.
- In scope:
  - `skills/harness-governance/**`
  - `skills/documentation-stewardship/**`
  - harness validator
  - harness validator tests
- Out of scope:
  - semantic duplicate detection that cannot be made durable
- Owned files and surfaces:
  - harness governance rules
  - validation checks
- Touched owner/component integrity:
  - acceptable if the check protects owner boundaries without becoming broad
    prose lint
- Locked invariants:
  - owner docs carry reusable doctrine
  - references and adapters point to owners unless local consequence differs
- Allowed local implementer decisions:
  - choose narrow durable duplicate checks
- Stop-and-handback triggers:
  - validation requires subjective semantic judgment
- Proof rows:
  - `P6`
- Deferred follow-up:
  - `none`

### `skills/compactness-pass`

- State:
  - `blank`
- Outcome:
  - Skill bodies and required references follow the density rule: each sentence
    carries owner, outcome, input, output, stop condition, proof obligation,
    exception boundary, or routing consequence.
- In scope:
  - `skills/**/SKILL.md`
  - required references for the touched owner group
- Out of scope:
  - deep runtime/design/testing rewrites already closed in prior waves unless
    stale prose remains
- Owned files and surfaces:
  - skill body prose
  - owner-critical references
- Touched owner/component integrity:
  - acceptable if compaction preserves rules, triggers, and quality bars
- Locked invariants:
  - `description` frontmatter is trigger; body is content
  - references are mandatory only when purpose-gated by the skill body
- Allowed local implementer decisions:
  - delete, merge, or replace prose with owner pointers
- Stop-and-handback triggers:
  - chunk touches unrelated skill owners only for apparent coverage
  - compaction removes a hard gate or owner rule
- Proof rows:
  - `P7`
- Deferred follow-up:
  - `none`

### `agents/instructions-review`

- State:
  - `blank`
- Outcome:
  - Global/project `AGENTS.md` and adapter-installed instructions are compact
    first-hop maps that do not duplicate skill doctrine or reference removed
    skills.
- In scope:
  - `AGENTS.md`
  - adapter instruction templates
  - generated-agent instruction sources
  - validation for stale routing names
- Out of scope:
  - project facts owned by project overlays
- Owned files and surfaces:
  - global agent baseline
  - adapter-installed instruction maps
- Touched owner/component integrity:
  - acceptable if global instructions route to owners and carry only global
    execution gates
- Locked invariants:
  - instructions are maps, not doctrine dumps
  - skill names in routing must exist
  - removed skills have no live references
- Allowed local implementer decisions:
  - compact, delete duplicate rules, or add validation
- Stop-and-handback triggers:
  - instruction text becomes the second owner for a skill rule
- Proof rows:
  - `P8`
- Deferred follow-up:
  - `none`

## Proof Plan

Proof command names below refer to this repo-root command set:
- harness validation: `uv run python scripts/validate_harness.py`
- harness validator tests: `uv run pytest tests/test_validate_harness.py -q`
- quality fast: `just quality-fast`
- governance check: `agent-harness governance check --repo-root .`
- diff whitespace check: `git diff --check`

Review artifact names below are task evidence entries recorded in this packet
before the task can move to `done`.

```json
{
  "proof_plan": [
    {
      "proof_id": "P1",
      "task_slug": "workflow/slice-state",
      "anchor_ids": ["A1"],
      "claim": "Slice state and one-task packet simplification are encoded and validated.",
      "material_variants": ["docs", "validator"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": [
        "Proof command: harness validation",
        "Proof command: harness validator tests",
        "Proof command: quality fast",
        "Proof command: governance check"
      ],
      "expected_evidence": ["validation and tests pass"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "task card omits State or uses a new state",
        "failing_assertion_or_artifact": "validator reports missing or invalid task card state"
      },
      "status": "satisfied"
    },
    {
      "proof_id": "P2",
      "task_slug": "adapters/prompt-drift",
      "anchor_ids": ["A2"],
      "claim": "Adapter prompts route to current owner skills and reject stale/advisory workflow language.",
      "material_variants": ["codex", "copilot"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "static-check",
      "exact_proof": [
        "Review artifact: adapter prompt drift audit",
        "Proof command: harness validation",
        "Proof command: harness validator tests"
      ],
      "expected_evidence": ["no stale owner names; validation covers durable prompt invariants"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "adapter says runtime findings are advisory or references removed workflow skills",
        "failing_assertion_or_artifact": "validator rejects the prompt"
      },
      "status": "satisfied"
    },
    {
      "proof_id": "P3",
      "task_slug": "reviewers/split",
      "anchor_ids": ["A3"],
      "claim": "Quality and final review have distinct approval boundaries tied to the binding objective.",
      "material_variants": ["quality_guard", "final_reviewer"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "static-check",
      "exact_proof": [
        "Review artifact: reviewer authority split audit",
        "Proof command: harness validation",
        "Proof command: harness validator tests"
      ],
      "expected_evidence": ["quality_guard cannot replace final closeout review"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "quality_guard approval permits final claim without isolated review",
        "failing_assertion_or_artifact": "review invariant check or prompt audit fails"
      },
      "status": "satisfied"
    },
    {
      "proof_id": "P4",
      "task_slug": "runtime/adapter-alignment",
      "anchor_ids": ["A4"],
      "claim": "Runtime evidence adapter language is binding and aligned with runtime-proof/platform owners.",
      "material_variants": ["runtime-proof", "web", "mobile"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "static-check",
      "exact_proof": [
        "Review artifact: runtime adapter alignment audit",
        "Proof command: harness validation",
        "Proof command: harness validator tests"
      ],
      "expected_evidence": ["runtime reject/blocked verdicts block or narrow claims"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "runtime findings are advisory or platform mechanics are duplicated in runtime-proof",
        "failing_assertion_or_artifact": "validator or owner audit rejects it"
      },
      "status": "satisfied"
    },
    {
      "proof_id": "P5",
      "task_slug": "examples/assets-cleanup",
      "anchor_ids": ["A5"],
      "claim": "Examples and assets are current, compact, and owned by live skills.",
      "material_variants": ["assets", "examples"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "static-check",
      "exact_proof": [
        "Review artifact: examples and assets inventory",
        "Review artifact: stale asset reference sweep",
        "Proof command: harness validation"
      ],
      "expected_evidence": ["no stale asset references or unowned examples"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "asset references deleted skill path",
        "failing_assertion_or_artifact": "stale-reference check reports the path"
      },
      "status": "satisfied"
    },
    {
      "proof_id": "P6",
      "task_slug": "governance/one-owner-validation",
      "anchor_ids": ["A6"],
      "claim": "High-risk reusable doctrine duplication is prevented by owner rules and durable checks.",
      "material_variants": ["skills", "adapters", "AGENTS"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "static-check",
      "exact_proof": [
        "Review artifact: one-owner doctrine audit",
        "Proof command: harness validation",
        "Proof command: harness validator tests"
      ],
      "expected_evidence": ["one-owner rules are enforced where durable"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "same doctrine appears as reusable policy in two owners",
        "failing_assertion_or_artifact": "validation or audit flags duplicate authority"
      },
      "status": "planned"
    },
    {
      "proof_id": "P7",
      "task_slug": "skills/compactness-pass",
      "anchor_ids": ["A7"],
      "claim": "Skills and required references are compact without losing hard gates.",
      "material_variants": ["skill bodies", "references"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-only",
      "exact_proof": [
        "Review artifact: touched-owner density audit",
        "Proof command: harness validation",
        "Proof command: governance check"
      ],
      "expected_evidence": ["low-value prose removed; triggers and hard gates remain"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "delete prose without successor readback for hard gates",
        "failing_assertion_or_artifact": "review blocks due lost rule or unclear trigger"
      },
      "status": "planned"
    },
    {
      "proof_id": "P8",
      "task_slug": "agents/instructions-review",
      "anchor_ids": ["A8"],
      "claim": "Agent instructions are compact maps to live owners and contain no stale workflow routes.",
      "material_variants": ["global AGENTS", "adapter templates"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "static-check",
      "exact_proof": [
        "Review artifact: AGENTS and instruction-template audit",
        "Proof command: harness validation",
        "Proof command: governance check"
      ],
      "expected_evidence": ["no removed skill routes; no duplicated doctrine dump"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "AGENTS references removed workflow skills or restates skill doctrine",
        "failing_assertion_or_artifact": "validator or audit rejects it"
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
| `decision` | Promote this draft to execution-ready | Require planning_critic and planning quality_guard approval | `agent` |

### Evidence

| Task | Evidence |
| --- | --- |
| `workflow/slice-state` | planning_critic `019defc4-b043-73d3-bc54-aee8f0279d1a` APPROVED; quality_guard `019def78-d73a-7ac0-ab5e-33fc6e14af7b` APPROVED after circular stop-condition fix; final_reviewer `019deedb-6470-74b2-80f2-994ca93bbb4e` APPROVED; proof passed: harness validation, harness validator tests, diff whitespace check, quality fast, governance check. |
| `adapters/prompt-drift` | quality_guard `019def78-d73a-7ac0-ab5e-33fc6e14af7b` APPROVED after plain-advisory counterfactual fix; proof passed: harness validation, harness validator tests, diff whitespace check, quality fast, governance check. |
| `reviewers/split` | quality_guard `019def78-d73a-7ac0-ab5e-33fc6e14af7b` APPROVED after final-approval negation validator fix; proof passed: harness validation, harness validator tests, diff whitespace check, quality fast, governance check. |
| `runtime/adapter-alignment` | quality_guard `019def78-d73a-7ac0-ab5e-33fc6e14af7b` APPROVED; proof passed: harness validation, harness validator tests, diff whitespace check, quality fast, governance check. |
| `examples/assets-cleanup` | quality_guard `019def78-d73a-7ac0-ab5e-33fc6e14af7b` APPROVED; proof passed: harness validation, harness validator tests, diff whitespace check, quality fast, governance check. |

### Technical Debt And Deferred Follow-Up

- `none`

## System-Boundary Architecture Disposition (conditional)

Use only when `System-boundary trigger: triggered`.

- Why triggered: `This wave changes or validates workflow routing, adapter
  prompts, reviewer authority, runtime verdict authority, AGENTS routing, and
  one-owner doctrine checks.`
- Planning disposition: `Execute one task at a time; each task owns one
  authority boundary and stops on duplicate-owner pressure.`
- Execution stop rule: `Stop if a task needs to redefine another task owner,
  weakens review/proof gates, or requires a new planning artifact type.`
- Changed authorities or contracts: `workflow routing state gate, provider
  adapter prompt invariants, reviewer authority split, runtime verdict
  alignment, one-owner validation, compactness rule application, AGENTS map
  routing.`
- Single owner after change: `Each reusable rule has one owner skill or global
  instruction gate; adapters and AGENTS point to that owner unless they carry a
  provider-local consequence.`
- Public write paths: `skills, adapters, agents, AGENTS.md, docs-ai current-work,
  validator, validator tests.`
- Read-repair paths: `harness validation, governance check, reviewer audits,
  stale-reference sweeps.`
- Forbidden bypass paths: `thread-only planning state, duplicate doctrine in
  adapters or AGENTS, reviewer prompts that approve only the narrowed handoff,
  runtime findings treated as advisory.`
- Rejected alternatives: `new Direct Brief document type, broad repo-wide prose
  churn, adapter-owned copies of skill doctrine.`
- Why not artificially narrowed: `The packet keeps the full queue and requires
  each task to finish one coherent owner/problem before the next task claims
  done.`
- Stable-to-extend expectation: `Future broad harness cleanup adds task cards to
  this wave shape instead of relying on thread memory.`
