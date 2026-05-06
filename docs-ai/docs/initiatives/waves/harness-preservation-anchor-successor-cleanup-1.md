# Wave harness-preservation-anchor-successor-cleanup-1 - Preservation Anchor Successor Cleanup

**Status:** done

## Objective Boundary

- original objective: continue completed-wave cleanup by deleting superseded
  completed wave briefs only after retained invariants are extracted to durable
  owners.
- accepted reductions: this tranche covers only
  `harness-design-preservation-anchor-gate-1.md`.
- residual gaps: remaining UI-runtime-evidence, mock-parity, and other
  completed briefs require separate successor review before deletion.

## Planning Gaps

- Prove whether the preservation-anchor invariant is already fully owned by
  `skills/user-apps-design/SKILL.md` and `design_judge` adapters.
- If not fully owned, add the smallest durable owner rule and parity check that
  preserves the invariant without reintroducing project-specific design taste
  or broad packet taxonomy.
- Preserve final-review coverage for the same invariant: final review must
  catch broad UI closeout where `design_judge` passed without covering required
  preservation anchors.
- Delete the superseded preservation-anchor brief only after successor owner,
  adapter parity, validation, stale-reference scan, quality review, final
  review, and verification cover the same claim.

## Starting Points

- `docs-ai/docs/initiatives/waves/harness-design-preservation-anchor-gate-1.md`
- `skills/user-apps-design/SKILL.md`
- `adapters/codex/agents/design-judge.toml`
- `adapters/github-copilot/agents/design_judge.agent.md`
- `skills/code-review/references/review-governance.md`
- `adapters/codex/agents/final-reviewer.toml`
- `adapters/github-copilot/agents/final_reviewer.agent.md`
- `./scripts/validate_harness.py`
- `tests/test_validate_harness.py`

## Promotion Requirement

Closed by `planning-intake`, `planning_critic`, and `quality_guard`.

- planning_critic: APPROVE after repairs for system-boundary disposition,
  final-review coverage, touched-owner integrity, stale-reference proof scope,
  and delivery-map scope drift.
- planning quality_guard: APPROVE after repairs for final-review coverage,
  delegation posture, boundary disposition, and touched-owner integrity.

## Packet

- closed after final review on 2026-05-06

## Closeout

- implementation `quality_guard`: APPROVE after durable UI approval owner,
  final-review coverage owner, adapter parity, validator proof, and deletion
  scope were reviewed.
- final_reviewer: APPROVE with no findings. Retained preservation-anchor
  invariants are represented in durable owners, and stale deleted-path
  references are limited to this active cleanup wave's own state before
  closeout cleanup.
- proof:
  - `uv run pytest tests/test_validate_harness.py -k design_judge` passed.
  - `uv run pytest tests/test_validate_harness.py -k 'final_reviewer or review_governance'`
    passed.
  - `uv run python scripts/validate_harness.py` passed.
  - `agent-harness governance check --repo-root .` passed.
  - `just quality-fast` passed with 85 tests, harness validation self-test,
    harness validation, and Codex install smoke.
