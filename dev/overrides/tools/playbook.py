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
    python tools/playbook.py check [--agnostic]                    library health: front matter, sections, product names

A build: the page -> the Studio's Eco engine (studio/page_to_spec.py, rules, no AI) -> the deck on the approved template ->
a build record (which slides are drawn visuals, template infographics, shortened lists) -> Presentation Central's own
finishing (fit, accessibility, type scale, plain punctuation) -> the delivery gate (validate_deck.py) -> version stamp.
Prints a status line, FAIL lines, PICTURE (the contact sheet to review), FILES and the RESULT line.
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
        status = ("READY" if overall.startswith("READY") else "DRAFT - VERIFICATION INCOMPLETE (no renderer here)"
                  if "VERIFICATION INCOMPLETE" in overall else "NEEDS CORRECTION")
        said = [f"{status} | {out} v{ver} | {len(spec['slides'])} slides" + (f" from {', '.join(ids)}" if ids else "")]
        fails = [l.strip() for l in log.getvalue().splitlines() if l.strip().startswith("FAIL")]
        for l in v.stdout.splitlines():               # the gate's table rows: | check | FAIL | detail |
            cells = [c.strip() for c in l.strip().strip("|").split("|")] if l.lstrip().startswith("|") else []
            if len(cells) >= 3 and cells[1] == "FAIL":
                fails.append(f"FAIL  {cells[0]}: {cells[2][:200]}")
        said += [f"  {l}" for l in list(dict.fromkeys(fails))[:10]] + [f"  FAIL  {p}" for p in probs[:5]]
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
