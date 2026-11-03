#!/usr/bin/env python3
"""The process library: ready-made Ulta decks, each one Markdown page, built on the template and checked like every deck.

    python tools/playbook.py list [--domain "Supply Chain"]        every template by domain and L1: id, name, slides
    python tools/playbook.py search cycle count                    ids whose name, summary, systems, tags or slide titles match
    python tools/playbook.py show <id>                             the template's page (Markdown): read it to adapt it
    python tools/playbook.py md <id> [<id> ...] --out page.md      one page from several templates (a chapter each), to edit
    python tools/playbook.py pick "three-way match controls; payment run KPIs; cutover timeline" --out page.md [--title T]
                                                                   the best slide for each request, from any template, as one page
                                                                   (--list: the candidates only; "<id>: words" picks inside one template)
    python tools/playbook.py build <id> [<id> ...] --out Deck.pptx [--title T] [--owner N] [--classification internal]
    python tools/playbook.py page page.md --out Deck.pptx [--title T] ...      an edited page (or any Markdown page) -> deck
    python tools/playbook.py review page.md [--title T]            the expert review of a page before it is built (seconds)
    python tools/playbook.py check [--agnostic]                    library health: front matter, sections, product names

A build: the page -> the Studio's Eco engine (studio/page_to_spec.py, rules, no AI) -> the deck on the approved template ->
a build record (which slides are drawn visuals, template infographics, shortened lists) -> Presentation Central's own
finishing (fit, accessibility, type scale, plain punctuation) -> the delivery gate (validate_deck.py) -> version stamp.
Prints a status line, FAIL lines, the EXPERT REVIEW (Presentation Central's tools/deck_expert.py on the page: the answer
first, the ask last, the right picture for each message, takeaway headlines, placeholders left), PICTURE (the contact
sheet to review), FILES and the RESULT line.
Pages live in library/<domain>/<l1>/<id>.md; a team folder can be added with ULTA_LIBRARY_DIR (several: separated by ':').
"""
import argparse, contextlib, io, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
STUDIO = ROOT / "studio"
TEMPLATES = ROOT / "modules" / "ultabranddeliverables" / "scripts" / "kit" / "templates"
sys.path.insert(0, str(TOOLS))
sys.path.insert(1, str(STUDIO))
import process_library as LIB   # noqa: E402

PY = sys.executable
INFO_FAMILIES = ("infographic-", "template-")   # template styles filled in place (quad, funnel, donut, map, ogsm, scorecard ...)


def _opt(args, name, default=None):
    if name in args:
        i = args.index(name)
        v = args[i + 1] if i + 1 < len(args) else default
        del args[i:i + 2]
        return v
    return default


# ---------------------------------------------------------------------------------------------- pick: slides, not templates
PICK_STOP = {"a", "an", "the", "and", "or", "of", "for", "to", "in", "on", "with", "our", "we", "us", "slide", "slides", "page",
             "deck", "from", "by", "at", "is", "are", "how", "what", "who", "it", "its", "this", "that", "show", "me", "about"}


PERIODS = {"daily": "day", "weekly": "week", "monthly": "month", "quarterly": "quarter", "yearly": "year", "annual": "year"}


def _norm(w):
    """Light stemming so "KPIs", "controls" and "processes" meet "KPI", "control", "process" (and "monthly" meets "month")."""
    if w in PERIODS:
        return PERIODS[w]
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 4 and w.endswith(("ses", "xes", "zes")):
        return w[:-2]
    if len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is")):
        return w[:-1]
    return w


def _toks(text):
    out = set()
    for w in __import__("re").findall(r"[a-z0-9][a-z0-9&'-]*", str(text).lower()):
        w = w.strip("-'")
        if w and w not in PICK_STOP:
            out.add(_norm(w))
            if "-" in w:
                out.update(_norm(p) for p in w.split("-") if p and p not in PICK_STOP)
    return out


def _sections(body):
    """[(heading, text)] - one per "## " slide, the text from the heading to the next one."""
    import re
    out, cur = [], None
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = [m.group(1), [line]]; out.append(cur)
        elif cur is not None and not line.startswith("# "):
            cur[1].append(line)
    return [(h, "\n".join(ls).rstrip()) for h, ls in out]


LAYOUT_KINDS = (   # a slide's layout answers to the words people use for that kind of slide
    (("timeline", "process phases", "gantt"), "timeline plan schedule roadmap milestone phase calendar date"),
    (("swimlane",), "swimlane handoff flow role who raci"),
    (("process",), "process flow step"),
    (("retail",), "diagram flow network"),
    (("kpi cards", "four numbers", "scorecard", "bullet", "rings"), "kpi number metric measure target scorecard"),
    (("matrix",), "matrix priority quadrant"),
    (("hub",), "stakeholder hub"),
)


