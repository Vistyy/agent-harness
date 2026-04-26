# Read-Only Diagnostics And Triage

Use these recipes when the parent thread already knows what GitHub question it needs answered.

## CI Failure Triage

1. Confirm auth and repository scope.
   - `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh auth status`
   - `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh pr view <number> --json url,headRefName,baseRefName,statusCheckRollup`
2. Inspect failing checks and runs.
   - `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh pr checks <number>`
   - `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh run list --branch <branch> --limit 5`
   - `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh run view <run-id> --log-failed`
3. Return the failing job, the failing step, the likely local verification command, and the user-owned next action.

## PR Comment Triage

1. Inspect the PR summary and comments without replying.
   - `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh pr view <number> --comments`
   - `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh pr view <number> --json url,reviewDecision,reviews,latestReviews`
2. When line comments need more detail, use a GET-only API call.
   - `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh api repos/<owner>/<repo>/pulls/<number>/comments`
3. Group findings by theme, identify which are already addressed locally, and leave reply/resolve actions to the user.

## Related Context Search

- `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh search prs --owner <owner> --repo <repo> <terms>`
- `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh search issues --owner <owner> --repo <repo> <terms>`
- `GH_TOKEN="${GITHUB_PAT_TOKEN}" gh api repos/<owner>/<repo>/commits/<sha>`

## Gotchas

- Do not switch to bare `gh`; always map `GH_TOKEN` explicitly.
- Do not escalate into PR mutation just because a comment is obviously actionable.
- Prefer a short triage summary over dumping raw logs when the user needs a decision, not the entire run transcript.