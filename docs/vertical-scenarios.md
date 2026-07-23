# Vertical Scenarios (hypothetical stress test)

> **Tier:** High-level (exploratory) · **Audience:** founder, deciding between candidate
> verticals · **Use when:** pressure-testing whether the vertical-agnostic reframe in
> `docs/business-idea.md` actually holds, or comparing candidates before picking a first
> vertical per `docs/entrepreneur-notes.md`.

## Why this doc exists

`docs/business-idea.md` claims the target market is defined by a qualification test, not
an industry — but that claim has only ever been tested against one vertical
(HVAC/auto-repair), which is also the one the source manual happened to use. A claim of
generality that's only been checked once isn't well-tested. This doc runs three
deliberately different hypothetical verticals through `docs/vertical-playbook.md`'s
Layer 1 screening and `docs/architecture.md`'s eight-stage table, to see where the
abstraction genuinely holds and where it strains. **None of this is researched** — no
web search was run for this doc, on purpose. It's a reasoning stress test, not a market
analysis; anything that looks promising here would need the same real research pass
HVAC/auto-repair already got before being trusted.

## Scenario A — Dental/medical practice front desk

**Layer 1 screening:**
1. 3-Trait Test plausibility: strong. Missed calls, insurance-form intake, and
   appointment-request emails are widely reported administrative pain points across
   small medical/dental practices, not just one anecdote.
2. Existing budget line to compete with: yes — practice-management software (Dentrix,
   Curve, athenahealth-class tools) and outsourced answering services are both common
   spend categories, similar in shape to HVAC's CRM/dispatch software line.
3. Regulatory dimension: **HIPAA**, not TCPA — a materially different and arguably
   higher-stakes compliance surface than the HVAC case study. Any pipeline touching
   patient data needs a Business Associate Agreement (BAA) with the LLM provider, not
   just a data-retention conversation — this is a new research question this vertical
   would add to `docs/research-handoff.md`'s queue, not one already answered by the
   HVAC/auto-repair research.
4. Architecture sketch: **Trigger** — missed-call webhook or inbound patient-portal
   message. **Extract** — patient name, reason for contact, urgency, insurance info from
   free text. **Destination** — practice-management system's patient/appointment record.
   Plausible to sketch, same shape as HVAC.
5. Real access: **unknown** — no personal connection established in this packet.

**Honest divergence from the HVAC case study:** the HITL gate (stage 7) may need to be
*stricter* here than in HVAC — a mishandled patient message has different stakes than a
mishandled quote request. The "human approval" concept in `docs/architecture.md` still
holds, but what counts as adequate review before a message reaches a patient likely
needs its own standard, not a copy of the HVAC one.

**Pricing tolerance (unresearched guess, not a finding):** plausibly similar or higher
than HVAC, given practice-management software often costs more than field-service
software — but this is a guess, not backed by anything like the HVAC research.

## Scenario B — Small law firm client intake

**Layer 1 screening:**
1. 3-Trait Test plausibility: moderate. Intake volume varies enormously by firm size and
   practice area — a solo practitioner may not clear the ≥10/week volume bar at all,
   which is a real constraint this scenario surfaces that HVAC didn't (HVAC shops
   clearing the volume bar was closer to assumed-plausible; here it needs firm-size
   segmentation from the start).
2. Existing budget line: yes — practice-management/case-management software (Clio,
   MyCase) is a comparable spend category.
3. Regulatory dimension: **attorney-client privilege and bar-association ethics rules**
   around AI use in client communications — a genuinely different category of risk than
   TCPA or HIPAA, and one this packet has no existing research or reasoning to draw on
   at all. This would need to be a first-class new research question, not an extension
   of anything already answered.
4. Architecture sketch: **Trigger** — inbound intake form or email. **Extract** — matter
   type, opposing party (for conflict checks), urgency. **Destination** — case-management
   system. Sketchable, but the conflict-check step doesn't map cleanly onto any existing
   stage — it's arguably a second HITL-adjacent gate specific to this vertical, which is
   a genuine gap in the eight-stage model as currently written, not just a plug-in detail.
5. Real access: **unknown**.

**Honest divergence:** this is the scenario that most stretches `docs/architecture.md`'s
claim that all eight stages are fixed and only the specifics are pluggable — the
conflict-check requirement suggests the model might need a *ninth* stage for some
verticals, not just different plug-ins into the existing eight. Worth flagging as a
real limit of the current architecture doc rather than glossing over it.

## Scenario C — E-commerce order & return processing

**Layer 1 screening:**
1. 3-Trait Test plausibility: strong, and volume is likely to clear the bar *more*
   easily than HVAC — order/return volume scales with sales, not with staff availability,
   so a moderately successful small e-commerce operation could plausibly exceed
   10 events/week faster than a trade shop's missed-call rate would.
2. Existing budget line: yes — return-management platforms (Loop, Returnly-class tools)
   and customer-service/helpdesk software (Gorgias, Zendesk) are direct comparables.
3. Regulatory dimension: lighter than the other two scenarios — mostly standard consumer
   protection and refund-policy law, not a specialized regime like HIPAA or bar rules.
   This is the scenario closest to HVAC/auto-repair's TCPA-as-the-main-issue profile,
   though payment-adjacent flows (refund processing) could touch PCI-DSS-adjacent
   concerns depending on exact scope.
4. Architecture sketch: **Trigger** — return-request form, support-email inbox.
   **Extract** — order number, reason for return, item condition claims from free text.
   **Destination** — order-management/inventory system, refund initiation. Sketches
   cleanly onto all eight stages, no obvious missing stage like Scenario B.
5. Real access: **unknown**.

**Honest divergence:** the least divergent of the three — this scenario is closest to a
straightforward re-skin of the HVAC invoice-extraction pattern (§7.2), which is a point
in its favor for architecture reuse, but also means it tests the "vertical-agnostic"
claim the least rigorously, since it's the most similar case.

## What this stress test actually shows

- **The eight-stage architecture holds up reasonably well across three quite different
  verticals** — trigger/extract/destination were sketchable in all three without
  forcing. That's real evidence the vertical-agnostic reframe isn't just wishful
  thinking.
- **It's not universally true without modification.** Scenario B (law firm) surfaced a
  plausible missing ninth stage (a vertical-specific compliance gate beyond the generic
  HITL step) — worth remembering `docs/architecture.md` as "strong default, not a proven
  law" rather than treating eight stages as fixed forever.
- **Regulatory research doesn't transfer between verticals.** All the TCPA/data-retention
  research already done is HVAC/auto-repair-specific; a different vertical means a
  materially different `docs/research-handoff.md` queue, not a reused one, even if the
  research *process* itself transfers fine.
- **None of these scenarios currently beat HVAC/auto-repair on the one criterion that
  actually matters most** (per `docs/entrepreneur-notes.md`): real access. This doc
  doesn't recommend switching away from HVAC/auto-repair — it demonstrates the framework
  survives contact with other industries, which is a different, useful thing.
