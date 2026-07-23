**Prompt used:** the full `===BEGIN PROMPT===`/`===END PROMPT===` block from
`docs/research-handoff.md` (all 6 questions, business context inlined).

**Engine:** ChatGPT deep research mode (real multi-step research, ~995 searches) ·
**Date:** 2026-07-23

**Status:** This supersedes the earlier quick-`WebSearch` pass
(`research/2026-07-23-competitor-pricing-claude-websearch.md`,
`research/2026-07-23-trade-software-baseline-cost-claude-websearch.md`,
`research/2026-07-23-tcpa-sms-compliance-claude-websearch.md`,
`research/2026-07-23-llm-provider-data-retention-claude-websearch.md`,
`research/2026-07-23-automation-build-cost-benchmark-claude-websearch.md`) on every
question it covers, with citations to primary sources rather than blog aggregators. One
finding from the quick pass was flatly **wrong** and is corrected here (see Q4) — the
quick pass should not be trusted over this on any point where they conflict.

---

# Workflow Repair Agency Research Brief

## Executive summary

**Q1 — Competitor landscape.** Market evidence is unfavorable to a mandatory monthly
retainer as a default condition of engagement. Real, currently-active competitors
(Never Miss Work, Gabe Works, CallbackPro, AutoShop SMS AI, Automation Warrior,
TradeWire, Pigeon AI, ContractorOps, CloseLoop) mostly use one-time-only, cancel-anytime,
or hybrid setup-plus-cancellable-recurring pricing. Never Miss Work sells a contractor
package at **$497 one-time, no monthly fee, no contract** — a direct contradiction of
"mandatory retainer." Mandatory long-term retainer as a condition of entry is **not**
the dominant visible norm in this niche.

**Q2 — Baseline software/labor spend.** Mainstream HVAC/field-service software clusters
around **$199–$627/mo** (Jobber, Housecall Pro, Service Fusion); auto-repair software
around **$199–$500+/mo** (Tekmetric, Shopmonkey); ServiceTitan is the expensive outlier
at ~$245–$500/tech/mo plus $5k–$50k+ implementation. Part-time in-house admin labor
(20 hrs/week) runs **~$1,490–$1,783/mo in wages alone**; outsourced VA **~$1,039–
$1,732/mo**; outsourced answering/reception service **~$250–$2,100+/mo**. Directly
competing automation products (not general CRM software) sell for **$8–$297/mo or
$497 one-time** — these, not CRM software, are the closer substitute for pricing
comparison.

**Q3 — Missed-call SMS legal compliance.** Not a clean yes/no. Federal rule requires
prior express consent for autodialed texts, prior *express written* consent if the
message is telemarketing. No primary FCC ruling was found creating a clean missed-call
safe harbor analogous to SoundBite's confirmatory-text exception (which covers a
consumer's own text, not a voice call). Case law (Zani v. Rite Aid, Latner v. Mount
Sinai) supports a narrower "closely related to why the number was given" consent
argument, which helps an immediate, non-promotional, contextual first text — but doesn't
make it safe by default. Post-Duguid ATDS narrowing helps some modern systems, but
McLaughlin v. McKesson and recent circuit rulings (Seventh Circuit Steidinger, July 2026)
make TCPA litigation less predictable, not more settled. **Needs actual legal review
before use** — this report is a briefing document for that review, not a legal opinion.

**Q4 — LLM provider data retention (CORRECTS the earlier quick pass).** OpenAI: default
retention **up to 30 days**, confirmed, ZDR requires approval, not self-serve (matches
the earlier finding). **Anthropic: current primary Anthropic materials say 30 days by
default**, not 7 days — the earlier quick-pass finding of "7 days as of Sept 2025" could
not be verified in current first-party Anthropic sources and should be treated as
**incorrect** going forward. ZDR for Anthropic requires approval, applies only to API
usage and products using the org's commercial API key (including Claude Code), and does
NOT cover Workbench in Console, Claude for Work, Claude Max, or beta products. UserSafety
classifier results are retained even under ZDR.

**Q5 — Build-time/pricing benchmark.** This pipeline's scope (discovery, webhook
signature verification, idempotency, direct LLM API calls, schema validation, HITL gate,
formal 50-valid/10-malformed test suite) is well above "simple Zapier automation"
pricing ($149–$975 one-time for basic work). Estimated realistic price: **$4,000–$10,000
for an experienced freelancer, $7,000–$18,000 for a small agency**, ~40–90 hours,
practical budgeting midpoint **~$6,000–$9,000/pipeline**, 2–4 weeks elapsed.

**Q6 — Market size/qualification rate.** Cannot be responsibly answered from public web
data — establishment counts exist (Census: ~20,587 plumbing/HVAC contractor
establishments with 5–9 employees, 13,148 with 10–19, 8,384 with 20–49 in NAICS 238220;
84,859 general auto-repair establishments in NAICS 811111) but weekly-frequency data
(quote intakes, invoice volume, missed calls) does not exist publicly. Confirms this
needs primary research (owner interviews, call-log sampling, CRM export review, survey),
exactly as flagged in the original handoff doc.

## Competitor landscape detail (Q1)

