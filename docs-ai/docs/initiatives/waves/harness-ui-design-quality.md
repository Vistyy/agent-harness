# Harness UI Design Quality

**Status:** done

Superseded by later UI workflow compaction: global design dimensions, anchors,
and mockup methodology were collapsed into a thin approval contract in
`skills/user-apps-design/SKILL.md`.

## Objective Boundary

- original objective: compact `user-apps-design` around measurable,
  verifiable visual approval, and allow Codex image-generated mockups as planning
  inspiration for broad UI direction.
- accepted reductions: none.
- residual gaps: none.

## Scope

- in scope: `skills/user-apps-design/**`, direct validation updates, stale
  reference cleanup.
- out of scope: project-specific design scorecards, runtime-proof verdict
  ownership changes, browser/mobile mechanics changes.

## Closed Decisions

- `user-apps-design` owns design dimensions, anchors, composition, parity,
  text, and mobile UI constraints.
- `runtime-proof` owns runtime verdict terms, claim-map fidelity, and
  completion impact.
- Generated mockups are optional inspected anchors for broad or underspecified
  visual direction. They are not pixel contracts or durable project truth.
- Delete references only after successor readback proves retained invariants.

## Proof Plan

- harness validation: `uv run python scripts/validate_harness.py`
- validator tests: `uv run pytest tests/test_validate_harness.py -q`
- quality fast: `just quality-fast`
- governance check: `agent-harness governance check --repo-root .`
- stale live-reference scan:
  `rg -n "(references/)?(ui-direction-workflow|parity-dimensions|atomic-design)\\.md" skills AGENTS.md docs-ai --glob '!docs-ai/current-work/harness-ui-design-quality/**' --glob '!docs-ai/docs/initiatives/waves/harness-ui-design-quality.md'`

## Planning Gate

- planning_critic: APPROVE on 2026-05-03. Revised packet preserves successor
  invariants, keeps runtime verdict authority in runtime-proof, bounds optional
  mockup use, fixes stale-reference proof scope, and requires planning
  quality_guard before implementation.
- planning quality_guard: APPROVE on 2026-05-03. Packet is execution-ready:
  successor readback covers retained `user-apps-design` invariants, mockup
  anchors are optional and subordinate to project design truth, runtime verdict
  authority remains in `runtime-proof`, stale-reference proof is executable
  with explicit no-match semantics, and touched-component integrity is
  acceptable with no accepted debt.
- implementation quality_guard: APPROVE on 2026-05-03. Successor invariants
  are preserved, mockup/imagegen remains optional planning support, runtime
  verdict authority remains in `runtime-proof`, and removed-path validation
  covers all three deleted UI-design references.

## Packet

- closed after final review on 2026-05-03.
