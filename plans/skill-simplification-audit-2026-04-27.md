# Skill Simplification Audit - 2026-04-27

## Purpose

Record current findings from the global harness skill audit and shape refactor
waves before editing skill content.

This is a planning artifact, not reusable doctrine.

## Durable Location Decision

Decision:

- Keep this audit under top-level `plans/` for now.

Reason:

- The harness repo currently has no `docs-ai/**` overlay.
- Creating `docs-ai/current-work/**` in the harness would import project-overlay
  workflow state into the reusable harness repository without an existing repo
  convention.
- This audit is repo-local planning state, not global reusable skill doctrine.

Constraint:

- If the harness adopts a durable planning-doc convention later, move this file
  in that migration rather than letting `plans/` silently become policy.

## Skill-Writing Doctrine Owner

Decision:

- Reusable "what makes a good harness skill" doctrine should live under
  `skills/harness-governance/`, likely as
  `skills/harness-governance/references/skill-architecture.md`.

Reason:

- `harness-governance` already owns skill architecture, reusable harness
  posture, and enforcement checks.
- `documentation-stewardship` owns source-of-truth placement, not skill authoring
  quality.
- `code-simplicity` is a review lens, not the owner for skill bundle structure.

Rule:

- Individual skills should not each restate the skill-writing doctrine. They
  should link to the harness-governance reference only when editing or reviewing
  skill architecture.

## Source Criteria

External guidance used for the audit:

- OpenAI GPT-5.5 latest-model guidance:
  <https://developers.openai.com/api/docs/guides/latest-model.md>
- OpenAI GPT-5.5 upgrade guidance:
  <https://developers.openai.com/api/docs/guides/upgrading-to-gpt-5p5.md>
- OpenAI prompt engineering guidance for coding and agentic tasks:
  <https://developers.openai.com/api/docs/guides/prompt-engineering#coding>
- OpenAI skills cookbook:
  <https://developers.openai.com/cookbook/examples/skills_in_api>
- Anthropic skill authoring best practices:
  <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
- Agent Skills best practices:
  <https://agentskills.io/skill-creation/best-practices>

Audit criteria distilled from those sources:

- `SKILL.md` is the routing and workflow entrypoint, not the full manual.
- Keep the skill discoverable: clear frontmatter, when to use, when not to use,
  how to run, expected outputs, and gotchas.
- Use progressive disclosure: move detail to directly linked references and
  tell the agent exactly when to read each one.
- Keep each skill a coherent unit. Split database-query and database-admin
  style mixes; keep one procedure per skill unless the combined workflow is
  genuinely inseparable.
- Prefer moderate detail. Exhaustive edge-case doctrine can reduce accuracy by
  making the relevant path harder to find.
- Match specificity to fragility. Use hard sequences for fragile operations;
  use principles and defaults for flexible judgment work.
- Provide defaults, not menus.
- Scripts should behave like tiny CLIs: deterministic stdout, clear failure,
  known output paths, explicit usage.
- Do not duplicate skill procedures in always-on prompts or sibling skills.
- For GPT-5.5, prefer outcome-first instructions, success criteria, allowed
  side effects, evidence rules, and output shape. Reduce detailed step-by-step
  process guidance unless the exact path matters.

## Corpus Snapshot

- Skill manifests: `29` `SKILL.md` files, `2690` total lines.
- Markdown under `skills/**`: `8533` total lines.
- Largest skill bodies:
  - `skills/planning-intake/SKILL.md`: `222` lines.
  - `skills/user-apps-design/SKILL.md`: `184` lines.
  - `skills/svelte-core-bestpractices/SKILL.md`: `178` lines.
  - `skills/subagent-orchestration/SKILL.md`: `169` lines.
  - `skills/webapp-testing/SKILL.md`: `156` lines.
- Largest references/assets:
  - `skills/testing-best-practices/references/testing-strategy.md`: `486` lines.
  - `skills/initiatives-workflow/references/initiatives-workflow.md`: `391` lines.
  - `skills/initiatives-workflow/assets/wave-execution.example.md`: `237` lines.
  - `skills/initiatives-workflow/assets/wave-execution.md`: `219` lines.
  - `skills/code-review/references/review-governance.md`: `186` lines.

No `SKILL.md` currently exceeds the common `500` line warning threshold, but
several are still too dense for fast routing because they carry multiple owners
or repeat policy owned elsewhere.

