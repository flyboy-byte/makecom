# Overview

*Source for the landing page's prose. Not part of the packet itself — see
`README.md` for the repository's front door.*

## What this is

A single technical manual sat in Google Drive describing an automation
consultancy: build deterministic, human-supervised pipelines that turn messy input —
emails, PDFs, missed calls — into structured records inside a business's CRM or ERP,
then charge for the build and the upkeep.

This is what happened when that document was taken seriously. It was expanded into a
strategic case, a reference architecture, a risk map and a research queue, then checked
against reality by external research engines. Some of it survived that check. Three
things did not, and those are listed above rather than quietly edited out.

**There are two outputs here, and only one of them is the business.**

The **specimen** is the evaluation itself — is this a real business, and should anyone
build it? That question is genuinely open. It sits at Phase 2, nothing has been sold or
built, and no customer has ever heard it described. It may not survive first contact.

The **method** is the way the evaluation was produced: capture the source verbatim, split
documents by altitude rather than topic, gate progress on things that happen outside the
files, queue whatever can't be verified instead of guessing it, and keep the corrections
visible when research proves you wrong. Unlike the business, that part is finished — it
has been through a full cycle including catching its own errors, and it has been
extracted into a reusable form. [The Method](method.html) is the honest account of it,
including which parts turned out to be overhead.

If you only read one page and you don't care about automation agencies, read that one.

## How to read it

**If you want the argument** — start with [The Idea](business-idea.html) for what's being
proposed and who it's for, then [Feasibility](feasibility.html) for whether it holds up
commercially. [Risks](risks.html) is the counterweight to both.

**If you want the engineering** — [Architecture](architecture.html) is the eight-stage
reference pipeline and the honest split between what's fixed for every client and what
has to be rebuilt per client. [Infrastructure](infrastructure.html) is what it takes to
stand up. The [Source Manual](source-manual.html) underneath both is the original
document everything else was derived from.

**If you want to know whether any of it is true** — [Framework](framework.html) tracks
what's actually been done versus merely written, [Research Handoff](research-handoff.html)
shows how open questions were handed to external research tools, and
[the evidence folder](research-index.html) holds the raw, unedited output of every pass.

**If you're here for the method rather than the business** — [The Method](method.html)
is the whole thing in five moves, with a retrospective on what worked and what was
wasted effort. [Documentation Guide](documentation-guide.html) explains the tier system
underneath it, and [Vertical Scenarios](vertical-scenarios.html) is a deliberate attempt
to break the model by applying it to three industries it wasn't designed around. One of
them broke it.

## The documents

### The case

- **[The Idea](business-idea.html)** — the pitch, the target defined by a qualification
  test rather than an industry, and a blunt section on what's genuinely novel here versus
  what's just competent execution of a known playbook.
- **[Feasibility](feasibility.html)** — demand, competitors, what one build costs, what
  the market already pays, and what still needs validating before any of it matters.
- **[Vertical Scenarios](vertical-scenarios.html)** — three hypothetical industries run
  through the architecture as a stress test. Explicitly unresearched; the point was to
  find where the abstraction strains, and it did.
- **[Working Notes](entrepreneur-notes.html)** — the live scratchpad. Positioning,
  pricing rationale, and the decisions still genuinely open.

### The build

- **[Architecture](architecture.html)** — eight stages, each marked fixed or pluggable.
  Mapping the source manual's own worked examples onto it exposed stages those examples
  quietly skip.
- **[Infrastructure](infrastructure.html)** — accounts, data stores, secrets, environment
  isolation, and the gaps the source manual never addressed.
- **[Source Manual](source-manual.html)** — the original document. Client qualification,
  hardened scenario design, deployment discipline, data governance, contract clauses, SLA
  tiers, and three worked pipelines.

### Cross-cutting

- **[Risks](risks.html)** — legal, technical, market and operational. Includes a
  genuinely unsettled TCPA problem with an active circuit split, which is the single
  thing most likely to hurt someone here.
- **[Vertical Playbook](vertical-playbook.html)** — how to screen a new industry before
  spending research time on it, then how to qualify a specific client inside it.

### About the packet

- **[The Method](method.html)** — the process as a first-class output, extracted into a
  reusable form and audited honestly, including the parts that cost more than they
  returned.
- **[Framework](framework.html)** — the phase tracker. Gates advance by doing something
  outside these files: a conversation, a test, a signature. Never by writing more of them.
- **[Documentation Guide](documentation-guide.html)** — which documents answer *should
  we* and which answer *how would we*, and why conflating the two ruins both.
- **[Research Handoff](research-handoff.html)** — the queue of claims nobody could vouch
  for, the exact prompt used to hand them to an external research engine, and what came
  back.

### Evidence

[The research folder](research-index.html) holds every pass verbatim, with citations and
dates — a fast web search first, then two independent deep-research runs. The two deep
runs found entirely different competitors from each other while reaching the same
conclusion, which is worth more than either would have been alone. They also both caught
a factual error the fast pass introduced.

## Running it locally

```bash
pip install markdown
python3 site/build.py            # writes _site/
python3 -m http.server -d _site 8000
```

The same build runs on every push to `main`, fails if any internal link wasn't rewritten,
and deploys here. The phase status above is parsed out of the tracker at build time, so
the published state cannot drift from the document that owns it.
