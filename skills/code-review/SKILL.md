---
name: code-review
description: "Review code or repository changes ruthlessly for bugs, quality regressions, objective fit, proof validity, maintainability, changed state, and final repo health. Use when the user asks for review or before claiming non-trivial work complete. Use this skill for always-on review doctrine, findings, and verdicts only; role prompts and handoffs own reference selection."
---

# Code Review

Owns always-on review doctrine, finding standards, and report shape.
`../solution-shaping/SKILL.md` owns review timing, the binding objective, valid
slice shape, and whether a finding changes scope.
`../verify-work/SKILL.md` owns proof selection. Reviewers may reject invalid
proof; they do not replace runtime, design, security, or test owners.

## Contract

Review is a blocking gate, not encouragement. A reviewer is expected to falsify
the parent story and find real defects.

Plans, work notes, delivery maps, summaries, previous approvals, and parent
claims are hypotheses. Code, owner docs, tests, runtime topology, data shape,
diffs, proof artifacts, and repository state are evidence.

For non-trivial work, approval is binary: every reference selected by the
caller, role prompt, or handoff must be applied deeply enough for the claim. If
required context is skipped, uncertain, or impossible from available context,
return `BLOCKED` or `BLOCK`, not approval.

Valid verdicts:

- `APPROVE`: the selected review scope passed, with no
  unresolved current-scope findings.
- `BLOCK`: the review found an actionable current-scope issue, invalid proof,
  incomplete objective coverage, or unclassified material finding.
- `BLOCKED`: required authority, context, changed surface, proof artifacts, or
  repo access is missing, so the reviewer cannot honestly judge the claim.

Diff-only approval is invalid for non-trivial work. Plan-compliance approval is
invalid. Test-pass approval is invalid.

## Always-On Review Setup

Before trusting the diff or parent story, reconstruct the review target:

- binding objective and user-accepted reductions
- expected finished repo state that would make the objective true
- authority inspected: owner docs, code paths, runtime topology, data/state
  shape, tests, changed surface, adjacent owner/interface paths, and proof
  artifacts treated as authority
- plan/note interpretation verdict
- known findings, finding dispositions, accepted temporary debt, and residual
  work

Do not inherit the finished state from the diff, branch history, backlog
wording, PR status, previous completion claims, or parent handoff. An internally
consistent plan that implements the wrong shape is `BLOCK`.

Use `../solution-shaping/SKILL.md` and its review lenses for non-trivial review.
Unassessed current-scope lens impact blocks approval.

## Finding Standard

Prefer fewer high-confidence findings over many weak comments. A finding is
valid only when it is concrete, actionable, and useful to the author.

Each finding must include:

- severity: `P0`, `P1`, `P2`, or `P3`
- confidence: `high`, `medium`, or `low`
- exact location: `file/path:line`
- current-scope reason: why this blocks the reviewed objective or approved
  scope
- impact: the failure mode, affected path/data/user, and when it happens
- required fix: the smallest owner-correct repair, not just a symptom patch
- disposition: fixed, current-scope blocker, separate debt, accepted temporary
  debt, no-change, or blocked

Severity guide:

- `P0`: must stop release immediately; critical security, data loss,
  corruption, irreversible migration/deployment breakage, or broad outage.
- `P1`: blocks the objective or normal-use correctness, security, reliability,
  data integrity, migration, or recovery path.
- `P2`: real current-scope bug or quality regression in a plausible edge path,
  secondary workflow, admin/observability path, or maintainability surface.
- `P3`: lower-severity current-scope cleanup or structural concern that should
  be fixed before approval because it will make the code harder to own.

Unclassified material findings block approval. A `NON-BLOCKING` observation is
valid only for separate debt or explicitly accepted temporary debt.

## Reference Index

Reference files are optional review lenses selected by the caller, role prompt,
or handoff before applying this skill. They are not activation rules.

- `references/patch-native-bug-hunt.md`: changed-surface bug finding.
- `references/structural-quality.md`: maintainability, abstraction, ownership,
  and simplification review.
- `references/objective-proof-closeout.md`: objective coverage, proof validity,
  cleanup, repo health, and closeout review.
- `references/finding-disposition.md`: current-scope, separate debt, accepted
  temporary debt, and no-change classification.

## Method

- Stay read-only.
- Use fresh context.
- Inspect the diff, changed files, adjacent owner/interface paths, tests, docs,
  proof artifacts, generated artifacts, and active finding ledger needed to
  judge the claim.
- Apply selected references only. Do not treat the reference index itself as an
  activation rule.
- If no findings remain, state which bug classes and quality classes were
  inspected and why the reviewed scope was sufficient.

## Output

Report:

- verdict: `APPROVE`, `BLOCK`, or `BLOCKED`
- binding objective and accepted reductions
- expected finished repo state
- authority inspected
- reviewed scope and why it is sufficient or insufficient
- plan/note interpretation verdict
- selected references and verdict for each
- findings with exact location, impact, severity, confidence, required fix, and
  disposition
- remaining required work or `none`
