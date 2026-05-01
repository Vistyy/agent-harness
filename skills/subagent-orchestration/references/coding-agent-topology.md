# Coding Agent Topology

Own durable cross-tool role vocabulary for coding agents.

## Goal

Keep role names, boundaries, and trust posture aligned across adapters without
embedding adapter-specific instruction files in this reference.

In scope:
- durable roles: `explorer`, `check_runner`, `planning_critic`,
  `implementer`, `quality_guard`, `final_reviewer`, `runtime_evidence`
- role boundaries and trust posture
- cross-tool naming compatibility
- enforcement destinations

Out of scope:
- product/runtime behavior changes
- freeform writable implementation workers
- compatibility aliases for legacy worker names
- adapter role TOML or provider-specific role files
- new in-house agent framework

## Roles

| Role | Mission | Must not do | Surface |
| --- | --- | --- | --- |
| `explorer` | default read-only repo discovery and code-path mapping; compress files, symbols, paths, open questions, next probes | propose fixes by default; edit code | adapter role plus wrapper where available |
| `check_runner` | narrowed non-runtime verification and diagnostics triage: targeted tests, quality gates, log/trace sweeps, bulky artifact summaries | act as final diagnosis, final review, implementation owner, or live runtime validator | adapter role plus wrapper where available |
| `planning_critic` | negative-bias plan critic for non-trivial planning | act as final approver, implementation reviewer, implementation owner | adapter role plus wrapper where available |
| `implementer` | plan-gated execution worker for one tightly scoped wave task card or one approved standalone-plan slice, with bounded local autonomy inside the declared slice | decide strategic design/proof/runtime/boundary shape outside its declared autonomy envelope; widen scope; own shared runtime; self-approve | adapter role plus wrapper where available |
| `quality_guard` | iterative in-thread correctness, simplicity, architecture-fit, and spec-alignment scrutiny after each meaningful chunk/task, not only at closeout | own final approval; edit code | adapter role plus wrapper where available |
| `final_reviewer` | final isolated breadth-first closeout review after implementation and local verification | perform planning-gate review, in-thread chunk review, implementation, diagnostics triage, or runtime validation | adapter role plus wrapper where available |
| `runtime_evidence` | live validation guard for a handed-off runtime-visible UI/API/service claim | become general debugger, planner, reviewer, implementation agent, code-quality approver, or routine bulk log archaeologist | adapter role plus wrapper where available |

## Review Topology

Review governance stays owned by `../../code-review/references/review-governance.md`.
Delegation mechanics stay owned by `../SKILL.md`.
Standalone-plan policy stays owned by
`../../writing-plans/references/standalone-plans.md`.

This reference keeps only role boundaries:
- parent thread is not a worker role
- parent owns orchestration, shared runtime lifecycle, integration, review
  routing, packet/queue state, and final synthesis
- `implementer` executes one bounded task card or approved standalone-plan
  slice only when the governing artifact closes the autonomy envelope
- `quality_guard` reviews in-thread and does not implement or final-approve
- `final_reviewer` performs isolated closeout review and does not implement
- `check_runner` handles targeted commands, gates, diagnostics, logs, and
  large-output summaries, but does not approve
- `runtime_evidence` handles bounded live runtime/UI/API validation only after
  parent gives the claim, target, and expected verdict shape
- generic word `reviewer` is not a worker identity

## Posture

- `explorer`: speed-first, read-only mapping and default discovery owner
- `check_runner`: speed-first, bounded checks and diagnostics triage
- `planning_critic`: negative-bias planning pressure for non-trivial planning
- `implementer`: execution-only coding against a closed task card or approved
  standalone-plan slice, with local discretion bounded by the governing artifact
- `quality_guard`: negative-bias correctness/simplicity scrutiny that pushes
  back early against plan drift, sloppy ownership, and overbuilt code
- `final_reviewer`: high-reasoning isolated closeout review for the whole
  changed slice
- `runtime_evidence`: strict live runtime verdicts under the applicable proof
  contract

Live delegation defaults stay owned by `../SKILL.md`.
This doc owns vocabulary and boundaries only. Exact model names and adapter
instruction details belong in adapter config, not durable role vocabulary.

## Adapter Role Files

Adapter role files are provider-facing runtime instructions. They may repeat
compact role-critical guardrails when the role must stand alone.

