# Wave Packet Contract

Owns the durable packet schema for `wave-execution.md`.

A packet exists only when work must survive queue tracking, handoff,
interruption, resume, review, or multiple execution slices. It stores the
minimum state needed to keep the objective, design, execution, and readiness
claim aligned.

## Required Sections

- `Objective`
- `Design Integrity`
- `Execution`
- `Readiness Claim`

## Objective

Record original objective, accepted reductions, residual gaps, and any current
user checkpoint or plan amendment that changes scope.

No task slice may replace this objective. A narrower outcome needs an accepted
reduction.

## Design Integrity

Record selected owner/interface, key decisions, design-integrity verdict,
accepted temporary debt or `none`, and blocker status.

Design doctrine belongs to `../../design-integrity/SKILL.md`; the packet only
stores the decision.

## Execution

Record task slices, owned surfaces, dependencies, blockers, decisions, evidence,
and follow-up.

Task cards are optional when one slice is enough. When used, each `### <task>`
card needs only:

- `State`: `blank`, `done`, or `blocked`
- `Correction posture`: `none`, `delete`, `reuse`, `collapse`, `move`,
  `deepen`, or `add`
- `Owned surfaces`
- `Checks/artifacts`

When `Correction posture` is not `none`, include one compact shape contract:

- `Shape contract`
- `Owner/interface`
- `Target or rejected simpler path`
- `Stop triggers`
- `Proof surface`

When `Correction posture` is `add`, `Target or rejected simpler path` names the
rejected non-add option and boundary harm. The packet stores the claimed shape;
`../../design-integrity/SKILL.md` owns whether it is true.

Add more fields only when they prevent real ambiguity.

## Closeout Evidence

While the wave is active, record closeout evidence needed to support the final
claim: retained value extracted to the durable owner or backlog, current-scope
issues fixed/routed/accepted, and disposable wave state that can be removed.

After closure, packet state is not successor authority. The durable owner,
valid backlog item, and queue status must preserve all retained authority.

## Readiness Claim

Record exact claim, claimed workflow/module interface, required evidence,
evidence status, unproved boundaries, and residual risks.

Claim doctrine belongs to `../../readiness-claim/SKILL.md`; the packet only
stores the current claim and evidence state.

No evidence may prove a smaller invented objective. If evidence crosses only
part of the claimed interface, narrow or block the claim.

## Trust

An implementer may trust an `execution-ready` packet for closed objective,
design, execution, and readiness state. Stop when the packet omits a material
owner, claimed interface, blocker, dependency, or accepted reduction needed for
the next step.
