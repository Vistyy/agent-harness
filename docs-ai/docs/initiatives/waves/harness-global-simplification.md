# Wave harness-global-simplification - Harness global simplification

**Status:** done

## Problem

Several global harness owners still carry overlapping workflow, proof, testing,
subagent, and validator doctrine. The harness is cleaner than before, but the
remaining repetition still invites shallow compliance, prompt bloat, and
unclear ownership.

## Objective

Make the remaining global harness surfaces smaller and more owner-correct
without weakening objective continuity, durable state, review/proof gates,
runtime evidence blocking, persistent-test admission, or subagent authorization.

## In Scope

- `workflow/state-owners`
- `runtime/platform-proof`
- `testing/persistent-contract`
- `global-agents-subagent-policy`
- `validator/role-term-owners`

## Out Of Scope

- Adapter model/tool selection changes.
- New planning document types.
- Runtime app/UI proof.
- Project-local overlays.

## Constraints / Non-Goals

- Preserve the explicit `AGENTS.md` subagent authorization rule.
- Prefer deleting, collapsing, or pointing to owners over adding new policy.
- Keep validation checks exact and high-signal; no subjective semantic lint.

## Risks / Dependencies

- Risk: compaction weakens gates. Disposition: preserve invariants in the
  packet, validator tests, `quality_guard`, and `final_reviewer`.

## References

- `AGENTS.md`
- `skills/work-routing/SKILL.md`
- `skills/planning-intake/SKILL.md`
- `skills/initiatives-workflow/SKILL.md`
- `skills/initiatives-workflow/references/wave-packet-contract.md`
- `skills/runtime-proof/SKILL.md`
- `skills/webapp-testing/SKILL.md`
- `skills/mobileapp-testing/SKILL.md`
- `skills/testing-best-practices/SKILL.md`
- `skills/testing-best-practices/references/persistent-test-contract.md`
- harness validator script

## Planning Gate

- planning_critic: APPROVE on 2026-05-04 after proof specificity fixes.
- planning quality_guard: APPROVE on 2026-05-04.

## Closeout

- quality_guard: APPROVE on 2026-05-04 after AGENTS owner-map fix and
  persistent-test typed-transport fix.
- final_reviewer: APPROVE on 2026-05-04 after typed-transport rule restoration.
- Proof passed: harness validation, harness validator tests, diff whitespace
  check, quality fast, and governance check.
- Result: workflow, packet, runtime/platform, persistent-test, AGENTS, and
  validator surfaces were compacted without accepted reductions.