Hybrid rule:
- non-trivial governance roles should name the global owner skill or reference
  they consume,
- tiny mechanical roles may stay self-contained when they only state role
  boundary, allowed work, and output shape,
- durable role vocabulary and boundaries stay in this reference,
- provider-specific model, tool, sandbox, and formatting details stay in the
  adapter file.

## Active Worker Preservation

- Never close, interrupt, replace, supersede, or reclaim the write scope of an
  active worker because it is slow, silent, timed out, or blocking local work.
- Active or timed-out workers stay alive by default.
- Only exceptions: explicit user instruction, plainly mistaken dispatch, or
  the worker itself reporting done, blocked, or irrelevant.
- A timed-out wait is not evidence of cancellation or safe-to-close state.
- Parent-local edits in an active worker's write scope require explicit user
  approval to take the packet back.

## Role Outputs

- `explorer`: files, symbols, relationships, open questions, next probes.
- `check_runner`: commands, pass/fail, top failures, failure-class summary,
  artifact paths, focused next checks.
- `planning_critic`: `APPROVE` or `REJECT`, planning gaps, ambiguous owner or
  proof paths, surviving legacy paths, and exact fields needed before handoff.
- `implementer`: changed files, verification run, green-or-blocked handback
  against assigned proof rows, explicit blockers, and no self-approval.
- `quality_guard`: `APPROVE` or `REJECT`, findings, reviewed scope, proof used.
- `final_reviewer`: final closeout `APPROVE`, `BLOCK`, or `NON-BLOCKING`
  verdict for the whole changed slice.
- `runtime_evidence`: claim boundary, recipe, flow, artifacts, verdict,
  block impact, findings, and trace/correlation identifiers or explicit
  `none observed` when relevant.

## Role-Specific Handoffs

`planning_critic` handoff:
- pass the governing brief, packet, or plan path
- name claimed owner boundary or contract-tightening outcome
- ask for materially equivalent legacy paths that still survive
- ask whether two competent implementers could still choose materially
  different owner, proof, state-authority, runtime, compatibility, migration,
  or public-behavior paths
- require explicit `APPROVE` or `REJECT`

`implementer` handoff:
- pass exact governing artifact path and exact proof rows
- state that material owner, proof, state-authority, runtime, compatibility,
  migration, and public-behavior decisions are closed
- include owned files/surfaces, locked invariants, allowed local decisions,
  stop-and-handback triggers, and proof rows
- keep helper names, decomposition, idiom, and framework mechanics local only
  when owner skills/docs already close the approach
- require one testing-strategy row per changed persistent test file

`quality_guard` handoff:
- pass the binding user objective, active plan/packet anchor when any, changed
  slice, touched owner/component, proof claim, and artifacts
- name known risks, suspected weak outcomes, or successor-owner concerns
- ask for `APPROVE` or `REJECT` against the objective, not only packet
  completion, and to reject proxy completion, objective narrowing, or
  unacceptable touched/successor-owner integrity

`final_reviewer` handoff:
- pass the binding user objective, active plan/packet anchor when any, full
  changed slice, touched owner/component, proof claim, and artifacts
- name known risks, prior review dispositions, suspected weak outcomes, and any
  successor-owner concerns
- ask for closeout verdict against the objective and review governance,
  treating planning and `quality_guard` approvals as history, not final
  approval

`runtime_evidence` handoff:
- pass exact runtime recipe or active runtime target
- name the runtime-visible claim and what a failed or blocked verdict affects
- name material branches or states to exercise
- include must-check constraints and surface brief when UI quality is in scope
- do not pre-identify design defects for the worker to echo back

## Enforcement Destinations

- `AGENTS.md` or equivalent project entrypoint for parent-thread policy
- `../SKILL.md` for delegation defaults and handoff policy
- adapter role files for provider-specific role identity and instructions
- wrapper files for tool parity where an adapter supports them
- consuming workflow skills for workflow-specific role references
- harness validation scripts and tests for mechanical enforcement

## Related Contracts

- review topology owner: `../../code-review/references/review-governance.md`
- policy ownership owner: `../../documentation-stewardship/references/policy-single-source-of-truth.md`
- standalone-plan owner: `../../writing-plans/references/standalone-plans.md`
- wave workflow owner: `../../initiatives-workflow/references/initiatives-workflow.md`
