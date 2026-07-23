# Entrepreneur Notes

> **Tier:** High-level (working scratchpad) · **Audience:** founder only — this is a
> living notes file, not a polished deliverable · **Use when:** ongoing, update as
> real answers replace open questions. Several items here are good deep-research
> handoff candidates — see [`research-handoff.md`](./research-handoff.md).

Working scratchpad for decisions and questions that are still open — not conclusions.
Update this file as answers come in from real client conversations.

## Positioning

- The manual's own framing is useful and should probably be the external pitch too: this
  is explicitly **not** an "autonomous AI employee" pitch — it's a "workflow repair"
  pitch grounded in the 76%-experiment/14%-deep-integration gap cited in the executive
  summary of `make.com review.md`. That's a credible, differentiated angle against the
  current wave of overhyped "AI agent" marketing — leans into reliability and
  boring-but-correct engineering as the sales point.
- Concrete workflow patterns (missed-call SMS resuscitation, invoice extraction, quote
  intake) are more sellable than abstract capability claims. Lead sales conversations with
  "we fix this exact problem you have" rather than "we build AI automations."

## Pricing rationale (untested)

- The SLA tiers ($499 / $1,250 / $2,950+) are plausible for the value described (patch
  windows, audits, credit pool management) but are not benchmarked against anything in the
  source material or validated with prospects. **Partial answer (2026-07-23, web search,
  see `research/2026-07-23-trade-software-baseline-cost-claude-websearch.md` and
  `research/2026-07-23-competitor-pricing-claude-websearch.md`):** existing HVAC
  CRM/dispatch software already runs $29–$1,750/mo depending on tier, so this packet's
  retainer isn't priced in an alien range for the buyer — but at least one competitor
  automation agency was found offering a **one-time build with no monthly retainer at
  all**, which directly threatens the "mandatory retainer" premise. This is now the
  single highest-priority thing to test with a real prospect: not "is $499/mo
  reasonable" but "will they pay ongoing at all when a competitor doesn't require it."
- The one-time implementation fee is an open blank in the SOW template (`review.md` §6).
  **Rough floor established (2026-07-23):** general Make.com freelance project rates run
  $1,500–$5,000+ for complex workflows (`research/2026-07-23-automation-build-cost-benchmark-claude-websearch.md`),
  and this packet's target workflows are at or above that complexity band before counting
  discovery/testing overhead — so the fee likely needs to sit at or above that range. Still
  needs a real time-tracked build (Phase 3 in `FRAMEWORK.md`) to set an actual number
  rather than a market-rate proxy.

## Go-to-market — open questions

- Who is the first prospect, specifically? Cold outreach to trade businesses vs. warm
  network vs. a specific local geography — not addressed in the source material at all.
- Is the "mandatory video capture of 5 recordings" intake step (`review.md` §1.2) too high
  friction for an unproven agency with no track record? It's a reasonable qualification
  filter once there's reputation/referrals to draw on, but may be an early barrier to the
  very first client, who has no reason yet to trust the process. Consider whether it needs
  to be relaxed for client #1.
- What's the actual channel for finding businesses that clear the 3-Trait Qualification
  Test (§1.3)? This test is good for filtering inbound leads but says nothing about how to
  generate them in the first place.

## Sequencing — a reasonable first-90-days plan (not in source material, inferred)

1. Talk to 5–10 real trade-business owners/ops people about their actual pain points
   before building anything (validates or kills the market assumption cheaply).
2. Pick the cheapest-to-build worked pattern (likely missed-call SMS resuscitation — no
   PDF/vision parsing, minimal integration surface) and build one working version as a
   demo/proof, even without a paying client yet.
3. Land one paying client on that pattern. Use it as the reference case.
4. Only then formalize the SOW numbers, retainer positioning, and MSA language with a
   real lawyer, based on what actually worked in that first deal.
5. Decide whether "mandatory retainer" framing survived contact with a real client, or
   needs softening.

## New open question from research (2026-07-23)

Given at least one competitor was found offering a no-retainer, one-time-build model
(see pricing rationale above), it's worth deciding in advance whether "mandatory
retainer" is a hill to defend in a first sales conversation, or whether there's a
fallback position (e.g., an optional retainer with a clearly worse SLA/no-retainer
tier, rather than an all-or-nothing mandate) — better to have that fallback thought
through before a prospect pushes back mid-conversation than to improvise one on the spot.

## Things to explicitly decide before writing a real contract

- Get the MSA clauses in `review.md` §4.2 reviewed by an actual lawyer — see `risks.md`.
- Decide ZDR (Zero Data Retention) policy per client tier — offer it standard on
  Enterprise, optional add-on below that, or something else entirely.
- Decide what happens contractually if a client's staff stops actually reviewing HITL
  approval gates and starts rubber-stamping — this undermines the entire liability
  shield and is worth addressing explicitly rather than assuming it won't happen.

## Open naming/branding question

No agency name, domain, or brand identity exists yet in the source material — this is
still an unnamed idea, not yet a formed business entity.
