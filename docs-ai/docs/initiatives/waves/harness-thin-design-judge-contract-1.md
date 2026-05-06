# Wave harness-thin-design-judge-contract-1 - Thin Design Judge Contract

**Status:** done

## Objective Boundary

- original objective: slim the reusable harness UI/design workflow so the
  harness exposes only a thin blocking `design_judge` visual-quality gate, while
  projects own design method, taste, mockup requirements, before/after
  comparison, preservation language, and generated-image workflow choices.
- accepted reductions: none.
- residual gaps: completed UI wave brief deletion remains out of scope unless a
  later successor review proves a specific brief has a full successor.

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
- Replace preservation-specific validator terms with thin-contract terms:
  `project design source requirements`, `declared project design source`,
  `visual quality only`, and role-boundary phrases that block app execution,
  code review, runtime proof, debugging, or invented design criteria.
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

Closed by `planning-intake`, `planning_critic`, and `quality_guard`.

- planning_critic: APPROVE after repairs for touched-owner integrity,
  semantic owner-boundary proof, successor validator terms, bounded write
  surfaces, and proof owner layers.
- planning quality_guard: APPROVE after repairs for exact successor validator
  terms, preservation-specific term removal, bounded task scopes, and semantic
  owner readback proof.

## Packet

- closed after final review on 2026-05-06

## Closeout

- implementation `quality_guard`: APPROVE after stale draft packet state was
  removed and the canonical packet remained the only execution authority.
- final_reviewer: APPROVE after the `visual quality only` validator coverage
  gap was repaired for both Codex and Copilot `design_judge` adapters.
- proof:
  - `uv run pytest tests/test_validate_harness.py -k 'design_judge or final_reviewer or review_governance or ui_approval or runtime_evidence_ui_default'`
    passed.
  - `uv run pytest tests/test_validate_harness.py -k design_judge` passed after
    the final-review repair.
  - `uv run python scripts/validate_harness.py` passed.
  - `rg -n "imagegen|before/after|preservation anchors|visual-language replacement|generic replacement" skills adapters scripts tests docs-ai/docs/initiatives/waves/harness-thin-design-judge-contract-1.md`
    found only project-owned method wording and this wave brief.
  - `agent-harness governance check --repo-root .` passed.
  - `just quality-fast` passed with 85 tests, harness validation self-test,
    harness validation, and Codex install smoke.
