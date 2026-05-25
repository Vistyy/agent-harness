# Patch-Native Bug Hunt

Changed-surface bug-finding lens for diffs, commits, PRs, working trees,
generated artifacts, executable code, schemas, migrations, API contracts,
runtime behavior, and data/state changes.

Start from the assumption that the patch is wrong. Inspect changed hunks before
the implementation story. Search for every discrete current-scope bug the author
would fix if told.

## Finding Bar

A bug finding must satisfy all of these:

- introduced, exposed, depended on, or made worse by the current change
- affects code, data, state, runtime behavior, user-visible behavior, security,
  privacy, reliability, compatibility, accessibility, performance, migrations,
  observability, or maintainability
- discrete, actionable, and high enough confidence that a required fix can be
  named
- located on the changed surface or the nearest changed line that causes the
  issue

Do not flag speculation, taste-only preferences, unrelated old defects, or
findings whose fix is not clear. Cross-file findings must name the affected
owner or path and the concrete breakage chain.

Do not omit a real bug because tests pass, the parent summary omitted the path,
or the code looks locally coherent.

## Bug Classes

Check all relevant classes:

- migration order, downgrade, rollback, constraint, enum, seed, fixture, and
  production-like data failures
- schema, parser, API, SDK, docs, fixture, generated artifact, or contract drift
- accepted input that downstream validation, decoding, storage, rendering, or
  processing rejects or mishandles
- state transitions, retries, recovery, idempotency, cancellation, cleanup,
  resume, and duplicate handling
- status, outcome, admin health, analytics, audit log, metric, and
  observability classification
- auth/authz confusion, capability loss, tenant/user boundary, and misleading
  recovery actions
- race, ordering, lease, transaction, partial update, atomicity, and eventual
  consistency hazards
- retained large objects, unbounded memory growth, resource leaks, orphaned
  storage, stale durable state, and background-worker lifecycle leaks
- compatibility, accessibility, performance, privacy, security, and data
  integrity regressions caused by the patch

Search callers, callees, schemas, migrations, fixtures, generated contracts,
runtime entrypoints, and cleanup paths when they can invalidate the local story.

## Output

Report:

- bug-hunt verdict: pass, block, blocked, or not-applicable
- changed hunks and adjacent paths inspected
- bug classes inspected and any intentionally skipped as not applicable
- findings using the main `code-review` Finding Standard
