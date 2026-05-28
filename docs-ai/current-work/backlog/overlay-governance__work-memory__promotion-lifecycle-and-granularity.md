# Backlog Entry: `overlay-governance/work-memory/promotion-lifecycle-and-granularity`

## Metadata

- status: `open`
- owner: `work-memory`
- bucket: `discovered separate debt`
- location: `skills/work-memory`, `agent_harness/memory.py`, `../../../scripts/validate_harness.py`
- queue state: `waiting`

## Problem

The current `work-memory` contract says memory is not authority and describes
active notes, work notes, backlog details, and delivery maps, but it does not
make promotion lifecycle and note granularity hard enough to follow under
pressure.

In Budgeat Lane 1B cleanup, multiple unrelated backlog items were grouped into
one active note or broad work-note bundles. The delivery map then listed
backlog IDs inside successor notes while the original backlog detail files
remained live. That created duplicate ownership: a promoted item existed both
as backlog and as work/current state, and the memory tooling did not make the
wrong shape obvious before edits.

## Next Action

Redesign this item through the active overlay-contract work:
`docs-ai/current-work/active/overlay-contract-redesign/active-work-note.md`.
Preserve the underlying promotion/granularity problem while deciding whether
the replacement shape is a unified queued work item plus active control sheet.

## Promotion / Removal Condition

Promote when editing `work-memory`, memory lifecycle tooling, or delivery-map
sync validation. Remove when the skill contract and checks prevent copied
promotions and weak grouping from passing unnoticed.

## References

- `skills/work-memory/SKILL.md`
- `skills/work-memory/references/durable-context-contract.md`
- `agent_harness/memory.py`
- `../../../scripts/validate_harness.py`
- Budgeat Lane 1B cleanup memory failure pattern:
  promoted backlog items copied into successor notes while original backlog
  detail files remained live.
