# Workflow Model Detail: Overlay Contract Redesign

This detail note records the current workflow model behind
`docs-ai/current-work/work-state-flow-map.html`.

## Core Model

- Use one five-step loop: probe, shape, slice, execute/review, close.
- Large-change audit is a probe mode, not a separate workflow.
- Atomic claims are the slicing rule, not a separate gate.
- Independent reconstruction is the review rule, not a separate gate.
- Artifact disposition is the close rule, not summary writing.

## Queued Item

Queued items preserve work that is not active. They need:

- problem
- queue state: `ready`, `waiting`, or `deferred`
- owner or suspected owner
- next discovery move

Optional fields exist only when useful:

- rank for multiple ready items
- domain or type for routing
- dependency, blocker, or wake-up condition for waiting items
- reason not active now

Queued defects are valid before work starts. During active work, defects in
the touched owner are current scope by default, not queue material.

The delivery map should render queued fields instead of inventing a second
classification scheme. Active work is a lifecycle state outside the queue.
Example queue-state meanings:

- `ready`: promotable now; rank decides which item is next
- `waiting`: follow-on, blocked, or triggered work with a named condition
- `deferred`: preserved without near-term scheduling pressure

## Active Control Sheet

The active control sheet should show:

- binding objective and expected finished state
- current repo reality
- owner/interface model
- required atomic claims and review/proof state
- blockers and user decisions
- closeout state
- links to detail notes when needed

The control sheet should answer "where are we and what remains?" without
becoming an investigation dump or rigid field checklist. Detail notes exist
only when owner mapping, large-change analysis, evidence, or slice reasoning
would make the control sheet unreadable.

## Probe

Probe falsifies the assumption that work is local and straightforward. For
large branches, probe includes mechanical diff inventory, owner clustering,
and risk ranking.

## Shape

Shape defines the expected finished repo state and the simplest owner-correct
target. Prefer delete, collapse, reuse, rewrite, and unification before adding
structure.

Fix-now applies only when all of these are true:

- the finding is exposed by current work or lies on the touched owner path
- it affects owner coherence, lifecycle consistency, proof validity, cleanup,
  or the simplicity of the current target shape
- the repair uses an established peer pattern already present in the repo
- the repair reduces or unifies structure instead of adding capability, public
  surface, optional behavior, compatibility path, or speculative abstraction
- the repair can be proved inside the current atomic claim or a directly
  adjacent atomic claim

Queue the work or stop for a decision when the finding adds capability,
introduces a new abstraction or pattern, requires broad migration outside the
touched owner path, has multiple valid target patterns, or cannot be proved
within the current or adjacent atomic claim.

## Slice

Atomic claim rule:

`For <owner/interface>, <behavior/state/contract> changes from <current> to
<target> through <entrypoint/lifecycle>, proved by <proof>.`

The slice includes every changed path needed to make exactly that claim true,
and nothing whose correctness is a separate claim. Split on independent
owners, state authorities, production triggers, failure policies, proof paths,
or cleanup dispositions. Merge slices that cannot prove an owner-visible claim
alone.

Example-derived lessons:

- A domain label can still be too broad; split by falsifiable claims.
- Review-only claims are valid when they block wrong implementation.
- Models-only, tests-only, or docs-only slices are invalid unless tied to a
  real owner claim.

## Execute And Review

Plan acceptance is not a lock. Re-enter shaping when discovery,
implementation, review, or proof evidence invalidates:

- owner/interface
- target shape
- slice order
- proof strategy
- current-scope boundary
- accepted complexity

Implementation should stop rather than reward-hack a stale plan.

Reviewer reconstruction is bounded by role:

- planning critic reconstructs objective, target state, and slice boundaries
- quality guard reconstructs the assigned atomic claim and enough lifecycle
  context to judge the implementation
- final reviewer reconstructs whole objective coverage from claim outcomes,
  proof, residuals, repo state, and artifact disposition

## Close

Closeout decides artifact disposition and blocks completion when unresolved
current-scope claims, unrouted findings, missing proof, or accepted debt are
not visible.
