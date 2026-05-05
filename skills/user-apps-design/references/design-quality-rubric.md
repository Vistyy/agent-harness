# Design Quality Rubric

Owner for measurable end-user UI quality, design anchors, composition, and
planning references.

## Inputs

Before broad UI direction, redesign, visual polish, IA, hierarchy, composition,
density, or UI-quality proof, name:

- binding objective and accepted reductions
- affected surfaces, states, roles, viewports, and devices
- design context source: project overlay, durable project doc, `PRODUCT.md`,
  `DESIGN.md`, or `missing`
- register: `brand`, `product`, or `mixed`
- project design contract, archetype, or explicit missing-design-source blocker
- `3-7` design anchors for the surface
- preservation anchors for changed UI with a project-defined visual language or
  product-defining UI pattern
- anti-generic taste posture: project-approved taste and anti-references, plus
  generic AI tells to avoid unless project truth explicitly approves them
- reference/mockup artifact path or URL when used, or `none`

If project design truth is missing or contradictory for the claim, stop before
changing UI behavior. Record the missing rule, expected owner doc, and smallest
source-of-truth update; continue only after confirmation or an explicitly
narrowed claim that avoids the missing truth.

`PRODUCT.md` is a portable strategic alias. When present, it must name
register, users, product purpose, voice, anti-references, and accessibility or
delivery constraints. `DESIGN.md` is a portable visual alias. When present, it
must name design anchors, colors/tokens, typography, components/patterns,
states or motion/elevation, and do/don't rules. Project overlays may point
elsewhere; the harness must not require these files at repo root.

Project-approved taste wins. Generic AI taste loses when no project truth
supports it. Do not reject an explicit project identity cue solely because it
resembles a common anti-pattern; do reject unsupported generic patterns such as
template card grids, purposeless gradient text, decorative glass effects, or
one-note AI palettes when they make the surface read as unowned.

Broad UI quality claims also name an `anti_generic_report`:

- `source`: manual checklist, automated detector, combined, or `not-run`
- `register`: `brand`, `product`, or `mixed`
- `project_context`: project-approved taste and anti-references used
- `findings`: concrete visible or static findings with severity and surfaces
- `disposition`: `none`, `project-approved`, `fix-required`, or `blocked`
- `artifact`: path, command output, screenshot note, or `none` with reason

Minimum checks: unsupported template card grids, nested cards, hero-metric
layouts, icon tile stacks, purposeless gradient text, decorative glass/glow
effects, one-note AI palettes, and generic centered-stack composition. Brand
also checks unsupported default typography, timid palette, and missing imagery
when imagery is core to the category. Product also checks component
inconsistency, decorative motion, over-styled standard controls, weak density,
and unfamiliar affordances without purpose.

`not-run` blocks broad UI design readiness unless the claim is explicitly
narrowed or the report is not applicable with a named reason. Detector-only
pass is invalid; anti-generic evidence never replaces screenshot-led design
judgment.

For broad visual redesign, record the approved archetype or explicit exception
before product-code implementation.

## Preservation Anchors

Changed UI with a project-defined visual language or product-defining UI
pattern requires preservation anchors unless replacement is explicit in the
binding objective. Missing anchors block design judgment.

Reject a cleaner but generic replacement when it removes named preservation
anchors without an approved visual-language replacement objective.

Do not reject project-approved identity cues solely because they are asymmetric,
rotated, handmade, dense, or otherwise distinctive. Judge whether they satisfy
the project anchors, task posture, accessibility, and visible quality bar.

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

`design_judge` handoffs for broad UI design claims include design context
source, register, anti-generic taste posture, design anchors, preservation
anchors or `not-applicable`, and screenshot/contact-sheet artifacts. Missing or
contradictory required context returns `blocked`; an explicitly narrowed claim
must name which design-context boundary is no longer claimed.

`design_judge` consumes `anti_generic_report` with screenshots. It may treat
project-approved findings as intentional, reject unsupported generic findings,
or block missing/invalid reports. Clean detector output alone is not a design
`pass`.
