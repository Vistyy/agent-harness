# Backlog Entry: harness/design-workflow/anti-pattern-gate

## Metadata

- Impact: `high`
- Effort: `M`
- Queue bucket: `Deferred Backlog`
- status: `open`
- owner: `user-apps-design`
- created: `2026-05-05`
- removal condition: promote to a wave after the design-context/register
  contract lands, or close if a project-neutral detector gate is rejected.

## Problem

Impeccable's deterministic anti-pattern detector is a core design-workflow
mechanism. The current wave does not add an automated anti-slop gate, so broad
UI work still depends on review judgment to catch generic patterns.

## Why This Bucket

Explicitly deferred follow-up. Detector rules need the design-context/register
contract first so project-approved taste and product-register defaults are not
rejected as global anti-patterns.

## Suggested Next Step

- Suggested target wave (if known): `harness-design-anti-pattern-gate-1`
- Dependencies/prerequisites: `harness-design-context-contract-1`
- Smallest next slice: define a register-aware anti-pattern report consumed by
  `user-apps-design`, `runtime_evidence`, and `design_judge`; start with
  documented checks before deciding whether to wrap `npx impeccable detect` or
  build a harness-native checker.
- Promotion/removal condition: promote when broad UI work needs automated
  anti-generic evidence; remove if the harness deliberately keeps this as
  human-review-only design judgment.

## References

- Owning durable doc: `skills/user-apps-design/references/design-quality-rubric.md`
- Queue/backlog source: `docs-ai/current-work/delivery-map.md`
- Source wave/task: `harness-design-context-contract-1/harness/design/context-contract`
- Files/evidence: `https://impeccable.style/slop/`
