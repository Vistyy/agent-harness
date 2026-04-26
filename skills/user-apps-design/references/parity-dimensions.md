# User Apps Parity Convention

Owner for end-user parity across web and mobile applications.

- This file defines parity meaning.
- project overlays define parity timing and staged handoff policy.

## Default Meaning

If request says "parity" and does not ask for pixel match, use this:

- match product behavior, state semantics, and user outcome,
- match copy meaning per the project language policy, not exact sentence length or layout,
- match brand direction and design-system semantics,
- keep component families recognizable across clients,
- let structure follow platform ergonomics.

Rule: same product, different surfaces.

If visual parity fights functional parity and no product decision exists,
functional parity wins.

## Parity Matrix

| Dimension | Default |
| --- | --- |
| Capability parity | Required |
| Behavior and state parity | Required |
| Copy semantics parity | Required |
| Component semantics parity | Required |
| Interaction parity | Required |
| Visual tone parity | Required |
| Layout and navigation structure parity | Optional unless explicitly locked |
| Pixel parity | Off by default |

Note: layout and navigation may diverge for platform ergonomics, but do not add
duplicate in-UI navigation when browser/system navigation already models the
transition cleanly.

## Functional Parity Gate

For flows implemented on both clients, functional parity is merge-blocking by
default.

For staged work with a missing follower implementation, follow the project delivery policy. Do not fake same-wave parity.

Required unless wave brief records allowed divergence:

- same capability for same user posture,
- same auth boundary,
- same state-transition outcome for same intent,
- same navigation semantics when browser/system history can represent them,
- same destructive-action posture,
- same lifecycle/read-only posture for archived, offline, or disabled states,
- same validation and retry/error posture.

Not enough:

- "primary surface correct, follower later" without queued or scheduled follow-up,
- screenshot match while capability or state drift remains,
- "mobile works differently" without explicit brief-level rationale.

## Allowed Divergence

Allowed without extra approval:

- layout density and spacing,
- container width and screen composition,
- navigation container shape with same task outcome,
- form presentation shape with same behavior and copy meaning,
- wider desktop/tablet shells on web,
- medium-appropriate discoverability or task-flow patterns with same semantics.

Not allowed by default:

- mobile viewport geometry copied onto web desktop,
- mobile visual structure ported 1:1 to web without explicit requirement,
- debug or dev affordances treated as parity-critical user flow,
- parity declared from screenshots alone,
- desktop shells clamped to narrow mobile-width columns without explicit UX
  decision,
- established IA/UX patterns rejected without rationale in parity matrix.

## Capability Boundary Rule

Do not infer shared capability rules independently in scattered view code.

Required:

- auth-gated, lifecycle-gated, read-only, and destructive-action availability
  come from explicit capability boundaries or contract-level policy in each
  client,
- parity review inspects that boundary directly, not only visible buttons.

Structure may differ per client. Rule ownership may not.

## Navigation Rule

Do not add in-UI navigation that only duplicates browser history, system back,
or native navigation.

Required:

- if transition is real navigation, let route/history/native navigation own it,
- model transition in navigation state before adding dedicated back or close
  UI,
- add in-UI navigation only when it serves product purpose beyond duplicated
  platform navigation, or platform navigation cannot represent transition
  cleanly.

Examples:

- web route-state detail prefers browser back over a redundant in-screen back control,
- mobile navigation transition prefers system back over extra in-screen back,
- mode, sheet, or inline editor may still use in-UI dismiss control when it is
  not duplicating platform back behavior.

Not allowed:

- in-screen back buttons used to hide missing route/history wiring,
- duplicated platform navigation without documented product reason.

## Shared Logic Gate

When both clients implement same domain behavior in separate codebases
(`compare-row grouping`, loyalty price selection, ranking, normalization,
similar), parity work must prove semantic equivalence.

Required evidence:

- name paired implementations,
- confirm same grouping keys and winner-selection criteria for same payload,
- include at least one fixture with duplicate retailer entries proving row-count
  parity.

Screenshot match without this evidence is not a parity claim.

## Planning Gate

Any parity wave or work item must include:

1. must-match set: capability, behavior, state, copy meaning,
2. allowed divergence set: layout, navigation, interaction form,
3. prohibited mirror moves,
4. evidence plan for both clients,
5. shared-logic check plan with paired functions and fixture cases,
6. IA pattern disposition with explicit `adopt` or `reject` when IA scope
   changes,
7. functional parity checklist covering capability boundary, auth posture,
   destructive-action posture, navigation ownership, and critical
   state-transition checks.

Missing these means not execution-ready.
