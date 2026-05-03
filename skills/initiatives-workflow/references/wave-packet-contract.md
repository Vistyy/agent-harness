# Wave Packet Contract

Owns packet, task-card, proof-row, and packet-state schema for
`docs-ai/current-work/<wave-id>/wave-execution.md`.

## Required Sections

- `Scope And Execution Posture`
- `Task Plan`
- `Proof Plan`
- `Execution State`
- `System-Boundary Architecture Disposition` when
  `System-boundary trigger: triggered`

## Scope And Execution Posture

Required fields:
- in-scope and out-of-scope work
- non-obvious constraints
- `System-boundary trigger`
- `Implementer delegation posture`
- `Parent-only rationale`
- frozen decisions
- planning exceptions

`implementer-eligible` is the default. `parent-only` needs a concrete reason:
`packet-declared-parent-only`, `repeated-implementer-handback`,
`tool-or-runtime-limit`, `shared-file-churn`, or `tiny-local-followup`.

Planning exceptions need owner, reason, and review/removal condition. Packets
must not substitute for missing planning closure.

## Task Cards

Task states are only `blank`, `done`, or `blocked`.

- `blank`: task is not yet closed
- `done`: scoped implementation, cleanup/removal, review gates, and proof rows
  are satisfied
- `blocked`: next required move depends on an external dependency or explicit
  user action

Do not invent extra task states; nuance belongs in proof rows, blocker entries,
or task evidence. Store state on each task card. Summary tables are optional.

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

Runtime proof rows use existing fields to carry the Runtime Claim Map:
- `exact_proof` names entrypoint, runtime target, action/request/flow,
  observable result, and simulation boundary or `none`
- `expected_evidence` ties to the same or downstream owner/user-visible surface
- simulated boundaries are named, not hidden in command text

## System-Boundary Appendix

When `System-boundary trigger: triggered`, include why triggered, planning
disposition, execution stop rule, changed authorities/contracts, single owner,
public write paths, read-repair paths, forbidden bypass paths, rejected
alternatives, why scope is not artificially narrowed, and stable-to-extend
expectation.

## Execution State

Track decisions, blockers, technical debt, and deferred follow-up.

Accepted touched-component debt must live here and link backlog detail with
owner, affected files/surfaces, accepted must-block signals, risk, removal
condition, and explicit user acceptance.

## Execution Trust

An implementer may trust an `execution-ready` packet for closed decisions and
owned scope. The implementer stops when scope is underfed, discovery leaks into
execution, proof drifts, or a current-objective owner defect appears.
