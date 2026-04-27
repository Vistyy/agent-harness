# Mobile Design Thinking

Use before UI implementation. Force context-first decisions.

## Required Input Packet

Capture:
- target platforms
- framework/runtime
- primary user task and success criteria
- key constraints: offline, low-end devices, accessibility, latency
- navigation model candidates
- risk level: performance, interaction complexity, data consistency

If unknown input changes behavior, stop and ask.

## Core Rules

1. Mobile sessions are short and interrupt-heavy.
   Optimize for quick recovery. Avoid deep fragile flows for common tasks.
2. Touch is imprecise.
   Design for reachability and target size. Do not hide critical actions behind gesture-only paths.
3. Network is unreliable.
   Define loading, empty, error, offline, retry behavior up front.
4. Battery and memory are product constraints.
   Optimize list and media paths before polish work.

## Anti-Default Rules

Do not default to:
- desktop-dense layouts on phones
- gesture-only critical actions
- large forms without progressive disclosure
- non-virtualized long lists
- animation-first designs without performance budget
- identical iOS and Android behavior without platform check

## Screen Decomposition

For each screen, define:
- primary intent
- top actions, max 1-2
- information hierarchy
- state model: default, loading, empty, error, offline
- interaction model: taps, scroll, gestures, back behavior
- analytics and observability needs

## Decision Questions

Navigation:
- is destination frequent enough for tabs or shell?
- is flow linear enough for stack?
- does back behavior match platform norms?

State:
- which data is blocking vs progressive?
- what stale-data tolerance is acceptable?
- which failures recover in place vs force exit?

Lists and content:
- expected dataset size and growth?
- which fields must stay above fold?
- which skeleton preserves layout stability?

Interactions:
- which actions need confirmation?
- which actions need haptic or visual feedback?
- which actions are dangerous and must be de-emphasized?

## Quick Risk Gate

Rate each dimension low, medium, high:
- platform divergence
- interaction complexity
- performance
- offline or sync
- accessibility

Guidance:
- mostly low: proceed
- any high: simplify UX or add explicit mitigation
- two or more high: redesign before implementation

## Project Type Bias

Internal tool:
- prioritize density and task speed
- allow steeper learning curve
- keep error explainability strong

Consumer app:
- prioritize discoverability and trust
- reduce choice overload
- bias toward forgiving flows and clear feedback

Transactional workflow:
- prioritize data integrity and confirmation
- keep progress resumable
- make failure handling explicit

## Ready Check

- [ ] input packet complete
- [ ] state model documented
- [ ] platform divergence explicit
- [ ] offline and retry behavior defined
- [ ] performance-sensitive surfaces identified
- [ ] accessibility constraints listed
- [ ] risky assumptions recorded

## Definition Of Ready

Ready when:
- intent and hierarchy are clear
- interaction model is explicit
- state behavior is complete
- platform constraints are addressed
- verification approach is defined
