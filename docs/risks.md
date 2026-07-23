# Risks

> **Tier:** Mixed — legal/market/business sections are high-level (founder + legal
> counsel); technical/operational sections are low-level (implementer) ·
> **Audience:** founder for the whole doc, plus a lawyer for the legal section
> specifically, plus whoever builds/operates for the technical section ·
> **Use when:** before writing a real contract (legal section), before scaling client
> count (operational section), and as an ongoing gut-check during build (technical
> section). Legal-research candidates are flagged in
> [`research-handoff.md`](./research-handoff.md).

## Legal / liability risk

- **Data handling of sensitive business records.** Pipelines process customer PII,
  invoices, and financial data. The source manual addresses this at the platform level
  (Make "confidentiality" flag, provider no-training defaults, optional Zero Data
  Retention — `review.md` §4.1) but this is a compliance posture, not a guarantee — the
  manual itself flags that Make's webhook queue still transiently holds data during
  transit. Mitigation: don't oversell "your data is safe" to clients without being
  precise about what's actually scrubbed vs. transiently cached vs. retained.
  **Update (2026-07-23, real ChatGPT deep-research pass, see
  `research/2026-07-23-full-deep-research-chatgpt.md`) — this corrects an earlier quick
  web-search finding:** an initial quick-search pass had claimed Anthropic's retention
  dropped to 7 days as of September 2025. A proper deep-research pass could not verify
  that against current first-party Anthropic materials — **Anthropic's current public
  commercial-data documentation states 30 days by default**, same as OpenAI, unless a
  specific ZDR arrangement is in place. Treat the "7 days" figure as unconfirmed/likely
  wrong going forward; the manual's original "30-Day Retention" framing was closer to
  correct than the quick-search correction was. ZDR is real for both providers but is not
  a simple settings flag: OpenAI requires an explicit enterprise request/approval, not
  self-serve; Anthropic's ZDR requires Anthropic approval, is scoped to API usage and
  products using the org's commercial API key (including Claude Code) — it does **not**
  cover Workbench in Console, Claude for Work, Claude Max, or beta products — and
  UserSafety classifier results are retained even under ZDR. Files API, some batch API
  calls, explicit prompt caching, and third-party web-search results can also override or
  fall outside ZDR assumptions for either provider. Don't represent ZDR to clients as a
  checkbox either provider just flips on request, and don't cite a specific retention
  number to a client without checking the provider's current first-party docs at the
  time, not this doc — these numbers move.
- **Liability for automation errors reaching customers or financial records.** The
  manual's stated mitigation is structural — Human-in-the-Loop gates mean nothing writes
  live data or messages customers without human approval (§2.2, §4.2) — combined with a
  contractual **Hallucination & Execution Waiver** shifting responsibility for verifying
  correctness onto the client once it reaches a human. This is a reasonable design but is
  only as strong as the actual MSA language and whether clients genuinely respect the
  review gate in practice (i.e., risk if a client's staff starts rubber-stamping approvals
  without reading them — a real failure mode, not a theoretical one).
- **Upstream system drift exemption.** The manual proposes a no-warranty clause for
  breakage caused by third-party API changes (ServiceTitan, QuickBooks, HubSpot, etc. —
  §4.2). Reasonable to include contractually, but doesn't eliminate the operational cost
  of drift — you'll still need to detect and fix breakage under the SLA windows regardless
  of who's contractually liable, since a broken automation is a churn risk even if you're
  not legally on the hook.
- **No actual legal review has happened.** The MSA clauses in `review.md` §4.2 are drafted
  language proposals, not vetted contract terms. Get an actual lawyer to review before
  using them with a real client — this is the single highest-leverage risk-reduction step
  before signing anyone.
