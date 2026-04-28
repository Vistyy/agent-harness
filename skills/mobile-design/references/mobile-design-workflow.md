# Mobile Design Workflow

Use before planning or editing mobile-specific UI or interaction behavior. This
reference owns required context, risk gate, guardrails, decision locks, manual
audit, and delivery checklist.

## Required Context

Capture first:
- target platform: iOS, Android, or both
- framework: Flutter, React Native, or native
- navigation model: tabs, stack, drawer, shell
- offline expectations and sync behavior
- target device classes and accessibility constraints

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

Keep domain logic and API contracts unified. Allow UI divergence only when
platform norms differ and divergence is explicit.

## Required Manual Audit

- [ ] touch targets and spacing meet platform minimums
- [ ] list-heavy screens use virtualized or builder rendering
- [ ] default, loading, empty, error states are complete
- [ ] back behavior and transitions match platform expectations
- [ ] text scaling and truncation are validated
- [ ] dark mode and critical contrast surfaces are validated

## Delivery Checklist

- [ ] required context captured
- [ ] risk-triggered mobile docs reviewed
- [ ] risk gate completed
- [ ] divergence decisions documented
- [ ] accessibility and performance checks defined
- [ ] verification plan includes real-device or equivalent runtime validation