| Business | Niche | Pricing model | Published pricing | Mandatory retainer? |
|---|---|---|---|---|
| Never Miss Work | Contractors (HVAC, plumbing, electrical, roofing) | One-time option + higher recurring tiers | $497 one-time, no monthly, no contract; or $1,200 setup + $500–800/mo; or $2,500 setup + $1,200–1,500/mo | **No** |
| Gabe Works | Trades | Setup + month-to-month | $497 one-time per automation, then $197–457/mo, cancel anytime | Yes for automation packages, but month-to-month, not long-term |
| CallbackPro | HVAC, roofing, plumbers, landscaping, security, auto repair | Pure monthly subscription | $99–599/mo, 7-day trial, cancel anytime | No long-term |
| AutoShop SMS AI | Auto repair | Pure monthly subscription | $199–499/mo | No long-term contract shown |
| Automation Warrior | Service businesses | Setup + recurring | $997 setup + $497/mo, or $4,500 setup + $1,997/mo; no contracts | No long-term |
| TradeWire | Contractors | Per-automation monthly | $8–189/mo depending on feature; no contracts, cancel anytime | No |
| Pigeon AI | Auto repair | Free-to-paid usage-based | Free tier, then usage-based, no setup fee, no long-term contract | No |
| ContractorOps | Contractors | Monthly subscription | $297/mo, free 14-day pilot, month-to-month | No |
| CloseLoop | Contractors, plumbers, HVAC, roofers, landscaping | Setup + recurring | $1,500 setup + $200/mo, no contracts | No |

**Inference:** requiring a retainer from day one prices against a market norm of
optionality, not compulsion. The retainer needs to be justified by reliability, incident
response speed, formal testing, auditability, and legal/compliance discipline — not
"maintenance exists" — or expect price-shopping pressure toward the no-contract
alternatives above.

## Baseline software/labor spend detail (Q2)

| Spend category | Market range | Notes |
|---|---|---|
| HVAC/field-service CRM-dispatch | ~$200–$700/mo mainstream | Jobber $199–499/mo, Housecall Pro $79–329/mo+users, Service Fusion $245–627/mo; ServiceTitan far above ($245–500/tech/mo + $5k–50k+ implementation) |
| Auto-repair shop software | ~$200–$500/mo | Tekmetric $199–439/mo, Shopmonkey $239–399/mo |
| Standalone automation tools | $20–$200/mo low-to-mid | Zapier Pro from $19.99/mo, Make Core $12/mo/10k credits, n8n Starter €20/mo, Twilio SMS from $0.0083/msg |
| Part-time in-house admin (20 hrs/wk) | ~$1,490–$1,783/mo wages | BLS median wages: CSR $20.59/hr, receptionist $17.23/hr, data entry $18.17/hr |
| Outsourced VA (20 hrs/wk) | ~$1,039–$1,732/mo | Upwork basic VA $12–20+/hr, broader average $18–35/hr |
| Outsourced answering/reception | ~$250–$2,100+/mo | Ruby $250–1,725/mo by minutes; Smith live $300–2,100/mo; Smith AI from $150/mo+per-call |

**Sourced fact:** the closest incumbent budget line item is probably not "automation
agency retainer" — it's either field-service software in the low hundreds/month, or
part-time admin/reception labor in the low thousands/month, or a **direct automation
competitor at $8–$297/mo or $497 one-time** (see Q1). The $499/mo Essentials tier is high
relative to basic Make/Zapier tooling and direct competitors, low-to-mid relative to
human labor replacement.

## Missed-call SMS compliance detail (Q3)

- Federal rule (47 C.F.R. § 64.1200): prior express consent for autodialed texts; prior
  express *written* consent if the message is telemarketing (encourages purchase/rental
  of goods/services).
- Case law supports a narrower consent theory: messages "closely related" to why the
  number was given can fall within existing consent (Latner v. Mount Sinai, a single flu-
  shot reminder). No primary authority found that a missed call alone always creates
  consent for an automated text-back to a new prospect.
- SoundBite's FCC safe harbor covers a single confirmatory text replying to the
  consumer's own **text**, not a voice call — not a clean fit for this workflow.
- Facebook v. Duguid narrowed the ATDS definition (random/sequential number generator
  required), which may help systems that just reply to known caller IDs — but
  McLaughlin v. McKesson (courts no longer bound to FCC interpretation) and a July 2026
  Seventh Circuit ruling (Steidinger, narrows one Do-Not-Call theory in that circuit)
  keep this area unsettled rather than resolved.
- **Operationally safer first-text pattern:** "Hi, this is [Business Name]. Sorry we
  missed your call. If you still need help, reply with a brief description and our team
  will follow up. Reply STOP to opt out." — contextual, non-promotional, opt-out
  included. Avoid "Book now," coupons, or nurture sequences sent without a reply — those
  read as telemarketing.
- **10DLC:** required for standard long-code SMS (brand + campaign registration, sample
  messages, consent/message-flow description; campaigns submitted after 2026-06-30 also
  need public privacy-policy/terms URLs; ~10–15 day review). Toll-free avoids 10DLC
  specifically but not consent/opt-out/carrier-filtering requirements generally.