- **TCPA exposure in the missed-call SMS resuscitation pattern specifically.**
  **Updated 2026-07-23 via two independent deep-research passes — informational only,
  not legal advice** (ChatGPT: `research/2026-07-23-full-deep-research-chatgpt.md`;
  Claude/Opus: `research/2026-07-23-full-deep-research-opus.md`, which added sharper
  case-law citations). The worked example in `review.md` §7.3 sends an automated first
  text to someone who just called but has no prior account/relationship. **This is
  genuinely unsettled law, not a clean violation or a clean exemption.** Neither the TCPA
  nor its implementing regs contain an explicit "returning a missed call" exception (per
  TCPA specialist Eric Troutman/Troutman Amin) — the regs require either prior express
  invitation/permission or an established business relationship from a voluntary
  two-way communication, and a "sterile" missed call with no voicemail doesn't cleanly
  satisfy either. Federal rule (47 C.F.R. § 64.1200) requires prior express consent for
  autodialed texts, and prior express *written* consent specifically if the message
  counts as telemarketing.
  **Case law trending favorable but unsettled:** *Butera v. Sugarhouse Real Estate
  Group* (D. Utah, June 30, 2025) held a return contact made "in response to [the
  consumer's] own call" was not "unsolicited" — placing a call without a voicemail "was
  an invitation for a return call" (though the court flagged the opposite would apply if
  the consumer had said they were on the DNC list). *Steidinger v. Blackstone Medical
  Services* (7th Cir., July 14, 2026) held texts are NOT "telephone calls" under
  §227(c)(5), eliminating the private DNC right of action for texts in the Seventh
  Circuit (IL, IN, WI) — but this creates an **unresolved circuit split** with the Ninth
  Circuit's *Howard v. RNC* (2026), and *Steidinger* does **not** immunize texts under
  §227(b), the actual autodialer/written-consent provision that matters most here. The
  often-cited SoundBite FCC safe harbor covers a reply to the consumer's own *text*, not
  a voice call, so it isn't a clean fit either. *Facebook v. Duguid* narrowed the
  autodialer definition in ways that may help simple caller-ID-triggered systems, but
  *McLaughlin Chiropractic v. McKesson* (2025, district courts no longer bound to FCC
  interpretations) keeps this area actively contested. Separately, the FCC's one-to-one
  consent rule was vacated by the Eleventh Circuit in *Insurance Marketing Coalition v.
  FCC* (Jan. 24, 2025) — bundled consent remains permissible, the lead-gen tightening
  did not take effect. **Litigation volume is real and rising:** TCPA class actions rose
  95.2% year-over-year in H1 2025 (1,052 vs. 539) per Troutman Amin/WebRecon — exposure
  is material even where the merits favor the defendant, given how expensive TCPA
  litigation is to fight regardless of outcome.
  **Safer first-message pattern identified:** contextual, non-promotional, identifies
  the business, includes opt-out language (e.g. "Hi, this is [Business]. Sorry we missed
  your call. Reply with what you need and we'll follow up. Reply STOP to opt out.") —
  avoid anything reading as an offer/promotion in that first message, and require
  separate opt-in before any follow-up/marketing sequence. Quiet hours (8am–9pm
  recipient local time) and state mini-TCPA laws (e.g. Florida's) apply independently of
  the federal analysis and should be screened per client state.
  **10DLC registration is mandatory**, not optional, for standard long-code SMS — since
  February 2025 all major US carriers block unregistered A2P traffic outright with no
  grace period (brand registration ~2–3 business days, then separate per-use-case
  campaign registration ~3–7 business days; toll-free avoids 10DLC specifically but not
  consent/opt-out requirements). TCPA penalties run $500–$1,500 per message, not per
  campaign, so exposure scales directly with volume — meaningful given this pattern's
  entire pitch is volume.
  **Design recommendation from both research passes:** make the missed-call text
  **human-triggered (one-tap approve)** rather than fully automated — this strengthens
  the "not an autodialer / individualized response" legal posture and also fits the
  product's existing HITL design philosophy elsewhere. **Do not represent "they called
  us first" as sufficient legal justification** for this pattern with a client — this is
  the single feature most likely to create class-action exposure for a client (and
  derivatively for the agency), and needs actual TCPA counsel review of the specific
  message template, cadence, and state-scoping before it's sold to anyone. The findings
  above are meant as the briefing document for that review, not a substitute for it.

## Technical risk

- **Credit/cost runaway from unguarded loops or webhooks.** The manual's entire Phase 2
  architecture (signature verification → idempotency gate → regex filter → HTTP model
  call, in that order) exists specifically to stop garbage or duplicate payloads from
  reaching paid AI calls. This is a well-designed mitigation, but it depends on disciplined
  implementation on every single client build — a shortcut taken under deadline pressure
  on client #3 is exactly how a credit-burn incident happens.
- **Rate limits scale with Make plan tier** (60/min up to 1,000/min, `review.md` §2) — a
  pipeline built and tested against one client's volume may not gracefully degrade if that
  client's volume spikes unexpectedly (e.g., a marketing campaign drives a burst of
  inbound leads). Worth explicitly load-testing beyond expected volume, not just at it.
- **Testing suite is manual and per-client.** The 50-valid/10-malformed test suite (§3.2)
  is good practice but currently has no described tooling to generate or replay these
  payload sets — as a solo operator or small team, this is a real time cost per deployment
  and a place shortcuts are likely to creep in as you scale client count.

## Market / business risk

- **Unvalidated demand.** Covered in depth in `feasibility.md` — the biggest single risk
  to the business is that the target vertical won't pay implementation + mandatory
  retainer pricing at the volumes assumed, or that qualified prospects (≥10 runs/week,
  unstructured input, structured destination) are rarer than expected.
- **Retainer framed as mandatory.** Positioning the ongoing SLA as non-optional is a
  double-edged design choice: it protects margin and system reliability, but it's also a
  harder sell than an optional add-on, and a client who balks at "mandatory" may walk from
  the deal entirely rather than negotiate down. **Updated 2026-07-23 — two independent
  deep-research passes both recommend the same fix:** offer a one-time build-and-own
  path at a premium ($5,000–$8,000+) alongside the incentivized retainer, rather than
  presenting the retainer as the only path to engagement — see `docs/entrepreneur-notes.md`
  for the full reasoning. Still needs real sales testing to confirm the fix actually
  lands, but this is no longer just "needs testing," it's a specific, sourced
  recommendation to test.
- **Platform dependency risk.** The entire technical model is built on Make.com as the
  orchestration layer. Pricing changes, feature deprecations, or reliability issues on
  Make's side are a single point of failure for the whole business model — not addressed
  anywhere in the source manual.
- **Competitive commoditization.** No-code/AI automation agencies are a fast-growing,
  increasingly crowded space. The differentiation here (engineering rigor, narrow vertical
  focus) is real but not defensible via any moat besides execution quality and reputation
  — a competitor can copy this exact playbook after reading a similar manual.

## Operational risk

- **SLA response-time commitments require actual availability.** The Enterprise tier's
  2-business-hour patch window (§5.1) is a real staffing commitment once there's more than
  one Enterprise client — solo-operator bandwidth is the practical ceiling on how many
  Enterprise-tier clients can be served concurrently without hiring.
- **14-day rollback window creates ongoing dual-maintenance overhead** during that period
  after every deployment (§3.3) — minor but worth factoring into delivery time estimates.
