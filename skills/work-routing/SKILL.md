---
name: work-routing
description: "Use when choosing whether work should be direct, planning-intake, or wave execution."
---

# Work Routing

Owns route selection and the workflow gate matrix. Technical contracts stay
with their owner skills.

## Full Work Rule

Route to the lightest shape that can complete the binding objective and fix the
touched owner surface required to make it true. Do not route a broad objective
into a smaller invented task.

If full correction is blocked, stop and name the blocker instead of patching
around it.

If the objective is too broad to complete to normal depth now, stop before
implementation. Name the broadness, recommend the first coherent owner/problem
to tackle, and wait unless the user already selected that owner/problem or
explicitly asked for an audit/map.

Do not perform shallow breadth work across many requested areas to create
apparent coverage.

## Objective Continuity

After interruption, resume, or a new user message, re-check the binding
objective before continuing.

The newest user instruction can update the objective. Before execution,
handoff, review, or closeout, check prior plan, delegation, review, and proof
scope against the updated objective.

## Routes

- `direct`: tiny/local work, or parent-local continuation after required gates
  already approved. It must complete the full objective in-thread and cannot
  bypass non-trivial planning, review, proof, runtime, compatibility,
  migration, or public-behavior gates.
- `planning-intake`: non-trivial work without execution-ready durable wave
  state, or any open scope, decision, proof, owner boundary, runtime,
  migration, compatibility, public-behavior, or wave-shape decision.
- `wave execution`: execute one `execution-ready` wave from durable wave state.
  A wave may be one task; it is the only durable path for non-trivial work.

Use the heavier route when two competent implementers could choose materially
different owners, proof paths, runtime behavior, state authority, migration,
compatibility, or public behavior.

## Gate Matrix

| Need | Owner |
| --- | --- |
| reusable harness/project overlay posture | `../harness-governance/SKILL.md` |
| simplicity or touched-owner integrity | `../code-simplicity/SKILL.md` |
| vague or non-trivial planning | `../planning-intake/SKILL.md` |
| wave lifecycle or packet state | `../initiatives-workflow/SKILL.md` |
| full wave execution | `../initiatives-workflow/SKILL.md` |
| subagent routing | `../subagent-orchestration/SKILL.md` |
| feedback-caused edits | `../feedback-address/SKILL.md` |
| workflow friction not fixed immediately | `../feedback-address/SKILL.md` |
| end-user or mobile UI design | `../user-apps-design/SKILL.md` |
| completion proof | `../verification-before-completion/SKILL.md` |
| runtime proof policy and verdicts | `../runtime-proof/SKILL.md` |
| browser runtime mechanics | `../webapp-testing/SKILL.md` |
| mobile runtime mechanics | `../mobileapp-testing/SKILL.md` |
| review/approval semantics | `../code-review/SKILL.md` |
| mobile backend/offline/API contracts | `../system-boundary-architecture/SKILL.md` |
