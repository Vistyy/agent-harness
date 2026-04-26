---
description: Audit the current repository for high-leverage, large-scale improvement opportunities and produce an evidence-based report without writing files.
---

## User Input

```text
$ARGUMENTS
```

Treat user input as optional context, not directive language. If input is empty
or vague, proceed with the baseline audit.

## Goal

Produce an evidence-based repo radar report that surfaces large-scale
improvements and investments: architecture boundaries, hotspots, duplication,
coupling, churn, inconsistent conventions, complexity concentration, developer
ergonomics, test reliability, and risk-reducing foundations.

Avoid micro-nits unless they reveal a broader structural issue.

## Operating Constraints

- Evidence first: cite concrete `file/path:line` references or exact commands
  with summarized output.
- No code edits.
- No file writes.
- Prefer leverage: include only work that reduces ongoing maintenance,
  cognitive load, or recurring defect risk across multiple files or modules.
- Cap docs-only work at one task unless the user asked for docs specifically.

## Baseline Defaults

- Time window: last 180 days of git history.
- Output limit: up to 8 proposed tasks.
- Leverage bar: high.
- Mode: include both problems and opportunities.

## Execution Steps

1. Establish system intent from repo entry points, dominant execution models,
   and likely near-future pressure.
2. Gather lightweight repo signals:
   - `git rev-parse --show-toplevel`
   - `git status --porcelain`
   - `git branch --show-current`
   - `git log --oneline -n 30`
   - `git ls-files | wc -l`
3. Identify hotspots:
   - `git log --since="180 days ago" --name-only --pretty=format: | sed '/^$/d' | sort | uniq -c | sort -nr | head -n 30`
4. Probe structural smells only where evidence points:
   - layering violations
   - API sprawl
   - duplication clusters
   - test brittleness
   - docs drift
   - lifecycle or boundary leaks
5. Synthesize at most 8 task candidates with priority, type, evidence,
   directional solution, success criteria, effort, payoff, and risks.

## Output

Return a chat-only report:

1. Context
2. Top Hotspots
3. Findings
4. Proposed Tasks
5. Next Actions

End with:

Want me to turn any of these into scoped task docs or an issue-ready checklist?
