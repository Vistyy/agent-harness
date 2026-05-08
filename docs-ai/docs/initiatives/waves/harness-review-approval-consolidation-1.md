# Wave harness-review-approval-consolidation-1 - Review Approval Consolidation

**Status:** done

## Objective Boundary

- original objective: make review stricter, simpler, and more enforceable by
  consolidating approval, debt, and disposition doctrine under the correct
  harness owners; remove low-value or duplicate instructions that breach
  `harness-governance`.
- accepted reductions: none.
- residual gaps: none intended.

## Planning Gaps

- Confirm `review-governance.md` is the sole owner for review approval
  semantics, verdicts, approval evidence, and issue disposition.
- Confirm adjacent skills keep only local routing, storage, or completion
  consequences.
- Confirm adapter role prompts can point to owner doctrine without copying
  review rules.
- Confirm validation covers the owner boundary and stale verdict terminology.

## Starting Points

- `skills/code-review/SKILL.md`
- `skills/code-review/references/review-governance.md`
- `skills/harness-governance/SKILL.md`
- `skills/harness-governance/references/harness-contracts.md`
- `skills/harness-governance/references/skill-architecture.md`
- `skills/code-simplicity/SKILL.md`
- `skills/work-routing/SKILL.md`
- `skills/planning-intake/SKILL.md`
- `skills/initiatives-workflow/SKILL.md`
- `skills/initiatives-workflow/assets/backlog-entry.md`
- `skills/verification-before-completion/SKILL.md`
- `skills/feedback-address/SKILL.md`
- `agents/roles.md`
- `adapters/codex/agents/planning-critic.toml`
- `adapters/codex/agents/quality-guard.toml`
- `adapters/codex/agents/final-reviewer.toml`
- `adapters/github-copilot/agents/planning_critic.agent.md`
- `adapters/github-copilot/agents/quality_guard.agent.md`
- `adapters/github-copilot/agents/final_reviewer.agent.md`

## Promotion Requirement

Promote only after `planning-intake`, `planning_critic`, and `quality_guard`
close scope, owner boundaries, proof, backlog semantics, adapter alignment, and
touched-owner integrity.

## Planning Gate

- `planning_critic`: APPROVE after repairs for `NON-BLOCKING` ownership,
  `harness-contracts` intake, planning-critic prompt scope, disposition
  readback proof, and backlog/issue-disposition owner split.
- `quality_guard`: APPROVE with no findings. Scope, owner split, proof rows,
  adapter alignment, backlog/packet surfaces, and touched-component integrity
  are execution-ready.

## Implementation Gate

- `quality_guard`: APPROVE with no findings. Touched-component integrity is
  acceptable, must-block signals are none, proof is sufficient, and no accepted
  temporary debt remains.

## Closeout

- final_reviewer: APPROVE with no findings after repairs for stale
  `NON-BLOCKING` verdict validation, canonical packet handoff path, legacy debt
  wording around non-blocking allowances, backlog schema alignment, and
  accepted-temporary-debt placeholder enforcement.
- verification: final claim covers the full binding objective with no accepted
  reductions and no residual risks.
- changed reusable owners: `code-review`, `harness-governance`,
  `code-simplicity`, `work-routing`, `planning-intake`,
  `initiatives-workflow`, `verification-before-completion`,
  `feedback-address`, reviewer adapter prompts, and harness validation.
- removed obsolete routes: `NON-BLOCKING` as a code-review verdict; ordinary
  backlog as a path for current-scope blockers; legacy non-blocking debt
  allowance.
- changed routing triggers: none.
- proof passed:
  - `uv run python scripts/validate_harness.py`
  - `uv run pytest tests/test_validate_harness.py -q` passed 62 tests
  - `agent-harness governance check --repo-root .`
  - `just quality-fast` passed 95 tests plus validation self-test, harness
    validation, and Codex install smoke
- harness repo status: changed reusable harness policy, adapter prompts,
  validation, tests, and this wave brief.
- project repo status: no project overlays changed.
