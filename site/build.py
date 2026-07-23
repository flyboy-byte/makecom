#!/usr/bin/env python3
"""Build the Workflow Repair packet into a static site.

Flattens every markdown doc in the packet into a single output directory,
rewriting inter-doc links, lifting each doc's `> **Tier:** ...` header block
into a chip row, and generating a landing page whose phase rail is parsed
live out of FRAMEWORK.md so it can never drift from the tracker.

Usage: python3 site/build.py   (writes to _site/)
"""

from __future__ import annotations

import html
import re
import shutil
import urllib.parse
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = ROOT / "_site"

SITE_TITLE = "Workflow Repair"
SITE_TAGLINE = "A phase-gated evaluation of a Make.com automation practice."

# (source path, slug, nav title, group). Order here is nav order.
PAGES: list[tuple[str, str, str, str]] = [
    ("FRAMEWORK.md", "framework", "Framework", "Start here"),
    ("docs/business-idea.md", "business-idea", "The Idea", "The case"),
    ("docs/feasibility.md", "feasibility", "Feasibility", "The case"),
    ("docs/vertical-scenarios.md", "vertical-scenarios", "Vertical Scenarios", "The case"),
    ("docs/entrepreneur-notes.md", "entrepreneur-notes", "Working Notes", "The case"),
    ("docs/architecture.md", "architecture", "Architecture", "The build"),
    ("docs/infrastructure.md", "infrastructure", "Infrastructure", "The build"),
    ("make.com review.md", "source-manual", "Source Manual", "The build"),
    ("docs/risks.md", "risks", "Risks", "Cross-cutting"),
    ("docs/vertical-playbook.md", "vertical-playbook", "Vertical Playbook", "Cross-cutting"),
    ("docs/documentation-guide.md", "documentation-guide", "Documentation Guide", "About the packet"),
    ("docs/research-handoff.md", "research-handoff", "Research Handoff", "About the packet"),
]

GROUP_ORDER = [
    "Start here",
    "The case",
    "The build",
    "Cross-cutting",
    "About the packet",
    "Evidence",
]

GROUP_NOTE = {
    "The case": "high-level",
    "The build": "low-level",
    "Cross-cutting": "mixed",
    "About the packet": "meta",
    "Evidence": "raw research",
}

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list", "toc"]

BOX_CHARS = set("│─┌┐└┘├┤┬┴┼▼►◄▲")


# ---------------------------------------------------------------- discovery


def research_pages() -> list[tuple[str, str, str, str]]:
    """Research files, newest first, as nav entries."""
    out = []
    for path in sorted((ROOT / "research").glob("*.md"), reverse=True):
        if path.name.lower() == "readme.md":
            title = "About the research folder"
            slug = "research-index"
        else:
            slug = "research-" + path.stem.lower()
            stem = path.stem
            m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+?)-(chatgpt|opus|claude-websearch)$", stem)
            if m:
                topic = m.group(2).replace("-", " ")
                engine = {"chatgpt": "ChatGPT", "opus": "Opus", "claude-websearch": "quick search"}[m.group(3)]
                title = f"{topic.title()} ({engine})"
            else:
                title = stem.replace("-", " ").title()
        out.append((f"research/{path.name}", slug, title, "Evidence"))
    return out


ALL_PAGES = PAGES + research_pages()

# basename (lowercased) -> slug, for link rewriting
LINK_MAP: dict[str, str] = {}
for src, slug, _title, _group in ALL_PAGES:
    LINK_MAP[Path(src).name.lower()] = slug
LINK_MAP["readme.md"] = "index"


# ------------------------------------------------------------- preprocessing


def wrap_ascii_diagrams(text: str) -> str:
    """Wrap runs of box-drawing lines in fenced code so diagrams survive.

    The source manual draws its architecture and decision trees in ASCII
    without fencing them; rendered as prose they collapse into noise.
    """
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    in_fence = False
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if in_fence or not any(c in BOX_CHARS for c in line):
            out.append(line)
            i += 1
            continue

        # start of a diagram run: consume until two consecutive non-diagram lines
        run: list[str] = []
        blanks = 0
        while i < len(lines):
            cur = lines[i]
            if any(c in BOX_CHARS for c in cur):
                run.extend([""] * blanks)
                blanks = 0
                run.append(cur)
                i += 1
            elif cur.strip() == "" and blanks < 1:
                blanks += 1
                i += 1
            elif cur.strip() and blanks == 0 and cur.startswith(" "):
                # indented caption line inside a diagram block
                run.append(cur)
                i += 1
            else:
                break
        cleaned = [re.sub(r"\\(?=[\[\]])", "", ln).rstrip() for ln in run]
        out.append("```text")
        out.extend(cleaned)
        out.append("```")
    return "\n".join(out)


