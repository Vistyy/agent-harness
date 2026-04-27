# Android Platform Guidelines

Use for Android-specific behavior and visual decisions.

## Priorities

Optimize for:
- clear task-oriented hierarchy
- Material-consistent interaction patterns
- predictable system back behavior
- accessibility across varied device classes

## Typography

- prefer Roboto or system typography
- respect Android text scaling
- keep hierarchy readable
- avoid fixed text assumptions across OEM scaling differences
- verify wrapping on narrow and large devices

## Color And Theme

- use semantic color roles
- support dark theme properly
- account for Material emphasis and state colors
- if dynamic color is used, keep legibility and semantic consistency

## Layout And Responsiveness

- use responsive layout for phone and tablet widths
- keep spacing and density aligned to task complexity
- avoid fragile pixel-specific placements

## Navigation

- bottom navigation for frequent top-level destinations
- stack flow for drill-down tasks
- rails/adaptive patterns on larger screens when relevant
- system back must be predictable
- avoid dead-end screens that need custom back workarounds

## Components

Buttons:
- clear primary, secondary, destructive hierarchy
- touch target about `48dp`

Cards and lists:
- keep strong content hierarchy
- preserve smooth scroll on large datasets

Inputs:
- explicit labels, validation states, helper/error messaging
- keyboard/action handling aligned to task flow

## Native Patterns

Prefer established patterns for:
- snackbars for transient feedback
- bottom sheets or dialogs by task scope
- pull to refresh when content model fits
- ripple/touch feedback consistency

## Icons

- prefer Material Symbols
- keep size and weight coherent
- avoid mixed icon families in one flow unless justified

## Accessibility Baseline

- readable contrast in light and dark modes
- accessible labels and semantics
- scalable text with resilient layout
- adequate touch targets and spacing

## Ready Check

- [ ] navigation and back behavior validated
- [ ] responsive behavior checked for target device classes
- [ ] states and feedback follow platform norms
- [ ] dark theme and contrast validated
- [ ] accessibility semantics and target sizes validated
