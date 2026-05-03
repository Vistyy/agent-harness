---
name: documentation-stewardship
description: Use when editing durable docs, assigning one source of truth, or deciding whether reusable policy belongs in the global harness or a project overlay.
---

# Documentation Stewardship

Owner for durable rule ownership, documentation placement, and durable-doc
writing posture.

## Source Of Truth

Every durable rule has one owner.

Rules:
- reusable agent workflow policy belongs in the global harness
- project product, architecture, runtime, roadmap, and queue truth belongs in
  the project overlay
- secondary docs point to the owner instead of copying full policy
- consumer skills may name another owner for routing or handoff, but must not
  restate that owner's procedure or approval rule
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

## Writing Contract

Durable docs are terse and contractual.

Write for enforceable clarity: use the fewest words that preserve the full
rule. Do not compress away the required outcome, forbidden workaround, owner,
exception boundary, or proof obligation when they matter. A durable rule should
leave a reviewer with one reasonable classification of the covered case.

Read `references/domain-language.md` when terminology, aliases, or wording
consistency matter. Do not introduce a new synonym for an owned workflow, proof,
review, role, or state concept unless the owner doc records it as an alias.

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
