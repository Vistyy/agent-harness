# Active Control Sheet: overlay-contract-redesign

This is the active control sheet for redesigning the overlay workflow contract.
It is working state, not authority. The current objective, repo reality,
reviewer evidence, and owner skills override this note.

## Objective

- original objective: Redesign the overlay contract so agents analyze,
  plan, implement, review, and close out work deeply instead of reward-hacking
  accepted plans or shallow diffs.
- expected finished repo state: The overlay has an explicit target design for
  work-state and the simplified probe/shape/slice/execute-review/close flow,
  with concrete skill, prompt, asset, and CLI changes implemented from that
  model.
- accepted reductions: none.
- accepted deferrals: Python-specific best-practices skill is not current
  focus; revisit only if broader shaping/review gates still leave
  Python-specific failures.
- residual gaps: Follow-up reviewer convergence and final closeout remain
  before claiming the redesign fully complete.

## Current Reality

- `skills/work-memory/SKILL.md` now treats `work-memory` as the legacy skill
  name for lightweight current-work state. It owns queued items, active control
  sheets, detail notes, mechanical `work-state` CLI checks, and closeout
  disposition only.
- `skills/solution-shaping/SKILL.md` now owns the single
  probe/shape/slice/execute-review/close loop, large-change probe mode, atomic
  claims, fix-now disposition, and replan triggers.
- `skills/code-review/SKILL.md`, `skills/subagent-handoff/SKILL.md`, and the
  Codex reviewer/implementer prompts now require independent reconstruction,
  convergence verdicts, and stronger simplicity/shape review.
- `agent_harness` now exposes `work-state status` and `work-state check` as
  minimal mechanical state helpers. The legacy `memory lifecycle/cleanup`
  commands remain for per-item artifact inventory while naming migrates.
- `docs-ai/current-work/work-state-flow-map.html` visualizes the emerging
  model as one five-step flow: probe, shape, slice, execute/review, close.
  Large-change audit, atomic claims, reviewer reconstruction, and closeout
  disposition are rules inside that flow, not separate ceremonies.
- The current backlog detail for work-memory promotion/granularity is related
  but narrower than the binding objective; it has been normalized to the
  current backlog validation contract.

## Objective Coverage

- probe/shape/slice flow: implemented in `solution-shaping`.
- queued item model: implemented in `work-memory` and templates; projects may
  temporarily store inactive items under legacy work-note/backlog paths, but
  each item has one live owner and one queue-state model.
- active control sheet: implemented in `work-memory` and the active-sheet
  asset; this note now follows that structure.
- large-change probe mode: implemented as a probe mode in `solution-shaping`,
  not a separate workflow.
- decomposition adequacy: implemented through atomic repo claims and reviewer
  convergence checks.
- replan trigger: implemented in `solution-shaping`, implementer prompt,
  quality guard prompt, and final reviewer prompt.
- reviewer anti-leniency: implemented in `code-review`, `subagent-handoff`,
  and reviewer prompts.
- simplicity/shape review: implemented in `solution-shaping`, `code-review`,
  quality guard, planning critic, and implementer prompts.
- CLI defaults: implemented as `work-state status` and `work-state check`.
- Python practice skill: deferred; not current scope.

## Detail Notes

- [Workflow model](details/workflow-model.md)
- [Skill redesign](details/skill-redesign.md)
- [Python skill candidate](details/python-skill-candidate.md)

## Required Claims

- `queued-active-state model: contribution = replace backlog/work-note split
  with one queued-item model plus thin active control sheet and optional detail
  notes; owner/interface = work-memory/work-state skill and memory CLI; change
  surface = skills/work-memory, work-memory assets, agent_harness memory/CLI,
  tests; evidence path = work-state status/check, CLI tests, harness
  validation; review state = passed; cleanup/residual boundary = preserve
  legacy lifecycle/cleanup commands until
  naming migration is deliberate; status = completed`
- `probe-shape-slice contract: contribution = make the five-step flow,
  large-change probe mode, atomic claims, fix-now disposition, and replan
  triggers blocking rules; owner/interface = solution-shaping plus role
  prompts; change surface = skills/solution-shaping and adapters/codex/agents;
  evidence path = prompt readback, prompt-input assertion, planning critic;
  review state = passed; cleanup/residual boundary = proof and review
  mechanics stay in their owner skills;
  status = completed`
- `reviewer hardening: contribution = make planning_critic, quality_guard, and
  final_reviewer independently reconstruct target shape, claim boundaries,
  proof route, cleanup, and simplicity before approval; owner/interface =
  code-review, subagent-handoff, and role prompts; change surface =
  skills/code-review, skills/subagent-handoff, adapters/codex/agents; evidence
  path = prompt-input assertion and planning critic; review state = passed;
  cleanup/residual boundary = keep reviewer output concise but blocking;
  status = completed`
