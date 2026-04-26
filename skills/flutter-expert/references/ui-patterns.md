# UI And Performance Patterns

Use this reference for rebuild-safe widget composition and performance-sensitive surfaces.

## Widget Composition Rules

- use `const` where values are static
- keep widgets focused and composable
- use stable keys in dynamic/reorderable collections
- avoid heavy computation inside `build`

## Rebuild Control

- isolate high-churn subtrees
- watch minimal state needed per widget
- split large widgets when different sections update at different rates

## List And Scroll Patterns

- use builder/sliver patterns for large datasets
- avoid eager building long lists
- keep item widgets lightweight and predictable

## Expensive UI Isolation

- use `RepaintBoundary` where repaint isolation is warranted
- avoid overusing repaint boundaries without evidence
- profile first when addressing jank

## Heavy Work Offloading

- move CPU-heavy transforms/parsing off the UI isolate (`compute`/isolates)
- keep async transitions explicit in UI state

## Image And Media Handling

- constrain decode sizes when possible
- avoid loading full-resolution assets into small containers
- use caching strategy appropriate to feature usage patterns

## Investigation Checklist

- [ ] issue reproduced on target runtime
- [ ] source identified (rebuild, layout, image, computation, animation)
- [ ] smallest structural fix applied
- [ ] behavior revalidated on same scenario
