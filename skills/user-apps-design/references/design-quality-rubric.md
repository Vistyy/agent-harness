# Design Quality Rubric

Owner for measurable end-user UI quality, design anchors, composition, and
planning references.

## Inputs

Before broad UI direction, redesign, visual polish, IA, hierarchy, composition,
density, or UI-quality proof, name:

- binding objective and accepted reductions
- affected surfaces, states, roles, viewports, and devices
- project design contract, archetype, or explicit missing-design-source blocker
- `3-7` design anchors for the surface
- reference/mockup artifact path or URL when used, or `none`

If project design truth is missing or contradictory for the claim, stop before
changing UI behavior. Record the missing rule, expected owner doc, and smallest
source-of-truth update; continue only after confirmation or an explicitly
narrowed claim that avoids the missing truth.

For broad visual redesign, record the approved archetype or explicit exception
before product-code implementation.

## Mockup Anchors

Generated mockups and external references are optional planning anchors for:

- broad redesign
- underspecified visual direction
- whole-screen composition quality

When used, cite the artifact path or URL, inspect it against the project design
anchors, and record what is adopted. A mockup that conflicts with project truth
is rejected. It never becomes pixel truth, product truth, or a replacement for
`DESIGN.md`.

Use Codex image generation only when a raster mockup would clarify visual
direction better than text, existing screenshots, or project references.

## Quality Dimensions

Assess each affected surface against the binding objective:

| Dimension | Pass condition |
| --- | --- |
| Product fit | matches domain, audience, task posture, and project anchors |
| Hierarchy | primary task, state, and next action are obvious without explanation |
| Composition | layout has intentional alignment, rhythm, grouping, and whitespace |
| Density | information density fits repeated use and does not hide needed context |
| Typography | scale, weight, line length, and wrapping preserve scanability |
| Color/material | emphasis, states, contrast, and surfaces are purposeful and accessible |
| Interaction feel | feedback, transitions, and controls fit the platform and task risk |
| State quality | loading, empty, error, disabled, success, and recovery states are designed where reachable |
| Distinctiveness | avoids generic template output when the objective asks for product character |

Reject UI-quality claims when the surface is merely functional, generic,
visually incoherent, unreadable, inaccessible, missing reachable states, or not
inspectable in the claimed viewports/devices.

## Composition

Screens and routes compose reusable atoms, controls, sections, and patterns.

Rules:

- promote repeated or cross-surface structure out of route-local markup
- avoid parallel component families for the same semantic role
- keep business/domain logic out of visual primitives when possible
- update a project design gallery or component inventory when a reusable block
  changes materially, unless follow-up is explicitly accepted
- prefer affordance over narration; if core interaction needs explanatory
  paragraphs, rework structure before adding copy

## Design-System Fit

Use project tokens, components, patterns, and design-system contracts. Do not
invent ad hoc styling values when a project owner already defines the choice.

For IA changes, record the established pattern as `adopt` or `reject` with
rationale before implementation.

When route, shell, navigation, or state authority changes, use
`../../system-boundary-architecture/SKILL.md` before styling around the
boundary.

## Runtime Consumption

UI-quality runtime evidence consumes the binding objective, design anchors,
affected surfaces/states/viewports/devices, and screenshot artifacts.

This file names UI-quality blockers. `../../runtime-proof/SKILL.md` owns
runtime claim maps, `pass`/`reject`/`blocked` verdict semantics, entrypoint
fidelity, and completion impact.

`design_judge` applies this rubric to screenshot/contact-sheet artifacts and
returns product UI design `pass`, `reject`, or `blocked`. Reject generic,
scaffold-like, incoherent, inaccessible, ugly, or non-shippable UI even when
functional assertions pass.
