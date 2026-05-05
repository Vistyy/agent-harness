# Harness Design Command Specialization

**Status:** done

## Objective Boundary

- original objective: finish the Impeccable-derived backlog by adding a small
  design operation vocabulary.
- accepted reductions: do not add user-facing slash commands, do not copy
  Impeccable's 23-command stack, and do not create a second router.
- residual gaps: none planned.

## Scope

- in scope: internal `user-apps-design` operation vocabulary for shape,
  critique, audit, polish, harden, and clarify; adapter-neutral
  handoff/readback guidance; validation that prevents the vocabulary from
  drifting or becoming a command router.
- out of scope: command installation, CLI prompts, live mode, detector
  automation, and project-specific workflow commands.

## Closed Decisions

- `user-apps-design` owns the operation vocabulary.
- Operations select design work posture; they do not replace owner-skill
  routing, runtime evidence, `design_judge`, or code review.
- Keep the vocabulary compact and internal.
- Handoffs/readbacks name the selected operation and required gates; they do
  not install prompts or commands.

## Planning Gate

- `planning_critic`: APPROVE after adapter-neutral handoff guidance,
  reference preservation for all six operations, and backlog closeout state
  were repaired.
- planning `quality_guard`: APPROVE after metadata, validation, handoff, and
  backlog proof surfaces were added.

## Implementation Gate

- implementation `quality_guard`: APPROVE after the packet stopped marking the
  task done before closeout and split implemented contract proof from planned
  workflow cleanup proof.
- final `final_reviewer`: APPROVE; final closeout may proceed.

## Proof

- `uv run pytest tests/test_validate_harness.py -q`: 53 passed.
- `uv run python scripts/validate_harness.py`: harness validation passed.
- `agent-harness governance check --repo-root .`: passed.
- `just quality-fast`: 99 tests passed, harness validation self-test passed,
  harness validation passed, Codex install smoke passed.

## Closeout

- added the internal `design_operation` labels `shape`, `critique`, `audit`,
  `polish`, `harden`, and `clarify` to `user-apps-design`.
- added adapter-neutral handoff/readback guidance and OpenAI metadata so agents
  name the operation without creating commands or another router.
- added harness validation and focused tests for operation terms, metadata, and
  no-bypass language.
- removed the promoted backlog entry and cleared active delivery-map evidence.

## Packet

- removed after final review approval.
