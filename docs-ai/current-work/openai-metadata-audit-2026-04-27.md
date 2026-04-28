# OpenAI Metadata Audit - 2026-04-27

Source report:
- `.tmp/harness-openai-metadata.tsv`

Validation command:
- `uv run python scripts/validate_harness.py --openai-metadata-report .tmp/harness-openai-metadata.tsv`

| Skill | Metadata path | Disposition | Changed file | Reason |
|---|---|---|---|---|
| adversarial-review | `skills/adversarial-review/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| code-review | `skills/code-review/agents/openai.yaml` | changed | `skills/code-review/agents/openai.yaml` | Made user-requested review explicit in the default prompt. |
| code-simplicity | `skills/code-simplicity/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| documentation-stewardship | `skills/documentation-stewardship/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| executing-plans | `skills/executing-plans/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| flutter-expert | `skills/flutter-expert/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| initiatives-workflow | `skills/initiatives-workflow/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| just-recipe-routing | `skills/just-recipe-routing/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| mobile-design | `skills/mobile-design/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| mobileapp-testing | `skills/mobileapp-testing/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| planning-intake | `skills/planning-intake/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| review-address | `skills/review-address/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| subagent-orchestration | `skills/subagent-orchestration/agents/openai.yaml` | changed | `skills/subagent-orchestration/agents/openai.yaml` | Made automatic subagent invocation/routing explicit in the default prompt. |
| svelte-code-writer | `skills/svelte-code-writer/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| svelte-core-bestpractices | `skills/svelte-core-bestpractices/agents/openai.yaml` | changed | `skills/svelte-core-bestpractices/agents/openai.yaml` | Shortened `short_description` to satisfy 25-64 character metadata constraint while preserving Svelte posture trigger. |
| systematic-debugging | `skills/systematic-debugging/agents/openai.yaml` | changed | `skills/systematic-debugging/agents/openai.yaml` | Expanded prompt trigger beyond bugs/test failures to failing checks, build failures, performance issues, and unexpected behavior. |
| tailwind-design-system | `skills/tailwind-design-system/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| test-driven-development | `skills/test-driven-development/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| testing-best-practices | `skills/testing-best-practices/agents/openai.yaml` | changed | `skills/testing-best-practices/agents/openai.yaml` | Added exact `$testing-best-practices` invocation to `default_prompt` while preserving testing-doctrine trigger. |
| user-apps-design | `skills/user-apps-design/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| uv | `skills/uv/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| verification-before-completion | `skills/verification-before-completion/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| wave-autopilot | `skills/wave-autopilot/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| webapp-testing | `skills/webapp-testing/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
| workflow-feedback | `skills/workflow-feedback/agents/openai.yaml` | added | `skills/workflow-feedback/agents/openai.yaml` | Broad trigger is intentional for ambient workflow/process issues; body is lean and routes durable promotion to governance. |
| writing-plans | `skills/writing-plans/agents/openai.yaml` | no-change | none | Matches current trigger/scope. |
