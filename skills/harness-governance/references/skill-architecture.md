# Skill Architecture

Owner for reusable harness skill structure and skill-authoring quality.

## Entry Point

`SKILL.md` is the routing and workflow entrypoint.

It should include:

- what triggers the skill,
- when not to use it,
- the smallest workflow needed every time,
- expected outputs or handback shape,
- gotchas that affect routing or correctness.

Keep long doctrine, examples, templates, scripts, and assets out of the entry
body unless the agent needs them on every invocation.

## Frontmatter

The `description` field is always-visible routing text.

It should be:

- explicit about the task class,
- clear about the skill's purpose,
- narrow enough to distinguish neighboring skills,
- concise enough for skill-list scanning.

Prefer trigger language over marketing language. Do not claim ownership the
skill body no longer has.

Broad descriptions are allowed only for ambient events with lean hot paths,
explicit exclusions, and owner handoff. They must not become backlog, bug,
diagnostics, decision, planning, or durable-policy catchalls.

## Ownership Isolation

Each skill should own one coherent concept, workflow, or role surface.

Rules:

- describe the skill's own capability, operating workflow, required inputs, and
  handback shape,
- do not use the skill body as a routing index or ownership map for neighboring
  skills,
- rely on frontmatter descriptions and `AGENTS.md` for ordinary routing,
- reference another skill only for direct coupling, complex routing, or owner
  lookup that cannot be made clear in frontmatter,
- do not restate another skill's procedure, approval rule, or policy,
- do not mix unrelated lifecycle phases just because the same agent may touch
  them in one run,
- split only when the parts have different triggers, inputs, outputs, or
  proof/review owners.

When a skill directly consumes another skill's doctrine or output, name the
reason to load it. Keep the meaning in the consumed skill.

## References

Use references for detail that is too large or conditional for `SKILL.md`.

Rules:

- link references directly from `SKILL.md`,
- say when to read each reference,
- keep references one topic each,
- add a table of contents or heading map when a reference grows past about
  `100` lines,
- avoid nested reference chains.

References should point to owner docs instead of copying shared doctrine.

## Scripts

Skill scripts should behave like small CLIs.

They should:

- have one clear purpose,
- print deterministic output,
- fail loudly with useful errors,
- document inputs and outputs,
- write artifacts to known paths when they write anything,
- avoid hidden project, host, or tool assumptions.

If a script is project-specific, example-only, or last-resort, name that in the
owning skill.

## Assets And Examples

Templates and examples are useful when they prevent prompt bloat or repeated
manual reconstruction.

Rules:

- templates should be copied or filled by a clear workflow,
- examples should name the scenario they demonstrate,
- evaluation or training assets must be labeled as non-runtime guidance,
- stale or generic examples should be deleted, moved, or explicitly marked as
  last-resort.

## Simplicity Bar

A skill is too broad when it owns unrelated procedures, repeats another
owner's durable rule, or requires broad reading for a narrow task.

Default correction order:

1. delete stale or unused material,
2. link to the existing owner,
3. move conditional detail to a directly linked reference,
4. split only when two procedures have different triggers or outputs.

Concise is not enough. The skill must still preserve the trigger terms and
workflow constraints an agent needs to choose and use it correctly.