## Findings

### F-01: Duplicate Standalone Plan Policy

Severity: high.

Files:

- `skills/executing-plans/references/standalone-plans.md`
- `skills/writing-plans/references/standalone-plans.md`

Problem:

- The two files are exact duplicates after whitespace normalization.
- This violates single-source ownership and creates drift risk.

Disposition:

- Keep one canonical owner, preferably under `skills/writing-plans/references/`
  if authoring owns the plan schema, or under a neutral shared owner if both
  authoring and execution need it.
- Replace the other file with a pointer or update the consuming skill to link
  to the canonical file.

### F-02: Testing Strategy Owns Too Many Proof Domains

Severity: high.

File:

- `skills/testing-best-practices/references/testing-strategy.md`

Problem:

- The file owns touched-test remediation, proof classes, exact-string rules,
  runtime proof depth, runtime UI evidence, backend runtime claims, and CI
  posture.
- Runtime-proof sections overlap with `verification-before-completion`,
  `webapp-testing`, and `mobileapp-testing`.
- Review-governance repeats substantial parts of this doctrine.

Disposition:

- Keep durable test-layer selection, touched-test remediation, invalid reason
  codes, exact-string/source-text rules here.
- Move runtime proof escalation and runtime evidence branch coverage to
  `verification-before-completion/references/runtime-proof-escalation.md`.
- Keep UI/browser/device mechanics in web/mobile testing skills.
- Replace duplicated review rules with owner links and short gates.

### F-03: Initiatives Workflow Is Lifecycle, Packet Schema, Delegation, And Closeout

Severity: high.

File:

- `skills/initiatives-workflow/references/initiatives-workflow.md`

Problem:

- The reference mixes queue rules, backlog promotion, wave status, execution
  readiness, packet schema, delegation posture, task sizing, closeout, and
  taxonomy maintenance.
- It overlaps with `planning-intake`, `wave-autopilot`, and
  `subagent-orchestration`.

Disposition:

- Keep wave/backlog lifecycle and source-of-truth placement here.
- Move packet schema and proof-row field contract to a packet reference or
  template owner.
- Move delegation posture rules to `subagent-orchestration`.
- Keep planning readiness criteria in `planning-intake`; this file should link
  to them.

### F-04: Review Governance Repeats Testing And Boundary Doctrine

Severity: high.

File:

- `skills/code-review/references/review-governance.md`

Problem:

- The file is the right owner for approval modes and completion claims, but it
  repeats long testing invalid-pattern and boundary/typing rule sets.
- This makes review governance a second source for testing and architecture
  doctrine.

Disposition:

- Keep approval modes, review cadence, disposition language, and completion
  claim fields.
- Replace detailed testing and boundary lists with concise gates that point to
  `testing-strategy.md` and `system-boundary-architecture` references.

### F-05: Runtime Evidence Doctrine Is Split Across Four Owners

Severity: high.

Files:

- `skills/verification-before-completion/references/runtime-proof-escalation.md`
- `skills/webapp-testing/SKILL.md`
- `skills/mobileapp-testing/SKILL.md`
- `skills/webapp-testing/references/runtime-evidence-visual-verdict-contract.md`

Problem:

- Browser and mobile testing duplicate observability, design anchors, archetype
  handling, telemetry, screenshot verdicts, and report fields.
- Runtime escalation overlaps with `testing-strategy.md`.
- The visual verdict contract is web-owned by path even though mobile consumes
  it too.

Disposition:

- Create one shared runtime evidence contract under a neutral owner, likely
  `verification-before-completion/references/runtime-evidence-contract.md`.
- Keep platform-specific mechanics only in `webapp-testing` and
  `mobileapp-testing`.
- Move shared screenshot verdict vocabulary out of webapp path or rename its
  ownership explicitly.

### F-06: Planning Intake Is Over-Prescriptive For GPT-5.5-Style Prompting

Severity: medium-high.

File:

- `skills/planning-intake/SKILL.md`

Problem:

- The skill carries decision taxonomy, proof allocation, deferral policy,
  critic routing, anti-misdirection, and output paths in one entrypoint.
- It repeats simplicity and structural pressure that should route to
  `code-simplicity` and `system-boundary-architecture`.
- GPT-5.5 guidance favors outcome, success criteria, side effects, evidence,
  and stop conditions over detailed step-by-step process unless the sequence is
  fragile.

Disposition:

