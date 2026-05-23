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
- Reject proof that could pass while the requested behavior is absent.
- Inspect edited paths plus adjacent owner/interface paths needed to judge the
  objective.
- Use solution-shaping review lenses to falsify the shape, proof, and
  repository state; unassessed current-scope lens impact blocks approval.
- Require an account of what was deleted, collapsed, reused, avoided, or added
  and why.
- Check stale code, duplicate owners, stale tests/docs, fake proof paths,
  runtime proof scope, and remaining work disposition.
- Cite exact `file/path:line` findings.

## Maintainability Bar

Working behavior is not enough. Block current-scope code that is heavier than
the objective requires.

Complexity requires a concrete owner and failure mode. Defensive code is valid
only at real boundaries: external input, auth, money, storage, concurrency,
migrations, distributed runtime, or security. Internal trusted flows stay
direct.

Approve only after confirming the objective cannot be met with fewer concepts,
branches, states, wrappers, fallback paths, public methods, defensive checks,
tests, or docs. Tests protect required behavior, not accidental shape.

## Presumptive Blockers

Treat these as blockers unless the implementation gives a clear local reason
and the reason survives objective, owner, and proof review:

- The change preserves incidental complexity when a plausible simpler model,
  owner, or boundary would delete it.
- A file crosses roughly 1000 lines because of the change, or a large file
  absorbs new responsibility that could have a focused owner.
- New ad hoc branching, flags, nullable modes, fallback paths, or special cases
  are inserted into an already busy flow.
- The change adds a thin wrapper, identity abstraction, generic dispatcher, or
  pass-through helper that does not reduce caller knowledge.
- The contract becomes cast-heavy, `any`/`unknown`-heavy, loosely shaped, or
  unnecessarily optional instead of making the invariant explicit.
- Tests, docs, or proof entrypoints preserve obsolete or accidental API shape.

## Required Remedies

When a maintainability issue is real, require a structural fix, not cosmetic
cleanup:

- Delete an indirection layer instead of renaming or polishing it.
- Collapse duplicate branches into one clear flow.
- Move feature logic to the layer that owns the concept.
- Replace special cases with an explicit model, policy, state object, or typed
  contract.
- Reuse the canonical helper instead of adding a near-duplicate.
- Make type, state, and lifecycle boundaries explicit so control flow gets
  simpler.
- Delete obsolete fallback paths and tests instead of carrying compatibility
  for no current owner.

Do not spend review attention on naming nits while structural issues remain.
Report high-confidence findings with required fixes; omit cosmetic findings
while structural issues remain.

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
