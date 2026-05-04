# Wave harness-runtime-evidence-live-use-contract-1 - Runtime evidence live-use contract

**Status:** discovery-required

## Objective Boundary

- original objective: make `runtime_evidence` clearly own independent live-use
  verification beyond tests, code review, quality gates, and final review.
- accepted reductions: none.
- residual gaps: UI design approval remains in
  `harness-ui-runtime-evidence-redesign-1`.

## Problem

Runtime evidence is still easy to read as generic proof review or artifact
checking. The intended job is stricter: use the real app, service, API,
integration, or operator path and catch failures that tests and reviewers miss.

## Scope

In scope:

- runtime-proof owner contract for live-use verification,
- `runtime_evidence` trigger and adapter prompt wording,
- subagent routing and handoff inputs,
- web/mobile mechanic owners pointing to runtime evidence without owning its
  verdict,
- testing relationship: e2e tests may be a proof vehicle, not default
  replacement,
- narrow validator coverage for role-contract drift.

Out of scope:

- `design_judge` implementation,
- product-grade UI design approval,
- broad e2e framework changes,
- project-specific runtime recipes.

## Candidate Task Cards

- `harness/runtime-proof/live-use-owner-contract`
- `harness/runtime-evidence/adapter-role-prompts`
- `harness/orchestration/runtime-evidence-routing`
- `harness/testing/e2e-runtime-proof-relationship`
- `harness/runtime-evidence/interrupted-edit-sweep`
- `harness/validation/runtime-evidence-live-use-drift`

## Required Planning Questions

- closed: Keep `runtime_evidence`; it is the role that uses the app/service and
  verifies runtime-visible behavior beyond tests and reviews.
- closed: E2e tests are authored by implementers when planned. Runtime evidence
  may consume e2e artifacts only when they exercise the same claim through a
  faithful entrypoint and leave inspectable evidence.
- closed: `quality_guard` verifies implementation quality and gate coverage;
  it does not perform live-use proof.
- closed: `design_judge` owns product-grade UI design approval; it does not run
  the app or replace runtime evidence.
- closed: Validator scope is exact-term contract protection, not semantic lint.
  It checks runtime-proof, runtime_evidence prompts, role/config routing, and
  fixtures for tests/reviews replacing live-use proof.

## Minimum Acceptance Bar

- `runtime-proof` states why runtime evidence exists: live-use verification
  beyond tests, code inspection, quality approval, and final review.
- Role lists, adapter config, runtime prompts, and orchestration wording use
  the same mission and trigger.
- Runtime evidence prompts block tests/reviews/approval history as substitutes
  for live runtime proof.
- Testing docs state e2e tests can support runtime evidence only with faithful
  entrypoint and inspectable artifacts.
- Validator coverage catches loss of the core live-use/beyond-tests contract
  and role-boundary drift.
- Existing interrupted edits are normalized, kept intentionally, or reverted
  under an explicit sweep task.

## Starting Points

- `skills/runtime-proof/SKILL.md`
- `agents/roles.md`
- `adapters/codex/config.toml`
- `adapters/codex/agents/runtime-evidence.toml`
- `adapters/github-copilot/agents/runtime_evidence.agent.md`
- `skills/subagent-orchestration/SKILL.md`
- `skills/webapp-testing/SKILL.md`
- `skills/mobileapp-testing/SKILL.md`
- `skills/testing-best-practices/SKILL.md`
- `skills/verification-before-completion/SKILL.md`
- harness validator
- `tests/test_validate_harness.py`

## Promotion Requirement

Promote only after `planning-intake`, `planning_critic`, and `quality_guard`
approve scope, role boundaries, proof allocation, validator terms, and touched
owner integrity.

## Packet

- `docs-ai/current-work/harness-runtime-evidence-live-use-contract-1/wave-execution.draft.md`