TIER_FIELD_RE = re.compile(
    r"\*\*(Tier|Audience|Use when):\*\*\s*(.*?)(?=\*\*(?:Tier|Audience|Use when):\*\*|$)",
    re.DOTALL,
)


def extract_tier_block(text: str) -> tuple[str, dict[str, str]]:
    """Pull a leading `> **Tier:** ...` blockquote out of the body."""
    lines = text.split("\n")
    start = None
    for idx, line in enumerate(lines):
        if line.startswith("> "):
            start = idx
            break
        if line.strip() and not line.startswith("#"):
            return text, {}
    if start is None:
        return text, {}

    end = start
    while end < len(lines) and (lines[end].startswith(">") or lines[end].strip() == ">"):
        end += 1
    block = " ".join(ln.lstrip("> ").strip() for ln in lines[start:end])
    if "**Tier:**" not in block:
        return text, {}

    fields = {}
    for key, value in TIER_FIELD_RE.findall(block):
        value = value.strip().rstrip("·").strip()
        value = re.sub(r"\s+", " ", value)
        fields[key.lower().replace(" ", "_")] = value

    remaining = lines[:start] + lines[end:]
    return "\n".join(remaining), fields


# The packet's epistemic state, as an index into the docs that substantiate each
# claim — not a new source of truth. Every row must cite a page that argues it.
LEDGER = {
    "settled": [
        ("Retainer norms in the case-study market", "feasibility",
         "17 competitors found across two independent research passes; a mandatory "
         "retainer is common but not universal."),
        ("What one pipeline costs to build", "feasibility",
         "$3k–18k depending on delivery model, ~$6–9k midpoint. Both passes converged."),
        ("What the market already pays for software and labour", "feasibility",
         "~$200–700/mo for field-service software; ~$250–4,000/mo for the labour it displaces."),
        ("LLM provider data retention", "risks",
         "30 days default at both providers; zero-retention is enterprise-gated, not a toggle."),
    ],
    "open": [
        ("Whether anyone actually wants this", "framework",
         "Zero conversations with a real business. Every demand claim in the packet is inference."),
        ("Which vertical to validate in first", "entrepreneur-notes",
         "Should follow real access, not whichever industry is already researched."),
        ("Whether the missed-call SMS product is legal", "risks",
         "Genuinely unsettled law with an active circuit split. Needs counsel, not more research."),
        ("What fraction of businesses qualify", "feasibility",
         "No public dataset measures workflow frequency. Primary research only."),
    ],
    "corrected": [
        ("Anthropic retains API data for 7 days", "risks",
         "Wrong — it is 30 days. A fast search got this wrong; two deep passes caught it."),
        ("The retainer must be mandatory", "entrepreneur-notes",
         "Inherited from the source manual. Research showed it is a competitive liability."),
        ("This is a business for HVAC and auto repair", "business-idea",
         "Those were the manual's examples, mistaken for the definition. Now a case study."),
    ],
}

LEDGER_META = {
    "settled": ("Established", "Sourced and corroborated.", "ok"),
    "open": ("Unresolved", "Cannot be closed from a desk.", "flag"),
    "corrected": ("Corrected", "Believed, then disproved.", "accent"),
}

# How the packet actually got made — a loop, not a pipeline.
PROVENANCE = [
    ("One source manual", "source-manual",
     "A technical SOP pulled off Google Drive. The only input."),
    ("Strategic layer", "business-idea",
     "Expanded into the case, the build plan, and the risk map."),
    ("Gaps made explicit", "research-handoff",
     "Every claim nobody could actually vouch for, queued as a question."),
    ("External research", "research-index",
     "Three passes, two independent engines, saved raw with citations."),
    ("Merged back — including corrections", "framework",
     "Findings folded in. Some overturned what the packet already said."),
]

PHASE_RE = re.compile(r"^### Phase (\d) — (.+?)\s+(✅|🔶|⬜)\s+(.+?)\s*$", re.MULTILINE)


