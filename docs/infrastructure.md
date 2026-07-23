# Infrastructure

> **Tier:** Low-level (build detail) · **Audience:** whoever is actually building the
> pipelines (you, or a contractor/engineer) · **Use when:** setting up accounts and
> scaffolding before building the first client scenario. Assumes the reader has already
> read [`business-idea.md`](./business-idea.md) and doesn't need the pitch re-explained.

What's actually needed to build and run the first client pipeline, distilled from the
technical architecture in `make.com review.md` (primarily §2–4 and §7).

## Core platform accounts

- **Make.com** — the orchestration platform itself. Plan tier determines execution rate
  limits: 60/min (Core), 120/min (Pro), 240/min (Teams), 1,000/min (Enterprise) per
  `review.md` §2. Start on the tier that matches expected client volume; the qualification
  bar of ≥10 runs/week per client is low enough that Core is probably sufficient for early
  clients.
- **LLM provider account(s)** (e.g., Anthropic, OpenAI) — called directly via Make's native
  **HTTP App** module rather than Make's built-in AI connector, specifically to avoid
  Make's token markup and to get precise rate-limit/usage visibility in the provider's own
  dashboard (`review.md` §2.2, "Token Isolation via HTTP Modules"). This means you need a
  developer-level API key and to track spend directly against provider billing, not Make
  credits. **Update (2026-07-23, real ChatGPT deep-research pass, see
  `research/2026-07-23-full-deep-research-chatgpt.md`):** if a client needs Zero Data
  Retention, it's not a self-service toggle on either provider — OpenAI requires an
  explicit enterprise request/approval on supported endpoints only, and Anthropic's ZDR
  requires Anthropic approval and is scoped to API usage and products using the org's
  commercial API key (including Claude Code) — it does not cover Workbench in Console,
  Claude for Work, Claude Max, or beta products. Default retention (absent a ZDR
  arrangement) is **30 days for both providers** — an earlier quick-search pass had
  claimed Anthropic dropped to 7 days, which a deeper research pass could not verify
  against current first-party Anthropic docs and should be treated as incorrect. Budget
  lead time for ZDR approval if a client's compliance needs require it, rather than
  assuming it can be flipped on at deployment time, and verify the current figure against
  the provider's live docs before quoting a number to a client — these terms move.
- **Client-side systems** the pipelines integrate with — varies per client, but the worked
  examples name: a CRM/dispatch tool, an ERP/inventory database, Google Drive (for invoice
  ingestion), Slack (for HITL approval and operational alerts), Twilio (for SMS), and a
  VoIP provider webhook (for missed-call detection). Each new client likely means new
  integration credentials, not a fixed integration set.

## Data store / caching layer

Needed for the idempotency gate (`review.md` §2.2, "Idempotency Key Enforcement"): a
lightweight key-value store to check/write a payload hash with a 24-hour TTL before letting
a run proceed. Make's native **Data Store module** is called out as sufficient — no
external database is strictly required for this piece, though one could be substituted.

## Security-relevant infrastructure

- **Webhook signature verification** — validating `X-Hub-Signature` or an authorization
  header on every inbound webhook, implemented via a native Make data store or a
  deterministic script step (`review.md` §2.2). This needs to exist per integration source,
  since signature schemes vary by upstream platform.
- **Secrets management** — API keys, connection secrets, and webhook tokens stored via
  Make's native encrypted connection profiles or an external vault; explicitly never
  hardcoded into module input fields (`review.md` §3.1).
- **Environment isolation** — separate Sandbox and Production folders inside Make.com per
  client, with a defined promotion path (export blueprint JSON from Sandbox → import to
  Production → remap connection variables → cut over webhook URL → retain the deprecated
  prior version for 14 days as rollback) — full sequence in `review.md` §3.3.

## Testing infrastructure

Not a separate tool, but a process that needs support: generating 50 distinct valid mock
payloads and 10 intentionally malformed payloads per client workflow, to run against the
Sandbox before promotion (`review.md` §3.2). Worth building a small internal
payload-generation habit/toolkit rather than hand-crafting 60 payloads per client from
scratch each time — this is the first candidate for internal tooling investment once you're
past the first couple of clients.

## Alerting / operational visibility

Slack (or Teams) integration is used both for HITL approval interactions and for error/log
alert routing (`review.md` §2.1, §7.1). This effectively becomes the operator's monitoring
dashboard across all client scenarios unless/until something more structured is built.

## What's notably absent from the source material (gaps to fill)

- No mention of a client-facing dashboard, status page, or reporting mechanism — retainer
  clients paying $499–$2,950+/mo may expect visible reporting on what they're getting, not
  just a Slack alert stream in your workspace.
- No CRM/practice-management tooling for running the agency itself (lead tracking, contract
  management, invoicing clients for the retainer). This is business operations
  infrastructure, separate from the delivery-side infrastructure above, and is entirely
  unaddressed in the source manual.
- No mention of a legal/contract tool for issuing the MSA (see `risks.md`) — will need
  either a lawyer-drafted template or a contract tool (e.g., PandaDoc/similar) before the
  first client signs.
