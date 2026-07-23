# Research Handoff Workflow

> **Tier:** Meta (process doc) · **Audience:** you, during the "document area expansion"
> phase · **Use when:** a doc in this packet has a claim marked unverified/inferred that
> needs real citations, current pricing, or legal specifics — things a coding agent
> shouldn't fabricate.

## Why this exists

Everything in this packet started as reasoning from a single source document plus
general priors. Three research passes have since run, all on 2026-07-23: a quick web
search first (shallow, fast, useful for surfacing what mattered), then a real ChatGPT
deep-research pass (`research/2026-07-23-full-deep-research-chatgpt.md`), then an
independent Claude/Opus deep-research pass on the same prompt as a second opinion
(`research/2026-07-23-full-deep-research-opus.md`). The two deep-research passes found
**completely different named competitors from each other** while reaching the same
conclusion on the retainer question — genuine independent corroboration, not just two
runs of the same search — and both agree on the Anthropic data-retention correction
(30 days, not the 7 days the quick pass had claimed). The Opus pass also added concrete
pricing/legal recommendations the ChatGPT pass didn't include. The status table below
reflects both deep-research passes as current. Nothing in the queue needs another round
unless something here becomes decision-critical enough to warrant a third opinion or
direct competitor/legal outreach.

## How to use this — the whole thing in one paste

You don't need to copy questions one at a time. Everything below the line, from
`===BEGIN PROMPT===` to `===END PROMPT===`, is one self-contained block. It carries all
the business context inline (the research tool has no access to this repo or any of
these docs, so nothing can be left implicit) and asks the engine to work through every
open question in order, in a single session.

**On mobile:** open this file on GitHub, tap to select the block, copy it, open
ChatGPT or Claude in the browser, switch on research/deep-research mode if there's a
toggle, paste, and send. When it's done, copy the whole response and send it back to
Claude Code (paste it in chat, or as a file) — it'll get saved into `research/` and
folded back into the docs, same as the first pass.

If a tool has a length limit or credit/turn cap that chokes on the full block, the
**individual blocks** further down repeat the same context per-question so any one of
them still works standalone — just pick the ones still worth running (see status notes).

---

