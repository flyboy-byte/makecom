# Research Handoff Workflow

> **Tier:** Meta (process doc) · **Audience:** you, during the "document area expansion"
> phase · **Use when:** a doc in this packet has a claim marked unverified/inferred that
> needs real citations, current pricing, or legal specifics — things a coding agent
> shouldn't fabricate.

## Why this exists

Everything written so far in this packet is reasoning from a single source document
(`make.com review.md`) plus general priors — there's no live market data, no competitor
pricing, no legal review, no current provider terms behind any of it. The docs say so
explicitly wherever this applies ("unverified," "inferred," "not addressed in the source
material"). The right tool for closing those gaps is a **deep research engine with live
web access** (Claude.ai research mode, ChatGPT research mode) run by you in the browser —
not this coding session, which can browse but shouldn't be the tool of record for
claims that need to be traceable, current, and citable months from now.

## What qualifies for handoff

Something is a good handoff candidate if it's **externally verifiable** (a real answer
exists somewhere on the web or in a regulation) and **not something this coding session
should guess at**. Internal decisions (pricing you're choosing to charge, which vertical
to target first) are not handoff candidates — those are entrepreneur judgment calls, not
research questions, and belong in `entrepreneur-notes.md` as decisions, not delegated out.

## Current handoff queue

Pulled directly from open items flagged in the other docs. Update this table as items are
resolved or new ones come up.

| # | Question | Source doc | Suggested engine | Status |
| - | -------- | ---------- | ----------------- | ------ |
| 1 | How many existing "Make.com/Zapier automation agency" competitors serve HVAC/auto-repair specifically, and at what price? | `feasibility.md` | Either — broad web survey | ✅ **Resolved 2026-07-23** (standard web search, not full deep-research — see `research/2026-07-23-competitor-pricing-claude-websearch.md`). Found a no-retainer competitor — this materially threatens the mandatory-retainer premise; consider re-running as a proper deep-research pass or direct competitor outreach given how load-bearing this turned out to be. |
| 2 | What do trade businesses currently spend on CRM/dispatch software, part-time admin labor, or existing automation tools (baseline to price against)? | `entrepreneur-notes.md` | Either | ✅ **Resolved 2026-07-23** — see `research/2026-07-23-trade-software-baseline-cost-claude-websearch.md`. |
| 3 | Current legal landscape for automated SMS outreach to leads (TCPA and similar) as it applies to the missed-call-resuscitation workflow (`review.md` §7.3) | `risks.md` | ChatGPT (often stronger on current US regulatory specifics) — treat as a research starting point, not legal advice | ⚠️ **First pass done 2026-07-23** (see `research/2026-07-23-tcpa-sms-compliance-claude-websearch.md`) — surfaced a real tension between the workflow-as-designed and consent requirements. **Still needs actual lawyer review** — do not treat as resolved. |
| 4 | Current Anthropic and OpenAI API data retention / Zero Data Retention terms and how to actually request ZDR (referenced in `review.md` §4.1) | `risks.md`, `infrastructure.md` | Claude (own provider docs, likely more precise on Anthropic specifics) | ✅ **Resolved 2026-07-23** — see `research/2026-07-23-llm-provider-data-retention-claude-websearch.md`. Anthropic's retention figure in the source manual was stale (30d → now 7d). |
| 5 | Typical fully-loaded build time for a webhook + idempotency + LLM-extraction + CRM-write pipeline, to sanity-check the implementation fee | `feasibility.md` | Either | ✅ **Resolved 2026-07-23** — see `research/2026-07-23-automation-build-cost-benchmark-claude-websearch.md`. Gives a rough floor only; real time-tracked build still recommended. |
| 6 | Fraction of realistic trade-business prospects that plausibly clear the ≥10 runs/week volume threshold (`review.md` §1.3) | `feasibility.md` | Neither — this needs primary research (talking to real business owners), not web research | ⬜ Not started — still requires real conversations, not research. |

**Note on how rows 1–5 were actually resolved:** these were run through Claude Code's own
`WebSearch` tool during this session, not a browser-based Claude.ai/ChatGPT deep-research
mode as originally specified in this doc's process below. That's a faster but shallower
substitute — standard web search rather than multi-step deep research. Good enough for a
first pass and for surfacing which questions turned out to be load-bearing (row 1
especially), but treat anything decision-critical here as still worth a proper
deep-research pass or direct outreach before finalizing pricing or contract terms.

## Handoff procedure

1. **Pick one row** from the queue above — don't batch multiple unrelated questions into
   one research session; it dilutes the result and makes sourcing harder to track.
2. **Write the prompt** using the template below and run it in the browser, at
   claude.ai (research/deep research mode) or chatgpt.com (deep research mode) per the
   suggested engine column. Ask for citations/sources explicitly — an answer without a
   source is not more trustworthy than what's already in these docs.
3. **Save the raw output** into `research/` (see folder structure below) before doing
   anything else with it — keep the source material even after you extract a summary.
4. **Merge findings back** into the originating doc: replace the "unverified/inferred"
   language with the finding, and add a citation line pointing at the saved file in
   `research/`. Do not delete the fact that it was once unverified — just update the
   status; the audit trail of what was assumed vs. confirmed is useful later.
5. **Update this queue** — mark the row resolved (or strike it) and add any new questions
   the research surfaced.

## Prompt template

```
I'm evaluating a business idea: a Make.com-based automation agency that builds
deterministic, human-supervised workflow pipelines for [target vertical — e.g. HVAC and
auto-repair trade businesses], covering [workflow pattern — e.g. missed-call SMS
follow-up / invoice PDF extraction / inbound quote intake].

Research question: [paste the question from the handoff queue table]

Please answer with current, sourced information — include links or citations for every
claim, note publication/last-verified dates where relevant, and flag anything that's
opinion/estimate rather than sourced fact.
```

## `research/` folder structure

Raw research session output gets saved as:

```
research/
  YYYY-MM-DD-<short-topic-slug>-<engine>.md
```

e.g. `research/2026-07-22-tcpa-sms-compliance-chatgpt.md`. Each file should start with
the exact prompt used, the engine and date, then the raw response. Don't edit the raw
response after saving — corrections/updates go in the doc that consumes it
(`risks.md`, `feasibility.md`, etc.), not in the source research file.
