---
name: code-review
description: "Use when the user asks for code review or when a non-trivial change needs skeptical review of objective fit, proof validity, maintainability, changed repository state, or final repo health before completion."
---

# Code Review

Owns isolated skeptical review and report shape. `../solution-shaping/SKILL.md`
owns when final review is required and what objective is being closed.

## Contract

Review against the original objective, accepted reductions, repo reality,
owner docs, current code/runtime topology, objective coverage, evidence, and
repo health. Plans, work notes, delivery maps, summaries, and claims are
hypotheses/context only.

Before judging implementation consistency, decide whether the note or plan is a
valid interpretation of the objective. An internally consistent plan that
implements the wrong shape is `BLOCK`.

Approval is binary: `APPROVE` or `BLOCK`. Approval means:

- the objective-relevant changed surface and adjacent owner paths were reviewed
  deeply enough
- the final shape is coherent for the objective
- evidence crosses the real interface or lifecycle
- obsolete current-scope paths, tests, docs, and proof-only entrypoints are
  removed or explicitly retained with reason
- remaining required work is visible and not hidden behind a narrowed claim

Diff-only approval is invalid for non-trivial work.

## Check

- Use fresh context and stay read-only.
- Read `../solution-shaping/SKILL.md` before non-trivial review; use its
  review lenses through that owner.
- Treat the plan/note as something to falsify, not as authority.
- Ask whether the proof could pass while the requested behavior is absent; if
  yes, block.
- Inspect edited paths plus adjacent owner/interface paths needed to judge the
  objective.
- Use solution-shaping review lenses to falsify the shape, proof, and
  repository state; unassessed current-scope lens impact blocks approval.
- Ask what was deleted, collapsed, reused, avoided, or added and why.
- Check stale code, duplicate owners, stale tests/docs, fake proof paths,
  runtime proof scope, and remaining work disposition.
- Cite exact `file/path:line` findings.

## Maintainability Bar

Working behavior is not enough when the implementation makes the codebase
harder to change. Block current-scope maintainability regressions.

Be ambitious about structural simplification. A good review asks whether the
change can be reframed so concepts, branches, wrappers, flags, special cases,
fallback paths, or helper layers disappear entirely. Do not approve a refactor
that only moves complexity around while leaving the same number of things a
maintainer must understand.

Prefer direct ownership, explicit models, clear type/state boundaries,
canonical helpers, and deletion of obsolete paths. Do not accept refactors that
move complexity around without reducing what a maintainer must understand.

## Presumptive Blockers

Treat these as blockers unless the implementation gives a clear local reason
and the reason survives objective, owner, and proof review:

- The change preserves incidental complexity when a plausible simpler model,
  owner, or boundary would delete it.
- A file crosses roughly 1000 lines because of the change, or a large file
  absorbs new responsibility that could have a focused owner.
- New ad hoc branching, flags, nullable modes, fallback paths, or special cases
  are inserted into an already busy flow.
- Feature-specific logic leaks into shared/general paths instead of the owning
  layer, module, service, component, policy, or adapter.
- The change adds a thin wrapper, identity abstraction, generic dispatcher, or
  pass-through helper that does not reduce caller knowledge.
- The contract becomes cast-heavy, `any`/`unknown`-heavy, loosely shaped, or
  unnecessarily optional instead of making the invariant explicit.
- A bespoke helper duplicates an existing canonical utility or near-identical
  local helper.
- The implementation serializes independent work or makes related state
  updates non-atomic when a cleaner structure is available.
- Tests pass but the changed path is harder to scan, reason about, or safely
  extend.

## Review Questions

Ask these for every meaningful changed surface:

- Can the change be reframed so fewer concepts, branches, flags, modes, or
  helper layers exist?
- Does this improve the local architecture, or does it add another exception
  to an already complicated path?
- Is the touched owner/interface still the right owner, or did the work expose
  a missing boundary?
- Is feature logic living in the canonical layer, package, service, component,
  or module?
- Are repeated conditionals signaling a missing model, state machine, policy,
  typed contract, or helper?
- Is this abstraction earning its keep, or could direct code be clearer?
- Did the diff introduce casts, loose objects, optional fields, silent
  fallbacks, or implicit invariants that should be explicit?
- Did the change reuse existing helpers and patterns before adding new ones?
- Did the changed file or component grow past a healthy size for its role?
- Could orchestration be simpler, more parallel, or more atomic without
  changing behavior?
- What obsolete branch, fallback, wrapper, test, doc, or proof-only entrypoint
  should be deleted in the same change?

## Preferred Remedies

When a maintainability issue is real, ask for a structural fix, not cosmetic
cleanup:

- Delete an indirection layer instead of renaming or polishing it.
- Collapse duplicate branches into one clear flow.
- Move feature logic to the layer that owns the concept.
- Replace special cases with an explicit model, policy, state object, or typed
  contract.
- Split a large file into focused modules or components with clear ownership.
- Reuse the canonical helper instead of adding a near-duplicate.
- Make type, state, and lifecycle boundaries explicit so control flow gets
  simpler.
- Separate orchestration from business logic when mixing them hides the real
  invariant.
- Make related updates atomic when partial state would be hard to reason about.
- Delete obsolete fallback paths and tests instead of carrying compatibility
  for no current owner.

Do not spend review attention on naming nits while structural issues remain.
Prefer a small number of high-confidence findings with required fixes over a
long cosmetic list.

## Issue Disposition

Every concrete issue is fixed, routed, tracked, accepted by the user as a
reduction/debt, or dropped as unevidenced.

Current-scope cleanup cannot be moved to backlog merely to approve the branch.

## Output

Report:

- verdict: `APPROVE` or `BLOCK`
- binding objective and accepted reductions
- authority inspected
- reviewed scope and why it is sufficient or insufficient
- plan/note interpretation verdict
- objective coverage verdict
- evidence/proof validity
- repo-health verdict
- findings with location, impact, required fix, and disposition
- remaining required work or `none`
