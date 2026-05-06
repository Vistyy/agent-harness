# Harness Contracts

Owns reusable harness/project-overlay boundaries and the governance check.

## Overlay Boundary

Projects own product facts, architecture maps, roadmap and queue state, runtime
topology, local command bodies, project-local skills, active execution state,
and project-only exceptions.

Project overlays point to global harness owners instead of copying reusable
doctrine. Temporary duplication needs a named retirement or pointerization path.

## AGENTS.md

`AGENTS.md` is a first-hop map: precedence, compact repo map,
project-specific invariants, and pointers to global skills or project owners.

It must not copy reusable harness doctrine. Skill routing is owned by
frontmatter `description`; read skill bodies only after selection.

## Documentation Layout

- `docs-ai/docs/**`: durable project truth.
- `docs-ai/current-work/**`: queue state, active execution state, evidence,
  blockers, and resume notes.

Code, tests, services, packages, runtime topology, and command bodies remain
project-owned unless a global harness owner explicitly owns a reusable
convention.

## Governance Check

`agent-harness governance check --repo-root .` validates local markdown links in
`AGENTS.md`, `docs-ai/docs/**`, and `docs-ai/current-work/**`. It ignores
external URLs, anchors, and template-like paths.

`docs.completed-wave-doctrine-reference` rejects durable non-wave docs that
link to `done` wave briefs. It scans markdown links and backticked local paths
in `AGENTS.md` and `docs-ai/docs/**`, excluding wave briefs themselves.

Reusable checks must stay narrow, high-signal, and tied to owned policy
surfaces.

## Blocking Gates

Reusable harness gates are blocking contracts, not advisory guidance.

- `pass`: required evidence supports the binding claim.
- `reject`: evidence contradicts the binding claim.
- `blocked`: required evidence, context, environment, or scope is missing.
- `not-applicable`: the gate is outside the claim and the reason is named.

Do not classify required rule, proof, review, runtime, architecture,
owner-integrity, or validation failures as advisory. Non-blocking observations
are valid only outside the binding objective or as accepted debt with owner,
risk, and removal condition.
