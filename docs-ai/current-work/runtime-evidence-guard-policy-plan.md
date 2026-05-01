# Wave runtime-evidence-guard-policy-1 — Agent harness: runtime evidence as first-class live validation guard

**Status:** planning-draft

Packet candidate: this file.

## Goal

Make `runtime_evidence` a first-class global harness guard for live
user/runtime validation, comparable in authority to `planning_critic` for
planning, `quality_guard` for implementation quality, and `final_reviewer` for
closeout review.

The change must make runtime validation mandatory for claims that depend on
live UI, live interaction, API/service behavior, uploads/downloads, generated
runtime wiring, or screenshot-backed visual quality. It must not turn
`runtime_evidence` into a general debugger, implementation reviewer, or bulk
log summarizer.

## Problem

Current harness docs contain runtime proof mechanics, but the role is still too
easy to treat as an optional helper. That leaves room for agents to:

- skip live inspection when tests pass,
- validate UI by DOM/text presence instead of screenshots and interaction,
- treat visual quality and usability as subjective or advisory even when the
  user objective depends on them,
- let API/service behavior pass on unit tests without real usage or response
  inspection,
- use `check_runner`, `quality_guard`, or `final_reviewer` as substitutes for a
  runtime/user-validation verdict.

## Intended Policy

`runtime_evidence` should be the live user/runtime validation guard.

It should be required when a completion claim depends on:

- browser-visible or device-visible UI,
- end-user visual quality, layout, interaction, usability, or screenshots,
- API or service behavior across a process boundary,
- uploads, downloads, files, object storage, external side effects,
- generated runtime config, environment wiring, startup/readiness, lifecycle,
- live auth, capability, session, offline/retry, or degraded-state behavior.

It may block completion for the runtime-visible claim even when automated tests,
`quality_guard`, or `final_reviewer` pass. If runtime evidence is blocked or
incomplete, the parent must narrow the claim or record the external blocker.

Closed implementation decisions:

- Delegation posture: delegate to `runtime_evidence` for non-trivial
  runtime-visible completion claims. Parent-local runtime evidence is allowed
  only for tiny local fixes where no public-behavior, visual-quality,
  interaction, API/service, upload/download, lifecycle, or cross-boundary claim
  is made beyond the directly changed line. If in doubt, delegate.
- API/service scope: API and service behavior across a process boundary is in
  scope for `runtime_evidence` when the claim needs real usage, response-shape
  inspection, ergonomics, degraded-state, auth/capability, or cross-service
  validation. `check_runner` may gather logs and command output, but does not
  replace the runtime guard verdict.
- Validation posture: deterministic harness validation is required in the same
  change. Behavioral/model evals may be deferred only with an explicit backlog
  item.

## Non-Goals

- Do not make `runtime_evidence` a code-quality reviewer.
- Do not make it a general debugger or planner.
- Do not route routine bulk logs, repeated test runs, or large artifact
  summarization to `runtime_evidence`; those remain `check_runner` work.
- Do not hard-code BudgEat-specific design standards into reusable harness
  policy.
- Do not require runtime evidence for tiny static-only changes with no
  runtime-visible claim.

## Owner And Boundary

- Touched owner/component: global harness workflow policy and named agent role
  topology.
- Highest expected scope: global `AGENTS.md`, role vocabulary, delegation
  topology, verification/runtime proof skills, runtime evidence role prompt,
  and harness validation/check docs where applicable.
- Touched-component integrity: acceptable if the implementation changes one
  policy owner per concept and avoids duplicated runtime-proof rules.
- Must-block signals: duplicate authority between verification docs and role
  prompt; role overreach into debugging/review/implementation; BudgEat-specific
  language in reusable harness docs; no validation command.
- Accepted-debt backlog link: none.

## Proposed Files To Change

Policy entrypoint:

- `AGENTS.md`
  - Add a global rule that runtime-visible completion claims require
    `runtime_evidence`, with blocked/incomplete evidence narrowing the claim.

Role vocabulary and delegation:

- `agents/roles.md`
  - Reword `runtime_evidence` as live user/runtime validation guard.
- `skills/subagent-orchestration/references/coding-agent-topology.md`
  - Make role mission/authority explicit.
  - Clarify interaction with `check_runner`, `quality_guard`, and
    `final_reviewer`.
  - Require handoffs to name what a runtime reject blocks.
- `skills/subagent-orchestration/references/delegation-policy.md`
  - Replace optional-helper runtime delegation posture with mandatory
    `runtime_evidence` delegation triggers, allowed tiny-fix exception, and
    non-overlap with `check_runner`.

Verification proof owners:

- `skills/verification-before-completion/SKILL.md`
  - Add runtime evidence guard step to completion checklist.
  - Make `runtime_evidence` mandatory for runtime-visible claim classes.
- `skills/verification-before-completion/references/runtime-proof-escalation.md`
  - Tighten escalation triggers and clarify parent-local checks vs delegated
    runtime guard verdicts.
- `skills/verification-before-completion/references/runtime-evidence-contract.md`
  - Add guard authority section.
  - Require explicit behavioral/design verdict authority and claim boundary.
  - Require screenshot inspection for UI quality claims.

Adapter prompt:

- `adapters/github-copilot/agents/runtime_evidence.agent.md`
  - Tighten role prompt so it behaves as validation guard, not helper.
  - Require explicit `pass` / `reject` / `blocked` verdicts and block impact.
  - Replace direct project-style document references such as
    `docs-ai/docs/initiatives/...` with reusable global owner references and
    instructions to consume project-overlay anchors when the parent supplies
    them.
