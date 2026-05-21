---
name: code-review
description: "Use when the user asks for code review or when delivery-workflow needs final isolated repo-health review."
---

# Code Review

Owns isolated skeptical review and report shape. `../delivery-workflow/SKILL.md`
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
- Read `../delivery-workflow/SKILL.md` before non-trivial review; use its
  review lenses through that owner.
- Treat the plan/note as something to falsify, not as authority.
- Ask whether the proof could pass while the requested behavior is absent; if
  yes, block.
- Inspect edited paths plus adjacent owner/interface paths needed to judge the
  objective.
- Use delivery-workflow review lenses to falsify the shape, proof, and
  repository state; unassessed current-scope lens impact blocks approval.
- Ask what was deleted, collapsed, reused, avoided, or added and why.
- Check stale code, duplicate owners, stale tests/docs, fake proof paths,
  runtime proof scope, and remaining work disposition.
- Cite exact `file/path:line` findings.

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
