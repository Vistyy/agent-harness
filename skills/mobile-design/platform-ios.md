# iOS Platform Guidelines

Use for iOS-specific behavior and visual decisions.

## Priorities

Optimize for:
- clarity and hierarchy
- smooth native-feeling transitions
- predictable gesture and back behavior
- strong accessibility support

## Typography

- prefer SF Pro or system typography
- respect Dynamic Type
- keep hierarchy consistent
- avoid fixed-size text that breaks with larger settings
- validate truncation and wrapping on common iPhone widths

## Color And Theme

- prefer semantic color roles
- support light and dark mode
- keep contrast clear in both
- avoid using saturated accent color as sole critical meaning

## Layout And Safe Areas

- respect safe areas on major containers
- avoid placing critical controls in gesture-conflict zones
- keep spacing rhythm consistent with platform feel

## Navigation

- tabs for frequent top-level destinations
- stack for drill-down flows
- modal or sheet for contextual tasks
- honor iOS back conventions and swipe gestures
- avoid unexpected navigation-model mixing

## Components

Buttons:
- clear primary, secondary, destructive hierarchy
- touch targets at least `44pt`

Lists:
- support standard list affordances and swipe actions when appropriate
- keep density readable for touch and Dynamic Type

Inputs:
- clear labels, placeholders, error states
- keyboard behavior matches field intent

## Native Patterns

Prefer native-feeling patterns for:
- pull to refresh
- swipe row actions
- context menus when discoverable
- sheet transitions and dismissal

## Icons

- prefer SF Symbols
- match weight and scale to nearby typography
- avoid mixed icon families in one surface

## Accessibility Baseline

- VoiceOver labels and actionable semantics
- Dynamic Type validation on changed screens
- sufficient contrast and clear focus/selection affordances
- target sizes and spacing preserved under larger text

## Ready Check

- [ ] navigation and back behavior match iOS norms
- [ ] Dynamic Type verified
- [ ] safe area handling verified
- [ ] iOS interaction patterns used where appropriate
- [ ] accessibility semantics and target sizes validated
