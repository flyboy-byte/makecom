# Workflow Repair

A phase-gated evaluation of a Make.com automation practice — built from one source
document, expanded in the open, and fact-checked against itself.

### **[→ Read it here](https://flyboy-byte.github.io/makecom/)**

Nothing has been built or sold. It's a working evaluation of whether the idea holds up,
kept honest about what's established, what's still a guess, and what turned out to be
wrong.

## Pages

**Start** · [Framework](https://flyboy-byte.github.io/makecom/framework.html) — where this
actually is, and what has to happen next

**The case** ·
[The Idea](https://flyboy-byte.github.io/makecom/business-idea.html) ·
[Feasibility](https://flyboy-byte.github.io/makecom/feasibility.html) ·
[Vertical Scenarios](https://flyboy-byte.github.io/makecom/vertical-scenarios.html) ·
[Working Notes](https://flyboy-byte.github.io/makecom/entrepreneur-notes.html)

**The build** ·
[Architecture](https://flyboy-byte.github.io/makecom/architecture.html) ·
[Infrastructure](https://flyboy-byte.github.io/makecom/infrastructure.html) ·
[Source Manual](https://flyboy-byte.github.io/makecom/source-manual.html)

**Cross-cutting** ·
[Risks](https://flyboy-byte.github.io/makecom/risks.html) ·
[Vertical Playbook](https://flyboy-byte.github.io/makecom/vertical-playbook.html)

**About the packet** ·
[Documentation Guide](https://flyboy-byte.github.io/makecom/documentation-guide.html) ·
[Research Handoff](https://flyboy-byte.github.io/makecom/research-handoff.html)

**Evidence** ·
[Research folder](https://flyboy-byte.github.io/makecom/research-index.html) — raw output
from every research pass, with citations

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
