---
name: system-boundary-architecture
description: "Use when work changes abstractions, ownership boundaries, cross-surface contracts, composition roots, state authority, or storage/runtime/interface boundaries."
---

# System-Boundary Architecture

Structural decision skill for boundary-shaping work.

Capability:

- detecting structural triggers,
- loading the relevant doctrine references,
- enforcing the hard stop when ownership, authority, or boundary decisions are
  unresolved.

Keep runtime proof depth, completion evidence, browser/mobile runtime mechanics,
and project runtime recipes out of structural doctrine.

## Load

Read only the references needed for the current task:

- `references/system-and-boundary-architecture.md`
- `references/engineering-principles.md`
- `references/code-shape-and-local-design.md`
- `references/engineering-doctrine.md`
- `references/migration-guardrails.md`
- `references/python-service-and-boundary-doctrine.md`
- `references/web-frontend-boundaries.md`
- `references/web-route-and-state-boundary-doctrine.md`

## Workflow

1. Confirm the trigger is structural, not merely local implementation.
2. Load `references/system-and-boundary-architecture.md`.
3. Load companion references only for the affected surface:
   - local code shape: `references/code-shape-and-local-design.md`
   - Python services, unit-of-work shape, or typing integrity:
     `references/python-service-and-boundary-doctrine.md`
   - web layer ownership, route ownership, or state authority:
     `references/web-frontend-boundaries.md` and
     `references/web-route-and-state-boundary-doctrine.md`
   - migration guardrails: `references/migration-guardrails.md`
4. Check whether the active plan, packet, or other governing artifact already
   closes the needed owner, proof, state-authority, runtime, compatibility,
   rollout, migration, storage, and public-behavior decisions.
5. If multiple confirmed bugs or findings collapse onto one shared owner,
   diagnose common cause before tactical fixes. Record current authority,
   leaked responsibilities, and target split.
6. If the structural decision is not closed, stop and route back to planning.
   Do not settle the boundary locally during implementation.
7. If the decision is closed, apply the references and keep the governing
   artifact's structural disposition aligned when one exists.

## Stop Conditions

Stop execution and return to planning when:

- a boundary changes but the new owner is ambiguous,
- two plausible authorities remain for the same contract, state, or policy,
- a composition root would need to make policy decisions to finish the change,
- the fix needs a new structural rule not already closed by the governing
  artifact or durable doctrine,
- a local tactical patch would preserve a wrong ownership boundary,
- runtime proof ownership would need to move into this structural skill.

## Structural Trigger Examples

- a route, screen, shell, service, or controller becomes a hidden state machine,
- a shared contract is parsed or normalized independently by multiple owners,
- one nullable or dynamic shape carries multiple semantic meanings across
  boundaries,
- a service owns transaction lifecycle, mapping, repository choreography,
  workflow policy, and error translation at once,
- a shared component or facade gains caller-specific behavior by default,
- a composition root starts deciding workflow policy instead of wiring declared
  boundaries.

## Anti-Patterns

- loading this skill for every medium-sized edit just to be safe,
- treating it as a general engineering-principles skill instead of a structural
  decision skill,
- using implementation judgment to settle unresolved ownership after the
  structural trigger fired,
- moving runtime proof taxonomy or project runtime recipes into structural
  doctrine.
