# Wave Packet Contract

Owner for wave execution packet schema, task-card fields, proof-row fields, and
packet state semantics.

Does not own:
- wave/backlog lifecycle or delivery-map placement:
  `initiatives-workflow.md`
- planning readiness and promotion decisions:
  `../../planning-intake/SKILL.md`
- delegation role policy:
  `../../subagent-orchestration/SKILL.md`
- completion and final approval fields:
  `../../code-review/references/review-governance.md`

## Paths

Canonical packet:
- `docs-ai/current-work/<wave-id>/wave-execution.md`

Planning-gate draft:
- `docs-ai/current-work/<wave-id>/wave-execution.draft.md`

Rules:
- one elastic packet layout; vary depth, not shape
- no canonical packet while wave status is `discovery-required`
- promote draft to canonical only with execution-ready promotion
- `done` and `retired` waves have no packet

## Required Sections

1. `Scope And Execution Posture`
2. `Task Plan`
3. `Proof Plan`
4. `Execution State`

Use `System-Boundary Architecture Disposition` only when the packet says
`System-boundary trigger: triggered`.

## Scope And Execution Posture

Required fields:
- in-scope and out-of-scope work
- non-obvious constraints
- `System-boundary trigger`
- `Implementer delegation posture`
- `Parent-only rationale`
- frozen decisions
- planning exceptions

Rules:
- `implementer-eligible` is the preferred default
- `parent-only` requires a concrete reason
- planning exceptions need owner, reason, and review/removal condition
- packets must not substitute for missing planning closure

Parent-only reason codes:
- `packet-declared-parent-only`
- `repeated-implementer-handback`
- `tool-or-runtime-limit`
- `shared-file-churn`
- `tiny-local-followup`

## Task Cards

Task states:
- blank
- `done`
- `blocked`

Meanings:
- blank: task is not yet closed
- `done`: all scoped implementation obligations, cleanup/removal obligations,
  review gates, and proof rows are satisfied
- `blocked`: next required move depends on an external dependency or explicit
  user action

State rules:
- do not invent extra task states to carry nuance that belongs in proof rows,
  blocker entries, or task evidence
- do not mark task `done` while any scoped cleanup/removal/demotion item is
  still intentionally deferred
- do not mark task `done` while any required hosted/runtime proof row remains
  unsatisfied
- use `blocked` only when the next required action is truly external;
  otherwise leave the state blank and keep working
- `Execution outcome` text in task sections must match the task-row state

Task cards must include:
- outcome
- in scope / out of scope
- owned files and surfaces
- touched owner/component integrity for non-trivial work
- locked invariants
- allowed local implementer decisions
- stop-and-handback triggers
- proof rows
- deferred follow-up disposition

Optional hints:
- starting files and symbols
- existing patterns
- implementation notes

Rules:
- task cards are outcome-and-proof shaped, not command lists
- allowed local decisions must stay minor and local
- material owner, proof, state-authority, runtime, compatibility, migration,
  public behavior, or forbidden-legacy-path choices are not implementer-local
- structural, hotspot, or state-authority task plans must migrate every listed
  write/read-repair path to the declared owner before follow-on cleanup

## Proof Plan

`proof_plan` rows include:
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

Proof rows assigned to a task define task-local verification obligations.
Handback should leave those checks green or return an explicit blocker.

## System-Boundary Appendix

When `System-boundary trigger: triggered`, include:
- why triggered
- planning disposition
- execution stop rule
- changed authorities or contracts
- single owner after change
- public write paths
- read-repair paths
- forbidden bypass paths
- rejected alternatives
- why scope is not artificially narrowed
- stable-to-extend expectation

## Execution State

Track only:
- decisions and blockers
- technical debt and deferred follow-up

Do not invent extra task states to carry nuance that belongs in proof rows,
blocker entries, or evidence notes.

Accepted touched-component debt must live under `technical debt and deferred
follow-up` and link a backlog detail file. The entry must include owner,
affected files/surfaces, accepted `code-simplicity` must-block signals, risk,
removal condition, and the explicit user-acceptance note. Approval or closeout
is invalid if accepted debt has no backlog link.
