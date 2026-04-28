# Workflow Feedback Ledger Entry Examples

Good entries are specific enough to review later without replaying the whole
conversation. They name the workflow issue, why it matters, where it surfaced,
and what disposition should happen next.

## Good Entries

### Repeated review misses stale references

- Reporter / context: final reviewer on harness skill cleanup
- Surface: `../../../scripts/validate_harness.py`, skill routing references
- Suggested disposition: `validation-candidate`
- Status: `open`

Observation:

A deleted skill left behind plain backticked route references where prose used
the word "use" before a backticked skill name. Existing validation checked
dollar-prefixed skill tokens and
`SKILL.md` paths but missed this live routing style.

Recommended next action:

Add validation for verb-triggered backticked skill names and regression tests
for missing skill references in `../../../scripts/validate_harness.py`.

### Subagent policy wording keeps being misread

- Reporter / context: main agent during non-trivial harness work
- Surface: `AGENTS.md`, `subagent-orchestration`
- Suggested disposition: `harness-candidate`
- Status: `open`

Observation:

The policy said subagents were automatically approved by category, but agents
still hesitated because it did not name the exact allowed roles.

Recommended next action:

Replace category wording with a closed allowlist of harness-defined subagents
and validate that the allowlist stays in sync with role vocabulary.

### Current-work directory accumulates closed evidence

- Reporter / context: closeout review after harness cleanup
- Surface: `docs-ai/current-work`
- Suggested disposition: `project-fix`
- Status: `open`

Observation:

Completed audit and handoff files remained loose in `current-work`, making it
look like active plans might still exist.

Recommended next action:

Compact closed records into one archive note and leave `delivery-map.md` as the
active queue index.

## Weak Entries

Avoid entries like:

- "Skill docs are confusing."
- "Subagents did not work well."
- "Maybe improve validation."

They are too broad to promote or discard later. Record the concrete trigger,
affected surface, and next action instead.
