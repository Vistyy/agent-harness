---
name: initiatives-workflow
description: "Use for durable wave/backlog context: delivery-map structure, context notes, backlog entries, and closeout cleanup."
---

# Initiatives Workflow

Owns durable context: delivery map, wave briefs, context notes, and backlog
entries. It does not own design, readiness, review, proof, runtime, or test
doctrine.

## Rule

Use durable context only when the work must survive queue tracking, handoff,
interruption, resume, review, or multiple slices. Durable context is memory, not
authority. When it conflicts with the binding objective, repo reality, or the
simplest correct end state, amend, supersede, or close it before continuing.

Read `references/durable-context-contract.md` when creating or updating durable
context.

## State

- map: `docs-ai/current-work/delivery-map.md`
- brief: `docs-ai/docs/initiatives/waves/<wave-id>.md` when queue-visible status
  is needed
- context note: `docs-ai/current-work/<wave-id>/wave-execution.md`
- draft context note: `docs-ai/current-work/<wave-id>/wave-execution.draft.md`
- delivery brief: `docs-ai/current-work/<wave-id>/delivery-brief.md` only when
  a durable closeout artifact is useful
- backlog: `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md`

Statuses: `discovery-required`, `execution-ready`, `done`, `retired`.

`execution-ready` means durable context is usable. It does not mean the plan is
still the right engineering move.

## Execute

Before execution:

- durable context, when used, preserves objective, accepted reductions, simplest
  correct end state, owner/interface, order, blockers, readiness claim, and
  evidence needs across handoff/resume
- `planning_critic` and `quality_guard` objections are resolved for
  non-trivial planning

During execution:

- execute in dependency order; if a later lane becomes the right lane, amend or
  supersede the context instead of silently jumping
- classify user checkpoints or feedback through `../feedback-address/SKILL.md`
  before code changes
- amend context objective, checkpoint, decisions, slices, readiness, or proof
  before code when feedback changes the work shape
- update blockers, decisions, evidence, residuals, and follow-up in the context
- use `quality_guard` after each non-trivial implementation chunk to challenge
  the current diff against the objective and end state

Stop on objective drift, stale context, missing design/readiness state,
discovery leakage, or current-scope owner defects not fixed/routed/accepted.

## Closeout

Close only after verification, final review, and `../readiness-claim/SKILL.md`
support the final claim and delivery brief when the work is non-trivial.

Extract retained value to the owning durable surface or valid backlog. Dispose
of every current-scope issue by fixing it, routing it to valid backlog, or
recording accepted temporary debt. Then remove, mark done, or supersede active
context and any durable delivery brief so no stale lane can steer later work.

## Assets

- discovery brief: `assets/wave-brief-discovery-required.md`
- execution-ready brief: `assets/wave-brief-execution-ready.md`
- context note: `assets/wave-execution.md`
- backlog item: `assets/backlog-entry.md`
