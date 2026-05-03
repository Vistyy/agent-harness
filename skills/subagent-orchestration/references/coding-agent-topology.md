# Coding Agent Topology

Owns reusable role boundaries for harness-defined subagents.

## Roles

| Role | Mission |
| --- | --- |
| `explorer` | Read-only repository discovery and context compression. |
| `check_runner` | Targeted checks, quality gates, logs, and diagnostics summary. |
| `planning_critic` | Hostile planning review before execution-ready promotion. |
| `implementer` | One bounded approved wave task card. |
| `quality_guard` | Planning-gate and in-thread implementation gate. |
| `final_reviewer` | Final isolated closeout review after verification. |
| `runtime_evidence` | Live validation guard for runtime-visible claims. |

Adapter configs must preserve these names unless one reviewed migration updates
every consumer together.

## Role Boundaries

- Parent owns orchestration, integration, shared runtime lifecycle, final
  synthesis, and queue/packet state.
- `explorer` and `check_runner` are read-only/support roles.
- `planning_critic` breaks non-trivial plans before execution readiness.
- `implementer` executes only its assigned approved slice.
- `quality_guard` approves or rejects planning gates and implementation chunks.
- `final_reviewer` performs final isolated closeout review.
- `runtime_evidence` proves handed-off live behavior and returns `pass`,
  `reject`, or `blocked`.

## Handoff Baseline

For non-trivial work, handoffs include:
- original objective
- accepted reductions and residual gaps
- exact role question
- artifacts/diff/paths to inspect
- proof claim and proof artifacts
- known risks and stop conditions

Reject or hand back when the prompt asks the role to approve or execute a
smaller invented objective.

## Owners

- wave packets: `../../initiatives-workflow/references/wave-packet-contract.md`
- review semantics: `../../code-review/references/review-governance.md`
- delegation policy: `../SKILL.md`
