# Touch Psychology

Use for touch interaction, control placement, and feedback decisions.

## Target Baselines

Minimum targets:
- iOS: `44pt`
- Android: `48dp`
- practical WCAG baseline: about `44px`

Spacing:
- keep at least `8px` between adjacent targets
- add more spacing for destructive or irreversible actions

Rule:
- visual affordance may be smaller than hit area only if hit area is explicitly expanded

## Reachability

- put frequent actions in easy-reach zones
- bias primary actions toward lower half on large phones
- avoid top-corner-only placement for frequent actions
- keep destructive actions out of high-frequency reach zones
- for one-handed use, reduce travel distance between key actions

## Feedback

Users expect immediate acknowledgment.

Required:
- visible state change on press
- immediate response feedback
- progress feedback for noticeable waits

Haptics:
- visual feedback is always baseline
- use haptics for confirmations, toggles, meaningful milestones
- avoid heavy haptic spam on routine high-frequency actions

## Gestures

- hidden gesture must never be only path for critical task
- provide visible fallback for swipe and long-press actions
- start with platform-standard gestures
- avoid conflicts with system navigation

Checklist:
- affordance is discoverable
- action is reversible where possible
- fallback control exists

## Cognitive Load

Reduce load by:
- limiting simultaneous choices on small screens
- chunking complex steps
- using progressive disclosure
- preserving progress across interruptions

Avoid:
- dense decision-heavy screens without hierarchy
- long unsegmented forms without save/resume

## Accessibility

- keep large targets and adequate spacing
- keep focus order and semantics consistent
- avoid precision-dependent interactions
- do not rely on color alone

Helpful patterns:
- explicit buttons over gesture-only paths
- strong labels for ambiguous icons
- forgiving controls with undo where feasible

## Trust

Perceived quality depends on:
- predictable feedback
- stable layout during loading
- clear confirmation for impactful actions
- explicit recovery path after error

## Quick Check

- [ ] targets meet platform minimums
- [ ] spacing reduces accidental taps
- [ ] primary actions are reachable
- [ ] gesture alternatives exist for critical actions
- [ ] feedback is immediate and clear
- [ ] accessibility constraints are covered
