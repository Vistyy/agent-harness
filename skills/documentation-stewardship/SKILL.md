---
name: documentation-stewardship
description: Use when editing durable docs, assigning one source of truth, or deciding whether reusable policy belongs in the global harness or a project overlay.
---

# Documentation Stewardship

Owns durable rule placement, one source of truth, terminology ownership, and
doc density.

## Source Of Truth

Every durable rule has one owner.
Every durable concept has one owner.

- reusable agent workflow policy: global harness
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

- global reusable policy: harness skill references
- project durable truth: project `docs-ai/docs/**`
- project active state: project `docs-ai/current-work/**`
- cleanup, migration, evidence, queue, resume state: current-work
- durable owner docs may link durable owners or exact validation surfaces
- current-work may link the durable owner being changed
- completed-wave context is retained only by extraction to the durable owner or
  valid backlog; do not preserve it through closed audit archives, ADR defaults,
  or closed-wave indexes.

## Successor Review

Before deleting or merging durable docs, prove every retained invariant exists
in the successor owner.

Stale-reference scans and line-count reduction are insufficient. If an
invariant has no successor owner, stop or get explicit accepted deletion.

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

## Owner-Only Checks

Validate duplicate doctrine only for exact high-risk phrases with a known owner.
Do not add subjective semantic lint.

Each check names:
- owner file
- owner-only phrase
- allowed test/validator exemptions
- counterexample that would create a second owner