```
===BEGIN PROMPT===

You are doing research to support a real business decision. Take your time, use
multiple independent sources per question where possible, and do not rush to a shallow
answer — this is being used to decide real pricing and legal exposure, not idle
curiosity. Work through the numbered questions below IN ORDER. For each one: answer with
current, sourced information, include a link/citation for every factual claim, note the
publication or last-verified date where relevant, and clearly separate sourced fact from
your own estimate or opinion. If a question genuinely cannot be answered with public web
research (see question 6), say so plainly instead of guessing — do not fabricate a number
to fill the gap.

BUSINESS CONTEXT (read this first, it applies to every question below):

I'm evaluating a business idea called a "Workflow Repair Agency": a Make.com-based
automation consultancy that builds deterministic, human-supervised automation pipelines
for small local trade and field-service businesses — initially targeting HVAC and
automotive repair shops. The pitch: replace manual data entry from unstructured inputs
(free-text emails, scanned PDFs, missed phone calls) with structured output written into
the business's CRM/ERP/dispatch system, with a mandatory human-approval step before
anything reaches a customer or a financial record (no fully autonomous customer-facing
automation). Target clients run the qualifying workflow at least 10 times/week.

Three concrete workflow patterns are the initial product:
1. Inbound quote/lead intake — parsing messy email inquiries into structured CRM records.
2. Invoice/parts extraction — parsing supplier PDF invoices into inventory records.
3. Missed-call SMS follow-up — automatically texting a prospect who called but didn't
   reach anyone and has no prior account with the business, offering help.

Revenue model: a one-time implementation fee (amount not yet set) plus what's currently
positioned as a MANDATORY ongoing monthly maintenance retainer, tiered:
- Essentials: $499/month (12-business-hour patch response, monthly audits, ~10k
  automation-platform credits/month)
- Growth: $1,250/month (4-hour response, weekly audits, ~50k credits/month)
- Enterprise: $2,950+/month (2-hour response, bi-weekly audits, custom credit pool)

Known findings so far, from an earlier quick-search pass — please VERIFY, CORRECT, or
DEEPEN these rather than starting from zero:
- At least one competing automation agency appears to offer a ONE-TIME build with NO
  monthly retainer for comparable trade-business workflows. This is a serious threat to
  the mandatory-retainer pricing model above and is the single most important thing to
  get right in this research pass.
- Existing HVAC CRM/dispatch software (a different product than what this business
  sells, but the closest existing budget line item) was found running roughly
  $29–$1,750/month depending on tier and business size.
- Anthropic's standard Claude API data retention period was found to be 7 days (reduced
  from 30 days in Sept 2025); OpenAI's default remains 30 days; Zero Data Retention (ZDR)
  exists for both but requires enterprise-level request/approval, not a simple toggle.
- A possible legal tension was flagged (see question 3) between automated first-contact
  SMS to someone with no prior relationship and consent requirements — this needs a much
  more rigorous answer than the first pass gave.

QUESTIONS (answer in order):

1. COMPETITOR LANDSCAPE (highest priority — this is the one most likely to change the
   business model): How many real businesses/agencies currently sell Make.com, Zapier,
   n8n, or similar no-code-automation-based services specifically to HVAC, automotive
   repair, or similar local trade/field-service businesses? For as many as you can find,
   report: their pricing model (one-time project fee vs. ongoing retainer vs. both),
   actual price points if published, and whether they require an ongoing retainer as a
   condition of the engagement or offer it as optional. The core question: is a
   MANDATORY ongoing retainer (not optional, not just recommended) a normal, acceptable
   market practice in this specific niche, or is it more common for competitors to offer
   one-time builds with no ongoing commitment?

2. BASELINE SOFTWARE/LABOR SPEND: What do small HVAC and auto-repair shops (roughly
   5–30 employees) typically spend per month on: (a) CRM/dispatch software, (b) any
   existing automation or workflow tools, (c) part-time or outsourced administrative
   labor for tasks like data entry, invoice processing, or answering/returning calls?
   Include ranges and sources, not just software vendor list prices — ideally something
   closer to what businesses actually report paying.

3. LEGAL: MISSED-CALL SMS COMPLIANCE (needs a much more rigorous answer than a
   surface-level TCPA overview): Under the U.S. Telephone Consumer Protection Act (TCPA)
   and any relevant FCC guidance or case law, what are the actual, current legal
   requirements for a business to send an automated first SMS text to someone who just
   called their business phone number, missed a live person, and has no pre-existing
   customer or account relationship with that business? Specifically address: (a) does
   "missed call text-back" in this context count as requiring PRIOR express written
   consent before that first automated message, or is there a recognized exception for
   an immediate, contextually-relevant reply to an inbound call the person themselves
   initiated; (b) how this differs (if it does) from cold marketing texts; (c) what
   specific message content, opt-out language, or 10DLC registration steps would be
   required to run this safely; (d) cite actual FCC rulings, case law, or authoritative
   legal-industry sources, not just SMS-marketing-vendor blog posts, wherever possible.
   State plainly if the law here is genuinely unsettled or fact-dependent rather than a
   clean yes/no. This will still be reviewed by an actual lawyer before being relied on —
   the goal here is the most accurate possible starting brief for that lawyer, not a
   final legal opinion.

4. LLM PROVIDER DATA RETENTION (verify/update the "known findings" above): What are
   Anthropic's and OpenAI's CURRENT (as of today) data retention and Zero Data Retention
   (ZDR) terms for API usage specifically (not their consumer chat products)? Include:
   default retention windows, exactly what ZDR requires to enable (self-service vs.
   enterprise request/approval, any minimum spend or contract requirements), what
   products/endpoints ZDR does and doesn't cover, and whether either policy has changed
   recently enough that older blog posts or articles might be citing stale numbers.

5. BUILD-TIME / PRICING BENCHMARK: For a freelancer or small agency building a
   production-grade Make.com (or comparable no-code platform) automation that includes:
   webhook signature verification, an idempotency/deduplication gate, a direct HTTP call
   to an LLM API (not the platform's built-in AI connector) for data extraction, JSON
   schema validation, a human-in-the-loop approval step, and a formal pre-launch test
   suite (roughly 50 valid + 10 intentionally malformed test payloads) before going live
   — what would be a realistic fully-loaded price range or time estimate for ONE such
   pipeline, end to end, including a discovery/requirements-gathering phase with the
   client? Compare against general automation-freelancer rates if pipeline-specific data
   isn't available, and note the gap between "simple Zapier automation" pricing and what
   this more rigorous scope of work would actually justify.

6. MARKET SIZE / QUALIFICATION RATE (answer only if genuinely possible from public data
   — otherwise explicitly say this needs primary research, don't estimate a number with
   no real basis): Of HVAC and auto-repair shops in the U.S., what portion might
   realistically have at least one of the three workflow patterns above (quote intake,
   invoice extraction, missed-call follow-up) occurring at 10+ times per week? If there's
   no reliable public data to ground this, say so directly rather than inventing a
   plausible-sounding percentage.

Present your answer as one numbered section per question, in order, each with its own
sources. At the end, add a short "Summary of anything that changes prior conclusions"
section highlighting any answer that contradicts or meaningfully updates the "known
findings so far" listed above.

===END PROMPT===
```

