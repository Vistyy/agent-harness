---
name: subagent-orchestration
description: "Use when subagents should be invoked or routed: delegation decisions, handoff inputs, active-worker handling, and implementer routes."
---

# Subagent Orchestration

Use for delegation policy. Parent keeps integration, shared runtime, and final
synthesis. Structured execution still defaults to `implementer` when one wave
task card or approved standalone-plan slice is closed tightly enough.

Durable worker role vocabulary and role boundaries live in:
- `references/coding-agent-topology.md`

## Default

- No user authorization is required to invoke these harness-defined subagents:
  `explorer`, `check_runner`, `planning_critic`, `implementer`,
  `quality_guard`, `final_reviewer`, and `runtime_evidence`.
- This preauthorization applies only to those named roles. Invoke them when the
  workflow calls for them. Skipping a required named role is a workflow defect.
  Only adapter/runtime hard limits may prevent invocation.
- Delegate bounded non-implementation work by default.
- Prefer one bounded substantial delegation over several micro-delegations on
  the same unchanged slice.
- For repo discovery beyond a tiny immediate probe, delegate to `explorer`
  first.
- Stay local for tiny immediate probes, shared-file churn, or tight edit loops.
- Non-trivial work uses `planning_critic` before implementation or scope
  expansion and `quality_guard` after implementation. Tiny local fixes are
  exempt only when no material owner, proof, runtime, compatibility, migration,
  or public-behavior decision is open.
- If the user changes design direction during non-trivial work, rerun
  `planning_critic` before continuing edits unless the change is wording-only
  or clearly within the already-approved shape.
- For structured wave task cards and approved standalone-plan slices, delegate
  implementation to `implementer` by default once the governing artifact closes
  the slice tightly enough.
- Keep implementation local only with a concrete reason such as packet-declared
  `parent-only` posture, repeated implementer handback, tool/runtime limits, or
  genuinely tiny follow-up churn.
- Use `implementer` only when the governing artifact closes strategic
  decisions and the task card declares a bounded autonomy envelope.
- For implementer-eligible task cards, that envelope requires owned
  files/surfaces, locked invariants, allowed local decisions,
  stop-and-handback triggers, and proof rows. Starting files/symbols, existing
  patterns, and implementation notes are optional handoff hints.
- Do not delegate to `implementer` when two competent implementers could still
  pick materially different owner, proof, state-authority, runtime,
  compatibility, migration, or public-behavior paths.
- Delegate isolated runtime proof only when startup/teardown is deterministic
  and ownership is unambiguous.

## Shared Handoff Baseline

- Pass the narrowed question, exact scope, changed surface or bounded-impact
  rationale, proof obligations or verdict shape, relevant paths/artifacts, and
  frozen decisions when they matter.
- Use `references/coding-agent-topology.md` for role outputs, active-worker
  preservation, and role-specific handoff fields.
- Omit leading assurances, hidden expected answers, and unnecessary repo-wide
  context.
- Ask reviewer/validator workers for one coherent slice and one full-scope
  pass. Do not micro-prompt the same unchanged slice twice unless the evidence
  materially changed.

## Reuse Vs Fresh Spawn

- Reuse or resume an existing worker by default for the same role on the same
  domain, topic, slice, task card, review loop, or verdict sequence.
- Do not reuse a worker across roles. If the next step needs a different role,
  spawn or resume a worker with that role instead of asking an existing worker
  to switch hats.
- A completed response, rejection, approval, or timeout is not by itself a
  reason to spawn fresh.
- Spawn fresh only when role, domain, slice, task card, write scope, or verdict
  target materially changes; the old context is no longer useful; the worker is
  unavailable; or unrelated context would distort the result.
- For iterative planning, review, or implementation-fix loops, return to the
  same worker when available and still relevant. Ask for a fresh pass over the
  updated artifact or diff.
- For iterative review of the same change set, reuse the same reviewer role
  thread by default, even when the diff expands or a blocker is fixed. Treat
  "updated diff after addressing findings" as the same domain/slice unless the
  work moved to an unrelated owner or product area.
- Role-owner fresh-context requirements override this reuse default. This
  section decides worker reuse vs fresh spawn only where the role owner leaves
  that choice open.

## Anti-Patterns

- worker code edits
- parent broad-scanning files while `explorer` is idle
- `implementer` used without one explicit wave task card or one approved
  standalone plan
- `implementer` deciding material owner, proof, state-authority, runtime,
  compatibility, migration, public-behavior, or boundary shape outside its
  declared autonomy envelope
- parent redoing delegated task after quiet/timed-out wait
- parent closing, interrupting, or reclaiming an active worker because it is
  slow, silent, timed out, or blocking local edits
- reusing a worker for a materially different task, role, or write scope
- spawning a replacement for the same role and same slice only because the
  existing worker is quiet, timed out, or inconvenient to wait for
- spawning a fresh `planning_critic` or `quality_guard` for the same diff after
  findings are addressed, instead of returning to the existing reviewer
- `explorer` as reviewer
- `planning_critic` used as implementation reviewer, final approver, or a
  generic sanity-check rubber stamp without exact legacy-path and proof-pressure asks
- `check_runner` as final approver or interactive runtime validator
- `runtime_evidence` used for routine bulk log or trace archaeology that
  `check_runner` could summarize
- `quality_guard` as final approval
- `final_reviewer` used for planning-gate or in-thread chunk review
- screenshot dump without runtime verdict
- generic delegation prose copied into unrelated skills
