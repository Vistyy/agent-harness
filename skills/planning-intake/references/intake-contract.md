# Intake Contract

Use this checklist for non-trivial planning.

## Decisions

Close decisions locally when the harness/project owner already gives a clear
default. Ask the user only for user-owned choices such as product intent,
priority, irreversible tradeoff, credential/tenant access, or acceptance of
temporary debt.

Every blocking question includes a recommendation and the reason.

## Touched Owner

Touched owner/component is the smallest owner whose contract, state, lifecycle,
design, workflow, or proof the change touches. Expand only to shared authority
required by the objective.

Assess whether the owner is coherent enough to complete the objective. If it is
not, fix the owner now or stop for explicit accepted debt.

## Omission Sweep

Check that the plan did not drop:
- original objective, breadth, quality bar, or runtime behavior
- public surfaces and entrypoints
- owner/state authority and migrations
- proof for each claimed surface
- cleanup of obsolete paths in touched scope
- valid deferrals and their durable home

## Proof Allocation

For every material claim, name:
- owner layer
- exact proof command or artifact
- expected evidence
- counterfactual regression probe

No exact proof means no broad completion claim.