---

## Individual blocks (use only if the combined prompt above doesn't fit in one session)

Each of these repeats the same business-context paragraph so it stands alone. Skip any
question already marked resolved below unless you specifically want a deeper re-check.

<details>
<summary>Question 1 — Competitor landscape (resolved 2026-07-23; kept here only for a second opinion or direct outreach follow-up)</summary>

```
I'm evaluating a business idea: a Make.com-based automation agency ("Workflow Repair
Agency") that builds deterministic, human-supervised automation pipelines for small local
trade businesses, initially HVAC and automotive repair shops, replacing manual data entry
from messy emails/PDFs/missed calls with structured CRM/ERP records. Current pricing plan
is a one-time implementation fee plus a MANDATORY ongoing monthly retainer ($499–$2,950+
depending on tier).

Research question: How many real businesses/agencies currently sell Make.com, Zapier,
n8n, or similar no-code-automation services specifically to HVAC, automotive repair, or
similar local trade/field-service businesses? For as many as you can find, report their
pricing model (one-time vs. retainer vs. both), actual prices if published, and whether
an ongoing retainer is mandatory, optional, or not offered at all. Core question: is a
MANDATORY retainer normal/accepted practice in this niche, or do competitors typically
sell one-time builds with no ongoing commitment? Please cite sources and dates.
```
</details>

<details>
<summary>Question 3 — Missed-call SMS legal compliance (researched 2026-07-23; still needs an actual lawyer, not another research pass)</summary>

```
I'm evaluating a business idea: a Make.com-based automation agency building automation
pipelines for HVAC/auto-repair trade businesses. One workflow pattern automatically texts
a prospect who just called the business's phone, missed a live person, and has NO prior
customer or account relationship — offering help via SMS.

Research question: Under the U.S. TCPA and any relevant FCC guidance or case law, what
are the current legal requirements for sending that first automated SMS to someone with
no prior relationship? Specifically: (a) does this require PRIOR express written consent
before the first automated message, or is there a recognized exception for an immediate
contextual reply to a call the person themselves just placed; (b) how does this differ
from cold marketing texts; (c) what message content, opt-out language, or 10DLC
registration would be required to do this safely; (d) cite actual FCC rulings, case law,
or authoritative legal sources, not just SMS-marketing-vendor blog posts. State plainly
if this is genuinely unsettled/fact-dependent rather than a clean yes/no. This will still
go to an actual lawyer before being relied on — the goal is the most accurate possible
briefing document for that review.
```
</details>

<details>
<summary>Questions 2, 4, 5 — already have a first-pass answer; rerun only if you want a deeper check</summary>

See `research/2026-07-23-trade-software-baseline-cost-claude-websearch.md`,
`research/2026-07-23-llm-provider-data-retention-claude-websearch.md`, and
`research/2026-07-23-automation-build-cost-benchmark-claude-websearch.md` for what's
already been found. The combined prompt above includes all three if you want a fresh,
deeper pass on all of them at once instead.

</details>