def pick(requests, top=3):
    """For each request ("three-way match controls"), the library slides ranked by the words they share with it: the
    template's name, tags, summary and L1 say WHAT (three-way match; a word few templates use counts most), the slide's
    heading, layout and text say WHICH SLIDE (controls; a word few of the template's slides use counts most). Rules, no
    AI: the same answer every time. "<id>: words" (or "<id>#words") picks inside one template.
    Returns [(request, [(rank key, id, heading, text)])], best first."""
    import re
    items = LIB.templates()
    index = []
    for tid, (meta, body) in items.items():
        tw = {}
        for field, w in ((meta["l2"], 3), (" ".join(meta["tags"]), 2), (tid.replace("-", " "), 1), (meta["l1"], 1),
                         (meta["domain"], 1), (meta.get("summary", ""), 1)):
            for t in _toks(field):
                tw[t] = max(tw.get(t, 0), w)
        for h, text in _sections(body):
            layout = " ".join(re.findall(r"(?im)^layout:\s*(.+)$", text)).lower()
            kinds = " ".join(words for keys, words in LAYOUT_KINDS if any(layout.startswith(k) or f" {k}" in f" {layout}" for k in keys))
            sw = {}
            for field, w in ((h, 3), (layout + " " + kinds, 2), (text, 1)):
                for t in _toks(field):
                    sw[t] = max(sw.get(t, 0), w)
            index.append((tid, meta, h, text, tw, sw))
    import math
    df, seen, sec_df, n_sec = {}, {}, {}, {}
    for tid, meta, h, text, tw, sw in index:
        seen.setdefault(tid, set()).update(tw, sw)
        n_sec[tid] = n_sec.get(tid, 0) + 1
        for t in sw:
            sec_df[(tid, t)] = sec_df.get((tid, t), 0) + 1
    for words in seen.values():
        for t in words:
            df[t] = df.get(t, 0) + 1
    idf = lambda t: math.log(1 + len(seen) / max(1, df.get(t, 0)))      # which template: a rare word (cutover) says more
    idf_in = lambda tid, t: math.log(1 + n_sec[tid] / sec_df[(tid, t)]) if sec_df.get((tid, t)) else 0.0   # which slide: a word few of its slides share
    out = []
    for req in requests:
        only, words = None, req
        m = re.match(r"^\s*([a-z]{2}-[a-z0-9-]+)\s*[:#]\s*(.*)$", req)
        if m and m.group(1) in items:
            only, words = m.group(1), m.group(2) or items[m.group(1)][0]["l2"]
        q = _toks(words)
        def rank(strict):
            ranked = []
            for tid, meta, h, text, tw, sw in index:
                if only and tid != only:
                    continue
                cover = sum(1 for t in q if t in tw or t in sw)
                if not cover or not any(t in sw for t in q) or (strict and not only and not any(t in tw for t in q)):
                    continue                              # the slide must answer the request, inside the right template
                score = round(sum(idf(t) * tw.get(t, 0) + idf_in(tid, t) * sw.get(t, 0) * (0.25 if t in tw else 1.0)
                                  for t in q), 3)   # the topic picks the template; the other words pick its slide
                ranked.append(((score, cover, -meta.get("order", 999)), tid, h, text))
            ranked.sort(key=lambda r: r[0], reverse=True)
            return ranked
        ranked = rank(True) or rank(False)            # a request that names only a kind of slide ("risks") still finds one
        out.append((req, ranked[:max(1, top)]))
    return out


# ------------------------------------------------------------------------------------- the expert review, on a page
PAGE_PICTURE = {   # deck_expert's better picture -> the page line that draws it
    "the risk table": "a table | Risk | Mitigation | Owner |",
    "the action table": "a table | Action | Owner | When |",
    "a diagram": '"A -> B: what flows" lines (a system diagram)',
    "a donut": "Layout: donut",
    "big numbers with a context line": "Layout: kpi cards",
    "a dumbbell": "Layout: slope",
    "a timeline": 'Layout: timeline quarters (dated lines, ranges with "to")',
    "big numbers": "Layout: four numbers",
    "a chart": "Layout: ranking",
    "a flow": "Layout: process chevrons",
    "a process flow in two rows": "Layout: process snake",
    "numbered tiles": "Layout: process numbered",
}


