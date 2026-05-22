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

## Document Lifecycle

Every memory document needs a live reason to exist. At closeout, decide the
fate of each touched or related memory artifact instead of leaving it because
it was useful during the work.

- active note: delete after branch closeout unless it still contains unresolved
  required work, an active blocker, or accepted temporary debt that cannot yet
  move to backlog
- draft note: delete after it is merged into the active note, superseded, or no
  longer needed for recovery
- work note: keep only when it remains a useful future discovery starting
  point; delete it when completed, invalidated, or fully extracted
- backlog detail: delete when completed, invalidated, superseded, or merged
  into a more accurate backlog item
- delivery-map entry: remove completed or obsolete entries; keep only terse
  starting points for real future discovery
- durable doc: delete or merge only under
  `../documentation-stewardship/SKILL.md` successor review, or with explicit
  user-accepted deletion of the invariant
- evidence artifact: keep only when project policy, review, audit, or future
  reproduction needs the raw artifact; otherwise summarize the needed fact in
  the owning note/doc and remove the transient artifact

Do not create archive folders, closed-note indexes, or historical ledgers just
to preserve completed execution context. If the content is reusable doctrine,
extract it to the owning skill or durable doc. If it is future work, move the
smallest useful problem statement to backlog. If it is only run history, delete
it.

## Closeout

Close memory only after the actual work outcome, evidence, reviewer verdicts
when used, repo-health cleanup, and remaining required work are known.

Closeout is a cleanup step, not a summary-writing step. For each memory
artifact, choose exactly one disposition:

- `delete`: no durable value remains after outcome, evidence, and residual work
  are recorded elsewhere or no longer matter
- `extract`: reusable rule, decision, term, or invariant moved to its owning
  skill/doc under `../documentation-stewardship/SKILL.md`
- `backlog`: future work preserved as a small owned problem with next action,
  user acceptance and removal condition when it is accepted temporary debt
- `keep active`: still needed for resume because required work, blocker,
  evidence, or accepted debt remains unresolved

Use `agent-harness memory cleanup --repo-root <project-root> --item <item-id>`
for active-note directories after confirming deletion is the right
disposition; run without `--execute` first unless the user explicitly asked for
immediate deletion.

Update the map/backlog only to preserve useful future starting points, remove
completed or obsolete memory, or keep remaining required work visible. Do not
leave completed current-work notes behind merely as proof that the work
happened; the proof belongs in the final report, durable owner, or retained
artifact named by project policy.

## Assets

- work note: `assets/work-note.md`
- active note: `assets/active-work-note.md`
- backlog item: `assets/backlog-entry.md`
- delivery map: `assets/delivery-map.md`
