---
name: delivery-workflow
description: "Use for non-trivial work from objective or delivery-map starting point through discovery, shape, implementation, evidence, review, and closeout."
---

# Delivery Workflow

Owns the path from user objective to PR-ready repository state.

## Contract

Preserve the binding objective until the repo actually satisfies it, the user
accepts a reduction, or the work is blocked and visible. Do not replace a broad
objective with a convenient slice, note, plan, claim, test, or map entry.

Delivery-map lanes, work notes, backlog notes, plans, and summaries are memory.
They are never authority. Picking a delivery-map item starts discovery from the
current objective and repo reality; it does not authorize direct execution.

## Flow

For non-trivial work: discover repo reality, define end-to-end objective
coverage, choose the simplest coherent target shape, decompose into valid
implementation slices, apply review lenses, get adversarial planning review,
implement valid slices, prove real behavior, get final repo-health review, then
close honestly and update memory.

Small, local work may run in-thread without a durable note, but the same
objective, evidence, and repo-health judgment still applies.

## Objective Coverage

For substantial behavior, architecture, workflow, runtime, or cross-boundary
work, cover: entrypoint/actor, production trigger, state authority,
lifecycle owner, core behavior, failure/retry/recovery, status projection,
user/operator visibility, persistence and side effects, cleanup/legacy
removal, observability, tests/runtime proof, docs/memory, and residual work.

If a slice is narrow, state how it moves the larger coverage model forward.
Coverage gaps are blockers unless explicitly deferred, tracked, and not needed
for the current branch claim.

## Implementation Slices

Any agent editing files for non-trivial work is acting as implementer, including
the parent thread. Implementation may proceed only from a valid slice.

A valid slice has objective contribution, accepted reductions, selected
owner/interface, target shape, expected change surface, evidence path,
cleanup/residual boundary, and no hidden design decision left to the
implementer.

Decompose into the smallest coherent slices that can be implemented and
verified honestly. A slice is too large when review cannot isolate its outcome
or it leaves multiple hidden decisions. A slice is too small when it cannot
prove meaningful progress toward the larger objective.

Invalid slices are blockers, not implementation challenges. Stop and route back
to planning when repo reality contradicts the slice, the owner/interface is
wrong, proof would be fake, required facts are inaccessible, necessary sibling
work is missing, or continuing would narrow the objective.

Do not substitute a convenient narrower diff and call it complete. Blockers must
name inspected evidence, the contradiction or missing decision, why continuing
risks wrong implementation or fake proof, and the smallest planning decision or
revised slice needed.

## Target Shape

Optimize for the simplest correct end state, not the smallest diff. Prefer
delete, collapse, reuse, and rewrite before adding owners, wrappers, gates,
flags, compatibility paths, docs, tests, or process state.

Correct implementation of an avoidably wrong final shape is not approvable.
Block wrong owners, duplicate state/lifecycle/policy/proof authority, hidden
lifecycle, fake proof paths, and compatibility paths without explicit user
acceptance.
This is solution correctness, not plan compliance.

## Active Work Notes

Use one active note for a branch-level objective when memory must survive
handoff, interruption, or multiple slices. It may link subordinate notes for
large subareas, but the top note owns the end-to-end objective.

The note records objective, accepted reductions, current reality, objective
coverage, decisions, blockers, target shape, rejected alternatives,
decomposition, evidence strategy, repo-health cleanup, remaining required work,
and closeout updates.

The note is a hypothesis. Amend, supersede, or discard it when it conflicts
with the objective, repo reality, or a simpler correct shape.

## Evidence

Evidence must cross the claimed real interface. A proof path is invalid when it
could pass while the requested production behavior is absent.

For workflow claims, direct private function calls, hand-built state, manual
tooling, and impossible preconditions do not prove the workflow unless the
production producer path is also exercised.

Use platform proof skills for mechanics only. They do not redefine the
objective or shrink proof obligations.

## Reference Gates

- Read `references/web-boundaries.md` when a browser route, page, shared UI
  module, facade, or screen model is the touched owner.
- Read `references/mobile-client-boundaries.md` when a mobile client/backend
  contract is the touched owner.
- Read `references/python-service-boundaries.md` when a Python service, unit of
  work, repository, handler, or dynamic input boundary is the touched owner.
- Read `references/review-lenses.md` before non-trivial planning, review,
  evidence design, or closeout.

## Review

Reviewers judge against original objective, accepted clarifications, repo
reality, owner docs, current code/runtime topology, active note as hypothesis,
and parent/implementer summary last.

Planning review uses review lenses and blocks if the note misinterprets the
objective, hides design decisions, decomposes around fake proof, creates invalid
slices, or leaves current-scope lifecycle, cleanup, lens, or proof obligations
uncovered.

Final review uses the same lenses on the whole changed slice and blocks if the
repo is not coherent for the objective: obsolete paths remain, owners are
duplicated, tests/docs prove or describe stale behavior, proof-only entrypoints
were added, or current-scope cleanup/lens impact is dumped into backlog.

## Closeout

Close only with outcome, real-interface evidence and limits, reviewer verdicts,
repo-health cleanup, remaining required work/blockers/reductions, and memory
updates or reason none were needed.

Remaining work required for the lane/objective stays visible. Do not hide it
behind a narrower success claim.