def _expert_slides(spec):
    """The page's slides in the shape Presentation Central's expert review reads (tools/deck_expert.py)."""
    import re
    out = []
    for s in spec.get("slides") or []:
        f = s.get("fills") or {}
        head = f.get("title")
        c = s.get("central") if isinstance(s.get("central"), dict) else {}
        head = head or c.get("headline")                # a template infographic's headline sits with its data
        x = {"source": s.get("source"), "headline": " ".join(head) if isinstance(head, list) else str(head or "")}
        if s.get("notes"):
            x["notes"] = s["notes"]
        if s.get("takeaway"):
            x["summary"] = s["takeaway"]
        fam, _, style = str(s.get("kind") or "").partition("-")
        if s.get("central") or s.get("graphic") or s.get("flow") or s.get("board") or s.get("chart"):
            if fam == "timeline":
                x["timeline"] = {}
            elif fam == "swimlane":
                x["swimlane"] = {}
            elif fam in ("process", "retail"):
                x[fam], x["style"] = {}, style
            elif fam == "infographic":
                x[style if style in ("donut", "results", "quad", "journey", "scorecard", "map", "priorities", "ogsm", "funnel")
                  else "graphic"] = {}
            elif fam == "modern":
                x["modern"], x["items"] = style, []
            elif s.get("graphic"):
                g = str((s.get("graphic") or {}).get("kind") or "graphic")
                x["graphic"] = {"hexagons": "honeycomb"}.get(g, g)
            elif s.get("flow"):
                x["steps"] = [{"label": "step"}]
            else:
                x["graphic"] = "graphic"
        else:
            items = []
            for k in ("text1", "text2"):
                v = f.get(k)
                for line in (v if isinstance(v, list) else [v] if v else []):
                    line = str(line or "").strip()
                    if line and not line.startswith("## "):
                        items.append(re.sub(r"^[•–◦▪✓✗→]\s*", "", line))
            if f.get("table") is not None:
                x["table"] = f["table"]
            elif items:
                x["text"] = items
            if s.get("bands"):
                x["source"] = 42                       # Today / Target bands: a designed comparison, not a wall of text
            asks = [v for v in (s.get("callouts") or {}).values() if v] + \
                   [i for i in items if re.match(r"(?i)(decision|ask|next steps?)\s*:", i)]
            if asks:
                x["decision"] = asks[0]
        out.append(x)
    return out


def _page_sections(md):
    """[(heading, layout, kind, items)] for each "## " section of a page: kind is table, cards, bands or list."""
    import re
    out = []
    for h, text in _sections(md or ""):
        layout = " ".join(re.findall(r"(?im)^layout:\s*(.+)$", text)).strip()
        lines = [l.strip() for l in text.splitlines()[1:] if l.strip() and not l.lstrip().startswith(">")]
        rows = [l for l in lines if l.startswith("|") and not re.match(r"^\|?\s*:?-{2,}", l)]
        subs = [l[4:].strip() for l in lines if l.startswith("### ")]
        if rows:
            kind_, items = "table", [" | ".join(c.strip() for c in r.strip("|").split("|")) for r in rows[1:]]
        elif subs and {x.lower() for x in subs} & {"today", "target", "tomorrow", "before", "after"}:
            kind_, items = "bands", []
        elif subs:
            kind_, items = "cards", [l[2:].strip() for l in lines if l.startswith(("- ", "* "))]
        else:
            kind_, items = "list", [l[2:].strip() for l in lines if l.startswith(("- ", "* "))]
        out.append((h, layout, kind_, items))
    return out


