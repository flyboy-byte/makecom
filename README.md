# Workflow Repair

**A phase-gated evaluation of a Make.com automation practice — built from one source
document, expanded in the open, and fact-checked against itself.**

📖 **[Read it as a site → flyboy-byte.github.io/makecom](https://flyboy-byte.github.io/makecom/)**
· built from these files on every push

---

This started as a single technical manual sitting in Google Drive
([`make.com review.md`](./make.com%20review.md)) describing an automation consultancy:
build deterministic, human-supervised pipelines that turn messy input (emails, PDFs,
missed calls) into structured records in a business's CRM or ERP, then charge for the
build and the upkeep.

This repo is what happened when that one document was taken seriously — expanded into a
strategic case, an architecture, a risk map, and a research queue, then checked against
reality. Some of it survived that check. Some of it didn't.

## What's actually here

It is documents. That's the honest description — scaffolding, plans, architecture, and
research, written as Markdown. The [site](https://flyboy-byte.github.io/makecom/) exists
because a pile of interlinked Markdown files doesn't communicate what it collectively
adds up to; the landing page shows the phase status, what's settled versus still a
guess, and how the pieces were actually produced.

| | Doc | What it's for |
|---|---|---|
| **Start** | [`FRAMEWORK.md`](./FRAMEWORK.md) | Phase tracker. Where this genuinely is, and what has to happen next. Gates advance by doing something outside these files, never by writing more of them. |
| **The case** | [`docs/business-idea.md`](./docs/business-idea.md) | The pitch: what it is, who it's for, what's actually novel versus just competent. |
| | [`docs/feasibility.md`](./docs/feasibility.md) | Demand, competitors, unit economics, and what still needs validating. |
| | [`docs/vertical-scenarios.md`](./docs/vertical-scenarios.md) | Three hypothetical industries stress-testing whether the model generalises. One of them broke it. |
| | [`docs/entrepreneur-notes.md`](./docs/entrepreneur-notes.md) | Live scratchpad of decisions still open. |
| **The build** | [`docs/architecture.md`](./docs/architecture.md) | Eight-stage reference pipeline, split into what's fixed for every client and what's pluggable per client. |
| | [`docs/infrastructure.md`](./docs/infrastructure.md) | Accounts, tooling, and what it costs to stand up. |
| | [`make.com review.md`](./make.com%20review.md) | The original source manual. The technical spine everything else is built on. |
| **Cross-cutting** | [`docs/risks.md`](./docs/risks.md) | Legal, technical, market, operational — including a genuinely unsettled TCPA problem. |
| | [`docs/vertical-playbook.md`](./docs/vertical-playbook.md) | Repeatable screening for a new industry, then a new client. |
| **About the packet** | [`docs/documentation-guide.md`](./docs/documentation-guide.md) | The tier system: which docs answer "should we" versus "how would we". |
| | [`docs/research-handoff.md`](./docs/research-handoff.md) | How unverifiable claims get handed to an external research engine, with the prompt used. |
| **Evidence** | [`research/`](./research/) | Raw, unedited output from every research pass, with citations. |

## The part worth knowing

Everything here is inference unless a page says otherwise. No customer has been spoken
to. Nothing has been built. The one thing this packet tries hard to do is keep a clean
line between what's been established, what's still assumed, and what turned out to be
wrong — that last category is real:

- **"Anthropic retains API data for 7 days."** Wrong; it's 30. A fast web search
  produced it, and two independent deep-research passes caught it.
- **"The maintenance retainer is mandatory."** Inherited from the source manual.
  Research found 17 competitors, several selling one-time builds and marketing
  explicitly against lock-in. It's a competitive liability, not a given.
- **"This is a business for HVAC and auto-repair shops."** Those were the manual's
  *examples*, mistaken for the definition. The target is now a qualification test —
  workflow volume, unstructured input, structured destination — that's industry-agnostic.

## Building the site locally

```bash
pip install markdown
python3 site/build.py     # writes _site/
python3 -m http.server -d _site 8000
```

[`.github/workflows/pages.yml`](./.github/workflows/pages.yml) runs the same build on
every push to `main`, fails if any internal link wasn't rewritten, and deploys to GitHub
Pages. The phase rail on the landing page is parsed out of `FRAMEWORK.md` at build time,
so it can't silently drift from the tracker.

## Licence

[GPL-3.0](./LICENSE).
