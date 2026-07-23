**Prompt used:**
> TCPA compliance automated SMS text message missed call follow up business

**Engine:** Claude Code `WebSearch` tool (standard web search) · **Date:** 2026-07-23

**This is informational research only, not legal advice, and does not substitute for the
actual lawyer review this packet already flags as required before any real client signs
anything (`docs/risks.md`, `FRAMEWORK.md` Phase 4).**

**Raw findings:**

The TCPA requires **prior express consent** before sending automated text messages via an
autodialer — this applies not just to marketing texts but potentially to transactional/
informational messages too, if sent through an autodialer. For a missed-call text-back
flow specifically, several sources state businesses need express written consent from the
recipient before texting back. Messages must include opt-out instructions (STOP/
UNSUBSCRIBE) and honor opt-out requests immediately. Businesses texting from standard
10-digit numbers are expected to register under the 10DLC system for deliverability and
brand verification. Penalties: $500/violation (unintentional) up to $1,500/violation
(willful) — per message, not per campaign, so exposure scales with volume.

**Direct relevance to this packet:** the missed-call SMS resuscitation pattern
(`make.com review.md` §7.3) sends an unsolicited first text to someone who called but
wasn't a prior customer — i.e., there is no pre-existing consent relationship at the
moment that first text is sent. Several sources frame missed-call text-back as requiring
prior express written consent, which is a real tension with the "text back someone who
just called" pattern as described in the source manual. This is exactly the kind of
finding that needs actual legal review before this specific workflow pattern is sold to
a client — the search results are not unanimous or authoritative enough to resolve
whether existing case law/FCC guidance treats a same-context missed-call callback
differently from a cold marketing text, and that distinction matters a lot here.

Sources:
- [Is Missed Call Text Back TCPA Compliant for Business?](https://www.justanswer.com/law/qfex0-i-d-talk-lawyer-tcpa-laws-no-want.html)
- [TCPA Compliance Checklist: SMS Texting Rules Guide | Textedly](https://www.textedly.com/sms-compliance-guide/tcpa-compliance-checklist)
- [TCPA Compliance for SMS Marketing: How to Avoid Fines - TermsFeed](https://www.termsfeed.com/blog/tcpa-compliance/)
- [SMS compliance checklist: Does TCPA apply to business customers?](https://www.text-em-all.com/blog/sms-compliance-checklist-for-tcpa-safe-business-messaging)
- [TCPA text messages: Rules and regulations guide for 2026 - ActiveProspect](https://activeprospect.com/blog/tcpa-text-messages/)
