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

If the objective is too broad to complete to normal depth now, pause breadth,
not responsibility. Use technical dependency, ordering, proof, and owner-boundary
evidence to select the first coherent owner/problem when the choice is
technical and reversible, then route and proceed deeply under the normal
direct/planning/wave gates.

The selected owner/problem is execution scope, not an accepted reduction. The
original objective remains binding for continuity and closeout; final wording
may claim only the completed owner/problem unless durable state covers the
rest.

Ask only when the first-owner choice depends on product priority, irreversible
tradeoff, accepted reduction, credentials/access, or another user-owned
decision, or when the user explicitly asks for an audit/map.

Do not perform shallow breadth work across many requested areas to create
apparent coverage.

## Objective Continuity

After interruption, resume, or a new user message, re-check the binding
objective before continuing.

The newest user instruction can update the objective. Before execution,
handoff, review, or closeout, check prior plan, delegation, review, and proof
scope against the updated objective.

## Routes

- `direct`: tiny/local work, or non-trivial in-thread work with an approved
  direct brief. It must complete the routed objective in-thread and cannot
  bypass planning, review, proof, runtime, compatibility, migration, or
  public-behavior gates.
- `planning-intake`: non-trivial work without execution-ready durable wave
  state when a direct brief cannot close scope, decisions, proof, owner
  boundary, runtime, migration, compatibility, or public behavior.
- `wave execution`: execute one `execution-ready` wave from durable wave state.
  A wave may be one task; it is the durable path when execution state must
  survive handoff, interruption, queue tracking, or multiple task cards.

Use the heavier route when two competent implementers could choose materially
different owners, proof paths, runtime behavior, state authority, migration,
compatibility, or public behavior.

## Direct Brief

Non-trivial direct work needs an in-thread direct brief approved by
`planning_critic` before implementation.

The brief names:
- binding objective and accepted reductions
- routed owner/problem and why durable wave state is unnecessary
- touched owner/component integrity
- closed material decisions
- proof allocation for each material claim: owner layer, exact proof command or
  artifact, expected evidence, and counterfactual regression probe
- stop triggers and handback conditions
- required `quality_guard`, verification, runtime proof, and final review
- parent-local implementation

Route to `planning-intake` when the brief cannot fit in the current thread, a
successor would need durable state to resume safely, or execution needs queue
tracking, backlog state, multiple task cards, cross-session handoff, or
implementer delegation, or implementation-shaping decisions not already
closed.

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
