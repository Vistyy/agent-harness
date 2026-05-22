# Mobile UI Constraints

Owner for mobile-specific UI constraints inside end-user app design.

Proof selection belongs to `../../verify-work/SKILL.md`. Backend, offline,
sync, and API contracts belong to
`../../solution-shaping/references/mobile-client-boundaries.md`.

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

## Proof

Mobile design claims require proof for the affected states and device classes.
Use `../../verify-work/SKILL.md` for proof selection and the Test Android Apps
plugin for Android emulator/device mechanics.
