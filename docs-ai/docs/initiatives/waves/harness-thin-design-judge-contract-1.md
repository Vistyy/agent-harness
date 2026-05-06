# Wave harness-thin-design-judge-contract-1 - Thin Design Judge Contract

**Status:** discovery-required

## Objective Boundary

- original objective: slim the reusable harness UI/design workflow so the
  harness exposes only a thin blocking `design_judge` visual-quality gate, while
  projects own design method, taste, mockup requirements, before/after
  comparison, preservation language, and generated-image workflow choices.
- accepted reductions: none.
- residual gaps: exact validator terms, adapter wording, and whether any
  completed UI wave briefs can be deleted require successor review before
  execution.

## Planning Gaps

- Decide the smallest durable `user-apps-design` contract that keeps broad UI
  completion enforceable without prescribing project-local design methods.
- Replace preservation-specific global language with project-design-source
  requirements where possible.
- Ensure `design_judge` adapter prompts contain only role-local instructions:
  inspect supplied visual artifacts, compare to the binding objective and
  declared project design source, return `pass`/`reject`/`blocked`, and do not
  run the app, review code, debug, prove runtime behavior, or invent design
  criteria.
- Keep `runtime_evidence` as a separate live-use behavior verifier, not a
  default UI visual approval role.
- Decide whether validation should protect generic thin-contract terms instead
  of preservation-specific terms.
- Prove that final review and verification check `design_judge` coverage
  against project design source requirements without duplicating design method.

## Starting Points

- `skills/user-apps-design/SKILL.md`
- `skills/verification-before-completion/SKILL.md`
- `skills/code-review/references/review-governance.md`
- `skills/subagent-orchestration/SKILL.md`
- `skills/runtime-proof/SKILL.md`
- `adapters/codex/agents/design-judge.toml`
- `adapters/github-copilot/agents/design_judge.agent.md`
- `adapters/codex/agents/final-reviewer.toml`
- `adapters/github-copilot/agents/final_reviewer.agent.md`
- `adapters/codex/agents/quality-guard.toml`
- `adapters/github-copilot/agents/quality_guard.agent.md`
- `adapters/codex/agents/runtime-evidence.toml`
- `adapters/github-copilot/agents/runtime_evidence.agent.md`
- `./scripts/validate_harness.py`
- `tests/test_validate_harness.py`

## Promotion Requirement

Promote only after `planning-intake`, `planning_critic`, and `quality_guard`
close scope, decisions, proof, deferrals, and touched-owner integrity.
