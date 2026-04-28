---
name: review-address
description: Use when receiving code review feedback (user or external) and you must triage each point rigorously before any edits.
---

# Review Address

Triage first. No reflex agreement. No edits before user confirms triage.

Use `../code-review/references/review-governance.md` for disposition terms.
Apply `../code-simplicity/SKILL.md` when feedback would add helpers, layers,
fallbacks, or tactical patches around a shared ownership flaw.

## Workflow

1. Read all feedback. Do not implement yet.
2. Clarify unclear comments before partial action.
3. Build numbered issue ledger in original order.
4. Check each item against code, diff, task/wave context, repo constraints.
5. Classify each item as exactly one:
   - `Valid`
   - `Not applicable`
   - `Already addressed`
   - `By design`
6. If 2+ `Valid` items collapse to same ownership flaw, say so explicitly and
   recommend common-cause refactor before local patches.
7. For `Valid`, propose doctrine-aligned fix shape. Prefer delete or common-cause
   correction over bounded patch when bounded patch preserves wrong authority.
8. Wait for user confirmation before edits.

## Guardrails

- Review comments are hypotheses, not truth.
- Push back on suggestions that break behavior, conflict with constraints, or add junk.
- Prefer delete over speculative extension.
- `Valid` issues do not go to `Ignore/defer`.

## Output Contract

Use this shape exactly:

1. `Issue 1`, `Issue 2`, ...
   - `Severity/Disposition (reviewer): ...`
   - `Verdict: Valid | Not applicable | Already addressed | By design`
   - `Evidence: ...`
   - `Severity/Disposition (updated): ...` or `unchanged`
   - `Recommended fix shape: ...` or `None`

Then four short sections:
- `Must-fix before merge`
- `Follow-up`
- `Ignore/defer`
- `Overall verdict: BLOCK | NON-BLOCKING | APPROVE`

Rules:
- `Follow-up` needs durable artifact + why too large for current merge.
- `Ignore/defer` only for `Not applicable` or `By design`.
- Do not restate same issue twice.
- When shared cause exists, `Overall verdict` should say that tactical fixes are
  insufficient unless user explicitly chooses scoped mitigation.
