# Durable Context Contract

Owns durable context notes for wave execution.

## Purpose

A durable context note exists only when context would otherwise be lost or
twisted across queueing, handoff, interruption, resume, review, or multiple
slices. It is memory, not authority.

## Sufficiency

The note is sufficient only when a future agent can recover:

- original objective, accepted reductions, residual gaps, and current checkpoint
- simplest correct end state and rejected alternatives
- selected owner/interface, key decisions, design-integrity verdict, and
  blocker status
- current slice, owned surfaces, dependency order, blockers, decisions,
  evidence, and follow-up
- exact readiness claim, claimed interface, evidence status, unproved
  boundaries, and residual risks
- context closeout state: removed, superseded, extracted, or intentionally
  active with reason

Use headings or prose that make those facts hard to lose. Do not add fields to
satisfy a template.

## Authority

The binding user objective, repo reality, `../../design-integrity/SKILL.md`,
`../../readiness-claim/SKILL.md`, and reviewer judgments outrank durable
context. Stop when context is stale, narrows the objective, omits a material
dependency, or points at a route that is no longer the simplest correct end
state.
