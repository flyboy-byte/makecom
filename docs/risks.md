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
  **Update (2026-07-23, web search, see
  `research/2026-07-23-llm-provider-data-retention-claude-websearch.md`):** the manual's
  "30-Day Retention" figure is now stale for Anthropic specifically — standard Claude API
  retention dropped to **7 days** as of September 2025. OpenAI's default remains 30 days.
  ZDR is real for both but is not a simple settings flag: for OpenAI it requires an
  explicit enterprise request and approval on supported endpoints only; for Anthropic
  it's scoped to eligible API usage and Claude Code on Claude Enterprise, not blanket
  chat-interface coverage, and certain "Covered Models" are excluded from ZDR entirely.
  Don't represent ZDR to clients as a checkbox either provider just flips on request.
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
  **New finding (2026-07-23, web search, informational only — not legal advice, see
  `research/2026-07-23-tcpa-sms-compliance-claude-websearch.md`):** the worked example in
  `review.md` §7.3 sends an automated first text to someone who just called but has no
  prior account/relationship — several sources describe missed-call text-back as needing
  *prior express written consent* before that first automated text, which is in direct
  tension with the pattern as designed (the whole point is texting someone with no prior
  relationship). TCPA penalties run $500–$1,500 per message, not per campaign, so exposure
  scales with volume — meaningful given this pattern's entire pitch is volume. This needs
  actual legal review before this specific pattern is sold to any client, not just the
  general MSA review already flagged above — flag it as its own line item, since it could
  mean this particular worked example needs redesigning (e.g., an opt-in-gated first
  message) rather than just needing better contract language.

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
