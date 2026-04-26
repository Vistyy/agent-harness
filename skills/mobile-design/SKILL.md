---
name: mobile-design
description: Companion skill for mobile platform constraints after `user-apps-design`; use for touch ergonomics, platform behavior, performance, and accessibility validation.
---

# Mobile Design

Use after `user-apps-design`. This skill owns mobile-specific constraints and validation, not cross-platform visual direction.

## Boundary

`user-apps-design` owns:
- visual direction
- parity decisions
- copy semantics

`mobile-design` owns:
- touch ergonomics and gesture fallback
- platform navigation and back behavior
- mobile performance constraints
- mobile accessibility behavior
- mobile-specific validation posture

If required context is missing and changes behavior, block and ask.

## Required Context

Capture first:
- target platform: iOS, Android, or both
- framework: Flutter, React Native, or native
- navigation model: tabs, stack, drawer, shell
- offline expectations and sync behavior
- target device classes and accessibility constraints

## Required Reading

Read only what matters:
- always: `mobile-design-thinking.md`, `touch-psychology.md`, `mobile-performance.md`, `mobile-testing.md`
- if networking or offline is in scope: `mobile-backend.md`
- if platform-specific behavior matters: `platform-ios.md`, `platform-android.md`

## Risk Gate

Rate 1-5:
- platform clarity
- interaction complexity
- performance risk
- offline dependence
- accessibility risk

Use result:
- high confidence: proceed with normal validation
- medium confidence: add explicit performance and UX checkpoints
- low confidence: simplify interaction model before coding

## Guardrails

Interaction and accessibility:
- touch targets meet platform minimums: `44pt` iOS, `48dp` Android
- every gesture path has explicit control fallback
- loading, empty, error, recovery states are mandatory
- back navigation follows platform conventions

Performance and reliability:
- no non-virtualized long lists
- avoid avoidable re-renders and JS-thread-heavy animation paths
- optimize for low-end devices and unstable networks
- do not ship debug logging or sensitive runtime data

Security basics:
- never store auth tokens in insecure local storage
- never hardcode shipped secrets

## Decision Locks

Navigation:
- use `tabs` for frequent top-level destinations
- use `stack` for drill-down flows
- use `modal` or `sheet` for contextual or interruptive tasks
- verify back behavior for every route
- define deep-link and resume behavior for critical flows

Typography and scaling:
- support system text scaling
- avoid fixed-size assumptions that break under accessibility text
- verify truncation and wrapping on small and large widths
- keep readable hierarchy under normal and large text

Color and readability:
- use semantic color roles consistently
- validate dark-mode contrast for text, controls, status feedback
- check outdoor readability for critical actions and status surfaces
- do not rely on color alone for important state

## Divergence Rule

Keep domain logic and API contracts unified.
Allow UI divergence only when platform norms differ and divergence is explicit.

## Required Manual Audit

- [ ] touch targets and spacing meet platform minimums
- [ ] list-heavy screens use virtualized or builder rendering
- [ ] default, loading, empty, error states are complete
- [ ] back behavior and transitions match platform expectations
- [ ] text scaling and truncation are validated
- [ ] dark mode and critical contrast surfaces are validated

## Delivery Checklist

- [ ] required context captured
- [ ] relevant reading reviewed
- [ ] risk gate completed
- [ ] divergence decisions documented
- [ ] accessibility and performance checks defined
- [ ] verification plan includes real-device or equivalent runtime validation

## Related Skills

- `user-apps-design` for design direction, parity matrix, end-user policy
- `flutter-expert` for Flutter implementation after mobile constraints are settled
