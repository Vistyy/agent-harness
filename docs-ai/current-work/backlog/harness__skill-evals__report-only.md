# Backlog Entry: harness/skill-evals/report-only

## Metadata

- Impact: `medium`
- Effort: `M`
- Queue bucket: `Deferred Backlog`

## Problem

Static validation protects durable wording and references, but it cannot prove
that high-risk skills consistently invoke the right role or return the right
shape in realistic conversations.

## Why This Bucket

This belongs in `Deferred Backlog` because the current wave should first fix
skill ownership and validation contracts. Behavioral/model-running evals should
not enter the required quality gate until recurring workflow regressions show
clear value.

## Suggested Next Step

- Suggested target wave (if known): none
- Dependencies/prerequisites: stable skill boundaries after
  `runtime-evidence-guard-policy-1`
- Smallest next slice: create a report-only eval harness for one high-risk
  routing question, likely `verification-before-completion` or
  `subagent-orchestration`.
- Promotion/removal condition: promote when recurring workflow regressions
  justify model-running eval cost, or delete if static checks and review roles
  cover the observed failure class.

## References

- Owning durable doc:
  `skills/harness-governance/references/skill-architecture.md`
- Queue/backlog source:
  `docs-ai/current-work/delivery-map.md` (`skill-evals-report-only`)
- Source wave/task:
  `docs-ai/current-work/runtime-evidence-guard-policy-1/wave-execution.md`
- Files/evidence:
  `../../../scripts/validate_harness.py`, `../../../tests/test_validate_harness.py`
