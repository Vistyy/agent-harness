# Skill Redesign Detail: Overlay Contract Redesign

This detail note records the skill-boundary changes chosen for the overlay
workflow redesign.

## Changed Existing Skills

- `solution-shaping`: own the probe, shape, and slice parts of the five-step
  flow, including large-change probe mode, atomic claims, unification fix-now,
  and replan triggers.
- `work-memory`: rewrite or rename toward `work-state`; own queued item,
  active control sheet, detail-note lifecycle, minimum CLI usage, and closeout
  artifact inventory.
- `code-review`: strengthen default-blocked review, simplicity/shape review,
  current-scope disposition, independent reconstruction, and convergence
  verdicts.
- `subagent-handoff`: require reviewers and implementers to receive active
  control sheet path or a named no-state reason, plus authority/proof inputs.
- `verify-work`: preserve proof selection and block proof that can pass while
  the target shape is wrong.

## Reference Decision

Do not create references for rules that are always needed after a skill is
loaded. Keep probe/shape/slice, fix-now, atomic claims, work-state shape, and
reviewer reconstruction in the owning skill bodies.

Use focused references only when the guidance is occasion-specific, such as
owner-boundary lenses or domain review lenses that are not always relevant.
Split into a new skill only if a distinct trigger, load gate, output, or
independent consumer appears.

## Reviewer Role Changes

Planning critic:

- default to `BLOCKED` until objective and expected finished state are
  reconstructed
- independently derive the objective, expected finished state, atomic slices,
  proof route, cleanup boundary, and current-scope debt disposition from repo
  evidence before comparing with the parent plan
- reject plans without probe evidence
- reject large-change plans without diff inventory, owner/risk clustering, and
  atomic claim derivation
- reject slices that cannot prove objective progress
- reject domain/file-count splits that are too broad to inspect, review, prove,
  and close as coherent owner/lifecycle units
- return a convergence verdict: converged, converged with non-material deltas,
  divergent, or blocked by missing authority

Quality guard:

- check whether implementation evidence invalidates the plan
- independently reconstruct the intended claim from objective, owner docs,
  changed surface, and proof artifacts; do not merely compare the diff to the
  accepted plan
- run simplicity/shape review, not only bug review
- block wrappers, shims, bypassed owners, stale compatibility paths, and
  unnecessary abstractions even when tests pass
- block missed simplification/unification when current work exposes an
  inconsistency and an established peer pattern would make the touched system
  simpler without adding capability
- return to planning when the target shape is wrong

Final reviewer:

- confirm reviewer/CLI gates ran or were explicitly skipped with reason
- confirm reviewer conclusions converged with repo evidence, not only with the
  parent story
- confirm no current-owner defect was parked as future work
- confirm final proof matches objective and target shape

Reviewer convergence:

- `converged`: independent reconstruction reaches the same objective, target
  shape, slice boundaries, proof route, and cleanup disposition.
- `converged with non-material deltas`: wording or sequencing differs, but no
  owner, proof, scope, cleanup, or objective coverage changes.
- `divergent`: reviewer finds a materially different objective interpretation,
  simpler target shape, slice boundary, proof route, current-scope debt
  disposition, or replan trigger. Verdict must be `BLOCK`.
- `blocked by missing authority`: reviewer cannot inspect enough evidence to
  reconstruct the target independently. Verdict must be `BLOCKED`.

Implementer:

- stop and return a replan finding when repo evidence contradicts the assigned
  slice
- do not continue polishing code built on the wrong shape

## CLI Direction

Core commands:

- `work-state status`
- `work-state check`

Reject tools that pretend to judge architecture mechanically. Mechanical
inventory may expose changed files, stats, deletes, renames, generated files,
and buckets; the agent must interpret owner and shape.

When these commands exist, agents should run the relevant command by default
instead of waiting for explicit user instruction. Skipping a relevant command
needs a short reason in the working state or final report.

## Decomposition Adequacy

Large scope must be decomposed, not reduced. Derive slices from falsifiable
repo claims, not folders, file counts, or prompt-sized chunks.

Atomic claim rule:

`For <owner/interface>, <behavior/state/contract> changes from <current> to
<target> through <entrypoint/lifecycle>, proved by <proof>.`

The slice includes every changed path needed to make exactly that claim true
end to end, and nothing whose correctness is a separate claim.

A proposed slice is admissible only when it can be reviewed and completed
deeply as one coherent unit:

- owner/interface is clear
- lifecycle and state authority are clear
- proof path would fail if the slice is incomplete
- cleanup boundary is explicit
- reviewer can inspect adjacent paths without hand-waving
- residual work is named and cannot hide current-scope defects

Reject splits based only on domain names, file counts, or convenience. If a
slice still contains multiple unrelated owners, hidden design decisions, or too
much surface for a reviewer to inspect rigorously, re-slice before
implementation.

Split when a proposed slice has more than one primary owner, state authority,
production trigger, failure policy, independent proof path, or cleanup
disposition. Merge when a proposed slice cannot prove a behavior or owner claim
alone, such as "models only", "tests only", or "docs only" work that leaves the
real lifecycle unproved.

## Fix-Now Disposition

Current-scope findings must be dispositioned immediately. Fix now only when the
finding is exposed by current work or lies on the touched owner path, affects
owner coherence/lifecycle/proof/cleanup/simplicity, follows an established
peer pattern, reduces or unifies structure, and can be proved inside the
current or directly adjacent atomic claim. Queue or stop for a decision when
the change adds capability, introduces a new abstraction or pattern, expands
product scope, requires broad migration outside the touched owner path, has
multiple valid target patterns, or cannot be proved in the current or adjacent
claim.

## Workflow Reduction

Do not add gates for gates. Keep one five-step flow:

- probe prevents shallow symptom fixes and first-found cleanup on broad branches
- shape prevents wrong owner and over-complex target design
- slice prevents sign-off decomposition
- execute/review prevents stale plans, parent-story approval, and over-shaped
  code
- close prevents hidden unfinished current-scope work
- CLI checks enforce only observable state where a mechanical check is reliable

If a proposed step does not prevent one of those failures, it does not belong
in the core workflow.
