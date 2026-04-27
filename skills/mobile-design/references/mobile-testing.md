# Mobile Testing Patterns

Use to choose test layer and avoid weak mobile validation.

## Strategy

Primary rule:
- validate at highest layer that gives reliable signal for acceptable cost

Layer targets:
- unit: pure logic and deterministic transforms
- component/widget: UI state rendering and local interaction
- integration: multi-component flows and boundary contracts
- end-to-end: critical journeys and platform/runtime integration

## Tool Choice

Use unit/component tests when:
- behavior is isolated and deterministic
- failure diagnosis should be fast

Use integration tests when:
- UI/state/network boundaries are changing
- regressions happen in feature composition

Use E2E when:
- runtime platform characteristics matter
- navigation, permissions, deep links, or lifecycle events matter

## Required Coverage

Every significant feature should cover:
- default, loading, empty, error states
- offline or poor-network behavior
- interruption/resume behavior
- back-navigation or system gestures
- accessibility semantics and focus order

## Platform-Specific Checks

- test iOS-specific gesture/UI rules on iOS
- test Android-specific back/navigation/material behavior on Android
- verify shared behavior stays aligned where divergence is not intended

## Network And Offline

Required scenarios:
- timeout and retry behavior
- partial connectivity
- offline launch for cached-data paths
- recovery after reconnection

Validate both UX and data integrity:
- visible messaging
- safe retry semantics
- no silent destructive conflict

## Performance And Stability

Include runtime check for:
- long-list scrolling
- animation-heavy path
- memory-sensitive transitions

For high-risk features, add stress on:
- repeated navigation cycles
- repeated load/retry loops
- background/foreground transitions

## Gate Split

- PR gate: unit plus selected component/integration
- pre-release gate: expanded integration plus E2E smoke on target platforms

Before release:
- [ ] critical journeys pass on iOS and Android, or declared scope
- [ ] offline and error handling validated for critical flows
- [ ] accessibility checks completed for changed screens
- [ ] performance regressions checked on representative device class

## Anti-Patterns

- over-reliance on snapshots or source/implementation-shape assertions
- claiming mobile behavior from desktop-only execution
- skipping interruption and network-failure scenarios
- treating one platform result as proof for both
- shipping without validating recovery UX
