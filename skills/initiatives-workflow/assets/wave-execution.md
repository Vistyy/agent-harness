# Wave <wave-id> Execution Packet

## Objective

- original objective: `<user objective>`
- accepted reductions: `<none | explicit>`
- residual gaps: `<none | explicit>`
- checkpoint: `<current user/context checkpoint>`

## Design Integrity

- owner/interface: `<owner/module/interface>`
- key decisions: `<decisions | none>`
- verdict: `<acceptable | blocked>`
- accepted temporary debt: `<none | backlog path>`

## Execution

### `<task-or-slice>`

- State: `<blank | done | blocked>`
- Correction posture: `<none | delete | reuse | collapse | move | deepen | add>`
- Owned surfaces: `<paths/surfaces>`
- Checks/artifacts: `<commands/artifacts>`

- Shape contract:
  - Owner/interface: `<owner/interface | omit when posture is none>`
  - Target or rejected simpler path: `<target or rejected path | omit when posture is none>`
  - Stop triggers: `<stop triggers | omit when posture is none>`
  - Proof surface: `<proof surface | omit when posture is none>`

- blockers/decisions: `<none | blocker/decision and owner>`

## Readiness Claim

- exact claim: `<claim>`
- claimed interface: `<workflow/module interface>`
- required evidence: `<tests/runtime/review/design/artifacts>`
- evidence status: `<planned | blocked | satisfied | narrowed>`
- unproved boundaries: `<none | entries>`
- residual risks: `<none | entries>`

## Closeout Evidence

- retained value: `<durable owner/backlog path | none yet>`
- current-scope issues: `<fixed/routed/accepted | none>`
- disposable wave state: `<removable without losing authority | blocked reason>`
