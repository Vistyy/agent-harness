# Overlay Contracts

Owns reusable workflow-overlay/project-overlay boundaries and the governance
check.

## Overlay Boundary

Projects own product facts, architecture maps, roadmap and queue state, runtime
topology, local command bodies, project-local skills, active execution state,
and project-only exceptions.

Project overlays point to global overlay owners instead of copying reusable
doctrine. Temporary duplication needs a named retirement or pointerization path.

## AGENTS.md

`AGENTS.md` is a first-hop map: precedence, compact repo map,
project-specific invariants, and pointers to global skills or project owners.

It must not copy reusable overlay doctrine. Skill routing is owned by
frontmatter `description`; read skill bodies only after selection.

## Documentation Layout

- `docs-ai/docs/**`: durable project truth.
- `docs-ai/current-work/**`: queue state, active execution state, evidence,
  blockers, and resume notes.

Code, tests, services, packages, runtime topology, and command bodies remain
project-owned unless a global overlay owner explicitly owns a reusable
convention.

## Governance Check

`agent-harness governance check --repo-root .` validates local markdown links in
`AGENTS.md`, `docs-ai/docs/**`, and `docs-ai/current-work/**`. It ignores
external URLs, anchors, and template-like paths.

`docs.work-note-location` rejects work notes under durable docs.
`docs.work-note-memory-reference` rejects durable docs that link to work-note or
current-work memory. It scans markdown links and backticked local paths in
`AGENTS.md` and `docs-ai/docs/**`; project `AGENTS.md` may point to
`docs-ai/current-work/delivery-map.md`.

Reusable checks must stay narrow, high-signal, and tied to owned policy
surfaces.

## Blocking Gates

Reusable overlay gates are blocking contracts, not advisory guidance.

- `pass`: required evidence supports the binding claim.
- `reject`: evidence contradicts the binding claim.
- `blocked`: required evidence, context, environment, or scope is missing.
- `not-applicable`: the gate is outside the claim and the reason is named.

Do not classify required rule, proof, review, runtime, architecture,
solution-shaping, or validation failures as advisory. Non-blocking observations
are not code-review verdicts and are valid only outside the binding objective or
as accepted temporary debt with owner, risk, and removal condition.
