# Backlog Entry: harness/design-workflow/command-specialization

## Metadata

- Impact: `medium`
- Effort: `M`
- Queue bucket: `Deferred Backlog`
- status: `open`
- owner: `user-apps-design`
- created: `2026-05-05`
- removal condition: promote to a wave after the context/register contract
  lands, or close if existing owner-skill routing is sufficient.

## Problem

Impeccable improves steering through named design operations such as shape,
critique, audit, polish, harden, clarify, typeset, and layout. The current
wave does not add a harness design sub-vocabulary, so agents may still handle
design requests as broad visual polish instead of choosing the right design
operation.

## Why This Bucket

Explicitly deferred follow-up. Command specialization should consume the
design-context/register contract instead of creating a second router or copying
Impeccable's 23-command stack.

## Suggested Next Step

- Suggested target wave (if known): `harness-design-command-specialization-1`
- Dependencies/prerequisites: `harness-design-context-contract-1`
- Smallest next slice: define a small operation vocabulary inside
  `user-apps-design` and adapter handoff guidance for shape, critique, audit,
  polish, harden, and clarify without adding user-facing slash commands.
- Promotion/removal condition: promote when repeated UI work shows routing
  ambiguity; remove if the design-context contract plus existing skills gives
  enough steering precision.

## References

- Owning durable doc: `skills/user-apps-design/SKILL.md`
- Queue/backlog source: `docs-ai/current-work/delivery-map.md`
- Source wave/task: `harness-design-context-contract-1/harness/design/context-contract`
- Files/evidence: `https://impeccable.style/docs/`