def parse_phases() -> list[dict[str, str]]:
    """Read phase status straight out of FRAMEWORK.md so it can't drift."""
    text = (ROOT / "FRAMEWORK.md").read_text(encoding="utf-8")
    phases = []
    for num, name, mark, status in PHASE_RE.findall(text):
        state = {"✅": "done", "🔶": "active", "⬜": "blocked"}[mark]
        phases.append({"num": num, "name": name.strip(), "state": state, "status": status.strip()})
    return phases


# ------------------------------------------------------------- link rewrite


def rewrite_links(html_text: str) -> str:
    """Point every intra-packet .md link at its built page."""

    def repl(match: re.Match) -> str:
        href = match.group(1)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        target, _, frag = href.partition("#")
        name = urllib.parse.unquote(Path(target).name).lower()
        slug = LINK_MAP.get(name)
        if not slug:
            if target.rstrip("/").endswith("research"):
                slug = "research-index"
            else:
                return match.group(0)
        return f'href="{slug}.html{"#" + frag if frag else ""}"'

    return re.sub(r'href="([^"]+)"', repl, html_text)


TASK_RE = re.compile(r"<li>\s*\[( |x)\]\s*")


def render_tasks(html_text: str) -> str:
    def repl(match: re.Match) -> str:
        done = match.group(1) == "x"
        cls = "task done" if done else "task"
        box = "✓" if done else ""
        return f'<li class="{cls}"><span class="box" aria-hidden="true">{box}</span>'

    return TASK_RE.sub(repl, html_text)


# ------------------------------------------------------------------ template


def nav_html(active_slug: str) -> str:
    groups: dict[str, list[tuple[str, str]]] = {}
    for _src, slug, title, group in ALL_PAGES:
        groups.setdefault(group, []).append((slug, title))

    parts = ['<a class="nav-home" href="index.html">Overview</a>']
    for group in GROUP_ORDER:
        if group not in groups:
            continue
        note = GROUP_NOTE.get(group)
        label = html.escape(group)
        note_html = f'<span class="nav-note">{html.escape(note)}</span>' if note else ""
        parts.append(f'<div class="nav-group"><div class="nav-head">{label}{note_html}</div><ul>')
        for slug, title in groups[group]:
            cls = ' class="active"' if slug == active_slug else ""
            parts.append(f'<li><a href="{slug}.html"{cls}>{html.escape(title)}</a></li>')
        parts.append("</ul></div>")
    return "\n".join(parts)


def chips_html(fields: dict[str, str]) -> str:
    if not fields:
        return ""
    inline = markdown.Markdown(extensions=[])
    rows = []
    for key, label in (("tier", "Tier"), ("audience", "Audience"), ("use_when", "Use when")):
        if key not in fields:
            continue
        value = inline.reset().convert(fields[key])
        value = re.sub(r"^<p>|</p>$", "", value.strip())
        value = rewrite_links(value)
        rows.append(
            f'<div class="chip-row"><span class="chip-key">{label}</span>'
            f'<span class="chip-val">{value}</span></div>'
        )
    return f'<aside class="tier-card">{"".join(rows)}</aside>'


def page_shell(*, title: str, slug: str, body: str, wide: bool = False) -> str:
    cls = ' class="wide"' if wide else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · {SITE_TITLE}</title>
<meta name="description" content="{html.escape(SITE_TAGLINE)}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="shell">
  <input type="checkbox" id="navtoggle" class="navtoggle">
  <label for="navtoggle" class="navbtn" aria-hidden="true">Contents</label>
  <nav class="sidebar" aria-label="Packet contents">
    <a class="brand" href="index.html">
      <span class="brand-mark" aria-hidden="true"></span>
      <span class="brand-text">{SITE_TITLE}</span>
    </a>
    {nav_html(slug)}
    <div class="nav-foot">
      <a href="https://github.com/flyboy-byte/makecom">Source on GitHub</a>
    </div>
  </nav>
  <main id="main"{cls}>
{body}
  </main>