- **Bottom line for lawyer review:** do not represent "they called us first" as a
  sufficient nationwide legal conclusion for automated first-contact SMS to new
  prospects. A single, immediate, contextual, non-promotional reply has the stronger
  argument but remains fact-dependent.

## LLM provider data retention detail (Q4) — corrects the earlier quick pass

- **OpenAI:** up to 30 days default for most API inputs/outputs (confirmed, matches
  earlier finding). ZDR requires approval, not self-serve. Endpoint-specific caveats:
  `/v1/responses` has 30-day application-state retention by default or when
  `store=true`; ZDR forces `store=false`; background mode is NOT compatible with ZDR;
  Code Interpreter cannot be used with ZDR; some image generation is ZDR-compatible only
  for specific models; Assistants/Threads/Vector-Stores kept until deleted, then removed
  30 days after deletion.
- **Anthropic:** current public commercial-data materials say Anthropic **automatically
  deletes inputs/outputs within 30 days** of receipt/generation by default, unless
  otherwise agreed (e.g. a ZDR arrangement) or unless longer retention is needed for
  policy enforcement/law. Flagged usage-policy-violation content may be retained up to 2
  years; trust-and-safety classifier scores up to 7 years. ZDR is available to some
  enterprise API customers subject to Anthropic approval, applies only to the Anthropic
  API and products using the org's commercial API key (including Claude Code) — does NOT
  cover Workbench in Console, Claude for Work, Claude Max, or beta products unless
  explicitly agreed. UserSafety classifier results are retained even under ZDR. Files
  API, some batch API calls, explicit prompt caching, and third-party websites accessed
  via web search can override or fall outside ZDR assumptions.
- **The earlier quick-pass claim that Anthropic's default dropped to 7 days (Sept 2025)
  could NOT be verified against current first-party Anthropic materials, which state 30
  days.** Treat the 7-day figure as unconfirmed/likely incorrect going forward — don't
  represent it to a client without a current contract/DPA specifically stating otherwise.

## Build-time/pricing benchmark detail (Q5)

Basic Zapier work sells for $149–$975 one-time (Automation Elves, Hispanic Market
Advisors) — much simpler than this packet's scoped deliverable. Market rates for capable
talent: mid-market specialists ~$65–110/hr, senior/architect ~$110–180/hr; no-code
freelancers ~$60–100/hr, developers ~$100–160/hr, boutique agencies ~$120–180/hr;
broader consultant range $75–200/hr or $150–350/hr for specialist agencies.

| Workstream | Estimated hours |
|---|---:|
| Discovery and requirements mapping | 4–8 |
| Trigger/auth layer (webhook + signature verification) | 4–10 |
| Idempotency and dedupe controls | 4–8 |
| LLM extraction + prompt/schema work | 8–20 |
| Human approval step and handoff UX | 4–10 |
| Validation and write-back logic | 6–12 |
| Formal test suite and launch hardening (50 valid + 10 malformed) | 10–20 |
| Documentation, training, go-live | 4–8 |

**Estimate:** $4,000–$10,000 (experienced freelancer) to $7,000–$18,000 (small agency),
practical budgeting midpoint ~$6,000–$9,000/pipeline, ~40–90 hours, 2–4 weeks elapsed.
Pricing materially below this suggests template reuse or under-scoped QA; materially
above it needs to be justified by real compliance/reliability guarantees.

## Market size/qualification rate detail (Q6)

Confirmed: cannot be answered responsibly from public web data. Census Bureau 2023
County Business Patterns (candidate-pool sizing only, NOT frequency data): NAICS 238220
(plumbing/heating/AC contractors) — 20,587 establishments with 5–9 employees, 13,148 with
10–19, 8,384 with 20–49. NAICS 811111 (general automotive repair) — 84,859 employer
establishments; broader NAICS 8111 (automotive repair and maintenance) — 169,572
employer establishments. None of this indicates weekly frequency of quote intakes,
invoice processing, or missed calls — that requires primary research (owner interviews,
call-log sampling, CRM export review, or a survey), per the original handoff framing.

## What changes prior conclusions

1. **Pricing-model viability** — strengthened concern: clear evidence of real,
   trade-focused competitors with no-monthly or cancel-anytime pricing. Mandatory
   retainer looks less normal than assumed, not more.
2. **Software-spend baseline** — mostly confirmed, refined: mainstream systems cluster
   in the low hundreds/month; ServiceTitan and enterprise tiers go well above the
   earlier rough range once per-tech pricing and implementation are counted. Also
   surfaces a *closer* substitute than CRM software: direct automation competitors at
   $8–$297/mo or $497 one-time.
3. **Missed-call SMS legal risk** — confirmed and sharpened: no clean safe harbor exists;
   real risk that scales with the volume this workflow pattern is designed around; needs
   counsel before launch, not just better contract language.
4. **Anthropic data retention — factual correction**, not just a refinement: 30 days
   default, not 7 days. This is the most important correction in this pass, since it
   directly reverses a specific number already written into `docs/risks.md` and
   `docs/infrastructure.md` from the earlier quick-search pass.