- Keep intake objective, user-owned versus agent-defaultable decision rules,
  blocking question format, and promotion gate.
- Link out for simplicity, proof allocation, structural boundary, and wave
  artifact schema.
- Convert long repeated questions into a compact checklist.

### F-07: Subagent Orchestration Mixes Defaults, Lifecycle, Roles, And Handoffs

Severity: medium-high.

File:

- `skills/subagent-orchestration/SKILL.md`

Problem:

- The skill owns delegation defaults, active-worker preservation, reuse rules,
  worker deltas, handoff addenda, and anti-patterns.
- Role boundaries are also represented in
  `skills/subagent-orchestration/references/coding-agent-topology.md`.
- Implementer eligibility overlaps with `initiatives-workflow`.

Disposition:

- Keep live delegation decisions and parent responsibilities in `SKILL.md`.
- Move role-specific handoff deltas and active-worker preservation into
  `coding-agent-topology.md` or one directly linked reference.
- Keep implementer eligibility in one owner and link to it.

### F-08: User Apps Design Is Strong But Too Broad

Severity: medium-high.

File:

- `skills/user-apps-design/SKILL.md`

Problem:

- The skill owns visual direction, parity, copy posture, archetypes, IA,
  runtime proof, missing-source escalation, and web route boundary stops.
- Runtime and route-boundary material should mostly route to web/mobile
  testing and system-boundary architecture.

Disposition:

- Keep product-facing UI direction, parity workflow, composition bar, and copy
  posture.
- Move runtime proof expectations to runtime-testing owners.
- Keep only short boundary-stop pointers for route/state authority.

### F-09: Mobile Design Forces Too Much Required Reading

Severity: medium.

Files:

- `skills/mobile-design/SKILL.md`
- `skills/mobile-design/mobile-design-thinking.md`
- `skills/mobile-design/touch-psychology.md`
- `skills/mobile-design/mobile-performance.md`
- `skills/mobile-design/mobile-testing.md`
- `skills/mobile-design/mobile-backend.md`
- `skills/mobile-design/platform-ios.md`
- `skills/mobile-design/platform-android.md`

Problem:

- The reference set is generally focused, but `SKILL.md` currently says several
  docs are always required.
- That makes simple mobile UI edits pay the context cost of backend,
  performance, testing, and broad design guidance.

Disposition:

- Replace always-read list with risk-triggered loading:
  touch/accessibility, platform behavior, performance, backend/offline,
  testing.
- Keep one compact preflight in `SKILL.md`.

### F-10: Svelte Core Best Practices Risks Becoming Stale Framework Docs

Severity: medium.

Files:

- `skills/svelte-core-bestpractices/SKILL.md`
- `skills/svelte-core-bestpractices/references/*.md`

Problem:

- The skill carries broad Svelte framework documentation and several local
  reference docs that can become stale.
- Some reference files are not clearly indexed from `SKILL.md`.
- Official docs lookup is already owned by `svelte-code-writer`.

Disposition:

- Keep durable repo-facing Svelte posture: runes, reactivity pitfalls, route
  ownership, and anti-patterns.
- Let `svelte-code-writer` and official docs own detailed version-sensitive
  API behavior.
- Add a direct one-level reference map for any retained local references.

### F-11: Systematic Debugging Contains Training/Evaluation Files In Runtime Bundle

Severity: medium.

Files:

- `skills/systematic-debugging/test-academic.md`
- `skills/systematic-debugging/test-pressure-1.md`
- `skills/systematic-debugging/test-pressure-2.md`
- `skills/systematic-debugging/test-pressure-3.md`
- `skills/systematic-debugging/condition-based-waiting-example.ts`
- `skills/systematic-debugging/find-polluter.sh`

Problem:

- Pressure tests and academic tests look like skill evaluation/training assets,
  not runtime guidance.
- `find-polluter.sh` is npm-specific and uses presentation noise.
- `condition-based-waiting-example.ts` references project-specific types and
  an old context.

Disposition:

- Move training/evaluation files under an explicit evaluation/examples folder
  or remove them from the installable runtime bundle if not used.
- Generalize or mark `find-polluter.sh` as example-only.
- Keep condition-based waiting as general guidance; remove project-specific
  imports from executable examples unless they are intentionally illustrative.

### F-12: Webapp Testing Helper Scripts And Examples Are Not Routed Clearly

Severity: medium.

Files:

