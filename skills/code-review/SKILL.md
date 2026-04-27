---
name: code-review
description: "Use for separate isolated review of implemented changes after local verification, or when closeout requires final separate review."
---

# Code Review

Separate full review. Not in-thread `quality_guard`.

Use when:
- user asks for review,
- final separate breadth-first review is required before closeout.

Use `final_reviewer` by default for subagent-backed closeout review. Do not use
`quality_guard` for this gate.

Write terse. This skill keeps the isolated-review posture and report shape only.
Owner docs and review lenses carry the doctrine.

## Owner Routing

- Shared review doctrine: `references/review-governance.md`
- Simplicity lens: `../code-simplicity/SKILL.md`
- Adversarial lens: `../adversarial-review/SKILL.md`
- Structural trigger handling: `../system-boundary-architecture/SKILL.md`

## Rules

- Use fresh isolated context. Do not inherit old clean impressions.
- Treat `quality_guard` approvals as implementation-loop history, not final
  approval.
- Cite exact `file/path:line` for every finding.
- Keep severity explicit and ordered.
- Load the owner docs and review lenses that the slice actually needs.
- Assume checks already ran unless user asked to run more.
- No code edits.

## Process

1. Resolve base branch and diff range. Ask only if ambiguous.
2. Load the owner docs and lenses needed for the slice.
3. List changed files and needed task/wave anchors.
4. Inspect the slice with skeptical posture. Try to falsify claims, not confirm vibes.
5. Report all material findings. Do not stop at first blocker.

## Output

### Review Summary

- Base branch: `<name>`
- Diff range: `<merge-base>...HEAD`
- Changed files: `N`
- Wave brief: `<path | none>`
- Wave packet: `<path | none>`
- Breadth verdict: `<coverage sufficient | concentrated risk in ...>`
- Stable to extend: `<yes | no | limited exception with durable deferral>`

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

### Open Questions

Only blocking questions. Else: `None.`
