---
name: initiatives-workflow
description: "Use for delivery-map, backlog, and active work-note memory; not for execution authority."
---

# Initiatives Workflow

Owns delivery-map, backlog, and active work-note memory. It does not own
execution authority, design, proof, review, runtime, test, or completion
doctrine.

## Rule

The delivery map is remembered intent and rough sequencing. Everything listed
there is a discovery starting point, not executable scope. Picking a lane
or item starts `../delivery-workflow/SKILL.md` discovery from the current user
objective and repo reality.

Use durable notes only when work must survive handoff, interruption, resume, or
multiple slices. Notes are hypotheses. When they conflict with the objective,
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

The map stays terse: lanes are independently pickable initiative tracks, lane
order is sequential by default, and each item is one or two lines with a link.
If strict dependencies exist across lanes, prefer one longer lane; rare
exceptions may be called out inline.

## Active Notes

An active note records objective, current reality, objective coverage,
decisions, target shape, decomposition, evidence strategy, cleanup, blockers,
and remaining required work. It may link subordinate notes, but the top note
owns the branch-level objective.

Do not encode status gates in the map. Do not treat lane order, work notes,
backlog notes, packets, plans, or summaries as authority.

## Backlog

Backlog files preserve work that should not be lost. They are not promises that
the next implementation shape is known. Keep problem, owner, bucket, affected
surface, and suggested next discovery move. Accepted temporary debt also needs
explicit user acceptance and removal condition.

Current-scope cleanup cannot be dumped into backlog unless the user accepts a
reduction or the work is genuinely separate from the active objective.

## Closeout

Close memory only after `../delivery-workflow/SKILL.md` closeout names completed
work, remaining required work, evidence, reviewer verdicts, and repo-health
cleanup.

Update the map/backlog only to preserve useful future starting points, remove
completed or obsolete memory, or keep remaining required work visible.

## Assets

- work note: `assets/work-note.md`
- active note: `assets/active-work-note.md`
- backlog item: `assets/backlog-entry.md`
