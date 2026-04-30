---
name: github-cli
description: Use for GitHub operations through gh CLI.
---

# GitHub CLI

This skill owns GitHub transport mechanics only. Reason about feedback with
`feedback-address`; reason about CI failures with the debugging and verification
owners.

## Workflow

1. Run `gh auth status` before relying on GitHub reads.
2. Resolve repository and item explicitly: owner/repo plus PR, issue, run, or
   branch.
3. Prefer read-only commands first:
   - `gh pr view`
   - `gh pr diff`
   - `gh issue view`
   - `gh run view`
   - `gh api graphql`
4. For PR review comments, use thread-aware GraphQL or an equivalent `gh api`
   read when resolved/outdated state matters. Flat comment lists are not enough
   for review-thread decisions.
5. Do not write to GitHub unless the user explicitly asks for that write.

## Writes Requiring Explicit User Instruction

- create, update, or delete comments
- submit reviews or approvals
- resolve or unresolve review threads
- request reviewers
- add or remove labels
- close, reopen, merge, or mark draft/ready
- push branches or tags
