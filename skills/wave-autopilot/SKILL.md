---
name: wave-autopilot
description: "WHEN user asks to execute a full wave, execute wave tasks end-to-end from one wave packet and proactively backlog deferred debt."
---

# Wave Autopilot

Execute one `execution-ready` wave from:
- `docs-ai/current-work/delivery-map.md`
- `docs-ai/docs/initiatives/waves/<wave-id>.md`
- `docs-ai/current-work/<wave-id>/wave-execution.md`

Workflow policy stays in `skills/initiatives-workflow/references/initiatives-workflow.md`.

## Inputs

- required: `<wave-id>`
- optional: constrained task subset

## Preflight

Before edits:
1. read map, wave brief, packet
2. confirm wave is `execution-ready`
3. confirm the durable brief's `planning_gate.planning_critic` already
   carries critic provenance
4. confirm packet is implementation-only and not a memory-only substitute for
   planning
5. resolve ordered task list
6. if resuming, reuse existing packet and queue state

If execution still needs discovery or material design choice, stop and send back to `planning-intake`.

## Task Loop

For each task:
1. execute from packet; no per-task artifacts
2. if the packet is `implementer-eligible`, delegate that task card to
   `implementer` by default; keeping code edits in the parent requires an
   explicit reason such as packet-declared `parent-only`, implementer handback,
   or tool/runtime limits
3. broader generic anti-spawn defaults do not apply here; execute-wave is
   explicit repo authorization for the required worker loop
4. if delegating to `implementer`, pass exact packet path, exact task card,
   owned files/surfaces, locked invariants, allowed local implementer
   decisions, proof rows, task-local verification commands, and explicit
   handback triggers
5. if `implementer` reports ambiguity, discovery leakage, boundary flaw, or
   proof drift, stop and return to planning or parent-thread resolution instead
   of letting the worker decide locally
6. require `implementer` to leave assigned task-local verification green before
   handback unless it returns an explicit blocker
7. keep task row current with commands, outcomes, evidence
8. use `verification-before-completion`
9. delegate substantial targeted tests and quality gates to `check_runner` by
   default when they are not part of the implementer's task-local handback
10. run in-thread `quality_guard` before marking task done
11. record real deferrals as backlog/mobile-parity state in same run
12. keep packet contradiction sweep aligned

Stop if task uncovers material gap outside the task card's declared autonomy
envelope.

## Closeout

When targeted tasks are implemented:
1. confirm touched task rows are done with fresh evidence
2. confirm required review loops are complete
3. run wave-level quality gate
4. run or confirm final reviewer closeout for the whole changed slice
5. reconcile durable brief or closed-brief removal, packet proof map, and
   backlog disposition
6. remove wave from map, delete packet, and then delete or slim the closed
   brief per the workflow owner doc only when the wave is truly ready for
   `done`

If final review is still pending, stop short of closeout and keep packet in place.

## Reporting

Per task, report:
- task slug
- verification commands and outcomes
- evidence pointers
- in-thread review status
- isolated/final review status
- backlog entries created or updated
