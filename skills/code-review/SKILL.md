---
name: code-review
description: "Use when the user asks for code review or when verified implementation requires final isolated closeout review."
---

# Code Review

Separate full review with fresh context and breadth-first skepticism.

Use `final_reviewer` by default for subagent-backed closeout review.

Write terse. This skill keeps the isolated-review posture and report shape only.
Owner docs and review gates carry the doctrine.

## Review Inputs

- Shared review doctrine: `references/review-governance.md`
- Simplicity gate: `../code-simplicity/SKILL.md`
- Structural trigger handling: `../system-boundary-architecture/SKILL.md`

## Rules

- Use fresh isolated context. Do not inherit old clean impressions.
- Treat `quality_guard` approvals as implementation-loop history.
- Cite exact `file/path:line` for every finding.
- Keep severity explicit and ordered.
- Load the owner docs and review gates that the slice actually needs.
- For non-trivial work, diff-only review is invalid. Assess touched-component
  integrity through `code-simplicity`.
- Pressure-test realistic failure modes, hidden assumptions, invalid or stale
  inputs, retries/races, partial updates, unsafe defaults, and proof gaps.
- Assume checks already ran unless user asked to run more.
- No code edits.

## Process

1. Resolve base branch and diff range. Ask only if ambiguous.
2. Load the owner docs and gates needed for the slice.
3. List changed files and needed task/wave anchors.
4. Inspect the slice with skeptical posture. Try to falsify claims, not confirm vibes.
5. Check whether tests or runtime proof cover the actual risky path, not only
   the nominal path.
6. Report all material findings. Do not stop at first blocker.

## Output

### Review Summary

- Base branch: `<name>`
- Diff range: `<merge-base>...HEAD`
- Changed files: `N`
- Wave brief: `<path | none>`
- Wave packet: `<path | none>`
- Breadth verdict: `<coverage sufficient | concentrated risk in ...>`
- Touched owner/component: `<path/symbol/responsibility>`
- Highest inspected scope: `<function | class | module | file | shared owner>`
- Touched component integrity: `<acceptable | unacceptable | not assessed>`
- Must-block signals: `<none | list>`
- Accepted-debt backlog link: `<none | path>`

### Findings

1. `[SEVERITY] title`
   - Location: `file/path:line`
   - Problem: `<what is wrong>`
   - Impact: `<what breaks>`
   - Fix: `<concrete fix>`
   - Disposition: `Must-fix before merge` or `Follow-up (<durable artifact>)`

### Verdict

- Overall: `BLOCK | NON-BLOCKING | APPROVE`
- Correctness: `<pass | blockers>`
- Simplicity: `<pass | blockers>`
- Proof: `<sufficient | gaps>`
- Required `code-simplicity`: `<yes | no | not applicable>`
- Top risks: `<max 3 bullets>`

`NON-BLOCKING` is residual outside the binding completion claim. Never use it
as softer approval for claim-required defects, proof gaps, runtime/design gate
failures, or unresolved owner-contract violations.

### Open Questions

Only blocking questions. Else: `None.`
