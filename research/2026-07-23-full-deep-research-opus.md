**Prompt used:** the full `===BEGIN PROMPT===`/`===END PROMPT===` block from
`docs/research-handoff.md` (all 6 questions, business context inlined) — same prompt as
the ChatGPT pass, run as a second, independent opinion.

**Engine:** Claude (Opus, extended/deep research mode) · **Date:** 2026-07-23

**Status:** Second independent deep-research pass on the same 6 questions already
answered by `research/2026-07-23-full-deep-research-chatgpt.md`. Notably found a
**completely different set of named competitors** (zero overlap) while reaching the
**same qualitative conclusion** on the retainer question — two independent searches
converging on the same finding is stronger evidence than either alone. Agrees with the
ChatGPT pass's correction of the Anthropic retention figure (30 days, not 7). Goes
further than the ChatGPT pass with concrete strategic recommendations (see below) and
more specific legal case citations.

---

# Workflow Repair Agency: Pricing & Legal Exposure Research Brief

## TL;DR

- **The mandatory monthly retainer is the single biggest vulnerability in this plan.**
  Setup-fee-plus-retainer is the dominant pattern, but a credible minority of
  competitors (QuickOutcomes, AutomateNexus) sell pure one-time builds with no retainer
  and win on "you own it, no lock-in." "Mandatory" is defensible as *common* practice,
  not *universal* — reframe as strongly incentivized, offer a one-time build path.
