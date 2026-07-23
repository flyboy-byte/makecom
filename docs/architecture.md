# Reference Architecture (vertical-agnostic)

> **Tier:** Low-level (technical design) · **Audience:** whoever is designing a pipeline
> for a specific client, in any vertical · **Use when:** scoping a new client's build,
> or evaluating whether a new candidate vertical actually fits the technical model —
> not just the business model. Complements
> [`infrastructure.md`](./infrastructure.md), which covers *accounts and setup*; this
> doc covers *the shape of the pipeline itself*.

## Why this doc exists

`make.com review.md` describes one hardened architecture (§2.1) and three worked
examples (§7) — but all three examples happen to be HVAC/auto-repair flavored, which
made it easy to read the architecture as HVAC-specific when it isn't. Per
`docs/business-idea.md`'s reframe around the 3-Trait Qualification Test, the target
market is now defined by workflow *shape*, not industry — this doc makes the technical
side of that claim concrete by separating what's **fixed** (true for every client,
regardless of vertical) from what's **pluggable** (varies per client, and is where actual
domain knowledge of that specific business gets applied).

## The eight stages

Every pipeline this business builds — regardless of vertical — is an instance of the
same eight-stage shape, taken directly from `make.com review.md` §2.1 and generalized:

| # | Stage | Fixed (always true) | Pluggable (varies per client) |
|---|-------|----------------------|-------------------------------|
| 1 | **Trigger** | Some inbound event kicks off the run | The specific event type: a webhook (email parser, form submit, VoIP call-status), a file-watch (Drive/Dropbox folder), a polling check — whatever produces this client's unstructured input |
| 2 | **Signature/auth verification** | Every inbound trigger is cryptographically or credential-verified before anything downstream runs; unverified requests are dropped with an immediate rejection, not processed | The specific signature scheme (varies by upstream platform — `X-Hub-Signature`, HMAC, API-key header, OAuth token) |
| 3 | **Idempotency/dedupe gate** | A hash of the payload is checked against a cache before proceeding; duplicates are acknowledged and halted, not reprocessed | What fields compose the hash (e.g. event ID + phone number for a call; invoice number + supplier ID for a document) |
| 4 | **Deterministic pre-filter** | Cheap, non-AI rules reject obviously invalid input *before* any paid model call — this is the credit-burn guardrail | The specific filter logic (regex, required-field check, file-type check) — entirely dependent on what "obviously invalid" means for this client's input |
| 5 | **Extraction** (direct LLM HTTP call) | Unstructured input goes in, structured JSON comes out, via a direct HTTP call to the model provider (never Make's native AI connector — cost/control reasons per `review.md` §2.2) | The extraction prompt and the destination JSON schema — this is where the pipeline actually encodes domain knowledge of the client's business |
| 6 | **Schema validation** | Model output is validated against a strict schema before anything downstream trusts it; invalid JSON routes to an error/alert path, not silently forward | The schema itself, which is derived directly from stage 5's domain knowledge |
| 7 | **Human-in-the-loop gate** | No pipeline writes live data or messages an end customer without a person approving first — this is non-negotiable across every vertical (liability firewall, not just UX — see `docs/risks.md`) | The approval surface (Slack button, in-app "pending review" queue, email digest) and who on the client's team is the approver |
| 8 | **Destination write** | Approved output lands in the client's actual system of record | The specific destination API (CRM, ERP, dispatch software, practice-management system, case-management system — whatever the client already runs on) |

## What this makes explicit

- **The actual technical moat is stages 1–4 and 6–7** — signature verification,
  idempotency, pre-filtering, schema validation, and the HITL gate. None of that changes
  based on industry. This is the part of `docs/business-idea.md`'s "engineering
  discipline as the differentiator" argument that's literally true regardless of vertical.
- **Stages 5 and 8 are where vertical/client-specific domain knowledge actually lives.**
  This is the technical mirror of the caveat already in `docs/business-idea.md`: the
  qualification test tells you a business has the right workflow *shape*, but designing
  stages 5 and 8 for a real client requires understanding that specific business's data
  and systems — no amount of abstraction removes that.
- **A new vertical is technically viable the moment you can define stages 1–8 concretely
  for it** — which is a lower bar than it might sound like, precisely because 6 of the 8
  stages are fixed. Use this as a second-pass technical check after the 3-Trait
  Qualification Test (business fit) — see `docs/vertical-playbook.md`.

## The three worked examples as instances of this shape

To show the abstraction isn't hand-wavy, here's how `make.com review.md`'s three
existing worked examples (§7.1–7.3) map onto the eight stages — useful as a template
when scoping a genuinely new vertical:

| Stage | §7.1 Quote intake | §7.2 Invoice extraction | §7.3 Missed-call SMS |
|---|---|---|---|
| Trigger | Inbound email webhook | Drive file-watch | VoIP call-status webhook |
| Verify | Webhook signature | N/A (Drive auth) | VoIP provider signature |
| Dedupe | Payload hash, 24h TTL | N/A in source example (gap — see below) | Phone number + timestamp hash |
| Pre-filter | Regex for trade-relevant terms | N/A in source example (gap) | CRM lookup: new vs. existing contact |
| Extract | Name/phone/parts from email body | Line items from PDF (vision model) | N/A — no extraction, just a lookup |
| Validate | JSON schema for CRM fields | N/A in source example (gap) | N/A |
| HITL | Draft CRM record, Slack alert | N/A in source example (gap) | N/A — this pattern is flagged in `docs/risks.md` as needing to become human-triggered, not fully automated |
| Write | CRM create-lead | Inventory database upsert | Twilio SMS send + CRM placeholder |

**Worth noting honestly:** §7.2 and §7.3 as originally written skip some stages (no
explicit dedupe/pre-filter/HITL in the invoice example; no real extraction/validation in
the SMS example, and per `docs/risks.md` it should gain a human-approval stage it
currently lacks). That's not this doc contradicting the source manual — it's evidence
the "eight fixed stages" framing is doing real work: it exposes gaps in the *existing*
examples that the narrative description glossed over, which is exactly the kind of thing
worth catching before scoping a new client, in any vertical.

## Using this for a new vertical

Before deep-researching or pitching a new vertical, sketch this table for it. If you
can't yet fill in stages 5 (schema) and 8 (destination) with something concrete, that's
a sign you don't yet have the domain knowledge to build for that vertical — go get it
(via `docs/vertical-playbook.md`'s discovery process) before doing anything else.
