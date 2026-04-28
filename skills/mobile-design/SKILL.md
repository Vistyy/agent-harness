---
name: mobile-design
description: "Use after user-apps-design for mobile-specific constraints: touch ergonomics, platform behavior, performance risk, accessibility, and mobile validation posture."
---

# Mobile Design

Use after `user-apps-design` for mobile-specific direction.

Owns touch ergonomics, platform navigation, mobile performance constraints,
mobile accessibility behavior, and mobile validation posture.

If missing context changes behavior, block and ask.

## Required References

Read `references/mobile-design-workflow.md` before planning or editing
mobile-specific UI or interaction behavior. It owns required context, risk gate,
guardrails, decision locks, manual audit, and delivery checklist.

Read only the companion reference needed for the current risk:
- product/mobile posture or unclear interaction model:
  `references/mobile-design-thinking.md`
- touch ergonomics, gestures, reach, or accessibility:
  `references/touch-psychology.md`
- list density, animation, startup, memory, or low-end device risk:
  `references/mobile-performance.md`
- mobile runtime verification strategy:
  `references/mobile-testing.md`
- networking, offline, sync, or backend handoff:
  `references/mobile-backend.md`
- platform-specific behavior:
  `references/platform-ios.md` and/or `references/platform-android.md`

Do not stop at this file for mobile design work.