- `skills/webapp-testing/scripts/with_server.py`
- `skills/webapp-testing/examples/console_logging.py`
- `skills/webapp-testing/examples/element_discovery.py`
- `skills/webapp-testing/examples/static_html_automation.py`

Problem:

- Scripts/examples are not surfaced clearly from `webapp-testing/SKILL.md`.
- `with_server.py` is a broad shell-command wrapper with `shell=True`; that is
  risky without explicit constraints and may conflict with project-owned
  runtime recipes.
- Examples use hardcoded paths and URLs.

Disposition:

- Either remove these as stale generic examples or explicitly mark them as
  last-resort examples.
- Prefer project-owned runtime recipes and Playwright CLI/durable specs.
- If retained, document exact safe use and limitations.

### F-13: Initiatives Workflow Scripts Are Under-Referenced

Severity: medium.

Files:

- `skills/initiatives-workflow/scripts/bootstrap_wave_docs.py`
- `skills/initiatives-workflow/scripts/current_wave_cleanup.py`
- `skills/initiatives-workflow/scripts/wave_brief_references.py`

Problem:

- `SKILL.md` only names `bootstrap_wave_docs.py`, while cleanup and reference
  scanning helpers are not surfaced.

Disposition:

- Add a small script index with when to use each helper.
- Ensure each helper acts as a tiny CLI with deterministic output and clear
  refusal behavior.

### F-14: Code Simplicity Repeats Testing Doctrine

Severity: low-medium.

File:

- `skills/code-simplicity/SKILL.md`

Problem:

- The simplicity lens repeats specific test deletion and test-value rules that
  belong to `testing-best-practices`.

Disposition:

- Keep the broad statement that tests are code and complexity candidates.
- Link detailed test remediation to `testing-best-practices`.

### F-15: Harness Governance Mixes Several Governance Concerns

Severity: low-medium.

File:

- `skills/harness-governance/SKILL.md`

Problem:

- The skill mixes operating model, overlay contract, repository posture, skill
  architecture, and enforcement check usage.

Disposition:

- Keep harness scope and skill-architecture rules in `SKILL.md`.
- Move overlay contract and repository posture to short references if they keep
  growing.

### F-16: Documentation Stewardship Is A Good Simplicity Baseline

Severity: positive finding.

Files:

- `skills/documentation-stewardship/SKILL.md`
- `skills/documentation-stewardship/references/*.md`

Observation:

- This skill is short, focused, and uses direct references.

Disposition:

- Use it as the target shape for policy-owner skills: short entrypoint, one
  clear goal, directly linked references.

### F-17: Flutter References Are Focused

Severity: positive finding.

Files:

- `skills/flutter-expert/SKILL.md`
- `skills/flutter-expert/references/*.md`

Observation:

- The references are compact and domain-specific.

Disposition:

- Leave mostly unchanged unless future mobile-design cleanup creates overlap.

## Simplicity And Terseness Assessment

Current state:

- The harness has strong doctrine, but several skills encode the same doctrine
  in multiple places instead of linking to owners.
- The biggest problem is not individual `SKILL.md` line count; it is ownership
  diffusion. A reader must reconcile overlapping rules across planning,
  review, testing, runtime evidence, and delegation.
- Several references are manuals rather than decision aids. They should be
  shorter where they merely restate another owner, and more explicitly indexed
  where detail is genuinely needed.

Instruction patterns to simplify:

- Replace repeated "two competent implementers could choose differently" text
  with one canonical planning-readiness rule and references.
- Replace repeated runtime evidence report field lists with one shared runtime
  evidence schema.
- Replace testing invalid-pattern copies in review governance with a single
  review gate linking to testing strategy.
- Replace always-read reference lists with conditional "read when" maps.
- Replace generic examples with templates tied to exact trigger conditions.
- Remove training/evaluation files from runtime skill paths unless a skill
  authoring workflow consumes them.

Target style:

- `SKILL.md`: 30-90 lines for most skills; up to 150 only when routing is
  inherently complex.
- References: one topic each, direct links from `SKILL.md`, table of contents
  for files over 100 lines.
- Scripts: one command purpose each, deterministic output, no hidden project
  assumptions.
- Cross-skill doctrine: one owner, many links.

## Proposed Waves

### Wave Dependencies

- Wave 1 must close the skill-writing doctrine owner and mechanical hygiene
  baseline before other waves edit broad skill policy.
