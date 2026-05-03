# Wave harness-adapter-agent-prompts - Harness adapter agent prompts

**Status:** done

## Problem

Adapter role profiles are live agent instructions. They can drift across Codex
and Copilot, duplicate skill doctrine, or blur role boundaries.

## Objective

Make Codex and Copilot role profiles compact, role-correct maps to owner skills.
Add durable checks for high-risk role-contract drift.

## In Scope

- `adapters/agent-prompts`

## Out Of Scope

- Provider install/config prompt policy already covered by the previous wave.
- Global `AGENTS.md` route-map policy already covered by the previous wave.
- Runtime app/UI proof.

## Constraints / Non-Goals

- Preserve role names and adapter file formats.
- Do not move reusable doctrine out of owner skills.
- Do not change model/tool selections unless required by role correctness.

## Risks / Dependencies

- Risk: compacting prompts weakens role gates. Disposition: validator and
  `quality_guard` must cover role boundary terms.

## References

- `agents/roles.md`
- `skills/subagent-orchestration/SKILL.md`
- `skills/harness-governance/SKILL.md`

## Prior Narrow-Pass Review

- planning_critic: APPROVE on 2026-05-04 after draft-packet reference and
  parent-only rationale fixes.
- planning quality_guard: APPROVE on 2026-05-04. Packet keeps the full adapter
  role profile surface together, preserves role owners, and allocates proof.
- Scope expansion: full prompt compaction is required before closeout because
  the first implementation only compacted obvious local duplicates.

## Planning Gate

- planning_critic: APPROVE on 2026-05-04 for expanded full-agent compaction.
- planning quality_guard: APPROVE on 2026-05-04.

## Packet

- closed after final review on 2026-05-04

## Closeout

- quality_guard: APPROVE on 2026-05-04 after full role-profile review.
- final_reviewer: APPROVE on 2026-05-04.
- Proof passed: harness validation, harness validator tests, diff whitespace
  check, quality fast, and governance check.
- Result: adapter prompt set reduced from 714 to 488 lines while preserving
  role-boundary validation.
