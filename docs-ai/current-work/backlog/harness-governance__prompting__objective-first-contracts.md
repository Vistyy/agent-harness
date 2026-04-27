# Objective-First Harness Prompt Contracts

## Backlog Item

Reshape process-heavy harness skills and adapter role prompts into
objective-first contracts where that reduces noise without weakening hard
invariants.

## Current Bucket

Deferred Backlog.

## Scope

Candidate files:
- `skills/planning-intake/SKILL.md`
- `skills/wave-autopilot/SKILL.md`
- `skills/verification-before-completion/SKILL.md`
- `skills/executing-plans/SKILL.md`
- `skills/writing-plans/SKILL.md`
- `adapters/codex/agents/*.toml`
- `adapters/github-copilot/agents/*.agent.md`

## Required Planning Shape

Before edits, inventory per-file invariants to preserve:
- planning gate and decision-closure semantics
- proof allocation and fresh-verification obligations
- stop-and-handback triggers
- role read/write limits
- ownership and boundary constraints
- final approval limits

Counterfactual proof must reject removing an invariant unless it is rehomed to
the owning skill or reference doc.

## Per-File Invariant Inventory

### `skills/planning-intake/SKILL.md`

Preserve:
- material decisions close before execution starts
- user-owned versus agent-defaultable decision split
- no silent material assumptions
- omission sweeps before promotion
- proof allocation fields and packet proof-row owner
- promotion blockers, including memory-only planning and materially divergent
  implementer choices
- `planning_critic` before planning-gate `quality_guard`
- durable outputs and deferral persistence

### `skills/wave-autopilot/SKILL.md`

Preserve:
- executes only one `execution-ready` wave with map, durable brief, and packet
- preflight checks for packet readiness and critic provenance
- stop on discovery leakage, unresolved material decisions, ambiguity, boundary
  flaws, or proof drift
- implementer delegation default when task card is eligible
- task-local proof, `verification-before-completion`, `quality_guard`, final
  review, and closeout requirements
- reporting fields for verification, evidence, review, and backlog state

### `skills/verification-before-completion/SKILL.md`

Preserve:
- no completion claim without fresh proof
- previous runs do not count
- quality gate map and normal completion gate expectation
- proof branch naming, counterfactual regression probe, owner-doc obligations,
  review status, runtime/diagnostic evidence fields
- small diffs do not waive gates
- interrupted delegated runtime proof is incomplete

### `skills/writing-plans/SKILL.md`

Preserve:
- standalone plans only, not waves
- closed requirements and material decisions before planning
- required sections, including decision closure, scope coverage, exact paths,
  task proof, follow-up, and approval record
- actual `planning_critic` and `quality_guard` approval before execution
- no memory-only non-trivial implementation

### `skills/executing-plans/SKILL.md`

Preserve:
- executes only approved standalone plans, not waves
- readiness preflight against decision closure, scope coverage, approval record,
  and requested scope
- execution does not reopen design
- minor local assumptions only through the ledger
- fresh proof before completion
- stop on missing surface, unresolved decision, or verification failure outside
  plan coverage

### Codex Role Prompts

Preserve:
- `explorer`: read-only, implementation-neutral discovery and context
  compression; no fixes unless asked
- `check_runner`: bounded verification/diagnostics, no edits, no final
  diagnosis or approval
- `planning_critic`: read-only hostile planning review, not approver,
  implementation reviewer, or implementer
- `implementer`: one assigned wave task or approved standalone-plan slice,
  bounded autonomy, no final approval, task-local proof
- `quality_guard`: read-only in-thread planning/implementation gate, not final
  approval or implementation owner
- `final_reviewer`: read-only final isolated closeout review only
- `runtime_evidence`: bounded live runtime proof, not debugger/planner/reviewer
  or implementation agent; interrupted proof is incomplete

### Copilot Role Prompts

Preserve the same role boundaries as Codex while keeping Copilot-specific
frontmatter, tool lists, and model metadata unchanged.

## Execution Tasks

### Task 1: Skill Prompt Contracts

Owned files:
- `skills/planning-intake/SKILL.md`
- `skills/wave-autopilot/SKILL.md`
- `skills/verification-before-completion/SKILL.md`
- `skills/writing-plans/SKILL.md`
- `skills/executing-plans/SKILL.md`

Allowed local decisions:
- rename sections toward outcome, success criteria, constraints, continuation,
  stop conditions, and output shape
- collapse repeated process wording only when invariant meaning remains present

Stop triggers:
- any listed invariant would need deletion or semantic weakening
- a skill would need a new owner boundary or reference extraction

### Task 2: Codex Role Prompt Contracts

Owned files:
- `adapters/codex/agents/*.toml`

Allowed local decisions:
- reshape instruction bodies into role outcome, constraints, stop conditions,
  and output contract
- keep model, reasoning, sandbox, and role names unchanged

Stop triggers:
- a role boundary becomes weaker or broader
- parity with Copilot would require changing adapter metadata or tools

### Task 3: Copilot Role Prompt Contracts And Parity

Owned files:
- `adapters/github-copilot/agents/*.agent.md`

Allowed local decisions:
- align wording with Codex role contracts where semantics are already shared
- preserve Copilot frontmatter, tool lists, model metadata, and user-invocable
  posture

Stop triggers:
- Copilot-specific capability/tooling would require different role semantics
- Codex/Copilot parity cannot be checked by focused diff inspection

### Task 4: Backlog Closeout

Owned files:
- `docs-ai/current-work/delivery-map.md`
- this backlog item

Close only after Tasks 1-3 land and verification passes. If any task is
deferred, narrow this backlog item instead of deleting it.

## Review Cadence

- Task 1 requires in-thread `quality_guard` approval before Task 2 starts.
- Task 2 requires in-thread `quality_guard` approval before Task 3 starts.
- Task 3 requires in-thread `quality_guard` approval before Task 4 starts.
- Task 4 closeout requires prior task approvals plus fresh `just quality`.

## Proof Rows

| Proof ID | Task | Claim | Exact proof | Counterfactual regression probe |
|---|---|---|---|---|
| P1 | Task 1 | Skill prompt reshaping preserves planning, execution, and completion invariants. | Inspect diff for each listed skill against the invariant inventory; get in-thread `quality_guard` approval before Task 2; run `just quality`. | Reject a diff that removes decision closure, proof allocation, fresh-proof gate, approval record, or stop-condition semantics without rehoming them to the owner doc. |
| P2 | Task 2 | Codex role prompts preserve role boundaries and output contracts. | Inspect diff for every Codex agent file; get in-thread `quality_guard` approval before Task 3; run `just quality`. | Reject a diff that lets read-only roles edit, lets non-review roles approve, lets implementer reopen material decisions, or lets runtime evidence become a debugger/reviewer. |
| P3 | Task 3 | Copilot role prompts preserve parity with Codex role boundaries while keeping adapter metadata unchanged. | Compare Codex and Copilot role diffs by role; get in-thread `quality_guard` approval before Task 4; run `just quality`. | Reject a diff that changes Copilot tools/model/frontmatter unexpectedly or weakens a shared role boundary relative to Codex. |
| P4 | Task 4 | Backlog closeout happens only after the full prompt-contract scope is complete. | Confirm Task 1-3 `quality_guard` approvals, inspect delivery-map diff and backlog deletion/narrowing, then run fresh `just quality`. | Reject deleting this backlog item while any candidate file remains unhandled or explicitly deferred without narrowed follow-up state. |
