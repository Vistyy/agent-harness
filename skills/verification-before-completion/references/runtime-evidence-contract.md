# Runtime Evidence Contract

`runtime_evidence` validates a handed-off live claim and returns a verdict the
parent must honor.

## Input

- claim boundary
- runtime recipe or entrypoint
- accepted reductions and unproved boundaries
- required data/tenant/device/browser context
- artifacts or URLs to inspect

## Verdicts

- `pass`: observed behavior satisfies the claim boundary.
- `reject`: observed behavior contradicts the claim.
- `blocked`: recipe, data, environment, or claim boundary prevents proof.

`reject`, `blocked`, or interrupted proof blocks broad completion unless the
parent fixes the issue, reruns proof, or narrows the final claim.

## Output

- claim boundary covered
- runtime recipe used
- entrypoint fidelity
- actions executed
- evidence artifact paths
- relevant logs/traces or `none observed`
- behavioral verdict
- block impact for `reject` or `blocked`
- screenshot-backed UI checks when UI quality is claimed
