---
name: documentation-stewardship
description: "Preserve durable documentation truth by assigning one source of truth, validating claims against repo reality, and safely moving, merging, deleting, or reorganizing docs. Use when creating, editing, auditing, or restructuring durable docs; designing doc IA or agent-readable entrypoints; or deciding whether guidance belongs in AGENTS.md, skills, project docs, current-work, or backlog. Use this skill for durable documentation ownership and lifecycle only; it does not own active execution planning, code behavior, product decisions, or backlog prioritization."
---

# Documentation Stewardship

Owns durable rule placement, one source of truth, terminology ownership, and
doc density.

## Rule

Durable docs are authority, not notes. Before preserving, moving, or deleting a
claim, identify its owner and verify whether it is current, obsolete, future
work, or accepted deletion.

Optimize durable docs for humans and agents: short entrypoints, clear owner
boundaries, grep-friendly terms, and on-demand detail instead of bloated
always-loaded instructions.

## Source Of Truth

Every durable rule has one owner.
Every durable concept has one owner.

- reusable agent workflow policy: workflow overlay
- project product, architecture, runtime, roadmap, queue truth: project overlay
- active execution detail: current-work
- exact behavior: code and tests
- secondary docs point to owners instead of copying full policy
- consumers may name another owner for routing/handoff only
- consumers may state local input, output, stop condition, or consequence
- consumers must not redefine another owner's criteria, procedure, verdict,
  approval semantics, exception policy, or canonical term
- rules name required outcome and forbidden workaround

## Placement

- global reusable policy: overlay skill docs
- project durable truth: project `docs-ai/docs/**`
- project active state: project `docs-ai/current-work/**`
- cleanup, migration, evidence, queue, resume state: current-work
- durable owner docs may link durable owners or exact validation surfaces
- current-work may link the durable owner being changed
- closed work-note context is retained only by extraction to the durable owner
  or valid backlog; do not preserve it through closed audit archives, ADR
  defaults, or closed-note indexes.

## Successor Review

Before deleting or merging durable docs, prove every retained invariant exists
in the successor owner.

Inventory the durable outcomes, rules, terms, exceptions, proof obligations,
and links that future work would rely on. For each one, choose exactly one
disposition:

- `moved`: copied or rewritten into the successor owner and linked or named
- `obsolete`: no longer true because code, tests, runtime, or project facts
  changed
- `accepted deletion`: the user explicitly accepts losing the invariant

Stale-reference scans, line-count reduction, and "the old doc looks unused" are
insufficient. If a retained invariant has no successor owner, stop or get
explicit accepted deletion.

After deleting or merging a durable doc, remove or retarget direct consumers in
the same change. Do not leave durable docs pointing at current-work memory,
closed notes, deleted paths, or superseded owner names.

## Writing Contract

Use the fewest words that preserve outcome, forbidden workaround, owner,
exception boundary, and proof obligation. Leave one reasonable classification.

## Density Rule

Each sentence should carry at least one durable function: owner, outcome,
input, output, stop condition, proof obligation, exception boundary, or routing
consequence.

If a sentence only explains, reassures, narrates history, or repeats an owner
rule without local consequence, delete it or replace it with the owner pointer.

## Terminology

One concept has one canonical term. The doc that owns the concept owns the
term.

- secondary docs reuse the owner term or record an explicit alias
- term changes update direct consumers in the same change or create backlog
- moving or splitting docs keeps the canonical term with the moved rule
- repo-wide wording churn requires a term owner and alias list

## Ownership Review

Review duplicate doctrine as a documentation-ownership issue, not as exact
phrase lint. A second durable owner exists when another file claims authority
for the same rule, decision, or concept in a way that can guide future work
independently of the owner.

Fix by deleting the duplicate, linking to the owner, or explicitly moving
ownership in the same change.

## Agent Readability

Agent-readable docs are a retrieval surface, not a substitute for loaded
instructions.

- Keep `AGENTS.md` short; point to durable entrypoints instead of loading
  domain truth.
- Prefer a durable docs `README.md` for human/agent navigation.
- Prefer an agent index for task-to-owner routing in repos with broad docs.
- Owner docs should state owner, non-owner, read-when, source-of-truth, and
  proof/check pointers when those are not obvious from the title.
- Use stable terms, aliases, concrete paths, and short headings.
- Repeated agent workflows belong in skills, not durable domain docs.
