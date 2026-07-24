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
  windows, audits, credit pool management) but were not benchmarked against anything in
  the source material. **Resolved via two independent deep-research passes, 2026-07-23**
  (ChatGPT: `research/2026-07-23-full-deep-research-chatgpt.md`; Claude/Opus:
  `research/2026-07-23-full-deep-research-opus.md`) — both supersede the earlier
  quick-search first pass and, notably, **found entirely different named competitors from
  each other** while reaching the same conclusion, which is stronger evidence than either
  pass alone. ChatGPT found Never Miss Work, Gabe Works, CallbackPro, AutoShop SMS AI,
  Automation Warrior, TradeWire, Pigeon AI, ContractorOps, CloseLoop. Opus independently
  found QuickOutcomes, AutomateNexus, Dorcia Automations, GoHighLevel-based offers, US
  Tech Automations, Leads4Build, Zachary Hoppaugh LLC, Evolv AI Agents. **Both agree**:
  setup-fee-plus-retainer is the *dominant* pattern in this niche, but a credible minority
  of real, published competitors (Never Miss Work at $497 one-time no-contract;
  QuickOutcomes from $1,000 one-time "we don't charge monthly fees at all"; AutomateNexus
  from $2,500 one-time "no subscriptions, no vendor lock-in") sell pure one-time builds
  and market explicitly against retainer lock-in. **Verdict: "mandatory" is defensible as
  common practice, not as universal practice** — treating it as an unavoidable
  requirement is a real, sourced competitive liability, not treating it as impossible to
  sell at all.
- **Concrete strategic recommendation from both research passes (worth taking seriously,
  not just testing):** drop the word "mandatory." Offer two paths — (a) a build-and-own
  one-time option priced at a premium (**$5,000–$8,000+/pipeline**) that neutralizes the
  no-lock-in objection outright, and (b) a strongly-incentivized ongoing plan where the
  retainer buys concrete, visible things (credits, monitoring, patch-response SLA,
  audits) rather than being sold as "maintenance exists." Keep the existing
  $499/$1,250/$2,950 tiers, but stop presenting them as the only path to engagement.
  *Threshold to reconsider this:* if real discovery calls show prospects consistently
  accept a mandatory retainer without objection, tighten back toward required — but
  default to assuming they won't until that's actually observed.
- The one-time implementation fee is an open blank in the SOW template (`review.md` §6).
  **Resolved via both deep-research passes, 2026-07-23** — converge closely: ChatGPT
  estimates $4,000–$10,000 (freelancer) to $7,000–$18,000 (small agency), midpoint
  ~$6,000–$9,000; Opus estimates $3,000–$12,000+, midpoint $6,000–$10,000, and gives a
  concrete recommendation: **set the fee at ≥$3,000, target $5,000–$8,000/pipeline.**
  Both are well above generic "simple Zapier automation" pricing ($149–$975 one-time, or
  even sub-$100 on gig platforms), which matches the added scope of discovery, formal
  testing, and the HITL/idempotency architecture. Anchoring the implementation fee at
  this level also reduces dependence on the contested retainer for margin — i.e., pricing
  the one-time build correctly is itself a partial hedge against the mandatory-retainer
  risk above. Still worth confirming against a real time-tracked build (Phase 3 in
  `FRAMEWORK.md`), but this is now a well-corroborated benchmark, not a rough proxy.

## Go-to-market — open questions

- **Which vertical to actually validate in first — reopened 2026-07-23, partially
  answered 2026-07-23.** The packet no longer defaults to HVAC/auto-repair by definition
  (see `docs/business-idea.md`), so this question is genuinely open rather than
  pre-answered by the source manual — **where do you have real domain knowledge or a
  real relationship**, not which industry sounds biggest, since the qualification test
  only screens for workflow *shape* and supplies none of the operational detail an actual
  pipeline needs. `docs/expansion.md` starts answering this concretely: two of the five
  planned first conversations are with people already running comparable or adjacent
  retainer businesses, which is a real in, not a hypothetical one.
- Who is the first prospect, specifically, within whichever vertical gets picked? Cold
  outreach vs. warm network vs. a specific local geography — see `docs/expansion.md` for
  the plan covering the first five conversations, at least.
- Is the "mandatory video capture of 5 recordings" intake step (`review.md` §1.2) too high
  friction for an unproven agency with no track record? It's a reasonable qualification
  filter once there's reputation/referrals to draw on, but may be an early barrier to the
  very first client, who has no reason yet to trust the process. Consider whether it needs
  to be relaxed for client #1.
- What's the actual channel for finding businesses that clear the 3-Trait Qualification
  Test (§1.3)? This test is good for filtering inbound leads but says nothing about how to
  generate them in the first place, in any vertical.

## Sequencing — a reasonable first-90-days plan (not in source material, inferred)

1. **Pick a first vertical based on real access** (see "Which vertical to actually
   validate in first" above), then talk to 5–10 real owners/ops people in that vertical
   about their actual pain points before building anything (validates or kills the
   market assumption cheaply). This step didn't used to be a real decision — the packet
   defaulted to HVAC/auto-repair — but it is now.
2. Pick the cheapest-to-build worked pattern (likely missed-call SMS resuscitation — no
   PDF/vision parsing, minimal integration surface) and build one working version as a
   demo/proof, even without a paying client yet.
3. Land one paying client on that pattern. Use it as the reference case.
4. Only then formalize the SOW numbers, retainer positioning, and MSA language with a
   real lawyer, based on what actually worked in that first deal.
5. Decide whether "mandatory retainer" framing survived contact with a real client, or
   needs softening.

## New open question from research (2026-07-23, confirmed by two independent deep-research passes)

Given multiple sourced competitors (found independently by two different research
engines — see pricing rationale above) offer no-retainer or cancel-anytime pricing, it's
worth deciding in advance whether "mandatory retainer" is a hill to defend in a first
sales conversation, or whether to lead with the two-path offer both research passes
recommend (one-time build-and-own at a premium, vs. an incentivized ongoing retainer) —
better to have that decided before a prospect pushes back mid-conversation than to
improvise one on the spot. If the mandatory framing is kept for some segment, the
research suggests a specific differentiation angle: sell it as compliance-grade,
formally tested, audited infrastructure (the 50-valid/10-malformed test suite, signature
verification, idempotency, HITL) rather than generic "maintenance" — that's the gap
between this packet's engineering rigor and what the cheaper no-retainer competitors
appear to offer.

## Market-size denominators (HVAC/auto-repair case study — context only, not a qualification-rate answer)

Both deep-research passes found real establishment-count data, useful as candidate-pool
context even though the actual qualification rate (§Q6) still requires primary research:
IBISWorld puts HVAC ("Heating & Air-Conditioning Contractors," NAICS 23822a) at 120,461
businesses as of 2026 (+1.7% from 2025), average ~5.2 employees/business, $159.4bn
industry size. Auto-repair estimates vary by source/NAICS definition — roughly
170,000–280,000 depending on definition (IBISWorld "over 280,000," BLS ~176,000+,
Statista ~174,200, commercial POI databases ~253,000). Treat these as the denominator
only — see `docs/feasibility.md` for why the qualification-rate multiplier still needs
real conversations, not a public-data estimate.

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
