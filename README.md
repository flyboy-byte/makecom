# Workflow Repair

A phase-gated evaluation of a Make.com automation practice — built from one source
document, expanded in the open, and fact-checked against itself.

### **[→ Read it here](https://flyboy-byte.github.io/makecom/)**

There are two things here. The **business evaluation** is unfinished and may not survive
contact with a real customer — nothing has been built or sold. The **method** that
produced it is finished, has caught its own errors, and has been extracted into a
reusable form. If you don't care about automation agencies, read
[The Method](https://flyboy-byte.github.io/makecom/method.html) and skip the rest.

## The documents

The site is one page — the idea, the offer, and an honest read on whether it holds up.
Everything below is the working detail, read here on GitHub.

| | |
|---|---|
| [The idea](./docs/business-idea.md) | Who it's for, and what's genuinely novel versus merely competent |
| [What to sell](./docs/what-to-sell.md) | Six product shapes, and why the platform choice decides most of them |
| [Feasibility](./docs/feasibility.md) | Competitors, pricing, build costs, what the market already pays |
| [Risks](./docs/risks.md) | Legal, technical, market, operational — including one unsettled legal question |
| [Architecture](./docs/architecture.md) | The eight stages, and which are the same for every client |
| [Infrastructure](./docs/infrastructure.md) | Accounts, storage, secrets, what it takes to stand up |
| [Where it stands](./FRAMEWORK.md) | Phase tracker. Gates advance on events outside these files, never on more writing |
| [Expansion plan](./docs/expansion.md) | Who this gets shown to first, and why — planned, not yet sent |
| [The method](./docs/method.md) | How it was built, what worked, what was overhead |
| [Vertical playbook](./docs/vertical-playbook.md) | Screening a new industry, then a client inside it |
| [Vertical scenarios](./docs/vertical-scenarios.md) | Three industries the model wasn't designed for. One broke it |
| [Documentation guide](./docs/documentation-guide.md) | Which docs answer *should we* and which answer *how would we* |
| [Research handoff](./docs/research-handoff.md) | How open questions were handed to external research engines |
| [Research](./research/) | Every pass in full, unedited, with sources |
| [Source manual](./make.com%20review.md) | The original document all of this came from |

## Repo

```
FRAMEWORK.md          phase tracker
docs/                 the packet
research/             raw research output, unedited
make.com review.md    the original source manual
site/                 static site build
```

Build it locally:

```bash
pip install markdown
python3 site/build.py
python3 -m http.server -d _site 8000
```

Every push to `main` runs the same build, fails on any unrewritten internal link, and
deploys to GitHub Pages.

## Licence

[GPL-3.0](./LICENSE)
