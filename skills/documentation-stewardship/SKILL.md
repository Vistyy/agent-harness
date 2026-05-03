---
name: documentation-stewardship
description: Use when editing durable docs, assigning one source of truth, or deciding whether reusable policy belongs in the global harness or a project overlay.
---

# Documentation Stewardship

Owner for durable rule ownership, documentation placement, and durable-doc
writing posture.

## Source Of Truth

Every durable rule has one owner.
Every durable concept has one owner.

Rules:
- reusable agent workflow policy belongs in the global harness
- project product, architecture, runtime, roadmap, and queue truth belongs in
  the project overlay
- secondary docs point to the owner instead of copying full policy
- consumer skills may name another owner for routing or handoff, but must not
  restate that owner's procedure or approval rule
- consumers may state only their local input, output, stop condition, or
  consequence for an owned concept
- consumers must not redefine another owner's criteria, procedure, verdict,
  approval semantics, exception policy, or canonical term
- active execution detail belongs in active-work state, not durable docs
- a rule must name the required outcome and forbidden workaround

## Placement

Stable contracts live in durable owner docs. Temporary cleanup, migration,
evidence, queue state, and resume state live in current-work.

Use this split:
- global reusable policy: harness skill references
- project durable truth: project `docs-ai/docs/**`
- project active execution state: project `docs-ai/current-work/**`
- exact behavior: code and tests

Do not store durable truth in active-work state.

Durable owner docs may link durable owner docs or exact validation surfaces.
Current-work items may link the durable owner they are cleaning up.

## Successor Review

Deleting or merging durable docs requires successor readback. Prove every
retained invariant exists in the successor owner before claiming the old doc can
go.

Stale-reference scans and line-count reduction are not enough. If an invariant
has no successor owner, stop or get explicit accepted deletion.

## Writing Contract

Durable docs are terse and contractual.

Write for enforceable clarity: use the fewest words that preserve the full
rule. Do not compress away the required outcome, forbidden workaround, owner,
exception boundary, or proof obligation when they matter. A durable rule should
leave a reviewer with one reasonable classification of the covered case.

## Terminology

One concept has one canonical term. The doc that owns the concept owns the
term.

Rules:
- secondary docs reuse the owner term or record an explicit alias
- do not rename a term casually during compaction
- when moving or splitting docs, keep the canonical term with the moved rule
- term changes update direct consumers in the same change or create backlog
- do not run repo-wide wording churn without a term owner and alias list

Use:
- short sections
- flat bullets
- links to owner docs
- required outcomes and forbidden workarounds
- explicit exception boundaries
- rationale only when it prevents drift

Avoid:
- copied owner policy
- runtime chatter
- stale implementation walkthroughs
- status notes that will expire
