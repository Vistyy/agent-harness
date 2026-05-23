# Backlog Entry: engineering-harness/overlay-governance/active-note-slice-review-loop

## Metadata

- status: `open`
- owner: `overlay-governance`
- bucket: `discovered separate debt`
- location:
  `skills/work-memory`,
  `skills/subagent-handoff`,
  `skills/solution-shaping`,
  `agents/roles.md`
- user acceptance: `not applicable`
- removal condition: `overlay guidance makes active notes operational enough
  that required slices are implemented, blocked, rejected, or backlogged with
  explicit route, and non-trivial slice drafts get quality_guard review before
  dependent work continues.`

## Problem

During Budgeat service-internal architecture hardening, the active note was
used too passively. It recorded a broad slice plan and many findings, but some
decomposed slices were left as note tail rather than implemented, explicitly
backlogged, rejected/no-change, blocked, or removed by an accepted reduction.

The practical failure was not that work memory existed. The failure was that
the note did not drive the implementation loop strongly enough:

- required slices were easy to confuse with discovery findings or future ideas;
- broad future cleanup was almost promoted as current work just because it
  should not be forgotten;
- `quality_guard` was not used mid-slice after non-trivial drafts, so later
  final review became the first serious independent check of accumulated work;
- final closeout review had to recover stale note state instead of checking a
  clean current/backlog/implemented ledger.

## Next Action

- Review whether `work-memory`, `solution-shaping`, and `subagent-handoff`
  need tighter positive guidance for active-note ledgers and routed discovery
  findings.
- Prefer a lightweight pattern over ceremony: active note as branch memory,
  required-slice ledger as resume checklist, and explicit finding routes.
- Clarify when `quality_guard` should run during a slice and how its verdict is
  reflected in active-note review state.
- Avoid adding negative legacy checks or tests for old note shapes. Use current
  structure and reviewer judgment unless a narrow mechanical invariant proves
  durable value.

## Evidence Boundary

Use recent Budgeat service-internal architecture hardening notes and reviewer
verdicts as examples. The durable fix belongs in overlay guidance only if it
improves future agent behavior without turning work memory into execution
authority.
