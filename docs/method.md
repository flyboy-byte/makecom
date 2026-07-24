# The Method

> **Tier:** Meta (about how the packet was made, not what it says) ·
> **Audience:** anyone who cares more about the process than the business —
> including future-you starting a different idea from scratch ·
> **Use when:** you want to reuse this approach on something else, or you want an
> honest account of which parts of it earned their keep.

## Why this doc exists

This project has two outputs, and only one of them is the business.

The first is the **specimen**: an evaluation of a specific idea — a Make.com automation
practice — which is unvalidated, sitting at Phase 2, and may never go anywhere. Every
other document in this packet serves that evaluation.

The second is the **method**: a repeatable way of taking a raw, unstructured spark and
turning it into something you can actually make a decision against. That output is
finished, has been through a full cycle including self-correction, and has already been
extracted into a reusable form. It is also the part most likely to be useful to anyone
who isn't building an automation agency.

Until now the method was implicit — spread across the phase model in
[`../FRAMEWORK.md`](../FRAMEWORK.md), the tier system in
[`documentation-guide.md`](./documentation-guide.md), and the handoff process in
[`research-handoff.md`](./research-handoff.md), with no page that named it as a thing.
This is that page.

## The method in five moves

**1. Capture the spark verbatim.** Keep the original source — the note, the PDF, the
manual — unedited and in the repository. Here that's
[`make.com review.md`](../make.com%20review.md). Everything downstream cites it by
section rather than restating it, so there's always a traceable line back to what was
actually claimed versus what got inferred later.

**2. Split by altitude, not by topic.** Every document declares a tier, an audience, and
a "use when" in its first three lines. High-level answers *should this exist*; low-level
answers *how would it get built*; meta describes the packet itself. This is the single
cheapest thing in the method and the one that pays off most — it stops pitch material
from drifting into implementation detail and vice versa, and it means a reader can find
the one page relevant to their question without reading the set. See
[`documentation-guide.md`](./documentation-guide.md).

**3. Gate progress on things that happen outside the documents.** The phase model in
[`../FRAMEWORK.md`](../FRAMEWORK.md) advances only on a conversation, a test, or a
signature — never on more writing. Without this, a packet like this becomes an elaborate
way of avoiding contact with reality: it feels like progress because the document count
goes up.

**4. Queue what you can't verify instead of guessing it.** Any claim that needs live
market data, current pricing, or legal specifics goes into
[`research-handoff.md`](./research-handoff.md) as an explicit question rather than being
asserted. The queue then gets handed to an external research engine with live web access,
and the raw output is saved unedited in [`../research/`](../research/) before anything is
merged. This is what makes the difference between a document that sounds researched and
one that is.

**5. Merge findings back, and keep the corrections visible.** When research contradicts
the packet, the packet changes — but the fact that it once said something different stays
on the page. The audit trail of what was assumed versus confirmed turns out to be more
useful than a clean document would have been.

## What actually worked

**The research handoff caught a real error.** A fast web search asserted that Anthropic's
API retention had dropped to 7 days. Two independent deep-research passes both found it
was 30, and the correction is recorded in [`risks.md`](./risks.md) rather than silently
patched. Had the fast pass been trusted, a false claim about client data handling would
have ended up in a sales conversation.

**Two independent research engines were worth more than one.** The ChatGPT and Opus
passes were given the identical prompt and returned *entirely different competitor
lists* — zero overlap — while reaching the same conclusion about pricing norms. Agreement
between two searches that found different evidence is much stronger than agreement
between two runs of the same search.

**Being forced to name the audience exposed a bad assumption.** Writing "who is this
for" at the top of every document made it obvious that the target market had been
inherited from the source manual's *examples* (HVAC and auto-repair) and mistaken for its
*definition*. That reframe — to a qualification test that's industry-agnostic — was the
single largest change the packet went through, and the tier header is what surfaced it.

**Stress-testing the abstraction found its limit.** [`vertical-scenarios.md`](./vertical-scenarios.md)
runs the architecture against three industries it wasn't designed for. Two fit. The third
— legal intake — needed a compliance step the eight-stage model has no slot for. A stress
test that had validated everything would have proved nothing.

## What was overhead

**The first research pass was net-negative.** The quick web search was fast, but it
introduced the one factual error the project has had to correct. Its only real value was
revealing *which* questions were load-bearing enough to deserve a proper pass. Starting
with real deep research would have been better.

**Some documents are thinner than their existence implies.**
[`vertical-playbook.md`](./vertical-playbook.md) mostly formalises a screening process
that the source manual already contained in vertical-agnostic form. It's useful as a
checklist, but it's closer to a restatement than a new contribution, and the packet would
survive without it.

**Document count is not progress, and this packet is not immune to that.** Roughly 1,800
lines of Markdown exist here, in service of an idea that has still never been described to
a single prospective customer. The phase model is explicitly designed to keep that fact
visible — but the temptation to write another document rather than make a phone call is
real, and writing this one is arguably an instance of it.

## The extracted form

The method has been generalised into a Claude Code skill at
`~/.claude/skills/idea-to-business/`, so it can be pointed at any future idea without
re-deriving the structure. It contains the phase-gated tracker, the tiered document
templates, and the research-handoff process as blank scaffolding.

It was tested by running it against this very project from scratch, in a separate
directory, to see whether it reproduced the packet. It mostly did — and the test surfaced
three defects worth fixing: it generated a link to a source document that didn't exist at
the path it assumed, it produced noticeably thinner reasoning than the hand-built version
when left unprompted, and its phase names had drifted from the ones in use here. The first
two were fixed in the skill.

## When not to use this

If the idea is small enough to just try — a weekend project, a script, something with no
commercial dimension — this is far too much apparatus. The honest test is whether there's
a decision worth being careful about. Evaluating whether to spend a year and real money on
something warrants this. Deciding whether to spend a Saturday does not.

If the idea has no clear buyer or user, the business framing distorts more than it
clarifies, and a research plan or project plan is the better shape.

And if the answer is already known and the packet is being built to justify it, none of
the gates will save you — the method assumes you are willing to be told no.