</div>
</body>
</html>
"""


def ledger_html() -> str:
    cols = []
    for key in ("settled", "open", "corrected"):
        label, note, tone = LEDGER_META[key]
        items = []
        for claim, slug, detail in LEDGER[key]:
            items.append(
                f'<li><a href="{slug}.html">{html.escape(claim)}</a>'
                f"<span>{html.escape(detail)}</span></li>"
            )
        cols.append(
            f'<div class="ledger-col {tone}">'
            f'<div class="ledger-head"><span class="ledger-label">{html.escape(label)}</span>'
            f'<span class="ledger-note">{html.escape(note)}</span></div>'
            f'<ul>{"".join(items)}</ul>'
            "</div>"
        )
    return (
        '<section class="ledger-wrap" aria-label="What is settled and what is not">'
        '<h2 class="block-title">What this packet actually knows</h2>'
        '<p class="block-lede">The point of the exercise was never to produce documents. '
        "It was to keep an honest line between what has been established, what is still "
        "a guess, and what turned out to be wrong.</p>"
        f'<div class="ledger">{"".join(cols)}</div>'
        "</section>"
    )


def provenance_html() -> str:
    steps = []
    for idx, (title, slug, detail) in enumerate(PROVENANCE, start=1):
        steps.append(
            f'<li class="step">'
            f'<span class="step-num">{idx:02d}</span>'
            f'<div class="step-body"><a href="{slug}.html">{html.escape(title)}</a>'
            f"<p>{html.escape(detail)}</p></div>"
            "</li>"
        )
    return (
        '<section class="prov-wrap" aria-label="How the packet was built">'
        '<h2 class="block-title">How it was built</h2>'
        f'<ol class="prov">{"".join(steps)}</ol>'
        '<p class="prov-loop">↺ &nbsp;The last step feeds the second. Research keeps '
        "reopening documents that looked finished.</p>"
        "</section>"
    )


def phase_rail_html() -> str:
    phases = parse_phases()
    cells = []
    for p in phases:
        cells.append(
            f'<li class="phase {p["state"]}">'
            f'<span class="phase-num">Phase {html.escape(p["num"])}</span>'
            f'<span class="phase-name">{html.escape(p["name"])}</span>'
            f'<span class="phase-state">{html.escape(p["status"])}</span>'
            f"</li>"
        )
    return (
        '<section class="rail-wrap" aria-label="Phase status">'
        '<h2 class="rail-title">Where this actually is</h2>'
        f'<ol class="rail">{"".join(cells)}</ol>'
        '<p class="rail-foot">Parsed directly from '
        '<a href="framework.html">FRAMEWORK.md</a> at build time — if the tracker moves, '
        "this moves with it.</p>"
        "</section>"
    )


# --------------------------------------------------------------------- build


def convert(src_rel: str) -> tuple[str, dict[str, str], str]:
    raw = (ROOT / src_rel).read_text(encoding="utf-8")
    raw = wrap_ascii_diagrams(raw)
    raw, fields = extract_tier_block(raw)

    m = re.search(r"^#\s+(.+)$", raw, re.MULTILINE)
    heading = m.group(1).strip() if m else src_rel
    raw = re.sub(r"^#\s+.+$", "", raw, count=1, flags=re.MULTILINE)

    md = markdown.Markdown(extensions=MD_EXTENSIONS)
    body = md.convert(raw)
    body = rewrite_links(body)
    body = render_tasks(body)
    return heading, fields, body


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copy(SITE / "style.css", OUT / "style.css")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    for src_rel, slug, nav_title, _group in ALL_PAGES:
        heading, fields, body = convert(src_rel)
        source_href = (
            "https://github.com/flyboy-byte/makecom/blob/main/"
            + urllib.parse.quote(src_rel)
        )
        article = (
            f'<header class="doc-head"><h1>{html.escape(heading)}</h1>'
            f'<a class="src-link" href="{source_href}">{html.escape(src_rel)}</a></header>'
            f"{chips_html(fields)}"
            f'<article class="prose">{body}</article>'
        )
        (OUT / f"{slug}.html").write_text(
            page_shell(title=nav_title, slug=slug, body=article), encoding="utf-8"
        )

    # landing page
    _heading, _fields, readme_body = convert("README.md")
    readme_body = re.sub(r"<h2[^>]*>Contents</h2>.*?</table>", "", readme_body, flags=re.DOTALL)
    hero = f"""<header class="hero">
  <p class="eyebrow">Idea → business, in public</p>
  <h1>{SITE_TITLE}</h1>
  <p class="lede">{SITE_TAGLINE} Built from one source manual, expanded and
  fact-checked in the open — including the parts that turned out to be wrong.</p>
</header>
{phase_rail_html()}
{ledger_html()}
{provenance_html()}
<article class="prose">{readme_body}</article>"""
    (OUT / "index.html").write_text(
        page_shell(title="Overview", slug="index", body=hero, wide=True), encoding="utf-8"
    )

    print(f"built {len(ALL_PAGES) + 1} pages → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