def expert_review(spec, title, md=None):
    """Presentation Central's expert review (tools/deck_expert.py: the answer first, the ask last, the right picture for
    each message, takeaway lines, no run of text slides) on a library page, its advice in page terms, plus two checks a
    page needs: headings that name a topic instead of the takeaway, and placeholders still on the slides."""
    import re
    import deck_expert as DX
    slides = _expert_slides(spec)
    try:
        got = DX.review({"title": title}, slides)
    except Exception as e:                             # noqa: BLE001  the review advises; it never stops a build
        return [f"EXPERT REVIEW: not available here ({type(e).__name__})"]
    head, lines = got[0], [l[len("EXPERT "):] for l in got[1:] if l.startswith("EXPERT ") and not l.startswith("EXPERT ...")]
    page = []
    secs = _page_sections(md) if md else []
    if secs:                                           # a page is edited by section: the better picture for each section
        lines = [l for l in lines if not re.match(r"slide \d+: ", l)]
        K = DX.consts()
        drawn = {x["headline"] for x in slides if any(x.get(k_) is not None for k_ in (
            "timeline", "swimlane", "process", "retail", "graphic", "modern", "steps", "quad", "scorecard", "donut", "results",
            "journey", "map", "priorities", "ogsm", "funnel"))}
        for k, (h, layout, kind_, items) in enumerate(secs, 1):
            if layout.lower().startswith("swimlane"):
                long_ = [i.split(":", 1)[1].strip() for i in items if ":" in i
                         and len(re.sub(r"(?i)^if (yes|no)\s*,?\s*", "", i.split(":", 1)[1].strip()).split()) > 5]
                if long_:
                    page.append(f"section '{h}': {len(long_)} swimlane step{'s' if len(long_) > 1 else ''} over 5 words - the "
                                f"slide shows only the first 5 ('{long_[0]}'): say each in 5 words, verb and object")
            if layout or kind_ in ("bands", "table") or len(items) < 2 or h in drawn:
                continue                               # (a Layout line or a table is the author's choice; the engine drew some itself)
            x = {"headline": h, "table": [["", ""]] + [[i, ""] for i in items]} if kind_ == "table" else {"headline": h, "text": items}
            try:
                sg = DX.suggest(x, k, K)
            except Exception:                          # noqa: BLE001
                sg = None
            if sg and sg[1] in PAGE_PICTURE:
                page.append(f"section '{h}': {sg[0].replace('text boxes', 'its lines')} - {sg[1]}: {PAGE_PICTURE[sg[1]]}")
        for n, s in enumerate(spec.get("slides") or [], 1):   # two sections the engine packed onto one slide
            f = s.get("fills") or {}
            boxed = [str(l)[3:].strip() for k_ in ("text1", "text2") for l in (f.get(k_) if isinstance(f.get(k_), list) else [])
                     if str(l).startswith("## ")]
            sec_names = {h for h, *_ in secs}
            merged = [b for b in boxed if b in sec_names]
            if merged:
                title_ = " ".join(f["title"]) if isinstance(f.get("title"), list) else str(f.get("title") or "")
                page.append(f"slide {n} holds {len(merged) + 1} sections ({', '.join(repr(m) for m in merged)} and '{title_}'): "
                            "one message a slide reads better - give each its own Layout: line or fold the lighter one "
                            "into the notes")
    for l in lines:
        if l.startswith("polish:"):
            continue                                   # (photo covers and dividers: storyboard choices a page does not make)
        l = re.sub(r"open with the answer and the ask: .*", "open with the answer and the ask: make the first section an At a "
                   "glance slide - a heading that states the answer and 3-5 \"Lead: detail\" lines, the decision needed among them", l)
        l = re.sub(r"open with the answer: .*", "open with the answer: make the first section an At a glance slide (a heading "
                   "that states the answer, 3-5 \"Lead: detail\" lines) or the headline numbers (Layout: four numbers)", l)
        l = re.sub(r"end with the ask: .*", "end with the ask: a last section with \"- Decision: ...\", \"- Ask: ...\" and "
                   "\"- Next step: ...\" lines, or an action table (| Action | Owner | When |)", l)
        l = re.sub(r"(\d+) content slides and no chapters: .*", r"\1 content slides and no chapters: put a \"# Chapter\" line "
                   "before each group of sections (2-4 chapters; each gets a divider and an agenda line)", l)
        l = re.sub(r"no agenda: .*", "no agenda: give the page 2-4 chapters (\"# Chapter\" lines) - the agenda follows", l)
        l = re.sub(r"\(a chart, big numbers, a timeline or a diagram of the same facts\)",
                   "(a Layout: line - four numbers, a timeline, a process or a matrix of the same facts)", l)
        l = re.sub(r"add \"summary\": .*", "add one sentence under its heading saying what the figures mean (it becomes "
                   "the slide's takeaway line)", l)
        l = re.sub(r"add \"decision\": .*", "add a \"- Decision: ...\" line to that section", l)
        if l.startswith("retail:"):
            l = re.sub(r" first: .*", " first: Layout: retail <starter> or a swimlane (guides/library.md lists the starters)", l)
        m = re.match(r"(slide \d+: .+? - )(.+?): .*", l)
        if m and m.group(2) in PAGE_PICTURE:
            l = f"{m.group(1)}{m.group(2)}: {PAGE_PICTURE[m.group(2)]}"
        page.append(l)
    try:
        import family_rules as FR
        content = [x for x in slides if not str(x.get("source")) in ("1", "2", "5", "32")]
        topics = [x["headline"] for x in content if x["headline"] and FR.is_label(x["headline"].replace(" (cont.)", ""))]
    except Exception:                                  # noqa: BLE001
        content, topics = [], []
    if topics:
        ex = ", ".join(f"'{t}'" for t in list(dict.fromkeys(topics))[:3])
        page.append(f"headlines: {len(topics)} of {len(content)} name a topic, not the takeaway ({ex}): with the user's facts, "
                    "say what each slide shows (at most 42 characters)")
    held = {}
    for n, s in enumerate(spec.get("slides") or [], 1):
        for t in re.findall(r"\[[a-z][^\]\n]{0,23}\]", json.dumps({k: v for k, v in s.items() if k != "notes"})):   # text and drawn data
            held.setdefault(t, set()).add(n)
    if held:
        where = sorted({n for v in held.values() for n in v})
        page.append(f"placeholders on slide{'s' if len(where) > 1 else ''} {', '.join(map(str, where[:8]))}: "
                    f"{', '.join(sorted(held)[:5])} - fill them with the user's facts, or tell the user they are placeholders")
    more = len(page) - 8
    return [head] + [f"EXPERT {l}" for l in page[:8]] + ([f"EXPERT ... {more} more: python tools/playbook.py review <page.md>"]
                                                       if more > 0 else [])


def picked_page(results, title):
    """One library page of the first choice for each request, in the order asked; each slide's notes name its template."""
    import re
    items = LIB.templates()
    parts, seen = [f"# {title}", ""], set()
    for req, ranked in results:
        if not ranked:
            continue
        _, tid, h, text = ranked[0]
        if (tid, h) in seen:
            continue
        seen.add((tid, h))
        src = f"From the library template {tid} ({items[tid][0]['l2']})."
        lines = text.splitlines()
        q = [k for k, l in enumerate(lines) if l.lstrip().startswith(">")]
        if q:                                          # one note per slide: the source joins the slide's own note
            k = q[-1]; lines[k] = lines[k].rstrip().rstrip(".") + ". " + src
        else:
            lines.append(f"> Notes: {src}")
        parts += lines + [""]
    return "\n".join(parts).rstrip() + "\n"