- `adapters/codex/agents/runtime-evidence.toml`
  - Apply the same guard-authority, output-contract, and project-local
    reference cleanup as the GitHub Copilot adapter prompt so role behavior
    stays adapter-parity-safe.

Validation and docs:

- `scripts/validate_harness.py`
  - Add deterministic checks for runtime-evidence guard policy consistency.
- `tests/test_validate_harness.py`
  - Add negative tests for stale optional-helper wording, missing required
    guard references, and adapter prompt references to nonexistent project
    docs.
- `skills/harness-governance/references/skill-evaluation.md`
  - If existing validation coverage expects role-invocation checks, add this
    role as a candidate for future eval/static validation only if it can be
    checked mechanically.
- `docs-ai/current-work/delivery-map.md`
  - Add follow-up backlog only if validation cannot be implemented in the same
    change.

## Implementation Tasks

### 1. Tighten Global Runtime Evidence Authority

- Exact paths:
  - `AGENTS.md`
  - `agents/roles.md`
  - `skills/subagent-orchestration/references/coding-agent-topology.md`
  - `skills/subagent-orchestration/references/delegation-policy.md`
- Changes:
  - define `runtime_evidence` as first-class guard for live user/runtime
    validation,
  - clarify that a runtime reject/blocked verdict blocks the affected claim,
  - preserve boundaries against debugging, code review, planning, and
    implementation.
  - replace "delegate isolated runtime proof only when startup/teardown is
    deterministic and ownership is unambiguous" with a posture that
    distinguishes mandatory runtime guard triggers from runtime ownership
    limits. If startup/runtime ownership is ambiguous, the claim becomes
    blocked or narrowed, not silently static-only.
- Verification:
  - `rg -n "runtime_evidence|runtime evidence|quality_guard|final_reviewer|check_runner" AGENTS.md agents/roles.md skills/subagent-orchestration/references/coding-agent-topology.md skills/subagent-orchestration/references/delegation-policy.md`
- Expected evidence:
  - role authority and boundaries are present in one consistent vocabulary.

### 2. Tighten Verification And Runtime Proof Contracts

- Exact paths:
  - `skills/verification-before-completion/SKILL.md`
  - `skills/verification-before-completion/references/runtime-proof-escalation.md`
  - `skills/verification-before-completion/references/runtime-evidence-contract.md`
- Changes:
  - add runtime evidence to completion gating,
  - name mandatory trigger classes,
  - distinguish runtime evidence from automated tests and static review,
  - require screenshot-backed verdicts for UI quality claims,
  - require claim boundary and block/narrowing consequences.
- Verification:
  - `rg -n "Runtime Evidence Guard|runtime_evidence|blocked|design-fidelity verdict|claim boundary" skills/verification-before-completion`
- Expected evidence:
  - completion checklist and runtime proof references require live guard proof
    for runtime-visible claims without duplicating role mechanics.

### 3. Tighten Adapter Runtime Evidence Prompt

- Exact paths:
  - `adapters/github-copilot/agents/runtime_evidence.agent.md`
  - `adapters/codex/agents/runtime-evidence.toml`
- Changes:
  - require actual use/inspection,
  - require explicit verdicts and block impact,
  - require UI screenshot inspection for UI claims,
  - remove global prompt references to project-local docs and instead require
    the parent handoff to pass project-specific design or runtime anchors,
  - keep output bounded and forbid debugging/review/implementation overreach.
- Verification:
  - `rg -n "validation guard|reject|blocked|screenshot|general debugger|check_runner|project" adapters/github-copilot/agents/runtime_evidence.agent.md adapters/codex/agents/runtime-evidence.toml`
- Expected evidence:
  - both adapter prompts are strict enough for the role to operate without
    parent-side interpretation and neither contains project-local docs paths.

### 4. Add Deterministic Harness Validation

- Exact paths:
  - `scripts/validate_harness.py`
  - `tests/test_validate_harness.py`
- Changes:
  - add checks that `runtime_evidence` is described as guard-authoritative in
    `AGENTS.md`, role topology, verification-before-completion, runtime proof
    escalation, runtime evidence contract, delegation policy, and adapter
    prompt,
  - add checks that the runtime evidence adapter prompt does not reference
    project-local `docs-ai/docs/...` paths in either Codex or GitHub Copilot
    role files,
  - add checks rejecting stale optional-helper delegation language that would
    allow runtime-visible claims to skip the guard.
- Verification:
  - `uv run pytest tests/test_validate_harness.py`
- Expected evidence:
  - tests fail on missing guard wording, stale optional-helper posture, or
    project-doc leakage.

### 5. Validate Harness Consistency

- Exact paths:
  - all changed harness files
- Changes:
  - run formatting/quality where applicable,
  - add validation follow-up only for behavioral/model evals that deterministic
    validation cannot cover.
- Verification:
  - `uv run pytest tests/test_validate_harness.py`
  - `just --justfile /home/syzom/projects/agent-harness/justfile --working-directory /home/syzom/projects/agent-harness quality-fast`
  - `git -C /home/syzom/projects/agent-harness diff --check`
- Expected evidence:
  - harness checks pass and no whitespace/doc hygiene issues remain.

## Approval Gates

No implementation should start until this draft receives:

1. `planning_critic` review with `APPROVE`.
2. `quality_guard` planning approval with `APPROVE`.

After implementation:

1. run harness verification,
2. run `quality_guard` on the implementation diff,
3. run `final_reviewer` before closeout.

## Deferred Follow-Up

Behavioral/model evals for role-invocation quality are out of this immediate
change. If implementation finds deterministic validation cannot cover a needed
guardrail, add a concrete backlog item under
`docs-ai/current-work/delivery-map.md` before approval.
