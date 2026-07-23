# The Idea

> **Tier:** High-level · **Audience:** founder/decision-maker, and anyone being pitched
> the idea (co-founder, early advisor, investor) · **Use when:** deciding whether to
> pursue this at all, or explaining the idea to someone new in under 5 minutes.
> See [`documentation-guide.md`](./documentation-guide.md) for how this fits with the
> rest of the packet.

## One-line pitch

A "Workflow Repair Agency" that replaces messy, manual, error-prone business processes at
local trade and service companies (HVAC, automotive repair, similar field-service trades)
with deterministic, human-supervised automation pipelines built on Make.com — sold as a
one-time build plus a mandatory ongoing maintenance retainer.

## Who it's for

Small-to-mid-size local trade businesses that:

- Run a repeatable operational workflow at real volume (the source manual sets a bar of
  ≥10 executions/week — see [`feasibility.md`](./feasibility.md) for whether that's the
  right threshold).
- Currently do that workflow by hand: someone reading emails, retyping data into a CRM/ERP,
  chasing missed calls, or manually keying supplier invoices into inventory systems.
- Have unstructured input (free-text emails, PDFs, call transcripts) that needs to land in
  a structured system (CRM, ERP, dispatch software) — i.e., an extraction/mapping problem,
  not an open-ended "AI assistant" problem.

Explicitly **not** the target: businesses wanting an open-ended AI chatbot, or businesses
whose process hasn't been mapped/diagrammed yet. The source manual is emphatic that
"vague AI executive assistant" and "fully autonomous customer service bot" pitches are
disqualifying — see the vertical mapping table in `make.com review.md` §1.4.

## Why this framing (vs. generic "AI automation agency")

The generic version of this business (broad "we automate anything with AI") is crowded and
commoditized. This version narrows on three specific, defensible choices:

1. **Narrow vertical + narrow workflow shapes.** Three concrete workflow patterns are
   named explicitly: inbound quote/lead intake, invoice/parts extraction, missed-call
   text follow-up (`make.com review.md` §7.1–7.3). Narrow scope is easier to sell, easier
   to productize, and easier to get right repeatedly.
2. **Engineering discipline as the differentiator.** Most no-code automation shops ship
   fragile scenarios that break on the first malformed input. This model's actual product
   is reliability: webhook signature verification, idempotency keys, schema validation,
   a formal 50-run/10-failure test suite before go-live (§2–3). That's a real technical
   moat against competitors who just drag-and-drop a demo together.
3. **Human-in-the-loop as a liability firewall, not just a UX choice.** No automation
   writes live data or messages customers without a human approval step (§2.2, §4.2).
   This is simultaneously a trust-building sales point and a legal risk mitigation — see
   [`risks.md`](./risks.md).

## Revenue model

Two-part, not project-only:

- **One-time implementation fee** for the initial build (discovery → sandbox build →
  testing → deployment). Amount left as a blank in the SOW template (`review.md` §6) —
  needs to be filled in based on your own cost/time estimate, see `feasibility.md`.
- **Mandatory ongoing SLA retainer**, tiered:
  - Essentials — $499/mo (12-hr patch window, monthly audits, 10k credit pool)
  - Growth — $1,250/mo (4-hr patch window, weekly audits, 50k credit pool)
  - Enterprise — $2,950+/mo (2-hr patch window, bi-weekly audits, custom credit pool)

  (Full tier detail in `review.md` §5.1.) The retainer is framed as mandatory, not
  optional — the underlying argument is that unmaintained automations rot as upstream
  APIs drift, so a retainer isn't upsell, it's a required part of the deliverable. Whether
  clients will accept "mandatory" as a term, or whether it needs softer framing, is an
  open sales question — see `entrepreneur-notes.md`.

## What's genuinely novel here vs. what's just good practice

Worth being honest about, since this affects how defensible the business is:

- The **engineering practices** (idempotency, signature verification, staged
  testing, HITL gates) are not novel — they're standard practice for any production
  webhook system, just rarely applied by no-code automation freelancers. The moat is
  applying rigor where competitors don't, not the rigor itself.
- The **vertical focus + productized retainer** structure is a well-worn playbook in the
  agency world (see "productized service" / niche agency models generally). Novelty is
  in execution and vertical choice, not the business model shape.
- The **specific workflow patterns** (missed-call SMS resuscitation, invoice line-item
  extraction, quote intake parsing) are concrete and testable — this is the part worth
  validating first, since it's the part that actually determines whether real businesses
  will pay.
