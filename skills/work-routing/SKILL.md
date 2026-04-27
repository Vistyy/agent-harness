---
name: work-routing
description: "Use when choosing whether work should be direct, small bounded, standalone-plan, planning-intake, or wave execution."
---

# Work Routing

Initial route selection only. This skill chooses the lightest execution route
that preserves the outcome, owner boundary, and proof bar.

It does not own planning readiness, wave promotion, packet schema, review
approval, completion proof, or subagent delegation mechanics.

## Route Table

- `direct`: tiny/local work; execute directly with fresh proof and no plan
  artifact.
- `small bounded`: in-thread objective, expected touched files or surfaces, and
  proof command or artifact; promote only if risk appears.
- `standalone plan`: requirements and material decisions are closed, but ordered
  implementation needs a durable plan under `docs/plans/**`.
- `planning-intake`: ambiguous work, material decision open, vague scope, or
  wave shaping.
- `wave execution`: full execution of one `execution-ready` wave from its
  delivery map, durable brief, and canonical packet.

## Escalate When

Use the next heavier route when two competent implementers could choose
materially different owners, proof paths, state authority, runtime posture,
compatibility/migration behavior, or public behavior.

## Owners

- project overlays and reusable harness posture: `../harness-governance/SKILL.md`
- ambiguous planning and wave shaping: `../planning-intake/SKILL.md`
- standalone plan writing: `../writing-plans/SKILL.md`
- standalone plan execution: `../executing-plans/SKILL.md`
- wave execution: `../wave-autopilot/SKILL.md`
- completion proof: `../verification-before-completion/SKILL.md`
- subagent delegation: `../subagent-orchestration/SKILL.md`
