---
name: work-memory
description: "Use when work needs remembered state across turns, compaction, subagents, backlog, or document lifecycle: delivery maps, active notes, work notes, incoming work, closeout notes, and cleanup. Memory only; not execution authority."
---

# Work Memory

Owns lightweight remembered work state. It does not own execution authority,
solution shape, proof, review, runtime, test, or completion doctrine.

## Rule

Delivery maps, notes, plans, and summaries are memory. They are never
authority. Picking an item starts `../solution-shaping/SKILL.md` from the
current user objective and repo reality.

Create or update an active note by default for non-trivial work. Skip only for
trivial, single-turn, low-risk work with no subagent, compaction, resume, or
multi-slice state. Notes are hypotheses. When they conflict with the objective,
repo reality, or a simpler coherent shape, amend, supersede, or discard them
before relying on them.

Read `references/durable-context-contract.md` when creating or updating
delivery-map, backlog, or active work-note memory.

## Memory Shapes

- delivery map: `docs-ai/current-work/delivery-map.md`
- work note: `docs-ai/docs/initiatives/work-notes/<item-id>.md` when a visible
  map item needs remembered detail
- active note: `docs-ai/current-work/<item-id>/active-work-note.md` when branch
  work needs resumable memory
- draft note: `docs-ai/current-work/<item-id>/active-work-note.draft.md`
- backlog detail: `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md`

The map stays terse. Do not encode status gates in the map. Do not treat lane
order, work notes, backlog notes, packets, plans, or summaries as authority.
Use `assets/delivery-map.md` as the map shape. Keep process instructions in
this skill, not in each project map.

## Active Notes

An active note records objective, current reality, objective coverage,
decisions, target shape, decomposition, evidence strategy, cleanup, blockers,
and remaining required work. It may link subordinate notes, but the top note
owns the branch-level objective.

## Backlog

Backlog files preserve work that should not be lost. They are not promises that
the next implementation shape is known. Keep problem, owner, bucket, affected
surface, and suggested next discovery move.

Accepted temporary debt needs explicit user acceptance, owner, risk, and
removal condition. Current-scope cleanup cannot be dumped into backlog unless
the user accepts a reduction or the work is genuinely separate from the active
objective.

## Closeout

Close memory only after the actual work outcome, evidence, reviewer verdicts
when used, repo-health cleanup, and remaining required work are known.

On closeout, delete active notes with no durable value, extract reusable
doctrine to the owning skill/doc, or move future work into backlog. Update the
map/backlog only to preserve useful future starting points, remove completed or
obsolete memory, or keep remaining required work visible.

## Assets

- work note: `assets/work-note.md`
- active note: `assets/active-work-note.md`
- backlog item: `assets/backlog-entry.md`
- delivery map: `assets/delivery-map.md`
