# Touched-Test Gate

Owner for changed persistent test file dispositions, invalid reason codes,
`required-proof`, `durable-gain`, new-test admission, and keep/shrink/rewrite/delete
remediation.

## Hard Gate

For every changed persistent test file in the diff:

- record exactly one row:
  `<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`
- `keep` is allowed only when the row has `none`
- `shrink`, `rewrite`, and `delete` require at least one invalid reason code
- if any invalid reason code applies, `keep` is forbidden
- `better than before`, `moved to the right owner`, helper extraction,
  explanation, or reviewer preference do not override this gate
- review approval is invalid if any changed persistent test file lacks a row or
  keeps any invalid reason code
- in addition to the row gate, each changed persistent test file must satisfy
  at least one of these:
  1. `required-proof`: the file is required to prove a changed durable
     boundary or changed regression target in the same slice, no existing
     same-layer or lower-layer proof already covers that changed boundary or
     target, and the changed file rejects one named regression introduced by
     that change
  2. `durable-gain`: for the same originally owned durable regression target
     previously represented by that file, the change produces an allowed
     durable gain

Allowed durable gains are limited to:
- `stronger-proof`: strictly stronger surviving proof of the same target
- `lower-layer-replacement`: replacement of a higher-layer persistent proof
  with an equally strong or stronger lower-layer proof that reduces higher-layer
  persistent-test surface
- `smaller-surface`: fewer persistent tests or files for the same target and
  same-or-stronger surviving proof
- `reason-code-removal`: removal of one or more invalid reason codes from the
  owned persistent-test slice

Re-labelling the contract does not count as a changed regression target or as a
durable gain. Pure helper extraction, parameter reshaping, file moves,
fixture/support churn, or other reorganization that leaves regression target,
strongest surviving proof, proof layer, and persistent-test surface unchanged is
invalid.

For a new persistent test:
- add it only when a durable boundary changed, no existing same-layer or
  lower-layer proof already covers that boundary, and the new test rejects one
  named regression
- otherwise do not add it

## Invalid Reason Codes

Any one of these makes `keep` invalid:

- `wrong-layer`: a lower owner can prove the same regression
- `implementation-coupled`: proves internals, private symbol names, private
  dependency wiring, private call/body shape, parsed production source
  structure, or refactor shape instead of behavior or durable public boundary
- `file-text-assertion`: proves source/file text, token presence or absence, or
  text mirrors instead of contract output, shipped artifact text, or a named
  architecture boundary surface
- `policy-mirroring`: duplicates another owner's inventory, metadata, or
  denylist instead of generated, loaded, or runtime behavior
- `mock-choreography`: proves call wiring more than behavior
- `snapshot-abuse`: broad snapshot or golden as primary proof
- `overscoped`: file covers more than one owner boundary or feature family
- `low-signal-assertion`: the file contains no assertion stronger than
  status-only, presence-only, call-count-only, or did-not-crash proof
- `exact-string-noncontract`: incidental wording treated as contract
- `non-hermetic`: depends on ambient machine, time, network, or shared state
- `order-dependent`: outcome depends on suite order or leaked state
- `flaky`: outcome is unstable for the same code
- `redundant`: adds no independent regression signal
- `assertion-thin`: file has more tests than behavior assertions
- `giant-suite`: file exceeds `300` non-comment lines or `15` tests
- `wait-heavy`: file uses more than `2` waits, settles, polls, or retry loops
- `runner-heavy`: subprocess, browser, container, or full runtime without a
  boundary reason

## Touched-Test Remediation

For each changed persistent test file, choose one:
- `keep`
- `shrink`
- `rewrite`
- `delete`

Reason codes:
- `wrong-layer`
- `implementation-coupled`
- `file-text-assertion`
- `policy-mirroring`
- `mock-choreography`
- `snapshot-abuse`
- `overscoped`
- `low-signal-assertion`
- `exact-string-noncontract`
- `non-hermetic`
- `order-dependent`
- `flaky`
- `redundant`
- `assertion-thin`
- `giant-suite`
- `wait-heavy`
- `runner-heavy`
- `valuable-high-layer`
- `benchmark-good-fit`

Defaults:
- no real regression protected -> delete
- behavior belongs lower -> move down
- high layer still matters -> shrink to minimum durable surface
- if a test can pass without the current action proving a fresh effect ->
  rewrite or delete
- any invalid reason code -> `keep` is forbidden
