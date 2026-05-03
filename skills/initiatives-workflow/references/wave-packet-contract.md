# Wave Packet Contract

Owns the durable packet schema for `wave-execution.md`.

## Sections

- `Scope And Execution Posture`
- `Task Plan`
- `Proof Plan`
- `Execution State`
- `System-Boundary Architecture Disposition` when
  `System-boundary trigger: triggered`

## Scope And Posture

Required: in/out scope, non-obvious constraints, system-boundary trigger,
delegation posture, parent-only rationale, frozen decisions, and planning
exceptions.

`implementer-eligible` is the default. `parent-only` needs a concrete reason:
`packet-declared-parent-only`, `repeated-implementer-handback`,
`tool-or-runtime-limit`, `shared-file-churn`, or `tiny-local-followup`.

Planning exceptions need owner, reason, and review/removal condition.

## Task Cards

Task states are only `blank`, `done`, or `blocked`.

- `blank`: task is not yet closed
- `done`: scoped implementation, cleanup/removal, review gates, and proof rows
  are satisfied
- `blocked`: next required move depends on an external dependency or explicit
  user action

Do not invent extra task states. Nuance belongs in proof rows, blocker entries,
or task evidence.

Each `### <task_slug>` card states:
- state
- outcome
- in scope / out of scope
- owned files and surfaces
- `Touched owner/component integrity:`
- locked invariants
- allowed local implementer decisions
- stop-and-handback triggers
- proof rows
- deferred follow-up

Task cards preserve the binding objective. Starting files, symbols, and
implementation notes are hints, not required ceremony.

Material owner, proof, state-authority, runtime, compatibility, migration,
public behavior, and forbidden-legacy-path choices are not implementer-local.

## Proof Rows

The `Proof Plan` JSON contains `proof_plan` rows with:
- `proof_id`
- `task_slug`
- `anchor_ids`
- `claim`
- `material_variants`
- `proof_classification`
- `owner_layer`
- `exact_proof`
- `expected_evidence`
- `counterfactual_regression_probe`
- `status`

Every material claim needs exact proof and a counterfactual probe. No proof row
may prove a smaller invented objective.

Runtime rows carry the Runtime Claim Map in existing fields: `exact_proof`
names entrypoint, target, action/flow, result, and simulation boundary;
`expected_evidence` ties to the same or downstream visible surface.

## System-Boundary Appendix

When triggered, include why, planning disposition, stop rule, changed
contracts, single owner, write/read-repair paths, forbidden bypasses, rejected
alternatives, why scope is not artificially narrowed, and stable-to-extend
expectation.

## Execution State

Track decisions, blockers, technical debt, task evidence, and deferred
follow-up.

Accepted touched-component debt must live here and link backlog detail with
owner, affected files/surfaces, accepted must-block signals, risk, removal
condition, and explicit user acceptance.

## Trust

An implementer may trust an `execution-ready` packet for closed decisions and
owned scope. The implementer stops when scope is underfed, discovery leaks into
execution, proof drifts, or a current-objective owner defect appears.
