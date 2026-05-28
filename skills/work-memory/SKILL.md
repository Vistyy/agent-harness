---
name: work-memory
description: "Manage lightweight work state: delivery maps, queued items, active control sheets, detail notes, closeout notes, and cleanup. Use when work must survive turns, compaction, subagents, queue routing, or document lifecycle. Use this skill for memory/state only; it does not own execution authority, solution shape, proof, review, runtime, tests, or completion doctrine."
---

# Work Memory

Owns lightweight work state. `work-memory` is the legacy skill name; the
concept is current-work state. It does not own execution authority, solution
shape, proof, review, runtime, test, or completion doctrine.

## Rule

Delivery maps, notes, plans, and summaries are memory. They are never
authority. Picking an item starts `../solution-shaping/SKILL.md` from the
current user objective and repo reality.

Create or update active work state by default once work is non-trivial or must
survive compaction, review, delegation, multiple slices, interruption, or
closeout. Skip only for trivial, single-turn, low-risk work with no durable
state need. Notes are hypotheses. When they conflict with the objective, repo
reality, or a simpler coherent shape, amend, supersede, or discard them before
relying on them.

Read `references/durable-context-contract.md` when creating or updating
delivery-map, backlog, or active work-note memory.

## State Shapes

- delivery map: `docs-ai/current-work/delivery-map.md`
- queued item: one inactive work format. Current projects may store this under
  `docs-ai/current-work/work-notes/<item-id>.md` or
  `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md` until the
  repo migrates, but the item still has one live owner.
- active control sheet:
  `docs-ai/current-work/active/<item-id>/active-work-note.md` when current work
  needs resumable memory and progress visibility
- detail note: optional files under `docs-ai/current-work/active/<item-id>/`
  when owner mapping, large-change analysis, evidence, or slice reasoning would
  make the control sheet unreadable
- draft note:
  `docs-ai/current-work/active/<item-id>/active-work-note.draft.md`

The delivery map is a terse queue view and dependency index. It renders the
ordering, dependency, state, and ownership cues needed to choose the next item;
it does not own implementation authority, status gates, or completion claims.
Exact behavior belongs in code, tests, schemas, config, generated artifacts, or
durable owner docs. Use `assets/delivery-map.md` as the map shape and keep
process instructions in this skill, not in each project map.

## Queued Items

Queued items preserve work that is not active. Minimum useful fields:

- problem
- queue state: `ready`, `waiting`, or `deferred`
- owner or suspected owner
- next discovery move

Optional fields exist only when useful: rank for multiple ready items, domain
or type for routing, dependency/blocker/wake-up condition for waiting items,
and reason not active now.

When a queued item becomes active, move retained context into the active
control sheet, retarget the delivery-map link, and delete or explicitly retire
the queued item. An item must not have both queued and active owners.

## Active Control Sheets

An active control sheet records one live objective, expected finished repo
state, current repo reality, owner/interface model, required atomic claims,
proof/review state, blockers, user decisions, closeout state, and links to
detail notes when needed. It should answer "where are we and what remains?"
without becoming an investigation diary or rigid field checklist.

For broad investigation or adaptation work, stop after discovery with a compact
disposition ledger and proposed owner changes, then wait for user signoff
before implementation. After signoff, the active control sheet is the coarse
progress ledger.

Separate discovery findings from required claims. Discovery findings need a
route: required claim, invalidates shape, claim-local detail, blocker or user
decision, separate backlog work, accepted temporary debt, or rejected/no-change.
Record the reason, owner/interface, and next action or evidence boundary.

Required atomic claims are the accepted objective-preserving decomposition from
`solution-shaping`. Record each required claim with current status, evidence
and review state, residual/cleanup boundary, and blocker or accepted reduction
when relevant. Use a small status vocabulary: `pending`, `implementing`,
`completed`, `blocked`, or `removed by user-accepted reduction`. Review state
names the next gate or result, including `quality_guard pending` for
non-trivial drafts before dependent work continues. Record material gaps
against the expected finished state as fix-now, future work, accepted debt,
rejected/no-change, or blocker. Required claims remain required until
completed, blocked, or removed by explicit user-accepted reduction; they cannot
be hidden in backlog or left unrouted to make closeout easier.

A finding or claim does not become current-scope authority merely by appearing
in work state. `solution-shaping` still owns validity, owner, objective
coverage, and stop conditions.

## Backlog

Backlog files and queued items preserve work that should not be lost. They are
not promises that the next implementation shape is known. Keep the problem,
owner, affected surface, and suggested next discovery move.

When a backlog item replaces investigation memory, make it resumable without
archaeology. Preserve the compact working model needed for pickup: findings,
uncertainty, owner/boundary, next action or evidence path, promotion/removal
condition, and references. Keep run history out unless it affects a future
decision.

Accepted temporary debt needs explicit user acceptance, owner, risk, and
removal condition. Current-scope simplification, cleanup, or unification cannot
be dumped into backlog unless the user accepts a reduction or the work is
genuinely separate from the active objective.

## Document Lifecycle

Every memory document needs a live reason to exist. Before closeout, run:

```bash
agent-harness work-state status --repo-root <project-root>
agent-harness work-state check --repo-root <project-root>
```

For per-item artifact inventory and cleanup while the CLI is migrating from
memory to work-state naming, use the legacy commands:

```bash
agent-harness memory lifecycle --repo-root <project-root> --item <item-id>
agent-harness memory cleanup --repo-root <project-root> --item <item-id>
```

Use status to see active control sheets, queued items, backlog details, owner
conflicts, claim/review state, queue state, and closeout text. Use check to
fail mechanical gaps: missing delivery map, duplicate live ownership, invalid
or missing queue state, invalid claim/review statuses, and missing claim/review
state. Use lifecycle to inventory one item's artifacts before closeout.

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

Close work state only after outcome, evidence, reviewer verdicts when used,
repo-health cleanup, and remaining required work are known. Every discovery
finding must be routed and every required claim completed, blocked, or removed
by explicit user-accepted reduction; otherwise completion is blocked.

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
for active state directories with disposition `delete`; run without `--execute`
first unless the user explicitly asked for immediate deletion.

Update the map/backlog only to preserve useful future starting points, remove
completed or obsolete memory, or keep remaining required work visible. Do not
leave completed current-work notes behind merely as proof that the work
happened; the proof belongs in the final report, durable owner, or retained
artifact named by project policy.

## Assets

- work note: `assets/work-note.md`
- active control sheet: `assets/active-work-note.md`
- backlog item: `assets/backlog-entry.md`
- delivery map: `assets/delivery-map.md`
