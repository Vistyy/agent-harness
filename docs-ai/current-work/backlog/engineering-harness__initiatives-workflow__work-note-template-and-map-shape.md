# Backlog Entry: engineering-harness/initiatives-workflow/work-note-template-and-map-shape

## Metadata

- status: `open`
- owner: `initiatives-workflow`
- bucket: `discovered separate debt`
- location: `skills/initiatives-workflow/`

## Problem

Budgeat's Lane 1A planning cleanup exposed reusable initiatives-workflow
guidance that should live in the global harness rather than inside a
project-local delivery map:

- visible map items should be terse linked queue entries, not heading-level
  mini-briefs,
- durable item memory should use
  `docs-ai/docs/initiatives/work-notes/<item-id>.md`,
- work notes should state that they are memory, not authority, without adding a
  separate local status field,
- acceptance-style anchors in memory notes should be expressed as discovery
  recheck points unless they are actual delivery acceptance criteria owned by
  the executing workflow.

## Next Action

Refine `$initiatives-workflow` assets and instructions so the work-note
template, delivery-map examples, and durable-context guidance make this shape
obvious for every project overlay.