def record(deck, spec):
    """The build record Presentation Central's gate reads (<deck>.ulta.json, also kept inside the file): drawn visuals
    are checked as drawn slides (readable text on what it sits on), template infographics and shortened tables keep
    the template's own shapes, everything else is compared shape by shape with its template slide."""
    import brand as B
    slides = spec["slides"]
    kind = lambda s: str(s.get("kind") or "")
    drawn = [i for i, s in enumerate(slides, 1) if (s.get("central") and not kind(s).startswith(INFO_FAMILIES))
             or any(s.get(k) for k in ("diagram", "graphic", "modern", "_points", "bands"))]   # drawn: diagrams, point graphics, bands
    info = [i for i, s in enumerate(slides, 1) if s.get("central") and kind(s).startswith(INFO_FAMILIES)]
    # shortened on purpose: empty rows dropped, rows grown, or a box removed and its neighbour widened ("hide": the
    # two-box slide as one wide box); the gate checks these with its template-fidelity rule (own shapes, same design)
    short = [i for i, s in enumerate(slides, 1) if (s.get("trim_empty_rows") or s.get("grow_rows") or s.get("hide"))
             and i not in drawn + info]
    rec = {"diagram_slides": drawn, "flow_slides": [], "library_slides": [], "list_slides": short, "infographic_slides": info,
           "drawn_slides": drawn, "trimmed_slides": [], "schema_version": 2,
           "source_mapping": {str(i): s["source"] for i, s in enumerate(slides, 1)}, "ways": [], "gallery": False,
           "reference_sha256": B.current().sha, "built_by": "process library (Studio Eco engine)"}
    Path(str(deck) + ".ulta.json").write_text(json.dumps(rec), encoding="utf-8")
    import layoutmeta
    layoutmeta.save(deck)
    return rec


A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"


def _bare(rpr):
    """No size and no font of its own (a colour alone does not make a run styled)."""
    return rpr is None or (rpr.get("sz") is None and rpr.find(f"{{{A_NS}}}latin") is None)


def conform_runs(deck, slides, skip):
    """Every run on a template-derived shape takes the template's own run style where the engine left it bare (no size,
    font or colour): Presentation Central writes into the template's existing runs, and its gate compares each run with
    the template cell or box it came from. Drawn slides (skip) have no template counterpart. Returns runs styled."""
    import copy
    from pptx import Presentation
    import brand as B
    from lxml import etree
    def named(shapes, out):
        for sh in shapes:
            if sh.shape_type == 6:
                named(sh.shapes, out)
            else:
                out.setdefault(sh.name, sh)
        return out
    def para_styles(txbody):
        styles = []
        for p in txbody.findall(f"{{{A_NS}}}p"):
            r = p.find(f"{{{A_NS}}}r/{{{A_NS}}}rPr")
            styles.append(r)
        first = next((s for s in styles if s is not None and not _bare(s)), None)
        return [s if s is not None and not _bare(s) else first for s in styles] or [first]
    import zipfile, re as _re
    _theme = zipfile.ZipFile(str(B.current().template)).read("ppt/theme/theme1.xml").decode("utf-8", "ignore")
    slots = {k: (v2 or v1).upper() for k, v1, v2 in _re.findall(
        r'<a:(dk1|lt1|dk2|lt2|accent\d|hlink|folHlink)>\s*<a:(?:srgbClr val="([0-9A-Fa-f]{6})"|sysClr [^>]*lastClr="([0-9A-Fa-f]{6})")', _theme)}
    alias = {"tx1": "dk1", "bg1": "lt1", "tx2": "dk2", "bg2": "lt2"}
    def colour(fill):
        """The RGB a solidFill shows, or None when it is not a plain colour (tints and shades are left alone)."""
        c = fill[0] if fill is not None and len(fill) else None
        if c is None or len(c):
            return None
        tag = c.tag.split("}")[-1]
        if tag == "srgbClr":
            return (c.get("val") or "").upper()
        if tag == "schemeClr":
            return slots.get(alias.get(c.get("val"), c.get("val")))
        return None
    def same_colour(rpr, st, same_fill):
        """The template run's colour, in the template's own notation, where the run shows that colour written another way
        (FFFFFF for the theme's bg1, 000000 for tx1) or none of its own on an unchanged cell or box. Returns 1 when set."""
        tf = st.find(f"{{{A_NS}}}solidFill")
        if rpr is None or tf is None:
            return 0
        own = rpr.find(f"{{{A_NS}}}solidFill")
        if own is None:
            if not same_fill:
                return 0
            ln = rpr.find(f"{{{A_NS}}}ln")
            (ln.addnext(copy.deepcopy(tf)) if ln is not None else rpr.insert(0, copy.deepcopy(tf)))
            return 1
        if etree.tostring(own) != etree.tostring(tf) and colour(own) and colour(own) == colour(tf):
            own.getparent().replace(own, copy.deepcopy(tf))
            return 1
        return 0
    def fill_of(el, tag):
        pr = el.find(tag) if el is not None else None
        f = None if pr is None else next((c for c in pr if c.tag.split("}")[-1] in ("noFill", "solidFill", "gradFill", "pattFill", "blipFill")), None)
        return b"" if f is None else etree.tostring(f)
    def apply(txbody, ref, same_fill=False):
        n = 0
        styles = para_styles(ref)
        if not any(s is not None for s in styles):
            return 0
        for k, p in enumerate(txbody.findall(f"{{{A_NS}}}p")):
            st = styles[min(k, len(styles) - 1)]
            if st is None:
                continue
            for r in p.findall(f"{{{A_NS}}}r"):
                rpr = r.find(f"{{{A_NS}}}rPr")
                t = r.find(f"{{{A_NS}}}t")
                mark = t is not None and (t.text or "").strip() and set((t.text or "").strip()) <= set("●○■□▲▼◆◇★►◀▶◄•")
                if not _bare(rpr):
                    n += 0 if mark else same_colour(rpr, st, same_fill)   # a status mark keeps its own colour
                    continue
                if _bare(rpr):
                    new = copy.deepcopy(st)
                    own_fill = rpr.find(f"{{{A_NS}}}solidFill") if rpr is not None else None
                    if own_fill is not None:   # the run's own colour (a status mark) stays; size and font come from the template
                        fills = [c for c in new if c.tag.split("}")[-1] in ("noFill", "solidFill", "gradFill", "blipFill", "pattFill", "grpFill")]
                        at = list(new).index(fills[0]) if fills else (1 if new.find(f"{{{A_NS}}}ln") is not None else 0)   # schema: ln, then the fill
                        for f in fills:
                            new.remove(f)
                        new.insert(at, copy.deepcopy(own_fill))
                    if rpr is not None:
                        r.remove(rpr)
                    r.insert(0, new); n += 1
        return n
    prs, tpl = Presentation(str(deck)), Presentation(str(B.current().template))
    total = 0
    for i, (sl, s) in enumerate(zip(prs.slides, slides), 1):
        src = s.get("source")
        if i in skip or not isinstance(src, int) or not 1 <= src <= len(tpl.slides):
            continue
        ref = named(tpl.slides[src - 1].shapes, {})
        for sh in named(sl.shapes, {}).values():
            rs = ref.get(sh.name)
            if rs is None:
                continue
            if getattr(sh, "has_table", False) and sh.has_table and getattr(rs, "has_table", False) and rs.has_table:
                t, rt = sh.table, rs.table
                for r in range(len(t.rows)):
                    for c in range(len(t.columns)):
                        rc = rt.cell(min(r, len(rt.rows) - 1), min(c, len(rt.columns) - 1))
                        tcp = f"{{{A_NS}}}tcPr"
                        same = fill_of(t.cell(r, c)._tc, tcp) == fill_of(rc._tc, tcp)   # the cell keeps the template's fill
                        total += apply(t.cell(r, c).text_frame._txBody, rc.text_frame._txBody, same)
            elif sh.has_text_frame and rs.has_text_frame:
                spp = "{http://schemas.openxmlformats.org/presentationml/2006/main}spPr"
                same = fill_of(sh._element, spp) == fill_of(rs._element, spp)
                total += apply(sh.text_frame._txBody, rs.text_frame._txBody, same)
    if total:
        import atomic
        atomic.save(prs, deck)
    return total


