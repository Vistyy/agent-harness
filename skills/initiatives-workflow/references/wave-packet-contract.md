# Wave Packet Contract

Owns the durable packet schema for `wave-execution.md`.

## Sections

Required sections:

- `Work Context`
- `Task Plan`
- `Proof Plan`
- `Execution State`

Include `System-Boundary Architecture Disposition` when the Work Context names
`System-boundary trigger: triggered`.

## Work Context

The Work Context is the single shared context capsule for parent and subagents.
It replaces duplicated planning/gate prose and must appear before task cards.

Required subsections:

- `Binding Objective`: original objective, accepted reductions, residual gaps,
  and newest-user-message checkpoint.
- `Owner Skill Intake`: route, project overlay/docs read, owner skills read,
  matched reference gates read, skipped references with reason, and open owner
  gaps. For non-trivial work this includes `code-simplicity`.
- `Scope And Owners`: in scope, out of scope, touched owner/component, owned
  files/surfaces, public entrypoints, and owner boundaries.
- `Decisions And Assumptions`: closed decisions, assumptions subagents may rely
  on, and decisions still user-owned or blocked.
- `Adequacy Challenge`: before-implementation verdict, highest inspected scope,
  must-block signals, and reshape/stop/accepted temporary debt disposition.
- `Required Gates`: compact rows with claim, owner, status, blocking condition,
  proof row IDs, and review/runtime/design role when applicable. Do not repeat
  exact proof commands here.
- `Subagent Handoff Payload`: packet path, objective/reductions, task slice,
  owned surfaces, assumptions, artifacts, proof rows, risks, and stop
  conditions for non-trivial handoff.
- `Stop Conditions`: objective mismatch, under-read owner skills, inadequate
  touched owner, proof drift, unaccepted reduction/debt, stale route, or context
  narrower than handoff/final claim.

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
- follow-up

Task cards own execution slices only. They do not restate the objective,
accepted reductions, global gates, or full owner-skill intake. Starting files,
symbols, and implementation notes are hints, not required ceremony.

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
may prove a smaller invented objective. Required Gates point to proof IDs
instead of repeating proof details.

Runtime rows carry the Runtime Claim Map in existing fields: `exact_proof`
names entrypoint, target, action/flow, result, and simulation boundary;
`expected_evidence` ties to the same or downstream visible surface.

## System-Boundary Appendix

When triggered, include why, planning disposition, stop rule, changed contracts,
single owner, write/read-repair paths, forbidden bypasses, rejected
alternatives, why scope is not artificially narrowed, and stable-to-extend
expectation.

## Execution State

Track changes from the Work Context: new decisions, blockers, technical debt,
task evidence, and follow-up. Do not restate static context.

Accepted touched-component debt must live here and link backlog detail with
owner, affected files/surfaces, accepted must-block signals, risk, removal
condition, and explicit user acceptance.

Discovered separate debt must live here or in a backlog item with owner,
location, risk, and recommended fix. It does not approve a current-scope
blocker.

## Trust

An implementer may trust an `execution-ready` packet for closed decisions, Work
Context, and owned scope. The implementer stops when scope is underfed,
discovery leaks into execution, proof drifts, owner-skill intake is missing, or
a current-objective owner defect appears.