- **The missed-call SMS product is the highest legal-risk element and is genuinely
  unsettled law.** No explicit statutory "missed-call exception"; recent rulings
  (*Butera*, Seventh Circuit's *Steidinger*) trend defense-favorable, but there's a live,
  unresolved circuit split (vs. Ninth Circuit's *Howard*), and 10DLC registration plus
  opt-out language is mandatory regardless. Treat as lawyer-reviewed, ideally
  human-triggered — not turnkey automation.
- **The "7-day" LLM retention finding needs correction** (confirms the ChatGPT pass):
  Anthropic's commercial API default is **30 days, not 7** — the 7-day figure applied to
  *consumer* products from Sept 2025, not the API. OpenAI's API default is also 30 days.
  ZDR for both requires enterprise application/approval, not a toggle.

## Competitor landscape (Q1) — different companies found than the ChatGPT pass, same conclusion

| Business | Model | Pricing | Retainer mandatory? |
|---|---|---|---|
| QuickOutcomes (Essex Junction, VT) | Pure one-time, project-based | From $1,000, "we don't charge monthly fees at all," positions Podium/Thryv/Broadly as the expensive alternative; explicitly serves contractors and auto repair | **No** |
| AutomateNexus | Pure one-time build | From $2,500 (typical $7,500), self-hosted n8n, "no subscriptions, no vendor lock-in, you own it"; only recurring cost is LLM API pass-through (~$30–150/mo) | **No** |
| Dorcia Automations (West Texas, contractors/construction) | One-time setup + mandatory low retainer | Spark $500–1,500 setup + $49/mo; Momentum $2,000–4,000 + $119/mo; Engine $5,000–15,000 + $259/mo | Yes, but low-cost |
| GoHighLevel contractor agencies (verified live pricing pages) | Setup + tiered monthly | $500 setup + $197/$297/$347/mo; another offer $1,997 setup + $197/mo | Yes, but "no contracts, cancel anytime" |
| US Tech Automations | Self-serve subscription | Solo $32/mo, Growth $124/mo, Scale $457/mo, custom managed tier | Yes (subscription-based) |
| Leads4Build, Zachary Hoppaugh LLC, Evolv AI Agents | HVAC/contractor-focused | Book-a-call custom quoting, ongoing management | Yes, none advertise one-time-only |

Industry playbooks (Ideaproof and others) explicitly advise "never sell hourly — always
fixed setup + monthly retainer," framing retainers as "non-negotiable," typically
15–25% of setup fee per month. General AI-automation-agency pricing: one-off builds
$1,500–$12,000, retainers $500–$5,000/month.

**Implication:** the $499/$1,250/$2,950 tiers are within market range on the monthly
number — the problem is the word "mandatory." At least two credible, published
competitors win specifically by promising no lock-in and client ownership, making a
mandatory retainer the easiest objection for a prospect to raise. **Recommended
reframe:** bundle genuinely valuable ongoing service (credits, monitoring, patch-response
SLA, audits), make it strongly recommended/incentivized, and offer a one-time
build-and-handoff path at a premium ($5,000–$8,000+) to neutralize the objection
entirely.

## Baseline software/labor spend (Q2)

- **CRM/dispatch/FSM:** Housecall Pro Basic ~$59–79/mo (1 user), Essentials ~$149–189/mo
  (up to 5 users, the practical small-shop tier), Max ~$299–329/mo (up to 8 users).
  ServiceTitan ~$245–398/tech/mo with 12-month minimums and **documented termination
  fees of $15,000–$46,000** (no month-to-month option) — mid-size operations commonly
  land at $398–600+/mo. Budget tools: Jobber ~$39/mo, QuoteIQ ~$29.99/mo. Corroborates
  and widens the earlier "$29–$1,750/mo" range.
- **Existing automation/marketing tools:** home-services marketing automation typically
  $149–499/mo; GoHighLevel $97–297/mo; big suites (Podium/Thryv/Broadly) $400–1,100/mo
  with $250–350 setup and annual contracts. First-year all-in for a 5–20 employee shop
  commonly $2,500–7,500.
- **Admin/call-handling labor:** answering services $150–500/mo typical, AI flat-rate
  HVAC services $697–2,197/mo; human virtual receptionists $235–2,400/mo (realistic small-
  business volume $300–900/mo); VAs offshore $5–15/hr, nearshore $9–18/hr, US $25–75/hr;
  full-time offshore VA $800–2,500/mo; part-time in-house receptionist $2,500–4,000/mo.

**Implication:** the Essentials tier ($499/mo) sits above a shop's entire FSM software
bill and roughly at the level of a mid-tier answering service or part-time offshore VA —
defensible only if the ROI narrative is explicit. The retainer competes against a real,
visualizable budget line (a VA or answering service), not against nothing.

## Missed-call SMS compliance (Q3) — detailed brief for counsel

**Bottom line: genuinely unsettled and fact-dependent, not a clean yes/no. No explicit
statutory or regulatory "missed-call text-back exception" exists.**

- Neither the TCPA nor implementing regs have an exception for "returning a missed
  call" (per TCPA specialist Eric Troutman/Troutman Amin). Regs require either prior
  express invitation/permission, or an established business relationship from a
  voluntary two-way communication based on a transaction or inquiry — a "sterile" missed
  call with no voicemail and no conversation doesn't cleanly satisfy either.
- **Case law trending favorable:** *Butera v. Sugarhouse Real Estate Group* (D. Utah,
  June 30, 2025) held a return contact made "in response to [the consumer's] own call"
  was not "unsolicited" — placing a call without leaving a voicemail "was an invitation
  for a return call." (Court flagged the opposite would apply if the consumer had left a
  message saying they were on the DNC list.) *Steidinger v. Blackstone Medical Services*
  (7th Cir., July 14, 2026) held text messages are NOT "telephone calls" under
  §227(c)(5), eliminating the private DNC right of action for texts in the Seventh
  Circuit (IL, IN, WI) — but this creates an **unresolved circuit split** with the Ninth
  Circuit's *Howard v. RNC* (2026), which read "call" more broadly under §227(b).
  *Steidinger* does NOT immunize texts under §227(b) — the actual autodialer/written-
  consent risk provision — it only addresses the DNC private right of action.
- **Differs from cold marketing texts:** a cold, unsolicited marketing text is squarely
  prohibited without prior express written consent (highest-risk category). A missed-
  call reply is distinguishable because the consumer initiated contact, and is on
  stronger footing if purely informational/transactional rather than promotional. The
  line not to cross: turning that first reply into a marketing drip sequence, or adding
  promotional content, without separate opt-in.
- **Compliance floor regardless of the consent debate:**
  - **10DLC registration is mandatory** — since February 2025 all major US carriers
    (AT&T, T-Mobile, Verizon) block unregistered A2P traffic outright, no grace period.
    Register the brand with The Campaign Registry (one-time; brand verification ~2–3
    business days), then register each use-case campaign separately (~3–7 business
    days) — don't mix use cases on one campaign.
  - Opt-out language in every message ("Reply STOP to unsubscribe").
  - Clear business identification.
  - Quiet hours: 8am–9pm recipient local time (stricter under some state mini-TCPA laws).
  - Keep the first message informational, not promotional; require separate opt-in
    before any subsequent/marketing texts.
  - State mini-TCPA laws (e.g. Florida Telephone Solicitation Act) independently
    restrict marketing texts and are increasingly used by plaintiffs as federal DNC
    theories erode — screen by client state.
- **Regulatory context for counsel:** the FCC's one-to-one consent rule was vacated by
  the Eleventh Circuit in *Insurance Marketing Coalition v. FCC* (No. 24-10277, Jan. 24,
  2025) and the FCC deleted the vacated language — bundled consent remains permissible,
  the lead-gen consent tightening did NOT take effect. Separately, *McLaughlin
  Chiropractic v. McKesson* (2025) held district courts aren't bound by FCC TCPA
  interpretations, which is why courts are reaching divergent results. **Litigation
  volume is real and rising:** 1,052 TCPA class actions filed in H1 2025 vs. 539 in the
  same period the prior year — a 95.2% increase (Troutman Amin/WebRecon Midyear
  Litigation Report), and 2024 was itself the prior record year.

**Recommendation:** make the missed-call text **human-triggered (one-tap approve)**
rather than fully automated — materially strengthens the "not an autodialer /
individualized response" posture, and fits the product's existing HITL design
philosophy. Get the specific message template, cadence, and state-scoping reviewed by
TCPA counsel before launch — this is the single feature most likely to create
class-action exposure for a client, and derivatively for the agency.

## LLM provider data retention (Q4) — confirms and sharpens the ChatGPT correction

- **Anthropic:** default **30 days** for API users — Anthropic's Privacy Center states
  verbatim: "For Anthropic API users, we automatically delete inputs and outputs on our
  backend within 30 days of receipt or generation, except: When you use a service with
  longer retention under your control (e.g. Files API) [or] When you and we have agreed
  otherwise (e.g. zero data retention agreement)." **The "7 days" figure is a
  mis-transfer** — the Sept 2025 shorter window applied to *consumer* products;
  commercial API customers were explicitly excluded from that change. Flagged
  (usage-policy-violation) content retained up to 2 years; trust-and-safety classifier
  scores up to 7 years. ZDR requires enterprise application/approval, covers eligible
  endpoints (Messages API, Token Counting API) but NOT stateful features (Batch, Files
  API, Managed Agents) nor Console/Workbench; certain newer "Covered Models" require
  mandatory 30-day retention and are excluded from ZDR entirely.
- **OpenAI:** default **up to 30 days** for abuse-monitoring logs, then deleted (unless
  legally required or needed to prevent harm). ZDR and "Modified Abuse Monitoring"
  require prior OpenAI approval, configured at project/org level, not self-service.
  Endpoint nuances: Responses API has 30-day application-state retention by default; the
  videos endpoint is blocked for ZDR; some image models are ZDR-compatible, dall-e-2/3
  are not; extended prompt caching is not ZDR-eligible. Azure OpenAI: same 30-day
  abuse-monitoring default; ZDR/modified monitoring only for Enterprise Agreement or
  Microsoft Customer Agreement customers on dedicated resources, not pay-as-you-go.

**This independently confirms the ChatGPT pass's correction** — both providers default
to 30 days for API/commercial use; the original quick-search "7 days" claim was wrong.

## Build-time/pricing benchmark (Q5)

The scoped pipeline (webhook signature verification, idempotency/dedup gate, direct HTTP
LLM call, JSON schema validation, HITL approval, 60-payload pre-launch test suite, plus
discovery) realistically justifies **$3,000–$12,000+ for a single production pipeline**,
with **$6,000–$10,000 as a defensible mid-point** for a small agency.

- Freelancer rates: Upwork automation engineers $10–100/hr; US-based AI-automation
  consultants $80–150/hr; nearshore LATAM $25–40/hr; n8n/Make dedicated developers
  $50–150/hr.
- Project pricing: basic one-off automation build $1,500–$12,000; local IT-consultant
  custom builds $3,500–9,000/project.
- Estimated hours: discovery 4–10, build (webhook+dedup+LLM+schema+HITL) 20–40, test
  suite construction/runs 8–16, documentation/handoff 4–8 → **~36–74 hours total**. At a
  blended $100–150/hr fully-loaded US rate: **~$3,600–$11,000**, converging with the
  project-pricing ranges above.

**Recommendation:** set the one-time implementation fee at **≥$3,000, target
$5,000–$8,000** per rigorous pipeline. This matches the real engineering scope and
reduces dependence on the contested mandatory retainer for margin.

## Market size/qualification rate (Q6)

**The denominator is knowable; the qualification rate is not, and needs primary
research** — confirms the ChatGPT pass's conclusion, with harder shop-count numbers:

- HVAC: IBISWorld (NAICS 23822a, updated Jan 2026) states 118,433 businesses as of 2025
  (+2.3% from 2024), 120,461 as of 2026 (+1.7%); average ~5.2 employees/business;
  industry market size $158.4bn (2025) / $159.4bn (2026).
- Auto repair: estimates vary by source/NAICS definition — IBISWorld "over 280,000,"
  BLS ~176,000+, Statista ~174,200 (Q4 2023), commercial POI databases ~253,000. Working
  range: **~170,000–280,000**.

**Why the rate can't be estimated responsibly:** the three workflow patterns each
occurring 10+ times/week is a behavioral/operational threshold no public dataset
measures. Adjacent (vendor-sourced, not authoritative) signals exist — Invoca reports
27% of inbound calls to home-services businesses go unanswered; PATLive reports 85% of
callers reaching voicemail never call back, 62% contact a competitor instead — but these
don't translate into a defensible qualification percentage. **Producing a single number
here would be fabrication.** Recommendation: run a short structured survey or 15–20
discovery calls measuring actual weekly volumes per workflow, then compute the
qualification rate empirically.

## Strategic recommendations (new — not present in the ChatGPT pass)

1. **Reposition the retainer immediately (highest priority).** Drop "mandatory." Offer
   two paths: (a) a build-and-own one-time option at a premium ($5,000–$8,000+/pipeline)
   to neutralize the no-lock-in objection; (b) a strongly-incentivized ongoing plan where
   the retainer buys tangibles (credits, monitoring, patch SLA, audits). Keep the
   $499/$1,250/$2,950 tiers but attach them to a build that already stands on its own
   economically. *Threshold to reconsider:* if discovery calls show prospects
   consistently accept mandatory retainers without objection, tighten back toward
   required — but assume they won't until proven.
2. **Re-engineer the missed-call SMS as human-approved, not fully autonomous**, and
   require counsel review before any client launch (detail above).
3. **Set the one-time implementation fee at ≥$3,000, target $5,000–$8,000/pipeline.**
4. **Correct internal materials on LLM retention** to 30-day API default for both
   providers; describe ZDR as an enterprise agreement, not a setting.
5. **Budget for primary market research** (survey + discovery calls) before any TAM/
   revenue projection. Use IBISWorld's ~120,000 HVAC figure and the ~170,000–280,000
   auto-repair range as the denominator only, not a qualification estimate.
6. **Stage go-to-market:** prove the three productized pipelines on 3–5 pilot HVAC shops
   first (cleanest business count, clearest missed-call ROI narrative), then expand to
   auto repair once the qualification rate is actually measured.

## Caveats (from the source report)

Legal content is a starting brief, not advice, and must be reviewed by a qualified
telecom attorney — the law is actively splitting across circuits. Some pricing sources
are vendor/marketing content rather than neutral data. Two of the verified GoHighLevel
competitor pricing pages are unbranded preview/checkout pages, confirming pricing
*structure* rather than a specific named brand. Auto-repair shop counts vary materially
by source/NAICS definition. Q6 is deliberately not answered with a number. LLM retention
policies change frequently — re-verify against provider documentation at contract time.
