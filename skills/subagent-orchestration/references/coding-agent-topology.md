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
| `runtime_evidence` | bounded live runtime and screenshot-reviewed verdict collection after target question is known | become general debugger, planner, reviewer, implementation agent, or routine bulk log archaeologist | adapter role plus wrapper where available |

## Review Topology

Review governance stays owned by `skills/code-review/references/review-governance.md`.
Delegation mechanics stay owned by `skills/subagent-orchestration/SKILL.md`.
Standalone-plan execution policy stays owned by
`skills/executing-plans/references/standalone-plans.md`.

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
- `runtime_evidence` handles live runtime/UI/API proof only after parent gives
  a bounded target and expected verdict shape
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
- `runtime_evidence`: bounded live runtime and strict screenshot/runtime
  verdicts under the applicable proof contract

Live delegation defaults stay owned by `skills/subagent-orchestration/SKILL.md`.
This doc owns vocabulary and boundaries only. Exact model names and adapter
instruction details belong in adapter config, not durable role vocabulary.

## Active Worker Preservation

- Never close, interrupt, replace, supersede, or reclaim the write scope of an
  active worker because it is slow, silent, timed out, or blocking local work.
- Active or timed-out workers stay alive by default.
- Only exceptions: explicit user instruction, plainly mistaken dispatch, or
  the worker itself reporting done, blocked, or irrelevant.
- Parent-local edits in an active worker's write scope require explicit user
  approval to take the packet back.

## Enforcement Destinations

- `AGENTS.md` or equivalent project entrypoint for parent-thread policy
- `skills/subagent-orchestration/SKILL.md` for delegation defaults and handoff policy
- adapter role files for provider-specific role identity and instructions
- wrapper files for tool parity where an adapter supports them
- `skills/**` for workflow-specific role references
- harness validation scripts and tests for mechanical enforcement

## Related Contracts

- review topology owner: `skills/code-review/references/review-governance.md`
- policy ownership owner: `skills/documentation-stewardship/references/policy-single-source-of-truth.md`
- standalone-plan owner: `skills/executing-plans/references/standalone-plans.md`
- wave workflow owner: `skills/initiatives-workflow/references/initiatives-workflow.md`
