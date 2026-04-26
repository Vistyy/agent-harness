# Project Setup And Integration

Use this reference when adding or restructuring Flutter features in this repository context.

## Integration Principles

- extend existing feature boundaries before introducing new top-level structure
- keep domain/state/navigation responsibilities separated
- prefer incremental structural changes over broad architecture rewrites

## New Feature Checklist

- define feature boundary and ownership
- wire routes in one place with explicit entry points
- register providers close to feature scope unless shared intentionally
- keep reusable UI primitives in shared layers only when reused
- align naming and folder conventions with adjacent mobile features

## Dependency Discipline

- add dependencies only when there is a concrete use case
- avoid adding overlapping libraries for the same concern
- keep codegen/runtime packages version-aligned with existing project choices

## App Entry Wiring

When wiring at app level:
- keep bootstrap deterministic
- ensure router/provider setup order is explicit
- avoid hidden global initialization side effects

## Common Failure Modes

- feature code leaking into unrelated layers
- route registration scattered across many files
- shared folder becoming a dumping ground for one-off widgets
- introducing new state framework patterns mid-feature without migration plan
