# Browser Runtime Proof

Owns browser-specific proof integrity. Browser mechanics come from
`$playwright-interactive`, `$playwright`, durable project tests, or another
project-owned browser recipe.

## Preflight

Name exact flow, route, role, auth/session, data, viewport, UI behavior risk,
and unproved browser/runtime boundaries or `none`.

Same route with different auth, authority, session, persistence, or viewport
behavior is a different proof. Anonymous browse proof does not cover
authenticated writes. Server-owned writes need mutation plus follow-up read or
reload in the same authenticated posture.

## Vehicle

Use `browser-proof-layering-contract.md` to choose durable spec,
`$playwright-interactive`, `$playwright`, screenshot-only capture, or a raw
script fallback. Vehicle follows claim shape and reuse value, not convenience.

## Evidence

Capture only evidence the verdict relies on: channel, pages/flows, viewport,
selected screenshots when layout or hit testing matters, bounded
console/network findings, trace IDs, and diagnostic paths when material.

Prefer snapshots or DOM/UI inventories for state checks. Use screenshots when
visual layout, hit testing, transitions, or responsive behavior is part of the
claim.

Browser proof does not approve broad product visual quality. For that, hand
fresh screenshot/contact-sheet artifacts to `design_judge` through
`../../user-apps-design/SKILL.md`.

Report selected vehicle, actions, reviewed artifacts, diagnostic artifacts when
material, verdict, and unproved browser/runtime boundaries.
