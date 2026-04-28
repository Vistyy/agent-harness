# Delegation Policy

Use before delegating, reusing workers, or deciding whether to keep
implementation local.

## Defaults

- Delegate bounded non-implementation work by default.
- Prefer one bounded substantial delegation over several micro-delegations on
  the same unchanged slice.
- For repo discovery beyond a tiny immediate probe, delegate to `explorer`.
- Stay local for tiny immediate probes, shared-file churn, or tight edit loops.
- Non-trivial work uses `planning_critic` before implementation or scope
  expansion and `quality_guard` after implementation.
- If the user changes design direction during non-trivial work, rerun
  `planning_critic` unless the change is wording-only or clearly inside the
  approved shape.
- Delegate implementation to `implementer` by default when one wave task card
  or approved standalone-plan slice is closed tightly enough.
- Keep implementation local only for a concrete reason: packet-declared
  `parent-only`, repeated implementer handback, tool/runtime limits, or tiny
  follow-up churn.
- Delegate isolated runtime proof only when startup/teardown is deterministic
  and ownership is unambiguous.

## Implementer Eligibility

Use `implementer` only when the governing artifact closes strategic decisions
and declares a bounded autonomy envelope.

That envelope requires:
- owned files/surfaces
- locked invariants
- allowed local decisions
- stop-and-handback triggers
- proof rows

Starting files/symbols, existing patterns, and implementation notes are hints,
not binding ceremony.

Do not delegate to `implementer` when two competent implementers could choose
different owner, proof, state-authority, runtime, compatibility, migration, or
public-behavior paths.

## Handoff Baseline

Pass:
- narrowed question
- exact scope
- changed surface or bounded-impact rationale
- proof obligations or verdict shape
- relevant paths/artifacts
- frozen decisions when material

Omit leading assurances, hidden expected answers, and unnecessary repo-wide
context.

Ask reviewer/validator workers for one coherent slice and one full-scope pass.
Do not micro-prompt the same unchanged slice twice unless evidence materially
changed.

## Reuse Vs Fresh Spawn

Reuse or resume an existing worker by default for the same role on the same
domain, topic, slice, task card, review loop, or verdict sequence.

Do not reuse across roles. If the next step needs a different role, spawn or
resume that role.

A completed response, rejection, approval, or timeout is not by itself a reason
to spawn fresh.

Spawn fresh only when role, domain, slice, task card, write scope, or verdict
target changes materially; old context is no longer useful; the worker is
unavailable; or unrelated context would distort the result.

For iterative planning, review, or implementation-fix loops, return to the same
worker when available and relevant. Ask for a fresh pass over the updated
artifact or diff.

Role-owner fresh-context requirements override this reuse default.

## Anti-Patterns

- worker code edits outside assigned implementation role
- parent broad-scanning files while `explorer` is idle
- `implementer` used without one explicit task card or approved standalone plan
- `implementer` deciding material owner/proof/runtime/boundary shape
- parent redoing delegated task after quiet or timed-out wait
- parent closing or replacing an active worker because it is slow or blocking
- reusing a worker for a materially different task, role, or write scope
- fresh `planning_critic` or `quality_guard` for the same diff after findings
  are addressed instead of returning to the existing reviewer
- `explorer` as reviewer
- `planning_critic` as implementation reviewer or final approver
- `check_runner` as final approver or interactive runtime validator
- `runtime_evidence` for routine bulk log/trace archaeology
- `quality_guard` as final approval
- `final_reviewer` as planning-gate or in-thread chunk review
- screenshot dump without runtime verdict
- generic delegation prose copied into unrelated skills