- Wave 2 depends on Wave 1 only for the skill-writing doctrine criteria, not for
  all mechanical cleanup.
- Wave 3 depends on Wave 1's durable planning/artifact decision and Wave 2's
  proof source-of-truth map.
- Wave 4 depends on Wave 1's skill-writing doctrine owner and should not start
  before Wave 2 finishes shared runtime/proof ownership.

### Wave 1: Skill Architecture Doctrine And Mechanical Hygiene

Goal:

- Establish the harness skill-writing criteria and remove obvious
  single-source/script hygiene problems.

Scope:

- Create the canonical skill-writing doctrine reference under
  `skills/harness-governance/references/`.
- Canonicalize duplicate standalone plan policy.
- Add or update script indexes for initiatives workflow, testing audit, and web
  testing helpers.
- Decide whether stale examples/training files stay, move, or are removed.
- Decide whether duplicate/orphan helper detection becomes a durable harness
  check or stays a one-off audit.

Closed decisions:

- Standalone plan policy canonical owner:
  `skills/writing-plans/references/standalone-plans.md`.
- `skills/executing-plans/references/standalone-plans.md`: delete the duplicate
  body and update consumers to link to the writing-plans owner.
- `initiatives-workflow/scripts/*.py`: retain all three helpers and index them
  from `skills/initiatives-workflow/SKILL.md`:
  - `bootstrap_wave_docs.py`: discovery-required brief scaffold.
  - `wave_brief_references.py`: exact wave-brief reference scan during closeout.
  - `current_wave_cleanup.py`: dry-run/execute cleanup of current-work wave
    directory after closeout prerequisites are satisfied.
- `testing-best-practices/scripts/test_suite_audit.py`: retain and index from
  `skills/testing-best-practices/SKILL.md` for corpus-wide audit inventory.
- `webapp-testing/scripts/with_server.py`: retain only as a last-resort helper
  for trusted local commands when no project runtime recipe exists; index with
  that constraint.
- `webapp-testing/examples/*.py`: retain as last-resort examples only, with
  explicit warning that durable specs, Playwright CLI, and project runtime
  recipes take precedence.
- `systematic-debugging/test-pressure-*` and `test-academic.md`: retain in Wave
  1 as evaluation-only assets and index from `SKILL.md`; Wave 4 may move or
  remove them.
- `systematic-debugging/condition-based-waiting-example.ts`: retain as an
  illustrative example, not a copy-paste utility, because it contains
  project-shaped imports.
- `systematic-debugging/find-polluter.sh`: retain as an npm-specific example
  helper and index with that limitation.
- Durable duplicate/orphan helper checker: not added in Wave 1. Wave 1 uses
  explicit proof commands below; a durable checker should be added only after
  the first cleanup establishes stable patterns worth enforcing.

Primary files:

- `skills/harness-governance/SKILL.md`
- `skills/harness-governance/references/skill-architecture.md` (new)
- `skills/executing-plans/references/standalone-plans.md`
- `skills/writing-plans/references/standalone-plans.md`
- `skills/initiatives-workflow/SKILL.md`
- `skills/testing-best-practices/SKILL.md`
- `skills/webapp-testing/SKILL.md`
- `skills/systematic-debugging/**`

Proof:

- `skill-architecture.md` names routing, progressive disclosure, reference,
  script, asset, and example rules without copying external docs.
- Duplicate standalone-plan policy has exactly one canonical owner; the other
  path is removed or reduced to a pointer.
- Retained scripts/examples have explicit triggers in owning `SKILL.md` or an
  intentional examples/evaluation location.
- If a checker is added, it must reject at least one representative duplicate
  or orphan-helper fixture and pass after cleanup.
- Harness validation passes.

Exact proof commands:

```bash
uv run python scripts/validate_harness.py
rg -n "Owner for standalone implementation plans" skills
rg -n "standalone-plan policy|standalone-plan owner|standalone-plans.md" skills/executing-plans skills/writing-plans skills/subagent-orchestration
rg -n "bootstrap_wave_docs|wave_brief_references|current_wave_cleanup|test_suite_audit|with_server.py|console_logging.py|element_discovery.py|static_html_automation.py|test-pressure|test-academic|condition-based-waiting-example|find-polluter.sh" skills/*/SKILL.md
```

Expected evidence:

- Harness validation passes.
- The full standalone-plan policy owner phrase appears in only one canonical
  policy body.
