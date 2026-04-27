---
name: subagent-orchestration
description: Use for Codex/Copilot subagent delegation decisions, handoff inputs, active-worker handling, and the narrow implementer routes for one closed wave task card or approved standalone plan.
---

# Subagent Orchestration

Use for delegation policy. Parent owns integration, shared runtime, and final
synthesis. Structured execution still defaults to `implementer` when one wave
task card or approved standalone-plan slice is closed tightly enough.

Durable worker role vocabulary and role boundaries are owned by:
- `references/coding-agent-topology.md`

## Default

- Delegate bounded non-implementation work by default.
- Prefer one bounded substantial delegation over several micro-delegations on
  the same unchanged slice.
- For repo discovery beyond a tiny immediate probe, delegate to `explorer`
  first.
- Stay local for tiny immediate probes, shared-file churn, or tight edit loops.
- Non-trivial planning uses `planning_critic` before planning-gate
  `quality_guard`.
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
- A completed response, rejection, approval, or timeout is not by itself a
  reason to spawn fresh.
- Spawn fresh only when role, domain, slice, task card, write scope, or verdict
  target materially changes; the old context is no longer useful; the worker is
  unavailable; or unrelated context would distort the result.
- For iterative planning, review, or implementation-fix loops, return to the
  same worker when available and still relevant. Ask for a fresh pass over the
  updated artifact or diff.
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
