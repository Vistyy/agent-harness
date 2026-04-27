# Mobile Performance

Use for performance-sensitive mobile decisions before and during implementation.

## Baseline

Target:
- smooth scrolling and interactions
- stable frame times on common tasks
- predictable memory behavior on list/media-heavy paths
- no obvious battery drain in normal sessions

Treat lists, animations, media as architecture concerns, not polish.

## React Native Guardrails

Lists:
- use `FlatList` or `SectionList`; use `FlashList` only when justified
- keep stable keys; prefer `id`, not index
- keep row render path light
- keep `renderItem` stable
- add layout hints when rows are fixed height

Do not:
- render long datasets with `ScrollView`
- use index key on reorderable or dynamic lists
- do heavy transforms inside row render

Animations:
- prefer transform and opacity
- use native-thread-capable tools for frequent or complex motion
- avoid continuous JS-thread-heavy animation on critical screens
- do not animate expensive layout properties without need

Resources:
- clean subscriptions, timers, listeners
- optimize image size and format
- strip or gate debug logging

## Flutter Guardrails

Rebuilds:
- prefer `const` where possible
- localize rebuild scope
- isolate state updates to smallest responsible subtree
- keep business logic out of large widget trees

Lists and media:
- use builder-based list widgets for large collections
- tune image loading and caching
- dispose controllers and resources reliably

Animations:
- keep high-traffic screens simple
- favor platform-consistent motion over heavy choreography

## Hotspots

Highest risk:
- infinite or large lists
- image-heavy feeds
- map or chart views
- nested scrolling
- multiple concurrent animations

For each hotspot define:
- expected data size and growth
- low-end-device fallback
- instrumentation needed to diagnose regressions

## Memory And Battery

Memory:
- release unused resources aggressively
- avoid long-lived large objects
- avoid duplicate decoded images when not needed

Battery:
- avoid unnecessary polling and high-frequency timers
- pause or limit background work when not visible
- avoid work on every frame or scroll tick

## Readiness Check

- [ ] long lists are virtualized or builder-based
- [ ] key paths stay smooth on representative low-end devices
- [ ] animation paths avoid avoidable jank
- [ ] no avoidable leaks in listeners or controllers
- [ ] media handling is size-appropriate
- [ ] debug logging is stripped or gated
- [ ] performance-sensitive screens have observability hooks

## Regression Workflow

1. reproduce on representative device/profile
2. isolate render, data, or animation path
3. confirm with targeted instrumentation
4. apply smallest structural fix
5. re-check same scenario
