# Queued Work Item: python-skill-candidate

This queued item is memory, not authority. Picking it starts discovery through
`solution-shaping`; it does not authorize direct execution.

## Queue

- problem: Decide whether the overlay needs a reusable Python practice skill or a smaller code-review reference.
- queue state: `ready`
- owner or suspected owner: `overlay-governance/code-review`
- next discovery move: inspect repeated Python-specific failures and decide whether they need Python-only rules beyond `uv`, `testing-best-practices`, `code-review`, and project docs.
- reason not active now: overlay work-state redesign was the current active item; this is the next candidate.

## Starting Points

- Candidate triggers: non-trivial Python code changes, Python code-quality review, Python module-boundary design, or Python runtime/test diagnosis not already owned by project recipes.
- Avoid duplicating `uv`, `testing-best-practices`, `code-review`, or project-local architecture docs.
- Likely useful scope: command routing, simple functions/data structures before classes/frameworks, clear I/O/parsing/validation/business owners, no hidden global state, no mutable default traps, no broad exception swallowing, typed boundaries where the repo already uses typing, behavior-boundary tests, structured parsers before ad hoc strings, and no compatibility wrappers without owner/removal condition.

## Recheck During Discovery

- A generic Python style skill can become low-signal bloat.
- First check whether `code-review` simplicity/shape and `solution-shaping` owner-boundary rules already cover the failures.

## Possible Sequence

- Compare Python-specific failures against existing owner skills.
- If failures are review-only, add a focused `code-review` reference.
- If failures affect implementation routing and recurring Python mechanics, propose a small Python implementation skill with a distinct trigger.
