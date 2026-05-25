# Objective, Proof, And Closeout

Objective, proof, cleanup, and repo-health lens for final readiness, merge
readiness, completion claims, stale paths, lifecycle coverage,
runtime-visible behavior, data integrity, and residual work.

Review the implementation against the binding objective, not the diff-sized
claim.

## Blockers

Block when:

- objective coverage is incomplete or hidden behind a narrowed claim
- a blocker was patched around instead of routed back to the owner
- required behavior is implemented only through a proof-only path, test-only
  entrypoint, fixture shortcut, or local assumption that production will not use
- proof could pass while the requested production behavior is absent
- proof is weaker or narrower than the real owner, interface, lifecycle, user
  path, migration path, data-integrity path, or cross-boundary contract
- obsolete current-scope code, stale tests/docs, duplicate owners, compatibility
  bridges, flags, scripts, or generated artifacts remain without explicit
  retained purpose
- remaining required work is not visible, routed, or explicitly accepted by the
  user as a reduction or temporary debt

If runtime behavior, visual quality, migrations, data integrity, security, or
cross-boundary contracts matter, code inspection alone is not proof.

## Closeout Check

Check:

- expected finished repo state against actual repo state
- changed surface and adjacent owner/interface paths
- proof artifacts and what they would fail to catch
- stale paths, dead tests, generated artifacts, compatibility bridges, and
  proof-only entrypoints
- unresolved findings, accepted temporary debt, residual risk, and next owner

Do not approve until every concrete issue is fixed, routed, tracked, accepted by
the user as debt/reduction, or dropped as unevidenced.

## Output

Report:

- objective/proof/closeout verdict: pass, block, blocked, or not-applicable
- proof inspected and why it is sufficient or insufficient
- cleanup and residual-work disposition
- findings using the main `code-review` Finding Standard
