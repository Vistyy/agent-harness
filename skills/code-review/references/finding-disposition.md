# Finding Disposition

Disposition lens for pre-existing bad code, outside-scope defects, accepted
temporary debt, unresolved findings, and ambiguous current-scope ownership.

Pre-existing bad code is evidence, not automatic scope. Classify every material
issue discovered during review.

## Dispositions

Use exactly one disposition:

- `current-scope blocker`: the patch depends on it, touches the owner, worsens
  it, normalizes it, copies it, blesses it in tests/docs, makes the objective
  fail, or makes future cleanup materially harder
- `separate debt`: real issue, outside the touched owner/interface, not worsened
  by the patch, and fixing it now would materially expand scope or risk
- `accepted temporary debt`: current-scope issue explicitly accepted by the user
  with owner, risk, removal condition, and backlog link
- `no-change`: invalid, speculative, intentional, taste-only, or no concrete
  affected behavior/owner can be named

Current-scope blockers cannot be moved to backlog merely to approve the branch.
Separate debt must include owner, risk, next action, and why it is outside the
binding objective.

Accepted temporary debt requires explicit user acceptance, owner, risk, removal
condition, and backlog or durable tracking link. Without all of those, it
remains a current-scope blocker.

## Output

Report:

- each material finding and disposition
- owner, risk, next action, and current-scope reason
- whether any disposition blocks approval
