---
name: work-routing
description: "Use when choosing whether work should be direct, small bounded, planning-intake, or wave execution."
---

# Work Routing

Owns route selection and the workflow gate matrix. Technical contracts stay
with their owner skills.

## Full Work Rule

Route to the lightest shape that can complete the binding objective and fix the
touched owner surface required to make it true. Do not route a broad objective
into a smaller invented task.

`small bounded` is valid only when the full objective is small. If full
correction is blocked, stop and name the blocker instead of patching around it.

## Routes

- `direct`: tiny/local work; no material owner, proof, runtime, compatibility,
  migration, or public-behavior decision is open.
- `small bounded`: the full objective is bounded in-thread, with named surfaces
  and proof.
- `planning-intake`: scope, decisions, proof, owner boundary, or wave shape is
  still open.
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
| completion proof | `../verification-before-completion/SKILL.md` |
| review/approval semantics | `../code-review/SKILL.md` |
