---
name: verify-work
description: "Choose honest proof for a work claim. Use before claiming non-trivial work is done, when deciding what evidence is needed, or when tests, runtime evidence, screenshots, performance, security, CI, static checks, or repo inspection must prove behavior, cleanup, migration, or replacement."
---

# Verify Work

Owns proof selection and proof honesty. Specialist skills and plugins own how
to obtain platform, test, security, performance, screenshot, browser, or mobile
evidence.

## Rule

Do not claim non-trivial work is done without proof that would fail if the
claim were false.

Start from the claim, not from convenient commands. Pick the smallest proof
surface that honestly covers the claim and material risks.

For non-trivial work, the claim must include the expected finished repo state
or an explicit accepted reduction. Do not prove only the latest edit, failing
test, or PR comment when the user objective requires a broader state to be
true.

Use unit tests, integration tests, e2e/browser/mobile flows, runtime evidence,
screenshots, performance traces, security scans, CI logs, static checks, or
repo inspection as appropriate. Read specialist skills in tandem for mechanics.
When proof adds, edits, deletes, reviews, or relies on persistent tests, use
`../testing-best-practices/SKILL.md`.

Proof is invalid when it could pass while the claimed behavior, cleanup,
migration, replacement, or integration is absent.

Cleanup and migration need positive replacement/reachability proof plus
supporting absence checks. Text-not-present, class-gone, or grep-only evidence
is not enough unless the claim is only that exact identifier was removed.

For migration, runtime, integration, or workflow failures, prefer rerunning the
real failed path or a faithful smoke/integration proof before adding mocked
persistent tests. A fake test around emitted commands, DDL, mocks, or call
choreography is not proof of the runtime boundary.

## Verdict

Report claim, proof surface, commands/actions, material artifacts, verdict
`pass | reject | blocked`, limits, and remaining unproved boundaries.

Return `blocked` when the right proof surface is unavailable, unsafe, too
expensive for the current turn, or requires missing user/project input. Do not
substitute narrower proof unless the user accepts a narrowed claim.

## Routing

- Use `../testing-best-practices/SKILL.md` when durable tests are added,
  changed, deleted, reviewed, or relied on as proof.
- Use `$playwright-interactive`, `$playwright`, or `$screenshot` for browser,
  Electron, or OS screenshot mechanics when installed.
- Use the Test Android Apps plugin for Android emulator/device QA or
  performance mechanics.
- Use the security plugin for explicit security scans or finding fixes.
- Use `../user-apps-design/SKILL.md` and `design_judge` for broad visual
  quality approval.

## References

- Read `references/browser-runtime-proof-workflow.md` before browser-visible
  runtime proof.
- Read `references/browser-proof-layering-contract.md` before choosing a
  browser proof channel.
- Read `references/mobile-runtime-proof-workflow.md` before mobile runtime
  proof.
- Read `references/mobile-emulator-proof-contract.md` when emulator/device
  lifecycle or parallel-device constraints matter.
