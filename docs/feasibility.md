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
- **Update (2026-07-23, web search, see `research/2026-07-23-competitor-pricing-claude-websearch.md`):**
  competitor agencies serving trades including HVAC were found charging **$2,000–$15,000
  one-time for a build, with no monthly retainer required** in at least some offerings —
  this is a direct contradiction of this packet's "mandatory retainer" assumption and is
  the single most important finding from this research pass. This was a standard web
  search, not a full deep-research or direct-outreach pass, so treat this as a first
  signal to test against real competitor conversations, not a settled fact — but it's
  strong enough to make "will clients accept the retainer as mandatory" (item 3 below)
  the highest-priority open question in this doc.

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
   priced sanely for the buyer. **Partially resolved (2026-07-23):** existing HVAC
   CRM/dispatch software alone runs roughly $29–$329/mo (small/mid tier) to $700–$1,750/mo
   (enterprise tier, e.g. ServiceTitan) — see
   `research/2026-07-23-trade-software-baseline-cost-claude-websearch.md`. This packet's
   retainer tiers land inside or above that range for a *second* piece of paid
   infrastructure on top of existing software spend, which cuts both ways: either the
   market already tolerates this price band for software, or budget headroom is thinner
   than assumed. Still needs a real prospect conversation to resolve which reading holds.

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
- **Build cost benchmark (2026-07-23, web search, see
  `research/2026-07-23-automation-build-cost-benchmark-claude-websearch.md`):** general
  freelance Make.com project rates run $1,500–$5,000+ for complex workflows, or
  $100–150/hr for experienced work — this packet's target workflows (signature
  verification, idempotency, LLM extraction, schema validation, HITL gate, plus formal
  50-run/10-failure testing) sit at or above that complexity band, before counting the
  discovery process. Gives a rough floor for the still-blank implementation fee in the
  SOW template (§6), but a real time-tracked build (Phase 3 in `FRAMEWORK.md`) remains
  the more reliable way to set the actual number.

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
