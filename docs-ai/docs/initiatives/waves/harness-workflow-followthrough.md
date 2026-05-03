# Wave harness-workflow-followthrough - Harness workflow follow-through

**Status:** execution-ready

## Problem

The remaining harness cleanup queue was held in thread memory after a broad
request. That repeats the failure this harness is meant to prevent: broad
objectives become shallow slices without durable successor state.

## Objective

Finish the remaining harness cleanup as file-backed, reviewed slices. Preserve
the original queue, compact low-value prose, and keep one owner per reusable
rule.

## In Scope

- `workflow/slice-state`
- `adapters/prompt-drift`
- `reviewers/split`
- `runtime/adapter-alignment`
- `examples/assets-cleanup`
- `governance/one-owner-validation`
- `skills/compactness-pass`
- `agents/instructions-review`

## Out Of Scope

- Runtime UI/app proof changes outside harness docs, validator, adapters, or
  agent instructions.

## Constraints / Non-Goals

- Use existing wave state; do not add another planning artifact type.
- Prefer deleting or moving rules to their owner over repeating them.
- Planning state lives in packet files, not thread summaries.

## Risks / Dependencies

- Risk: broad queue gets shallow treatment. Disposition: each task owns one
  issue and requires proof/review before `done`.

## References

- `docs-ai/current-work/harness-workflow-followthrough/wave-execution.md`
- `skills/work-routing/SKILL.md`
- `skills/initiatives-workflow/SKILL.md`
- `skills/harness-governance/SKILL.md`

## Planning Gate

- planning_critic: APPROVE on 2026-05-03. Required fixes closed:
  system-boundary disposition, completed-slice evidence, adapter scope,
  compactness breadth, and proof artifacts.
- planning quality_guard: APPROVE on 2026-05-03. Packet preserves the full
  remaining queue, separates owner slices, blocks shallow breadth, and is ready
  for execution.

## Packet

- `docs-ai/current-work/harness-workflow-followthrough/wave-execution.md`
