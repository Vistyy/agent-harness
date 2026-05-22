# Backlog Entry: engineering-harness/testing-posture/fake-migration-unit-test-fallback

## Metadata

- status: `open`
- owner: `testing-best-practices`
- bucket: `discovered separate debt`
- location: `skills/testing-best-practices/`

## Problem

During Budgeat Lane 1A branch hardening, `just python quality-full` exposed a
real runtime migration failure in migration `064`: the runtime database could
already lack an old `processing_failures` constraint that the migration tried
to drop unconditionally.

The attempted fix initially added a unit test that faked Alembic `op` and
asserted emitted DDL strings. That was the wrong instinct. It protected
implementation mechanics rather than the durable migration/runtime boundary,
and it contradicted the existing testing posture:

- persistent tests should protect durable behavior or contracts,
- workflow, infra, and runtime wiring need integration or smoke evidence,
- fake mock choreography is not valid evidence for a migration path.

The user challenged this as not a ceremony gap but a judgment failure: the
existing testing guidance was clear enough, and the bad test came from applying
the generic "bug fix needs regression test" habit without first asking what
boundary the test actually proves.

## Next Action

Discuss whether `$testing-best-practices` or delivery closeout should include a
lighter decision cue for migration/runtime failures: prefer rerunning the real
failed path or a real migration execution over adding fake persistent tests.
Avoid adding checklist ceremony unless it changes that judgment at the point of
work.
