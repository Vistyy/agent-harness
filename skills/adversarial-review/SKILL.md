---
name: adversarial-review
description: "Use for adversarial review of implemented changes when you need to pressure-test assumptions, failure modes, misuse paths, edge conditions, and hidden coupling. Apply as a reusable review lens inside either the in-thread quality-guard loop or the full isolated review."
---

Use this skill as a review lens, not as a separate approval mode.

Review for:
- hidden assumptions that only hold on happy paths,
- failure behavior and degraded-condition handling,
- invalid, missing, conflicting, or stale inputs,
- temporal ordering problems, retries, races, and partial-update states,
- boundary misuse, unexpected caller behavior, and unsafe defaults,
- cases where proofs or tests cover the nominal path but not the actual risk.

Do not edit code in this run. Produce findings only.

## Process

1. Identify the concrete contract the code claims to satisfy.
2. Enumerate how that contract can be violated in realistic non-happy-path use.
3. Check whether the implementation guards, rejects, recovers, or leaks through.
4. Check whether tests or runtime proof actually cover the risky path.
5. Report only material adversarial findings; ignore style-only concerns.

## Output

- Findings, or an explicit no-findings statement.
- Contract or assumption pressure-tested.
- Failure modes inspected.
- Residual risks or missing proof.