<details>
<summary>Question 6 — market size / qualification rate (not a research question — flagged so it isn't skipped by mistake)</summary>

This one is intentionally excluded from a standalone block. No public dataset reliably
answers "what fraction of HVAC/auto-repair shops run this specific workflow 10+
times/week" — it needs real conversations with real shop owners, not web research. See
`FRAMEWORK.md` Phase 2.

</details>

## Current status of each question

Two independent deep-research passes ran 2026-07-23 against the combined prompt above —
ChatGPT (`research/2026-07-23-full-deep-research-chatgpt.md`) and Claude/Opus
(`research/2026-07-23-full-deep-research-opus.md`) — and both resolved (or properly
confirmed "not resolvable by web research" on) all 6 questions. Both **supersede** the
earlier quick-`WebSearch` first pass, and both **independently corrected the same
error** from that first pass (Anthropic's data-retention figure — see row 4). Where the
two deep-research passes found different specifics (e.g. different named competitors),
that's noted below as corroboration, not conflict — see `docs/feasibility.md` and
`docs/entrepreneur-notes.md` for the merged view.

| # | Question | Status |
| - | -------- | ------ |
| 1 | Competitor landscape / mandatory retainer viability | ✅ **Resolved 2026-07-23, confirmed by two independent passes** — ChatGPT found 9 competitors, Opus independently found 8 different ones; both conclude mandatory retainer is common but not universal, and both recommend the same fix (one-time build-and-own path + incentivized retainer). See `docs/feasibility.md` and `docs/entrepreneur-notes.md`. |
| 2 | Baseline software/labor spend | ✅ **Resolved 2026-07-23, confirmed by both passes** — closely converging ranges; identified direct automation competitors as the closer pricing comparison than CRM software. |
| 3 | Missed-call SMS legal compliance | ⚠️ **Researched by both passes 2026-07-23** — genuinely unsettled area even with real research; Opus added specific case citations (*Butera*, *Steidinger* vs. *Howard* circuit split, *McLaughlin*, *Insurance Marketing Coalition v. FCC*) and a concrete design recommendation (human-triggered send). **Still requires actual lawyer review before this workflow pattern is sold to anyone** — do not treat as resolved in the legal sense, only as "as researched as this can get without counsel." |
| 4 | LLM provider data retention / ZDR | ✅ **Resolved 2026-07-23, independently confirmed by both passes** — Anthropic's default is 30 days, not 7 days as the quick-search pass had claimed; both deep-research passes agree. See `docs/risks.md` and `docs/infrastructure.md`, both updated. |
| 5 | Build-time/pricing benchmark | ✅ **Resolved 2026-07-23, confirmed by both passes** — closely converging estimates (~$6,000–$9,000/pipeline midpoint); Opus adds a concrete recommendation to set the fee at ≥$3,000, target $5,000–$8,000. |
| 6 | Market size / qualification rate | ⬜ **Confirmed not answerable from public data by all three passes** (quick pass and both deep-research passes agree) — still needs real conversations, per `FRAMEWORK.md` Phase 2. Establishment-count data (Census/IBISWorld) was found as candidate-pool context only, not a frequency answer — see `docs/entrepreneur-notes.md` for the numbers. |

**Nothing left in the queue needs another research round.** The two independent
deep-research passes corroborate each other closely enough that a third opinion isn't
likely to add much, short of direct competitor outreach or actual legal counsel on
question 3. The real remaining blocker across the board is Phase 2's primary research:
talking to actual trade-business owners, and getting question 3 in front of an actual
lawyer.

## After you get a response back

Just send it to Claude Code — paste it in chat or attach it as a file. It'll get saved
into `research/` with the date and source, and the findings will get merged into whichever
docs they affect (`feasibility.md`, `risks.md`, `entrepreneur-notes.md`, etc.), the same
way the first pass was handled. You don't need to do the filing yourself.

## `research/` folder structure (for reference — you don't need to manage this by hand)

```
research/
  YYYY-MM-DD-<short-topic-slug>-<engine>.md
```

Each file starts with the exact prompt used, the engine and date, then the raw response,
unedited. Corrections/synthesis happen in the consuming doc, not in the saved research file.
