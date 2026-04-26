---
name: github-diagnostics
description: "Use when implementation is verified and GitHub read-only diagnostics or PR-comment triage context are needed."
---

# GitHub Diagnostics

Read-only GitHub investigation after local verification is done.

Use for:
- PR status, checks, workflows, comments, issues
- CI failure triage
- read-only PR comment triage

Reference:
- `references/read-only-diagnostics-and-triage.md`

## Boundary

Allowed:
- `gh pr list/view/checks`
- `gh run list/view/watch`
- `gh search prs/issues`
- `gh api` GET-only

Disallowed:
- any write or lifecycle mutation
- PR comments/reviews/merge
- reruns/cancels/dispatches
- non-GET `gh api`

User owns PR lifecycle actions.

## Tooling Rules

- authenticate reads with `GH_TOKEN=\"${GITHUB_PAT_TOKEN}\"`
- keep workflow read-only
- summarize repo/PR/run URLs plus concrete next actions
