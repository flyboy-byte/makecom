# Workflow Repair

A phase-gated evaluation of a Make.com automation practice — built from one source
document, expanded in the open, and fact-checked against itself.

### **[→ Read it here](https://flyboy-byte.github.io/makecom/)**

There are two things here. The **business evaluation** is unfinished and may not survive
contact with a real customer — nothing has been built or sold. The **method** that
produced it is finished, has caught its own errors, and has been extracted into a
reusable form. If you don't care about automation agencies, read
[The Method](https://flyboy-byte.github.io/makecom/method.html) and skip the rest.

## Pages

**Start here** ·
[The Idea](https://flyboy-byte.github.io/makecom/business-idea.html) ·
[What To Sell](https://flyboy-byte.github.io/makecom/what-to-sell.html) ·
[Where It Stands](https://flyboy-byte.github.io/makecom/framework.html)

**The case** ·
[Feasibility](https://flyboy-byte.github.io/makecom/feasibility.html) ·
[Risks](https://flyboy-byte.github.io/makecom/risks.html) ·
[Working Notes](https://flyboy-byte.github.io/makecom/entrepreneur-notes.html)

**The build** ·
[Architecture](https://flyboy-byte.github.io/makecom/architecture.html) ·
[Infrastructure](https://flyboy-byte.github.io/makecom/infrastructure.html)

**Reference** ·
[Source Manual](https://flyboy-byte.github.io/makecom/source-manual.html) ·
[Vertical Playbook](https://flyboy-byte.github.io/makecom/vertical-playbook.html) ·
[Vertical Scenarios](https://flyboy-byte.github.io/makecom/vertical-scenarios.html) ·
[The Method](https://flyboy-byte.github.io/makecom/method.html) ·
[Documentation Guide](https://flyboy-byte.github.io/makecom/documentation-guide.html) ·
[Research Handoff](https://flyboy-byte.github.io/makecom/research-handoff.html)

**Evidence** ·
[Research & sources](https://flyboy-byte.github.io/makecom/research-index.html) — every
pass in full, with citations

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
