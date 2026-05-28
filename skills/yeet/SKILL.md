---
name: "yeet"
description: "Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR with `git` and `gh`. Use when the user asks to commit, push, publish, or open a PR from the local checkout."
---

# GitHub Publish Changes

## Overview

Use this skill only when the user explicitly wants the full publish flow from the local checkout: branch setup if needed, staging, commit, push, and opening a pull request.

This workflow is CLI-first:

- Use local `git` for branch creation, staging, commit, and push.
- Use `gh` for repository discovery, authentication checks, current-branch PR discovery, and PR creation.
- Follow explicit user instructions and repo-local conventions for branch names, commit messages, PR titles, and PR bodies. Do not impose overlay-specific prefixes or labels.

## Prerequisites

- Require GitHub CLI `gh`. Check `gh --version`. If missing, ask the user to install `gh` and stop.
- Require authenticated `gh` session. Run `gh auth status`. If not authenticated, ask the user to run `gh auth login` (and re-run `gh auth status`) before continuing.
- Require a local git repository with a clean understanding of which changes belong in the PR.

## Naming

- If the user gives a branch name, commit message, PR title, or PR body format, use it.
- If the repo has documented conventions, follow them.
- If no convention is known, choose plain, descriptive names without fixed prefixes:
  - Branch: short kebab-case topic when starting from main/master/default.
  - Commit: terse imperative summary.
  - PR title: concise summary of the full diff.
- Never add `[codex]`, `codex/`, or other tool-identifying conventions unless the user or repo explicitly asks for them.

## Workflow

1. Confirm intended scope.
   - Run `git status -sb` and inspect the diff before staging.
   - If the working tree contains unrelated changes, do not default to `git add -A`. Ask the user which files belong in the PR.
2. Determine the branch strategy.
   - If on `main`, `master`, or another default branch, create a topic branch using the naming rules above.
   - Otherwise stay on the current branch.
3. Stage only the intended changes.
   - Prefer explicit file paths when the worktree is mixed.
   - Use `git add -A` only when the user has confirmed the whole worktree belongs in scope.
4. Commit tersely with the confirmed description.
5. Run the most relevant checks available if they have not already been run.
   - If checks fail due to missing dependencies or tools, install what is needed and rerun once.
6. Push with tracking: `git push -u origin $(git branch --show-current)`.
7. Open a draft PR.
   - Derive `repository_full_name` from the remote, for example by normalizing `git remote get-url origin` or by using `gh repo view --json nameWithOwner`.
   - Derive `head_branch` from `git branch --show-current`.
   - Derive `base_branch` from the user request when specified; otherwise use the remote default branch, for example via `gh repo view --json defaultBranchRef`.
   - Use `gh pr create --draft` unless the user explicitly asks for ready-for-review.
   - If the branch is being pushed from a fork or the PR target differs from the remote that was just pushed, pass the correct `--repo`, `--base`, and `--head` arguments explicitly.
   - Write the PR body to a temp file with real newlines when using CLI fallback so the markdown renders cleanly.
8. Summarize the result with branch name, commit, PR target, validation, and anything the user still needs to confirm.

## Write Safety

- Never stage unrelated user changes silently.
- Never push without confirming scope when the worktree is mixed.
- Default to a draft PR unless the user explicitly asks for a ready-for-review PR.
- If the repository does not appear to be connected to an accessible GitHub remote, stop and explain the blocker before making assumptions.

## PR Body Expectations

The PR description should use real Markdown prose and cover:

- what changed
- why it changed
- the user or developer impact
- the root cause when the PR is a fix
- the checks used to validate it
