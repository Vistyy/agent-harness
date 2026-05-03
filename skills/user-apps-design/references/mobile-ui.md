# Mobile UI Constraints

Owner for mobile-specific UI constraints inside end-user app design.

Runtime mechanics belong to `../../mobileapp-testing/SKILL.md`. Backend,
offline, sync, and API contracts belong to
`../../system-boundary-architecture/references/mobile-client-boundaries.md`.

## Rule

Mobile UI work must preserve touch ergonomics, platform navigation, safe areas,
accessibility, responsive text, and performance constraints. Platform divergence
is allowed only when it serves platform ergonomics and preserves product
behavior.

## Required Inputs

Name target platform, framework, navigation model, device classes,
accessibility constraints, and offline or interruption behavior that changes
the user experience.

## Hard Constraints

- Touch targets meet platform minimums: `44pt` iOS, `48dp` Android.
- Critical gestures need visible control fallback.
- Back/navigation behavior follows platform conventions.
- Safe areas, keyboard/IME, sheets, and overlays are checked where affected.
- Text scaling preserves hierarchy, wrapping, truncation, and target sizes.
- Reachable loading, empty, error, recovery, interruption, and resume states are
  designed.
- Long lists use virtualized or builder rendering.
- Animation and media-heavy surfaces avoid avoidable jank, leaks, and battery
  cost.
- Dark mode, contrast, focus order, semantics, and non-color state cues are
  checked when the surface claims mobile quality.

## Platform Notes

iOS:
- respect Dynamic Type, safe areas, swipe/back conventions, sheets, and native
  list affordances
- prefer system typography and SF Symbols when the project has no stricter
  design system

Android:
- respect system back, text scaling, responsive phone/tablet layouts, Material
  feedback, and dark theme
- prefer Material Symbols when the project has no stricter design system

## Proof

Mobile design claims require proof for the affected states and device classes.
Use `../../runtime-proof/SKILL.md` for runtime verdict authority and
`../../mobileapp-testing/SKILL.md` for emulator/device mechanics.