- `CLI gate design: contribution = keep only status/check as deterministic
  helpers and reject fake mechanical architecture judgment; owner/interface =
  agent_harness work-state CLI; change surface = agent_harness/memory.py,
  agent_harness/cli.py, tests; evidence path = CLI tests, work-state
  status/check, harness validation; review state = passed; cleanup/residual
  boundary = optional diff inventory is not implemented because it is not
  required for the accepted core workflow; status = completed`
- `closeout validation: contribution = prove the overlay redesign matches the
  accepted model, no stale work-state contradiction remains, and remaining
  work is visible; owner/interface = active control sheet plus final review;
  change surface = current-work state, final validation, reviewer follow-up;
  evidence path = work-state check/status, tests, final reviewer or code-review
  readback; review state = passed; cleanup/residual boundary = keep active
  state only while the user decides whether to iterate further or close/delete;
  status = completed`

## Discovery Findings

- `Backlog/work-note split: route = required slice; owner/interface =
  work-state; reason = duplicates inactive state and hides queue visibility;
  next action = implemented as one queued item model with legacy storage paths
  allowed during migration.`
- `Active note explosion: route = required slice; owner/interface =
  work-state; reason = one large note cannot represent distributed work
  clearly; next action = implemented as control sheet plus optional detail
  notes.`
- `Scope-size classification is unsafe: route = required slice;
  owner/interface = solution-shaping; reason = agents may label symptoms
  trivial and skip root-cause analysis; next action = implemented as probe
  evidence inside the five-step flow.`
- `Surface decomposition is unsafe: route = required slice; owner/interface =
  solution-shaping/code-review; reason = agents may split large work by domains
  or file counts without producing reviewable owner/lifecycle/proof slices;
  next action = implemented through atomic claim split/merge rules.`
- `Reliable slicing needs atomic claims: route = required slice;
  owner/interface = solution-shaping/code-review; reason = smaller slices do
  not help unless each slice owns one falsifiable repo claim end to end; next
  action = implemented in shaping and reviewer prompts.`
- `Queued scheduling needs explicit fields: route = required slice;
  owner/interface = work-state; reason = map sections currently encode
  scheduling semantics inconsistently; next action = use minimal queued fields
  with ready/waiting/deferred state and optional rank/dependency/wake-up data.`
- `Current-owner debt parked as backlog: route = required slice;
  owner/interface = solution-shaping/code-review; reason = backlog should not
  hide defects in the touched owner; next action = implemented as explicit
  fix-now rule plus queue/decision boundary.`
- `Heavy examples can confuse durable overlay contracts: route =
  rejected/no-change for durable policy, retained as generic lessons only;
  owner/interface = documentation-stewardship/overlay-governance; reason =
  project-specific examples are useful for discovery but too heavy for reusable
  doctrine; next action = keep only example-derived rules in the workflow
  model.`
- `Reviewer leniency: route = required slice; owner/interface = code-review
  and role prompts; reason = reviewers approve plausible stories instead of
  reconstructing authority; next action = implemented through independent
  reconstruction and convergence verdicts.`
- `Reviewer convergence: route = required slice; owner/interface =
  code-review/subagent-handoff/role prompts; reason = reviewers must derive
  objective, target shape, slices, proof, and cleanup from repo evidence before
  comparing with the parent story; next action = implemented and still needs
  follow-up review after P1/P2 fixes.`
- `Python practices: route = separate future work; owner/interface = possible
  Python skill or code-review reference; reason = user agreed not to focus on
  it now; next action = revisit only after broader overlay gates are hardened.`

## Evidence And Review

- evidence strategy: Keep the HTML model as discussion evidence and durable
  skill/prompt/CLI changes as the implemented contract.
- mechanical evidence: `uv run pytest tests/test_agent_harness_cli.py`;
  `uv run python scripts/validate_harness.py`; `uv run python
  adapters/codex/assert_prompt_input_agents.py --self-test`; `uv run python -m
  agent_harness.cli work-state check --repo-root .`.
- planning review: initial planning_critic returned one P1 CLI mismatch and
  one P2 stale active-state mismatch. Both have been addressed; follow-up
  planning_critic approved with convergence.
- final repo-health review: final_reviewer initially blocked stale HTML CLI
  overclaim; after correction it approved with convergence.

## Closeout

- repo-health cleanup: completed.
- discovery findings routed: all currently routed.
- required claims closed: all completed.
- remaining required work: none for merge readiness.
- memory updates: delivery map and backlog cleanup completed for current discussion state.
