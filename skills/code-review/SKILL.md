---
name: code-review
description: "Use when the user asks for code review or when verified implementation requires final isolated closeout review."
---

# Code Review

Separate review with fresh context and breadth-first skepticism.

Use `final_reviewer` by default for subagent-backed closeout review.

Write terse. Review governance owns approval semantics, review modes, and issue
disposition.

## Review Inputs

- Read `references/review-governance.md` when review governance, report shape,
  verdict semantics, or closeout approval rules matter.
- Simplicity gate: `../code-simplicity/SKILL.md`
- Structural trigger handling: `../system-boundary-architecture/SKILL.md`

## Rules

- Use fresh isolated context. Do not inherit old clean impressions.
- Treat `quality_guard` approvals as implementation-loop history.
- Load the owner docs and review gates that the slice actually needs.
- Review against the binding objective and accepted reductions, not only the
  parent's narrowed summary.
- For non-trivial work, assess touched-component integrity through
  `code-simplicity`; diff-only approval is invalid.
- Pressure-test correctness, proof, ownership, maintainability, runtime/design
  gate coverage, stale paths, and existing authority.
- Cite exact `file/path:line` for every finding.
- Assume checks already ran unless user asked to run more.
- No code edits.

## Process

1. Resolve base branch, diff range, changed files, and task/wave anchors.
2. Load only owner docs and gates needed for the slice.
3. Try to falsify the claim against the binding objective and risky paths.
4. Report every concrete finding with disposition.

## Output

### Review Summary

- Base branch: `<name>`
- Diff range: `<merge-base>...HEAD`
- Changed files: `N`
- Wave brief: `<path | none>`
- Wave packet: `<path | none>`
- Binding objective: `<objective>`
- Accepted reductions: `<none | list>`
- Breadth verdict: `<coverage sufficient | concentrated risk in ...>`
- Touched owner/component: `<path/symbol/responsibility>`
- Approval boundary: `<owner/component approved | none>`
- Boundary sufficiency: `<why this boundary is enough | blocker>`
- Existing authority checked: `<paths/symbols/queries | not applicable>`
- Highest inspected scope: `<function | class | module | file | shared owner>`
- Touched component integrity: `<acceptable | unacceptable | not assessed>`
- Must-block signals: `<none | list>`
- Proof reviewed: `<commands/artifacts | none>`
- Accepted temporary debt backlog link: `<none | path>`
- Issue disposition: `<none | fixed | routed | tracked discovered debt | accepted temporary debt | dropped>`

### Findings

1. `[SEVERITY] title`
   - Location: `file/path:line`
   - Problem: `<what is wrong>`
   - Impact: `<what breaks>`
   - Fix: `<concrete fix>`
   - Disposition: `<fixed | routed | tracked discovered debt | accepted temporary debt | dropped>`

### Verdict

- Overall: `BLOCK | APPROVE`
- Correctness: `<pass | blockers>`
- Simplicity: `<pass | blockers>`
- Proof: `<sufficient | gaps>`
- Required `code-simplicity`: `<yes | no | not applicable>`
- Top risks: `<max 3 bullets>`

### Open Questions

Only blocking questions. Else: `None.`
