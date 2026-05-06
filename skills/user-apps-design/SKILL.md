---
name: user-apps-design
description: "Use for product-facing UI work that needs project design context, rendered artifacts, or screenshot-led visual approval."
---

# User Apps Design

Owns the reusable UI completion contract. Projects own design taste and method.

## Contract

Broad product UI is not complete from code, tests, selectors, logs, detectors,
runtime evidence, or review alone.

It needs:

- project design source, or a narrowed claim that does not assert project
  visual quality;
- rendered screenshot/contact-sheet artifacts for claimed screens, states,
  viewports, and devices;
- `design_judge` `pass` for the same claim.

When a project has a local design workflow such as Impeccable, shape there
first. Use `imagegen` for mockups or reference images when a visual target would
improve implementation. Generated mockups become design sources only after user
approval or project-workflow recording.

If the project design source or declared local design workflow is missing or
contradictory, stop or narrow the claim. Do not invent visual direction in the
global harness.

## Approval

Handoffs for broad UI approval name:

- binding objective and accepted reductions;
- affected screens, states, viewports, and devices;
- project design source, or `missing`;
- project-local artifacts required by that source, or `none`;
- screenshot/contact-sheet artifact paths.

Missing project design source blocks broad visual-quality approval unless the
claim is explicitly narrowed.

`design_judge` compares rendered artifacts against the binding objective,
project design source, and required project-local artifacts. Reject when the
rendered UI is not inspectable, visibly broken, generic against the project
target, materially weaker than an approved target, inaccessible, clipped,
incoherent, or non-shippable.

Runtime evidence, tests, selectors, detector output, numeric scores, code
review, and final review do not approve visual quality. `design_judge` returns
`pass`, `reject`, or `blocked` for visual quality only; it does not decide live
behavior or code quality.

## Boundary

A project design source is any current, project-owned, or user-approved source
that defines visual intent for the claim. It can be a local doc, design-system
contract, mockup, screenshot, reference, workflow artifact, or direct user
decision.

The global harness does not prescribe that source's format, tool, artifact
names, or design method. It only checks that the declared source was followed
for the claim.

## References

Read project overlay docs first.
Read `references/parity.md` when cross-client parity, staged delivery, or UX divergence is part of the claim.
Read `references/text-constraints.md` when copy, truncation, overflow, i18n, validation text, or UX copy is part of the claim.
Read `references/mobile-ui.md` when mobile touch ergonomics, safe areas, platform navigation, gestures, accessibility, text scaling, or mobile performance is part of the claim.
