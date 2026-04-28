# Touched Component Integrity Gate

Use this for all non-trivial work, all reviews, all implementation handbacks,
and any time a must-block signal may exist.

## Touched Owner

Name the smallest owner/component whose contract, state, lifecycle, design,
workflow, or proof the change touches. Expand only to shared authority required
by the change.

Escalation order: hunk -> function/method -> class/component/module -> file ->
shared owner/authority.

Escalate when behavior depends on wider state, lifecycle, policy, proof,
duplicate authority, or missing/weak modeling. Do not block on unrelated repo
debt outside the touched owner or required shared authority.

## Must-Block Signals

Unacceptable touched-component integrity means anchored evidence in the touched
owner shows one or more of:

- `responsibility-overload`: one unit owns multiple independent
  responsibilities, policies, lifecycle phases, or proof concerns.
- `patch-through-architecture`: the fix adds indirection instead of deleting,
  collapsing, or reshaping the bad structure.
- `fake-boundary`: wrapper, protocol, adapter, cast, dynamic call, or
  type-erased bridge hides use of the real owner contract.
- `contract-weakening`: domain data crosses an owner boundary as `dict`,
  `object`, `Any`, stringly state, partial copied object, nullable multi-meaning
  value, or broad cast when a stronger shape exists.
- `duplicate-authority`: multiple places decide the same policy, plan,
  normalization, state, or lifecycle repair.
- `repeated-discovery`: one flow resolves, checks, or derives the same state
  repeatedly instead of modeling it once and passing it through.
- `private-test-choreography`: tests prove private globals, call order, or
  internal seams more than behavior or owner contract.
- `ownerless-compatibility`: fallback, shim, alternate path, migration bridge,
  or old/new coexistence survives without owner, protected surface, and removal
  condition.

If a local defect is a symptom of one of these signals, scope moves to the
touched owner/component.

## Successor Owner

When work moves, collapses, splits, centralizes, deletes wrappers around, or
transfers behavior, assess the successor owner/component as touched.

The successor must be acceptable on its own. Do not approve because old
complexity was removed, owners became fewer, tests pass, or the implementation
matches the packet. If the successor has responsibility-overload, unclear
internal boundaries, private-test choreography, duplicate authority, or another
must-block signal, reshape before approval or record accepted debt with a
backlog link.

## Required Action

- Planner: reshape before approval.
- Implementer: stop and hand back if the approved task preserves or adds to an
  unacceptable touched owner outside accepted debt.
- `quality_guard`: reject; approval with unacceptable or unassessed integrity is
  reviewer failure.
- `final_reviewer`: block closeout.

`not assessed` is valid only on `REJECT` or `BLOCKED` reports. It is never
approvable for non-trivial work.

## Accepted Debt

Debt acceptance is valid only after presenting:
- touched owner/component
- must-block signal(s)
- risk
- recommended reshape
- proposed backlog path

Blanket, prior, vague, or chat-only acceptance is invalid. Accepted debt needs a
backlog item with owner, risk, and removal condition, and approval/closeout must
link it.

## Report

When this gate applies, state:
- touched owner/component
- highest inspected scope
- integrity: `acceptable`, `unacceptable`, or `not assessed`
- must-block signals, or `none`
- accepted-debt backlog link, or `none`