- Executing-plan and subagent references point to the writing-plans owner.
- Every retained Wave 1 helper/example/evaluation asset appears in an owning
  `SKILL.md` with a trigger or limitation.

Counterfactual regressions:

- Two identical standalone-plan policy bodies can survive.
- A helper script can remain in a skill directory without any owning trigger or
  explicit example/evaluation disposition.
- Skill-writing doctrine can be introduced without a canonical owner reference.

### Wave 2: Proof, Review, And Runtime Evidence Ownership

Goal:

- Collapse duplicated proof/review/runtime doctrine into one-owner references.

Source-of-truth map:

- Persistent test validity, touched-test remediation, layer selection,
  exact-string/source-text rules: `testing-strategy.md`.
- Runtime proof escalation, runtime evidence minimum, branch coverage, and
  artifact/evidence placement: `verification-before-completion` references.
- Browser proof mechanics: `webapp-testing`.
- Mobile/device proof mechanics, including emulator/device posture:
  `mobileapp-testing`.
- Shared screenshot/visual runtime verdict vocabulary: neutral
  `verification-before-completion` reference, not web-owned path.
- Review approval/disposition/completion fields: `review-governance.md`.
- CI/quality-tier semantics: `quality-gate-selection.md`.

Scope:

- Split runtime-proof doctrine out of `testing-strategy.md`.
- Slim `review-governance.md` so it owns approval/disposition/completion, not
  detailed testing and boundary doctrine.
- Create or rename one shared runtime evidence contract.
- Trim web/mobile testing to platform mechanics.

Primary files:

- `skills/testing-best-practices/references/testing-strategy.md`
- `skills/code-review/references/review-governance.md`
- `skills/verification-before-completion/references/runtime-proof-escalation.md`
- `skills/webapp-testing/SKILL.md`
- `skills/mobileapp-testing/SKILL.md`
- `skills/webapp-testing/references/runtime-evidence-visual-verdict-contract.md`

Proof:

- Diff review confirms each durable rule has one owner.
- Existing harness validation passes.
- Targeted grep confirms removed duplicated phrases now appear in one owner or
  as short links only.

Counterfactual regressions:

- Runtime proof requirements still live in both testing strategy and
  verification/runtime references.
- Review governance still carries detailed testing invalid-pattern or boundary
  doctrine instead of linking to owners.
- Mobile testing still links to a web-owned visual verdict contract.

### Wave 3: Workflow, Planning, And Delegation Simplification

Goal:

- Separate wave lifecycle, packet schema, planning readiness, and delegation
  boundaries.

Scope:

- Slim `planning-intake` to intake decisions and promotion gate.
- Split `initiatives-workflow` lifecycle from packet schema/delegation details.
- Slim `subagent-orchestration` to live delegation decisions and route role
  boundary details to `coding-agent-topology.md`.
- Align `wave-autopilot` with the new owners.

Primary files:

- `skills/planning-intake/SKILL.md`
- `skills/initiatives-workflow/references/initiatives-workflow.md`
- `skills/initiatives-workflow/assets/wave-execution.md`
- `skills/subagent-orchestration/SKILL.md`
- `skills/subagent-orchestration/references/coding-agent-topology.md`
- `skills/wave-autopilot/SKILL.md`

Proof:

- One owner each for lifecycle, packet schema, planning readiness, delegation
  role vocabulary, and execution workflow.
- Planning artifact examples still validate against the packet contract.

Counterfactual regressions:

- `initiatives-workflow`, `planning-intake`, and `subagent-orchestration` all
  continue to define implementer eligibility in parallel.
- A future wave packet can satisfy one workflow doc while violating another.
- Two implementers can choose different locations for packet schema or planning
  readiness rules.

### Wave 4: Domain Skill Slimdown

Goal:

- Make domain skills lighter, more conditional, and less stale-prone.

Scope:

- Convert mobile-design required reading into risk-triggered reference loading.
- Slim Svelte best-practices to repo posture and route version-sensitive detail
  to official docs through `svelte-code-writer`.
- Slim user-apps-design by moving proof and boundary material to owners.
- Decide final home for systematic-debugging evaluation/training assets.

Primary files:

- `skills/mobile-design/SKILL.md`
- `skills/mobile-design/*.md`
- `skills/svelte-core-bestpractices/SKILL.md`
- `skills/svelte-core-bestpractices/references/*.md`
- `skills/user-apps-design/SKILL.md`
- `skills/systematic-debugging/**`

