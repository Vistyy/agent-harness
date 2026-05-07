# Harness Work-Control Refactor

**Status:** done

## Objective Boundary

- original objective: Refactor the harness workflow so agents consistently own complete repository outcomes, read the right owner skills early enough, challenge adequacy before and after implementation, preserve original context outside memory, hand subagents shared assumptions, and remove or collapse wave ceremony that adds more friction than value.
- accepted reductions: none.
- residual gaps: none accepted.

## Planning Gaps

- Selected path: keep wave packets, collapse them around a smaller `Work Context` capsule, and update validation/assets to match.
- Broaden the `code-simplicity` trigger so it is loaded for non-trivial work before local implementation choices are made.
- Add a general adequacy challenge that forces agents to prove the chosen scope repairs the touched owner/component, not just the local symptom.
- Make subagent handoffs consume the same durable objective, assumptions, decisions, proof rows, and stop conditions instead of narrow task summaries.
- Keep proof and final-claim gates strong while reducing duplicated process fields.

## Starting Points

- `AGENTS.md`
- `skills/work-routing/SKILL.md`
- `skills/code-simplicity/SKILL.md`
- `skills/code-simplicity/references/touched-component-integrity-gate.md`
- `skills/planning-intake/SKILL.md`
- `skills/initiatives-workflow/SKILL.md`
- `skills/initiatives-workflow/references/wave-packet-contract.md`
- `skills/subagent-orchestration/SKILL.md`
- `skills/verification-before-completion/SKILL.md`
- `agent_harness/waves.py`, `agent_harness/cli.py`, `../../../../scripts/validate_harness.py`, adapter role prompts, and related tests if packet or handoff shape changes.

## Promotion Requirement

Promote only after `planning-intake`, `planning_critic`, and `quality_guard` approve a specific refactor path: keep as-is with hardening, collapse packet schema, replace with a context capsule, or remove the wave layer. The approved plan must name retained context, subagent handoff payload, adequacy gate, code-simplicity trigger, proof/final-claim gates, validation changes, and cleanup of obsolete artifacts.

## Planning Gate

- planning_critic: REJECTED initial draft; material schema, allowlist owner, adequacy timing, and owner-skill intake decisions were still open. Corrected draft closes those decisions before re-review.
- quality_guard: REJECTED initial review; adapter role prompt surfaces and negative validator coverage were underfed. Corrected draft adds adapter prompts and drift tests to scope/proof.
- quality_guard: APPROVED corrected draft for promotion; adapter prompt scope and validator drift proof are covered.

## Closeout

- outcome: harness work-control refactor completed with no accepted reductions.
- changed authority: non-trivial work now requires early `code-simplicity`, owner-skill intake, adequacy challenge before implementation and completion, durable Work Context handoff, and final claims scoped to owner intake/proof/review.
- packet shape: wave packets now center on `Work Context` and reject obsolete top-level `Scope And Execution Posture` / `Required Gates` ceremony.
- subagent context: `AGENTS.md` owns explicit preauthorization, `agents/roles.md` owns role names/missions, and `subagent-orchestration` plus adapter prompts require binding objective, reductions, assumptions, risks, proof/artifacts, and stop conditions.
- validation: validator and tests cover Work Context packet shape, duplicate subagent metadata allowlists, adapter handoff context drift, and obsolete packet ceremony.
- review: final_reviewer approved closeout after blocker fixes.
- proof: `uv run pytest tests/test_validate_harness.py` passed 55 tests; `uv run pytest tests/test_agent_harness_cli.py` passed 29 tests; `uv run python scripts/validate_harness.py` passed; `just quality-fast` passed 88 tests plus validation self-test, harness validation, and codex install smoke; `uv run agent-harness governance check --repo-root /home/syzom/projects/agent-harness` passed with no output.
