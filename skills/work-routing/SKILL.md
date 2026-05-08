---
name: work-routing
description: "Use when choosing whether work should be direct, planning-intake, or wave execution."
---

# Work Routing

Owns route selection. Technical contracts stay with their owner skills.

## Rule

- Route to the lightest shape that can complete the binding objective and fix
  the touched owner surface required to make it true.
- Do not route a broad objective into a smaller invented task.
- If full correction is blocked, stop and name the blocker.
- Review-discovered current-scope blockers are routed to the lightest shape that
  can complete the owner-correct fix; they are not ordinary backlog.
- If the objective is too broad to complete deeply now, pause breadth, not
  responsibility. Select the first coherent owner/problem only from technical
  dependency, ordering, proof, or owner-boundary evidence.
- The selected owner/problem is execution scope, not an accepted reduction.
- The original objective remains binding; final wording may claim only completed
  scope unless durable state covers the rest.
- For non-trivial work, route-selected owner skills, project overlay docs,
  matched reference gates, and `code-simplicity` must be read before
  implementation, handoff, review, proof, or completion; otherwise stop as
  under-routed.
- Ask or stop only at the `User-Owned Decision Boundary`.
- Do not perform shallow breadth work for apparent coverage.

## User-Owned Decision Boundary

Implementation, design, architecture, test, cleanup, and proof choices inside
the routed objective are agent-owned; asking the user to choose them is a
routing failure unless the decision crosses this boundary.

Ask or stop only for:

- Product intent or priority.
- Irreversible, destructive, or high-impact tradeoff.
- Credential, tenant, secret, or external access.
- Accepted scope reduction.
- Accepted temporary debt.
- Dependency, infrastructure, cost, or compatibility posture whose impact
  exceeds the current owner.

## Objective Continuity

- Re-check the binding objective after interruption, resume, or a new user
  message.
- Before execution, handoff, review, or closeout, compare plan, delegation,
  review, and proof scope to the newest objective.

## Routes

- `direct`: tiny/local work, or bounded parent-only continuation from an
  approved wave/packet. It must complete the routed objective without carrying
  non-trivial planning state in thread and cannot bypass review, proof,
  runtime, compatibility, migration, or public-behavior gates.
- `planning-intake`: non-trivial work without execution-ready durable wave
  state, or any work whose planning state must survive compaction, resume, or
  handoff.
- `wave execution`: execute one `execution-ready` wave from durable wave state.
  A wave may be one task; it is the durable path when execution state must
  survive handoff, interruption, queue tracking, or multiple task cards.

Use the heavier route when two competent implementers could choose materially
different owners, proof paths, runtime behavior, state authority, migration,
compatibility, or public behavior.

## State Gate

- Non-trivial planning state must be file-backed.
- Use existing wave state; do not invent another planning document type.
- If a one-task parent-local change needs a plan, make the wave smaller.
- Direct parent-only continuation requires approved wave/packet state and
  bounded remaining work.
- Prior thread discussion alone never authorizes non-trivial resumed direct
  work.
- A narrowed broad-objective slice is execution scope, not replacement
  objective.
- Execution starts only from an `execution-ready` wave brief and canonical
  packet.
- Draft packets preserve candidate slice state during planning; they do not
  authorize execution.
- Durable state preserves objective continuity, route scope, proof/review gates,
  and stop conditions through `initiatives-workflow`.
- Thread discussion is not planning state.
- If the packet feels too heavy, shrink the packet template; do not execute from
  memory or create another artifact.

After route selection, use the owner skill named by `AGENTS.md` or the active
project overlay. This skill does not own downstream proof, review, runtime,
testing, architecture, or design doctrine.
