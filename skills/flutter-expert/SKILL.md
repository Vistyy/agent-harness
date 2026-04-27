---
name: flutter-expert
description: "Use when implementing or debugging Flutter/Dart mobile code: repo-consistent architecture, state management, navigation, widget composition, and performance."
---

# Flutter Expert

Use for Flutter/Dart implementation and debugging mechanics.

For end-user visual direction, use `user-apps-design`.
For mobile UX constraints, use `mobile-design`.

## Scope

In:
- feature implementation
- state/provider design
- navigation and route behavior
- widget composition and rebuild behavior
- performance/platform debugging

Out:
- end-user copy and UX policy
- mobile design policy
- web Tailwind styling

## Workflow

1. clarify feature boundary and runtime surface
2. choose smallest viable state/navigation shape
3. implement with rebuild-safe composition
4. verify with tests and runtime checks
5. optimize only when evidence shows risk

## References

- state/providers: `references/state-and-providers.md`
- navigation: `references/navigation.md`
- project setup: `references/project-setup.md`
- UI/performance: `references/ui-patterns.md`

Load only what current issue needs.

## Guardrails

- keep rebuild scopes narrow
- avoid global mutable shortcuts
- make route transitions and back behavior explicit
- prefer clear composition over clever abstractions
- do not claim runtime behavior from static inspection alone
