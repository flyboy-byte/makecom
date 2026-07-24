#!/usr/bin/env python3
"""Build the single-page site.

The packet itself is Markdown and is read on GitHub. This produces one page that
explains the idea, states where it honestly stands, and links out. The phase status
is parsed from FRAMEWORK.md at build time so it can't drift from the tracker.

Usage: python3 site/build.py   (writes to _site/)
"""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = ROOT / "_site"
REPO = "https://github.com/flyboy-byte/makecom"

TITLE = "Workflow Repair"
TAGLINE = (
    "Automating the paperwork small businesses still do by hand — "
    "and an honest account of whether that is a business."
)

# The eight-stage pipeline, condensed. The fixed/pluggable split is the whole claim
# of docs/architecture.md, so it's what the strip encodes.
PIPELINE = [
    ("Trigger", "plug", "however this business receives work"),
    ("Verify", "fixed", "reject anything unsigned"),
    ("Dedupe", "fixed", "the same event twice costs nothing"),
    ("Filter", "fixed", "bin the junk before it costs money"),
    ("Extract", "plug", "messy input to structured data"),
    ("Validate", "fixed", "reject malformed output"),
    ("Approve", "fixed", "a person signs off"),
    ("Write", "plug", "into whatever they already run"),
]

# An index into the docs that substantiate each claim, not a new source of truth.
LEDGER = {
    "settled": [
        ("What competitors charge", "docs/feasibility.md",
         "17 found across two independent research passes. A mandatory retainer is "
         "common but not the norm."),
        ("What one pipeline costs to build", "docs/feasibility.md",
         "$3k–18k depending on who builds it. Both passes converged."),
        ("What the market already pays", "docs/feasibility.md",
         "~$200–700/mo for field-service software; ~$250–4,000/mo for the labour it "
         "displaces."),
    ],
    "open": [
        ("Whether anyone wants it", "FRAMEWORK.md",
         "No conversation with a real business has happened. Every demand claim is "
         "inference."),
        ("Whether the SMS product is legal", "docs/risks.md",
         "Unsettled law with an active circuit split. Needs counsel."),
        ("How many businesses qualify", "docs/feasibility.md",
         "No public dataset measures workflow frequency."),
    ],
    "corrected": [
        ("Anthropic keeps API data 7 days", "docs/risks.md",
         "Wrong — 30. A fast search got it wrong; two deep passes caught it."),
        ("The retainer must be mandatory", "docs/what-to-sell.md",
         "Inherited from the source manual. It's a competitive liability."),
        ("This is a business for HVAC shops", "docs/business-idea.md",
         "Those were the manual's examples, mistaken for the definition."),
    ],
}

LEDGER_META = {
    "settled": ("Established", "Sourced and corroborated", "ok"),
    "open": ("Unresolved", "Cannot be closed from a desk", "flag"),
    "corrected": ("Corrected", "Believed, then disproved", "accent"),
}

PHASE_RE = re.compile(r"^### Phase (\d) — (.+?)\s+(✅|🔶|⬜)\s+(.+?)\s*$", re.MULTILINE)


def parse_phases() -> list[dict[str, str]]:
    """Read phase status out of FRAMEWORK.md so the published state can't drift."""
    text = (ROOT / "FRAMEWORK.md").read_text(encoding="utf-8")
    return [
        {"num": n, "name": name.strip(),
         "state": {"✅": "done", "🔶": "active", "⬜": "blocked"}[mark],
         "status": status.strip()}
        for n, name, mark, status in PHASE_RE.findall(text)
    ]


def phase_rail() -> str:
    cells = "".join(
        f'<li class="phase {p["state"]}">'
        f'<span class="phase-num">Phase {html.escape(p["num"])}</span>'
        f'<span class="phase-name">{html.escape(p["name"])}</span>'
        f'<span class="phase-state">{html.escape(p["status"])}</span></li>'
        for p in parse_phases()
    )
    return (
        '<ol class="rail">' + cells + "</ol>"
        '<p class="rail-foot">Parsed from '
        f'<a href="{REPO}/blob/main/FRAMEWORK.md">FRAMEWORK.md</a> when this page was '
        "built.</p>"
    )


