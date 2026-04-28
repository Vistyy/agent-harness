# Skill Evaluation

Use this when a skill needs behavioral regression coverage beyond static
harness validation.

## Default Posture

Start report-only and lightweight. Do not add model-running evals to the
required quality gate until the suite is stable, cheap enough, and demonstrably
catches regressions that static validation misses.

Prefer this correction order:

1. static validation in `../../../scripts/validate_harness.py`
2. deterministic fixture tests for skill files, metadata, references, and
   adapter prompts
3. small behavioral eval prompt set
4. trace/artifact checks from an agent run
5. structured rubric grading only for qualitative behavior

## Eval Shape

A useful skill eval has:

- prompt or task fixture
- expected trigger posture: `must-trigger`, `must-not-trigger`, or
  `explicit-only`
- expected process events, such as skill invocation, command choice, subagent
  role, or file writes
- expected artifacts or final output shape
- deterministic checks first
- optional structured rubric for judgment-heavy conventions

Keep prompt sets small. Start with `10-20` cases for a high-risk skill:

- explicit invocation
- implicit invocation through the description trigger
- realistic noisy/contextual invocation
- adjacent negative control that should not invoke the skill
- regression case from a real workflow-feedback entry or review finding

## Deterministic Checks

Prefer checks that are cheap and explainable:

- selected skill name or trace event is present
- expected command ran, or forbidden command did not run
- expected file exists or no unexpected files were created
- required subagent role was invoked
- required validation or quality gate ran
- output is valid JSON or matches a schema
- command count or token usage stays below a loose ceiling

Use model/rubric grading only when deterministic checks cannot express the
behavior, such as prose quality, instruction fidelity, or design/style
conventions. Rubric output must be structured so it can be compared over time.

## Candidate Harness Evals

Good first eval candidates:

- `subagent-orchestration`: prompts that require `planning_critic`,
  `quality_guard`, or `final_reviewer`; check named role invocation.
- `workflow-feedback`: prompt with a recurring process issue; check ledger
  entry shape and avoid product-bug capture.
- `work-routing`: direct/small-bounded/standalone-plan/wave examples; check
  route classification.
- `verification-before-completion`: completion claim without fresh proof; check
  refusal to claim done.

## Source Notes

- OpenAI's skill-eval guidance recommends defining success first, using small
  prompt sets, capturing agent traces/artifacts, applying deterministic checks,
  and adding structured rubric grading only where rules fall short:
  `https://developers.openai.com/blog/eval-skills`
- General eval guidance favors objective, metrics, datasets, and continuous
  comparison; for agents, evaluate tool choice, handoff accuracy, and edge
  cases where nondeterminism enters:
  `https://developers.openai.com/api/docs/guides/evaluation-best-practices`
