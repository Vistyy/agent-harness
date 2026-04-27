---
name: subagent-orchestration
description: Delegation policy for Codex/Copilot subagents. Use when deciding whether to stay local or delegate bounded non-implementation work, or the narrow `implementer` exceptions for one wave task card or one approved standalone plan, preparing handoff inputs, or updating docs/skills that describe subagent routing or verification delegation.
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
- Omit leading assurances, hidden expected answers, and unnecessary repo-wide
  context.
- Ask reviewer/validator workers for one coherent slice and one full-scope
  pass. Do not micro-prompt the same unchanged slice twice unless the evidence
  materially changed.

## Reuse Vs Fresh Spawn

- Reuse or resume an existing worker when the next ask is the same role on the
  same topic, slice, task card, review, or verdict, and the worker remains
  available, relevant, and uncontaminated by unrelated write scope. A completed
  response or verdict is not by itself a reason to spawn a fresh worker.
- Spawn a fresh worker only when the role changes, the topic, slice, task card,
  review, verdict, or write scope materially changes, the previous worker is
  unavailable or no longer relevant, or the reusable thread has unrelated
  context pollution that could distort the next verdict or edits.
- Role-specific fresh-context rules override the reuse default. `final_reviewer`
  closeout review requires fresh isolated context by default, including after a
  blocked final review and changed diff. Reuse a prior final reviewer only when
  the review owner explicitly permits reuse for the same unchanged final-review
  context.
- Same `quality_guard` revised review on the same unchanged slice should return
  to the same reviewer thread when available.
- Same `implementer` fixes for `quality_guard` findings on the assigned slice
  should return to the original implementer when available and still relevant.
- Different task card, different standalone-plan slice, or different write
  surface gets a fresh worker.

## Active Worker Preservation

- Never close, interrupt, replace, supersede, or reclaim the write scope of an
  active subagent because it is slow, silent, timed out, or blocking local
  work.
- Active or timed-out subagents stay alive by default.
- Only exceptions: explicit user instruction, plainly mistaken dispatch, or
  the subagent itself reporting done, blocked, or irrelevant.
- A timed-out `wait_agent` or quiet worker is not evidence of stall,
  cancellation, or safe-to-close state.
- Parent-local edits in an active worker's write scope are forbidden unless
  the user explicitly approves taking the packet back.
- After timeout, keep the worker alive, continue non-overlapping local work,
  and wait again only when the result is on the critical path.

## Worker Deltas

- `explorer`: files, symbols, relationships, open questions, next probes.
- `check_runner`: commands, pass/fail, top failures, failure-class summary,
  artifact paths, focused next checks.
- `planning_critic`: `APPROVE` or `REJECT`, planning gaps, ambiguous owner or
  proof paths, surviving legacy paths, and exact decision/proof fields that
  must be added before implementer handoff.
- `implementer`: changed files, verification run, green-or-blocked handback
  against assigned proof rows, explicit blocker when packet/task detail is
  underfed, and no self-approval.
- `quality_guard`: `APPROVE` or `REJECT`, findings, reviewed scope, proof used.
- `final_reviewer`: final closeout `APPROVE`, `BLOCK`, or `NON-BLOCKING`
  verdict for the whole changed slice; not for chunk review.
- `runtime_evidence`: recipe, flow, artifacts, behavioral verdict,
  blocking defects, advisory notes, and trace/correlation identifiers or
  explicit `none observed` when observability mattered.

## Worker-Specific Addenda

- `planning_critic`:
  - pass the exact governing brief/packet or plan path and the claimed owner
    boundary or contract-tightening outcome
  - require the critic to enumerate the materially equivalent legacy paths
    named in the governing artifact and say whether any still survive
  - ask whether the packet still leaves two competent implementers free to pick
    materially different owner, proof, state-authority, runtime,
    compatibility, migration, or public-behavior paths
  - ask whether the change removes complexity or only moves it to a deeper
    owner or adjacent wrapper
  - require explicit `APPROVE` or `REJECT`; no soft endorsement counts as
    planning closure
- `implementer`:
  - pass the exact governing artifact path and exact proof rows
  - state that the governing artifact closes material owner, proof,
    state-authority, runtime, compatibility, migration, and public-behavior
    decisions
  - require task-card owned files/surfaces, locked invariants, allowed local
    decisions, stop-and-handback triggers, and proof rows; do not require
    starting files/symbols, existing patterns, or implementation notes unless
    they are needed to remove ambiguity
  - keep local helper names, decomposition, exact idiom, and framework
    mechanics implementer-local when owner skills/docs already close them
  - include stop-and-handback triggers for ambiguity, discovery leakage,
    boundary flaws, or proof drift
  - if the task changes persistent tests, hand back one testing-strategy row
    per changed persistent test file; if any row is missing or any row keeps an
    invalid reason code, stop and hand back blocked
- `runtime_evidence`:
  - pass the exact runtime recipe or active runtime target, material branches or
    states to exercise, required must-check constraints, and a surface brief
    when UI quality is in scope
  - do not pre-identify design defects for the worker to echo back

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