def finish(deck, spec, rec, story):
    """Presentation Central's finishing steps, in build_deck's order, on a deck the Eco engine built."""
    import build_deck as BD, typeset, plain, brand as B
    slides = spec["slides"]
    mapping = ",".join(str(s["source"]) for s in slides)
    if rec["diagram_slides"]:                         # as build_deck: text on a drawn card goes INSIDE its shape (edits like hand-made)
        nz = subprocess.run([PY, str(TOOLS / "nativize.py"), str(deck), "--slides", ",".join(map(str, rec["diagram_slides"]))],
                            capture_output=True, text=True)
        print((nz.stdout.strip().splitlines() or ["nativize: no output"])[-1])
    print(f"runs styled from the template: {conform_runs(deck, slides, set(rec['diagram_slides']))}")
    fh = subprocess.run([PY, str(TOOLS / "autofit.py"), str(deck), "--mapping", mapping, "--out", str(deck)], capture_output=True, text=True)
    print(fh.stdout.strip())
    BD.finish_before_validate(deck, story)
    BD.no_theme_effects(deck, rec["diagram_slides"])
    exempt = list(rec["diagram_slides"])
    keep = list(rec["infographic_slides"])
    component = [k for k, s in enumerate(slides, 1) if s.get("source") in typeset.component_sources(B.current())
                 and k not in exempt and k not in keep]
    probs = typeset.apply(deck, {k: s.get("source") for k, s in enumerate(slides, 1)}, exempt, keep=keep, component=component)
    plain.clean_all([deck])
    conform_runs(deck, slides, set(rec["diagram_slides"]))   # last: the accessibility pass writes white as FFFFFF; the template says bg1
    return mapping, probs, fh.returncode


