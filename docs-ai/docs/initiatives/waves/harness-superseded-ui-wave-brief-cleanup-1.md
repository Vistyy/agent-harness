# Wave harness-superseded-ui-wave-brief-cleanup-1 - Superseded UI wave brief cleanup

**Status:** done

## Objective Boundary

- original objective: apply completed-wave/reference governance to delete a
  first tranche of superseded UI/design wave briefs whose retained invariants
  already live in real durable owners.
- accepted reductions: non-UI completed wave brief cleanup remains a later
  tranche; the current consolidated UI workflow brief, preservation-anchor
  brief, and UI-runtime-evidence redesign brief remain for later successor
  review; no replacement archive, index, ADR, or backlog.
- residual gaps: completed non-UI wave briefs, the consolidated UI workflow
  brief, preservation-anchor brief, and UI-runtime-evidence redesign brief
  remain pending separate cleanup.

## Context

- The target briefs explicitly state they were superseded by later UI workflow
  compaction or folded into `user-apps-design`.
- Current durable owners already carry the reusable UI design, `design_judge`,
  runtime-proof, browser/mobile screenshot mechanics, final-review, adapter,
  and validation contracts.

## Cleanup Tranche

- `docs-ai/docs/initiatives/waves/harness-design-anti-pattern-gate-1.md`
- `docs-ai/docs/initiatives/waves/harness-design-command-specialization-1.md`
- `docs-ai/docs/initiatives/waves/harness-design-context-contract-1.md`
- `docs-ai/docs/initiatives/waves/harness-ui-design-quality.md`

## Promotion Requirements

- successor review maps every retained invariant class to a durable owner or
  accepted deletion;
- stale-reference scan names any remaining direct references to deleted wave
  IDs;
- `planning_critic` and `quality_guard` approve before canonical packet
  promotion.

## Planning Gate Record

- `planning_critic`: approved; touched-component integrity acceptable, no
  must-block signals, no accepted-debt backlog link, and residual risk limited
  to deferred preservation-anchor, UI-runtime-evidence redesign, consolidated
  UI workflow, and non-UI cleanup tranches.
- `quality_guard`: approved; touched-component integrity acceptable, no
  must-block signals, no accepted-debt backlog link, and residual risk limited
  to the same deferred tranches.

## Closeout

- deleted:
  - `docs-ai/docs/initiatives/waves/harness-design-anti-pattern-gate-1.md`;
  - `docs-ai/docs/initiatives/waves/harness-design-command-specialization-1.md`;
  - `docs-ai/docs/initiatives/waves/harness-design-context-contract-1.md`;
  - `docs-ai/docs/initiatives/waves/harness-ui-design-quality.md`.
- successor review:
  - project design source, generated mockup posture, broad UI dimensions, and
    removed UI reference validation remain in durable owners;
  - former operation labels and global report contracts are accepted deletion
    as obsolete after later UI workflow compaction.
- proof:
  - exact stale-reference scan for the four target IDs reported only this
    cleanup wave's durable brief/current-work packet references;
  - `uv run python scripts/validate_harness.py`: passed;
  - `agent-harness governance check --repo-root .`: passed;
  - `just quality-fast`: 85 tests passed, harness validation self-test passed,
    harness validation passed, and Codex install smoke passed.
- reviews:
  - `planning_critic`: approved promotion;
  - `quality_guard`: approved promotion and implementation;
  - `final_reviewer`: approved closeout review with no findings.
- residual scope: preservation-anchor, UI-runtime-evidence redesign,
  consolidated UI workflow, non-UI completed wave briefs, and no-replacement
  cleanup remain later tranches.
