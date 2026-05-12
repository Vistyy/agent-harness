# Wave harness-done-brief-closeout-validator-1 - Done wave brief closeout validator

**Status:** discovery-required

## Objective Boundary

- original objective: define the global harness fix for completed wave brief
  cleanup so closeout can identify briefs that are delete-ready, blocked, or
  still need retained-invariant extraction.
- accepted reductions: do not implement the validator or cleanup command in
  this wave brief; this is a planning target for later execution.
- residual gaps: command shape, check placement, and exact successor-detection
  rules remain open for planning intake.

## Planning Gaps

- Decide whether the owner is `agent-harness wave cleanup`,
  `agent-harness governance check`, a new `wave closeout-check`, or a
  combination of report plus optional `--execute` cleanup.
- Define a disposability report for done briefs:
  - `delete-ready` when no current-work packet, no delivery-map entry, no live
    durable references, and no retained-only sections remain.
  - `needs-extraction` when retained closeout, audit, retrospective,
    acceptance-anchor, or process-correction content lacks a durable successor.
  - `blocked` when durable docs or current-work still depend on the done brief.
  - `manual-review` when automation cannot classify the retained content.
- Preserve the documentation-stewardship rule: completed wave briefs are not
  durable doctrine, but deletion is valid only after retained invariants move
  to a durable owner or valid backlog.
- Decide how the tool detects stale delivery-map planning slugs after an
  execution-ready packet defines bounded slices.
- Define tests with synthetic projects proving the tool refuses blind deletion,
  reports successor gaps, and allows cleanup only for delete-ready briefs.

## Starting Points

- `skills/initiatives-workflow/SKILL.md`
- `skills/documentation-stewardship/SKILL.md`
- `skills/harness-governance/SKILL.md`
- `agent_harness/waves.py`
- `agent_harness/governance.py`
- `tests/test_agent_harness_cli.py`
- `tests/test_validate_harness.py`

## Promotion Requirement

Promote only after `planning-intake`, `planning_critic`, and `quality_guard`
approve the command/check owner, successor evidence model, refusal behavior,
test matrix, and closeout workflow wording.
