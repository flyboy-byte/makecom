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
  **Updated (2026-07-23, real ChatGPT deep-research pass — informational only, not legal
  advice, see `research/2026-07-23-full-deep-research-chatgpt.md`):** the worked example
  in `review.md` §7.3 sends an automated first text to someone who just called but has no
  prior account/relationship. This is genuinely unsettled, not a clean violation or a
  clean exemption: federal rule (47 C.F.R. § 64.1200) requires prior express consent for
  autodialed texts and prior express *written* consent specifically if the message counts
  as telemarketing; case law (e.g. Latner v. Mount Sinai) supports consent extending to
  messages "closely related" to why the number was given, which helps an immediate,
  non-promotional, purely contextual first text — but no primary FCC ruling was found
  creating a clean missed-call-specific safe harbor (the often-cited SoundBite ruling
  covers a reply to the consumer's own *text*, not a voice call). Facebook v. Duguid
  narrowed the autodialer definition in ways that may help simple caller-ID-triggered
  systems, but McLaughlin v. McKesson and a July 2026 Seventh Circuit ruling keep this
  area actively contested rather than settled. **Safer first-message pattern identified:**
  contextual, non-promotional, identifies the business, includes opt-out language (e.g.
  "Hi, this is [Business]. Sorry we missed your call. Reply with what you need and we'll
  follow up. Reply STOP to opt out.") — avoid anything that reads as an offer/promotion
  in that first message. **10DLC registration is required** for standard long-code SMS
  (brand + campaign registration, sample messages, consent-flow description; toll-free
  avoids 10DLC specifically but not consent/opt-out requirements). TCPA penalties run
  $500–$1,500 per message, not per campaign, so exposure scales directly with volume —
  meaningful given this pattern's entire pitch is volume. **Do not represent "they called
  us first" as sufficient legal justification** for this pattern with a client — this
  needs actual legal review before it's sold to anyone, and the finding above is meant as
  the briefing document for that review, not a substitute for it.

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
  the deal entirely rather than negotiate down. Needs real sales testing.
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
