# Backlog Entry: harness/skill-reference-gates/normalization

## Metadata

- Impact: `medium`
- Effort: `M`
- Queue bucket: `Deferred Backlog`

## Problem

`harness-governance` now defines skill references as mandatory purpose gates:
if the current task matches a reference row, the agent must read it before
acting on that purpose. Existing skill bodies still contain mixed wording, such
as optional reference sections, bare reference maps, and soft "load what you
need" phrasing.

## Why This Bucket

This belongs in `Deferred Backlog` because the current change establishes the
governance rule and fixes the owner first. Repo-wide normalization should be a
separate cleanup slice so each skill can preserve its hot-path invariants while
converting reference rows to mandatory gates.

## Suggested Next Step

- Suggested target wave (if known): none
- Dependencies/prerequisites: finalized `harness-governance` reference-gate
  policy
- Smallest next slice: audit all `skills/*/SKILL.md` reference sections and
  classify each row as mandatory gate, always-needed invariant, stale link, or
  optional background to delete/demote.
- Promotion/removal condition: remove this backlog item when all reusable skill
  reference sections use mandatory purpose-gate wording or no longer contain
  non-contract reference links.

## References

- Owning durable doc:
  `skills/harness-governance/SKILL.md`
- Authoring rule:
  `skills/harness-governance/references/skill-architecture.md`
- Queue/backlog source:
  `docs-ai/current-work/delivery-map.md`
- Source wave/task:
  none; user-requested harness governance simplification pass
- Files/evidence:
  `skills/mobile-design/SKILL.md`, `skills/webapp-testing/SKILL.md`,
  `skills/mobileapp-testing/SKILL.md`
