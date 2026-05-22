# Skill Architecture

Reusable skills are small post-selection contracts.

## Shape

- `description` = trigger and routing contract.
- `SKILL.md` body = post-selection contract.
- references = mandatory purpose gates.
- scripts/assets = owned supporting artifacts.

## Body

Include only content needed for correct use after selection:

- owner and outcome
- inputs, outputs, and handback shape
- boundaries and exclusions
- stop conditions
- proof or review requirements
- correctness gotchas

Delete rationale, examples, and process prose unless needed to prevent misuse.
Do not restate ordinary trigger text.

## References

Use references only for conditional contracts. A matched reference gate must be
read before acting on that purpose. Always-needed invariants stay in `SKILL.md`.

Write gates with required language: `Read <reference> before ...` or
`Read <reference> when ...`. Do not load unmatched references speculatively.

## Split

Split a skill, add a router, or extract a reference only for a distinct
trigger, load gate, input/output, proof/review owner, or independent consumer.
Never split for length alone.

Correction order: delete stale material, link owner, tighten wording, add a
heading map, then split only with separability proof.

## Supporting Artifacts

Project-facing helpers should be installed `agent-harness` commands.

Scripts need one purpose, deterministic output, clear failure, documented
inputs/outputs, and known artifact paths when writing files.

Assets own templates copied or consumed by the skill. Delete stale examples.

## Skill Evals

Start with static validation and deterministic fixtures. Keep model-running
skill evals report-only until stable, cheap, and useful.
