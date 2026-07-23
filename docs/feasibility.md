# Feasibility

> **Tier:** High-level (decision input) · **Audience:** founder/decision-maker ·
> **Use when:** deciding go/no-go, and planning what to validate before spending real
> time or money. Several open items here are flagged for handoff to external deep
> research — see [`research-handoff.md`](./research-handoff.md).

This is Phase 1 reasoning — none of the numbers below are validated with real client
conversations or a built prototype. Treat every figure as a placeholder to test, not a
forecast.

## Demand signal (inferred, unverified)

- Trade businesses (HVAC, auto repair, similar field service) are a large, fragmented
  market that generally under-invests in software relative to enterprise, and commonly
  runs on a patchwork of email, spreadsheets, and one CRM/dispatch tool. That's a
  reasonable prior for "manual process pain exists," but it's not evidence any specific
  shop will pay $499+/mo plus an implementation fee to fix it.
- The manual's own qualification bar (≥10 executions/week, unstructured input, structured
  destination schema — §1.3) is a useful filter but also a real constraint: a lot of
  candidate businesses will fail this test, especially the volume threshold. Worth
  validating what fraction of realistic prospects actually clear it before assuming a
  large addressable pool.
- **Update (2026-07-23, real ChatGPT deep-research pass, see
  `research/2026-07-23-full-deep-research-chatgpt.md`) — confirms and strengthens the
  earlier quick-search finding:** a proper deep-research pass identified at least 9 real,
  currently-active competitors selling automation to this exact niche (HVAC, auto repair,
  and adjacent trades) — Never Miss Work, Gabe Works, CallbackPro, AutoShop SMS AI,
  Automation Warrior, TradeWire, Pigeon AI, ContractorOps, CloseLoop. Most use one-time,
  cancel-anytime, or hybrid setup-plus-cancellable pricing, not a mandatory long-term
  retainer. Never Miss Work sells a contractor package at **$497 one-time, no monthly
  fee, no contract** — a direct, well-sourced contradiction of this packet's mandatory-
  retainer premise. This is no longer a "first signal to test" — it's a sourced market
  fact: **mandatory retainer as a condition of entry is not the visible norm in this
  niche.** The retainer needs to be sold on a specific differentiator (reliability,
  incident response speed, formal testing, auditability, legal/compliance discipline),
  not just "maintenance exists," or expect prospects to price-shop toward these
  no-contract alternatives. This is now the single most important open question to
  resolve with a real prospect conversation, ahead of everything else in this doc.

## What needs to be validated before investing real time

In rough priority order:

1. **Will a real trade business pay for this?** Talk to 5–10 owners/ops managers in the
   target verticals about their actual pain (missed calls, invoice entry, quote intake)
   before building anything. This is cheaper than building a demo scenario first.
2. **Can the implementation actually be delivered profitably at a plausible one-time
   fee?** The SOW template leaves the fee blank (`review.md` §6) — build a real time
   estimate for one of the three worked examples (§7.1–7.3) and back into a fee that
   covers your time plus margin.
3. **Will clients accept the retainer as mandatory?** The manual frames the SLA retainer
   as non-optional, justified by API/system drift. That's a defensible technical
   argument but an unproven sales pitch — test it directly rather than assuming it lands.
4. **Competitive pricing sanity check.** $499–$2,950+/mo plus an implementation fee needs
   to be checked against what trade businesses currently pay for comparable software
   (CRM/dispatch tools, virtual assistants, existing automation vendors) to know if it's
   priced sanely for the buyer. **Resolved 2026-07-23** (real deep-research pass, see
   `research/2026-07-23-full-deep-research-chatgpt.md`): mainstream HVAC CRM/dispatch
   software clusters at **~$200–$700/mo** (Jobber $199–499/mo, Housecall Pro $79–329/mo
   + per-user, Service Fusion $245–627/mo), with ServiceTitan far above that
   (~$245–500/tech/mo plus $5k–$50k+ implementation). Auto-repair software clusters
   similarly, ~$200–$500/mo (Tekmetric, Shopmonkey). But the **closer substitute for
   pricing purposes isn't CRM software at all — it's the direct automation competitors
   identified above, selling at $8–$297/mo or $497 one-time.** Against CRM-software
   spend, this packet's retainer sits in a plausible range; against direct competitors,
   it's priced well above the visible market. Both comparisons matter, but the second one
   is more load-bearing given it's an apples-to-apples product comparison, not just a
   budget-line comparison.

## Cost side (founder/operator time and cash)

Rough categories to size, using the technical manual as the basis for scope:

- **Time per implementation:** discovery (video review + intake questionnaire) → sandbox
  build (webhook + signature verification + idempotency + HTTP model calls + schema
  validation + HITL gate) → 50-run stress test + 10-run failure test → deployment. This
  is nontrivial engineering work per client, not a five-minute Zapier template — estimate
  it honestly (see `infrastructure.md` for the pieces involved).
- **Ongoing retainer delivery cost:** patch response windows (2–12 business hours
  depending on tier) imply you (or someone) needs to be reachable and available on that
  cadence. At the Enterprise tier (2-hr response), this has real staffing implications
  once you have more than a handful of clients.
- **Platform + API costs:** Make.com plan tier (rate limits scale 60/min Core up to
  1,000/min Enterprise per `review.md` §2), plus direct LLM API costs (bypassing Make's
  native AI markup by using HTTP modules directly, per §2.2 — this lowers per-run cost
  but shifts billing to you directly against usage).
- **Build cost benchmark — resolved 2026-07-23** (real deep-research pass, see
  `research/2026-07-23-full-deep-research-chatgpt.md`, supersedes the earlier rougher
  quick-search estimate): basic Zapier-style automations sell for $149–$975 one-time —
  much simpler than this packet's scoped deliverable. For work at this packet's actual
  scope (discovery, webhook signature verification, idempotency, direct LLM API calls,
  schema validation, HITL gate, formal 50-valid/10-malformed test suite), a realistic
  fully-loaded price is **$4,000–$10,000 for an experienced freelancer, $7,000–$18,000
  for a small agency**, roughly **40–90 hours**, practical budgeting midpoint
  **~$6,000–$9,000/pipeline**, 2–4 weeks elapsed. This gives a real floor for the
  still-blank implementation fee in the SOW template (§6) — pricing materially below
  this range likely means under-scoped testing/hardening; a real time-tracked build
  (Phase 3 in `FRAMEWORK.md`) is still worth doing to confirm against this benchmark
  rather than replace it.

## Time-to-first-dollar

The likely fastest path to revenue is **not** a large enterprise-style engagement — it's
landing one qualified local business, running one of the three worked patterns
(missed-call SMS resuscitation is probably the cheapest to build and fastest to
demonstrate value, since it's a single trigger → lookup → send-SMS chain with no PDF/vision
parsing involved), and using that as a reference case before selling the second client.

## Bottom line (working hypothesis, not a conclusion)

The technical model is coherent and the engineering discipline described is a real
differentiator against sloppy competitors. The unresolved question is entirely commercial:
whether real trade businesses at the targeted volume will pay implementation + mandatory
retainer pricing, and how many of them exist and are reachable. That's a sales/market
question, not an engineering one — resolve it before investing further build time.