def build(md, out, title=None, owner=None, classification=None, ids=()):
    """Markdown page -> checked deck at out. Returns the exit code (0 = READY)."""
    t0 = time.time()
    out = Path(out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="ulta-playbook-"))
    page, spec_p, deck = work / "page.md", work / "spec.json", work / out.name
    page.write_text(md, encoding="utf-8")
    log = io.StringIO()
    story = {"owner": owner, "classification": classification}
    try:
        cmd = [PY, str(STUDIO / "page_to_spec.py"), str(page), "--out", str(spec_p)] + (["--title", title] if title else [])
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(work))
        log.write(r.stdout + r.stderr)
        if r.returncode or not spec_p.exists():
            print("NOT BUILT | the page could not be read: " + (r.stderr or r.stdout).strip()[-300:]); return 2
        spec = json.loads(spec_p.read_text(encoding="utf-8"))
        r = subprocess.run([PY, str(STUDIO / "build_from_storyboard.py"), str(spec_p), "--templates", str(TEMPLATES), "--out", str(deck)],
                           capture_output=True, text=True, cwd=str(work))
        log.write(r.stdout + r.stderr)
        if r.returncode or not deck.exists():
            print("NOT BUILT | the engine stopped: " + (r.stderr or r.stdout).strip()[-300:]); return 2
        with contextlib.redirect_stdout(log):
            rec = record(deck, spec)
            mapping, probs, fit_code = finish(deck, spec, rec, story)
        v = subprocess.run([PY, str(TOOLS / "validate_deck.py"), str(deck), "--mapping", mapping], capture_output=True, text=True)
        log.write(v.stdout + v.stderr)
        overall = next((l.split(":", 1)[1].strip() for l in v.stdout.splitlines() if l.startswith("OVERALL")), "NOT VALIDATED")
        if probs:
            overall = "NEEDS CORRECTION - type scale"
        import checks, validate_deck as V, stamp as ST
        rows = [("Type scale on every run (typeset.py)", "FAIL" if probs else "PASS", "; ".join(probs[:3]))]
        if ids:                                       # a library build: its templates' own page rules (not for a user's page)
            lint = [f"{a}: {b}" for a, b in LIB.lint() if a in ids]
            rows.insert(0, ("Library page rules (front matter, one slide per section)", "FAIL" if lint else "PASS", "; ".join(lint[:3])))
        checks.add(deck, rows, requires="Template validation (validate_deck.py)")
        held, where = V.hold_back(deck)
        if held:
            print(f"NOT WRITTEN | template placeholder text on {where}: edit the page so each section fills its layout, then rebuild")
            return 1
        ver = ST.stamp(deck, "built from the process library", overall, owner, classification)
        # into place: the deck, its records and its review pictures (nothing half-made is ever left at out)
        moved = []
        for p in sorted(work.iterdir()):
            if p.name.startswith(out.stem) and p.name != spec_p.name:
                dst = out.parent / p.name
                if dst.exists():
                    shutil.rmtree(dst) if dst.is_dir() else dst.unlink()
                shutil.move(str(p), str(dst)); moved.append(dst)
        vd = out.parent / (out.stem + "_validation"); vd.mkdir(exist_ok=True)
        (vd / "build-log.txt").write_text(log.getvalue(), encoding="utf-8")
        shutil.copy2(spec_p, vd / "spec.json")
        review = [c[0] for c in ([x.strip() for x in l.strip().strip("|").split("|")] for l in v.stdout.splitlines()
                                 if l.lstrip().startswith("|")) if len(c) >= 3 and c[1] in ("REVIEW", "UNVERIFIED")
                  and not c[0].startswith("Template structure")]
        why = "no renderer here" if "LibreOffice not available" in v.stdout else "to review: " + ", ".join(review[:3])
        status = ("READY" if overall.startswith("READY") else f"DRAFT - VERIFICATION INCOMPLETE ({why})"
                  if "VERIFICATION INCOMPLETE" in overall else "NEEDS CORRECTION")
        said = [f"{status} | {out} v{ver} | {len(spec['slides'])} slides" + (f" from {', '.join(ids)}" if ids else "")]
        fails = [l.strip() for l in log.getvalue().splitlines() if l.strip().startswith("FAIL")]
        for l in v.stdout.splitlines():               # the gate's table rows: | check | FAIL | detail |
            cells = [c.strip() for c in l.strip().strip("|").split("|")] if l.lstrip().startswith("|") else []
            if len(cells) >= 3 and cells[1] == "FAIL":
                fails.append(f"FAIL  {cells[0]}: {cells[2][:200]}")
        said += [f"  {l}" for l in list(dict.fromkeys(fails))[:10]] + [f"  FAIL  {p}" for p in probs[:5]]
        said += expert_review(spec, title or "", md)   # Presentation Central's expert review: act on its lines, then rebuild
        pic = vd / "contact-sheet.png"
        if pic.exists():
            said.append(f"PICTURE {pic}")
        said.append(f"FILES: {out}")
        text = "\n".join(said)
        print(text)
        import tokens as TK
        print(TK.report(out, md, text, "built"))
        print(f"took {time.time() - t0:.1f} s")
        return 0 if status == "READY" and v.returncode == 0 and fit_code == 0 else 1
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); return 0
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "list":
        dom = _opt(args, "--domain")
        cat = LIB.catalogue()
        for d in cat["domains"]:
            if dom and d["name"].lower() != dom.lower():
                continue
            print(f"{d['name']} ({d['count']})")
            for l1 in d["l1"]:
                print(f"  {l1['name']}")
                for it in l1["items"]:
                    print(f"    {it['id']:36} {it['l2']}  [{it['slides']} slides]")
        print(f"{cat['count']} templates")
        return 0
    if cmd == "search":
        hits = LIB.search(" ".join(args))
        items = LIB.templates()
        for h in hits:
            m = items[h][0]
            print(f"{h:36} {m['domain']} > {m['l1']} > {m['l2']}: {m.get('summary', '')[:90]}")
        print(f"{len(hits)} match(es)" if hits else "no match - try fewer or broader words, or: python tools/playbook.py list")
        return 0
    if cmd == "pick":
        out, title = _opt(args, "--out"), _opt(args, "--title")
        top = int(_opt(args, "--top", "3") or 3)
        only_list = "--list" in args
        args = [a for a in args if a != "--list"]
        text = " ".join(args).strip()
        reqs = [r.strip() for r in (text.split(";") if ";" in text else text.split(",")) if r.strip()]
        if not reqs:
            print('pick needs requests: "three-way match controls; payment run KPIs" (one per slide, separated by ";")'); return 2
        if not out and not only_list:
            print("--out is required (or --list to see the candidates)"); return 2
        res = pick(reqs, top)
        items = LIB.templates()
        for n, (req, ranked) in enumerate(res, 1):
            if not ranked:
                print(f"{n}. {req} -> no match: try other words (python tools/playbook.py search <words>)"); continue
            (_, tid, h, _t), rest = ranked[0], ranked[1:]
            print(f"{n}. {req} -> {tid} | {h}  ({items[tid][0]['l2']})")
            if rest:
                print("   also: " + "; ".join(f"{t} | {hh}" for _, t, hh, _x in rest))
        if only_list:
            return 0
        got = [r for r in res if r[1]]
        if not got:
            print("NOT WRITTEN | nothing matched"); return 1
        Path(out).write_text(picked_page(res, title or "Selected process slides"), encoding="utf-8")
        print(f"FILES: {out}")
        print(f"next: put the user's facts into the page (placeholders, names, dates), then "
              f"python tools/playbook.py page {out} --out <Name>.pptx" + ("" if title else '  (give the deck its own --title)'))
        return 0 if len(got) == len(res) else 1
    if cmd == "review":
        title = _opt(args, "--title")
        if not args:
            print("review needs a page: python tools/playbook.py review page.md [--title T]"); return 2
        md = Path(args[0]).read_text(encoding="utf-8")
        m = LIB.FRONT.match(md)
        if m:
            title = title or next((l.split(":", 1)[1].strip() for l in m.group(1).splitlines() if l.lower().startswith("l2:")), None)
            md = md[m.end():]
        work = Path(tempfile.mkdtemp(prefix="ulta-review-"))
        try:
            (work / "page.md").write_text(md, encoding="utf-8")
            r = subprocess.run([PY, str(STUDIO / "page_to_spec.py"), str(work / "page.md"), "--out", str(work / "spec.json")]
                               + (["--title", title] if title else []), capture_output=True, text=True, cwd=str(work))
            if r.returncode or not (work / "spec.json").exists():
                print("NOT READ | the page could not be read: " + (r.stderr or r.stdout).strip()[-300:]); return 2
            spec = json.loads((work / "spec.json").read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(work, ignore_errors=True)
        for l in expert_review(spec, title or "", md):
            print(l)
        return 0
    if cmd == "show":
        items = LIB.templates()
        for i in args:
            if i not in items:
                print(f"not in the library: {i}"); return 2
            print(Path(items[i][0]["path"]).read_text(encoding="utf-8"))
        return 0
    if cmd == "check":
        bad = LIB.lint(agnostic="--agnostic" in args)
        for a, b in bad:
            print(f"  {a}: {b}")
        print(f"{LIB.catalogue()['count']} templates, {len(bad)} problem(s)")
        return 1 if bad else 0
    if cmd in ("md", "build", "page"):
        out = _opt(args, "--out"); title = _opt(args, "--title")
        owner = _opt(args, "--owner"); cls = _opt(args, "--classification")
        if not out:
            print("--out is required"); return 2
        if cmd == "page":
            if not args:
                print("page needs a Markdown file"); return 2
            md, ids = Path(args[0]).read_text(encoding="utf-8"), ()
            m = LIB.FRONT.match(md)                   # a library file passed as is: its front matter is not slide content
            if m:
                title = title or next((l.split(":", 1)[1].strip() for l in m.group(1).splitlines() if l.lower().startswith("l2:")), None)
                md = md[m.end():]
        else:
            ids = tuple(a for a in args if not a.startswith("--"))
            try:
                md, t = LIB.compose(ids, title)
            except KeyError as e:
                print(str(e).strip("'\"") + " - find ids with: python tools/playbook.py search <words>"); return 2
            title = title or t
        if cmd == "md":
            Path(out).write_text(md, encoding="utf-8"); print(f"FILES: {out}"); return 0
        return build(md, out, title, owner, cls, ids)
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main())