def pipeline() -> str:
    cells = "".join(
        f'<li class="stage {kind}"><span class="stage-num">{i}</span>'
        f'<span class="stage-name">{html.escape(name)}</span>'
        f'<span class="stage-note">{html.escape(note)}</span></li>'
        for i, (name, kind, note) in enumerate(PIPELINE, start=1)
    )
    return (
        '<section class="block"><h2>What has actually been designed</h2>'
        "<p>One pipeline shape, eight stages. Five are identical for every client and "
        "are where the engineering argument lives; three have to be rebuilt each time, "
        "and are where knowing the customer's business becomes unavoidable.</p>"
        f'<ol class="pipe">{cells}</ol>'
        '<p class="pipe-key"><span class="key fixed">same every time</span>'
        '<span class="key plug">rebuilt per client</span>'
        f'<a href="{REPO}/blob/main/docs/architecture.md">Full architecture →</a></p>'
        "</section>"
    )


def ledger() -> str:
    cols = []
    for key in ("settled", "open", "corrected"):
        label, note, tone = LEDGER_META[key]
        items = "".join(
            f'<li><a href="{REPO}/blob/main/{doc}">{html.escape(claim)}</a>'
            f"<span>{html.escape(detail)}</span></li>"
            for claim, doc, detail in LEDGER[key]
        )
        cols.append(
            f'<div class="ledger-col {tone}"><div class="ledger-head">'
            f'<span class="ledger-label">{html.escape(label)}</span>'
            f'<span class="ledger-note">{html.escape(note)}</span></div>'
            f"<ul>{items}</ul></div>"
        )
    return (
        '<section class="block"><h2>What is actually known</h2>'
        "<p>Three rounds of research, two of them independent deep passes given the "
        "identical brief. They found different evidence and reached the same "
        "conclusions — and both caught an error the first round introduced.</p>"
        f'<div class="ledger">{"".join(cols)}</div></section>'
    )


def render_page() -> str:
    raw = (SITE / "page.md").read_text(encoding="utf-8")
    raw = re.sub(r"^#\s+.+$", "", raw, count=1, flags=re.MULTILINE)
    raw = re.sub(r"^\*Source for the single-page site.*?\*$", "", raw, flags=re.MULTILINE)

    md = markdown.Markdown(extensions=["tables", "sane_lists", "attr_list"])
    body = md.convert(raw)

    # Split the rendered prose so the visual blocks land between the right sections.
    # Keys are reduced to letters only, so punctuation in a heading can't break the
    # lookup and silently drop a whole section from the page.
    def key(text: str) -> str:
        return re.sub(r"[^a-z]", "", text.lower())

    parts = re.split(r"(?=<h2[^>]*>)", body)
    sections = {
        key(m.group(1)): part
        for part in parts
        if (m := re.match(r"<h2[^>]*>(.*?)</h2>", part))
    }
    lead = parts[0]

    def section(name: str) -> str:
        found = sections.get(key(name))
        if found is None:
            raise SystemExit(f"build: no '{name}' section in site/page.md")
        return found

    return "".join([
        '<header class="hero"><p class="eyebrow">Idea → business, in public</p>'
        f'<h1>{TITLE}</h1><p class="lede">{TAGLINE}</p></header>',
        f'<section class="block">{lead}{section("The idea")}</section>',
        pipeline(),
        f'<section class="block">{section("What you\'d sell")}</section>',
        ledger(),
        f'<section class="block verdict">{section("The honest read")}{phase_rail()}</section>',
        f'<section class="block docs">{section("The documents")}</section>',
    ])


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copy(SITE / "style.css", OUT / "style.css")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{html.escape(TAGLINE)}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
{render_page()}
<footer>
  <a href="{REPO}">Source on GitHub</a>
  <span>GPL-3.0</span>
</footer>
</main>
</body>
</html>
"""
    (OUT / "index.html").write_text(page, encoding="utf-8")
    print(f"built 1 page → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