Proof:

- Each domain skill has a conditional reference map.
- No retained domain skill tries to own runtime proof, planning gates, or
  unrelated framework documentation.

Per-domain target dispositions:

- `mobile-design`: slim `SKILL.md`, keep references, convert always-read list to
  conditional risk-triggered loading.
- `svelte-core-bestpractices`: slim `SKILL.md`, retain only repo-posture
  guidance and a one-level reference index; demote or remove stale-prone local
  framework docs where official Svelte docs lookup is enough.
- `user-apps-design`: slim `SKILL.md`, keep UI direction/parity/composition
  authority, route proof and route-state stops to owner skills.
- `systematic-debugging`: keep runtime workflow concise; move pressure tests
  and academic tests to evaluation/examples or remove if unused; generalize
  project-specific executable examples.

Counterfactual regressions:

- Mobile skill still says multiple broad references are always required.
- Svelte skill still duplicates official version-sensitive docs without an
  owner refresh policy.
- User-apps-design still owns runtime proof field lists.
- Systematic-debugging runtime bundle still includes training tests as if they
  were operational instructions.

### Wave 5: Trigger Description Review

Goal:

- Review every `description` frontmatter field after ownership and scope are
  simplified.

Reason:

- Skill descriptions are loaded into the agent's always-available skill list.
- They are the primary trigger surface for when and why a skill should be used.
- Concision matters, but clarity and explicit trigger boundaries matter more.

Scope:

- Inspect all `skills/*/SKILL.md` frontmatter descriptions.
- Ensure each description names:
  - the task class that should trigger the skill,
  - the skill's specific purpose,
  - important exclusions or routing boundaries when ambiguity is likely.
- Remove vague adjectives and broad catch-all phrasing.
- Keep descriptions concise enough for skill-list scanning.
- Align descriptions with the final post-refactor owner boundaries from Waves
  1-4.

Primary files:

- `skills/*/SKILL.md`

Proof:

- Every skill has one concise, explicit trigger description.
- No description claims ownership that the skill body no longer owns.
- Similar skills have distinguishable trigger boundaries.
- Harness validation passes.

Counterfactual regressions:

- A refactored skill body is narrow, but its frontmatter still triggers on the
  old broad scope.
- Two related skills remain indistinguishable from description alone.
- A terse description omits the key trigger term an agent would need to select
  the skill.

## Rejected Alternative Wave Splits

### Alternative A: One Large Refactor Wave

Rejected because:

- Proof, workflow, domain guidance, and mechanical hygiene have different owner
  boundaries and verification shapes.
- A single wave would make review too broad and would hide whether duplication
  was removed or only moved.

### Alternative B: Split Strictly By Existing Skill Directory

Rejected because:

- The main defects are cross-skill ownership duplicates, not isolated file
  quality problems.
- Editing one skill at a time would preserve repeated rules until late in the
  sequence and increase drift.

### Alternative C: Start With Domain Skill Cleanup

Rejected because:

- Domain skills depend on shared proof/runtime and skill-writing doctrine
  ownership.
- Slimming domain skills first would force local decisions about proof,
  references, and scripts that should be closed by Waves 1 and 2.

### Alternative D: Introduce `docs-ai/**` First

Rejected for now because:

- The harness repo does not currently use project-overlay workflow state.
- The user asked to plan harness skill refactors, not to migrate the harness
  repository to a project-style active-work topology.
- This can be revisited only as an explicit harness governance change.

## Open Decisions

1. Whether to introduce a top-level `plans/` convention permanently, or move
   this artifact if the harness adopts a different durable planning location.

## Post-Wave Follow-Ups

- Wave 4 may move or remove systematic-debugging pressure-test files after the
  runtime skill body is simplified.
- Wave 4 may delete or modernize webapp-testing examples after runtime proof
  ownership is split in Wave 2.
- A later enforcement wave may add duplicate/orphan helper validation after
  Wave 1 establishes stable owner/index patterns.

## Planning Critic

Initial review: `REJECT`.

Disposition:

- Added durable audit location decision.
- Added skill-writing doctrine owner.
- Added proof/runtime/review source-of-truth map.
- Added wave dependencies.
- Added proof rows and counterfactual regressions.
- Added per-domain Wave 4 target dispositions.
- Added rejected alternative split rationale.
