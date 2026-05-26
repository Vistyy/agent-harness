---
name: work-memory
description: "Manage lightweight remembered work state: delivery maps, active notes, work notes, incoming work, backlog details, closeout notes, and cleanup. Use when work must survive turns, compaction, subagents, backlog routing, or document lifecycle. Use this skill for memory only; it does not own execution authority, solution shape, proof, review, runtime, tests, or completion doctrine."
---

# Work Memory

Owns lightweight remembered work state. It does not own execution authority,
solution shape, proof, review, runtime, test, or completion doctrine.

## Rule

Delivery maps, notes, plans, and summaries are memory. They are never
authority. Picking an item starts `../solution-shaping/SKILL.md` from the
current user objective and repo reality.

Create or update an active note by default for non-trivial work after the user
has accepted the plan when the work moved through discovery or shaping first.
Skip only for trivial, single-turn, low-risk work with no subagent, compaction,
resume, or multi-slice state. Notes are hypotheses. When they conflict with the
objective, repo reality, or a simpler coherent shape, amend, supersede, or
discard them before relying on them.

Read `references/durable-context-contract.md` when creating or updating
delivery-map, backlog, or active work-note memory.

## Memory Shapes

- delivery map: `docs-ai/current-work/delivery-map.md`
- work note: `docs-ai/current-work/work-notes/<item-id>.md` when a visible map
  item or future candidate needs remembered starting detail but work has not
  started
- active note:
  `docs-ai/current-work/active/<item-id>/active-work-note.md` when current
  branch work needs resumable memory and progress visibility
- draft note:
  `docs-ai/current-work/active/<item-id>/active-work-note.draft.md`
- backlog detail: `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md`

The map stays terse. Do not encode status gates in the map. Work notes are not
active progress ledgers; they preserve queued or future starting context only.
Do not treat lane order, work notes, backlog notes, packets, plans, or
summaries as authority. Use `assets/delivery-map.md` as the map shape. Keep
process instructions in this skill, not in each project map.

## Active Notes

An active note records objective, expected finished repo state, current reality,
objective coverage, decisions, target shape, decomposition, evidence strategy,
cleanup, blockers, and remaining required work. It may link subordinate notes,
but the top note owns the branch-level objective.

For broad investigation or adaptation work, stop after discovery with a compact
disposition ledger and proposed owner changes, then wait for user signoff
before implementation. After signoff, the active note is the coarse progress
ledger.

Separate discovery findings from required slices. Discovery findings need a
route: required slice, invalidates shape, slice-local detail, blocker or user
decision, separate backlog work, accepted temporary debt, or rejected/no-change.
Record the reason, owner/interface, and next action or evidence boundary.

Required slices are the accepted objective-preserving decomposition from
`solution-shaping`. Record each required slice with current status, evidence
and review state, residual/cleanup boundary, and blocker or accepted reduction
when relevant. Use a small status vocabulary: `pending`, `implementing`,
`completed`, `blocked`, or `removed by user-accepted reduction`. Review state
names the next gate or result, including `quality_guard pending` for
non-trivial slice drafts before dependent work continues. Record material gaps
against the expected finished state as fix-now, future work, accepted debt,
rejected/no-change, or blocker. Required slices remain required until
completed, blocked, or removed by explicit user-accepted reduction; they cannot
be hidden in backlog or left unrouted to make closeout easier.

A finding or slice does not become current-scope authority merely by appearing
in a note. `solution-shaping` still owns validity, owner, objective coverage,
and stop conditions.

## Backlog

Backlog files preserve work that should not be lost. They are not promises that
the next implementation shape is known. Keep problem, owner, bucket, affected
surface, and suggested next discovery move.

When a backlog item replaces investigation memory, make it resumable without
archaeology. Preserve the compact working model needed for pickup: findings,
uncertainty, owner/boundary, next action or evidence path, promotion/removal
condition, and references. Keep run history out unless it affects a future
decision.

Accepted temporary debt needs explicit user acceptance, owner, risk, and
removal condition. Current-scope cleanup cannot be dumped into backlog unless
the user accepts a reduction or the work is genuinely separate from the active
objective.

## Document Lifecycle

Every memory document needs a live reason to exist. Before closeout, run:

```bash
agent-harness memory status --repo-root <project-root>
agent-harness memory lifecycle --repo-root <project-root> --item <item-id>
```

Use status to see active notes, work notes, and backlog details at a glance.
Use lifecycle to inventory one item's active note, drafts, work note, backlog
details, delivery-map presence, and references before deciding what remains.

Do not create archive folders, closed-note indexes, or historical ledgers just
to preserve completed execution context. If the content is reusable doctrine,
extract it to the owning skill or durable doc and reference existing artifacts
instead of duplicating them. If it is future work, move the smallest useful
problem statement to backlog. If it is only run history, delete it.

Before deleting a non-trivial work note, verify successor coverage for its
durable value. Findings, decisions, uncertainties, owner boundaries, and next
evidence steps must be extracted to a durable doc/backlog item, obsolete by repo
reality, or explicitly accepted as deleted. If coverage is incomplete, keep the
note or keep the unresolved successor state visible.

## Closeout

Close memory only after the actual work outcome, evidence, reviewer verdicts
when used, repo-health cleanup, and remaining required work are known.
If an active note has discovery findings or required slices, closeout first
verifies that every finding is routed and every required slice is completed,
blocked, or removed by explicit user-accepted reduction. The final objective
claim must match that state; unrouted findings or unfinished required slices
block a completion claim.

Closeout is cleanup, not summary-writing. For each artifact reported by
`agent-harness memory lifecycle`, choose exactly one disposition:

- `delete`: no durable value remains after outcome, evidence, and residual work
  are recorded elsewhere or no longer matter
- `extract`: reusable rule, decision, term, or invariant moved to its owning
  skill/doc under `../documentation-stewardship/SKILL.md`
- `backlog`: future work preserved as a small owned problem with next action,
  user acceptance and removal condition when it is accepted temporary debt
- `keep active`: still needed for resume because required work, blocker,
  evidence, or accepted debt remains unresolved

Use `agent-harness memory cleanup --repo-root <project-root> --item <item-id>`
for active-note directories with disposition `delete`; run without `--execute`
first unless the user explicitly asked for immediate deletion.

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
