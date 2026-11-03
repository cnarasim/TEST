#!/usr/bin/env python3
"""Build the ULTA SlideGlam skill from its two sources (reproducible, no network).

    python3 dev/build_skill.py --upc <ulta-presentation-central dir> --studio <Deliverable Studio runtime-kit dir> --out <dir>

Sources
  - ULTA Presentation Central v141 (the skill): tools/, modules/, guides/, brands/, fonts/, assets/
  - ULTA Deliverable Studio 6.37.1 (the Mac app's runtime-kit): the Eco page engine, the process library, and the
    Studio's own fixes to the shared Presentation Central tools (its central/ folder, v140 plus Studio fixes)

Layout of the result (Presentation Central's layout at the root, so every guide's tools/... path still works):
  SKILL.md, WORKFLOWS.md, CHANGELOG.md   written for this skill (dev/overrides)
  tools/      Presentation Central tools (PowerPoint only) + the Studio's fixes and extra tools + tools/playbook.py
  modules/    the PowerPoint modules (Word table guard dropped)
  studio/     the Studio's Eco engine: Markdown page -> spec -> deck, its families, process library reader, icons
  library/    the process library: ready-made decks as Markdown pages (Studio's 147 + this skill's additions)
  guides/     the PowerPoint guides (+ library.md)

Every patch names the exact text it replaces and the number of times it must occur: a source that changed stops the
build instead of being patched wrongly.
"""
import argparse, hashlib, json, os, re, shutil, sys
from pathlib import Path

DEV = Path(__file__).resolve().parent
OVERRIDES = DEV / "overrides"
NAME, PRODUCER, VERSION = "ulta-slideglam", "ULTA SlideGlam", "v1.0"

# ---------------------------------------------------------------------------------------------------------------- what ships
UPC_DROP = [   # not PowerPoint (Word, Excel, HTML dashboards and sites, UI screens, BigQuery demo) or not needed at run time
    "CHANGELOG.md", "PLAYBOOK.md", "integrity.json",
    "tools/bq_demo.py", "tools/ui_screens.py", "tools/site.py", "tools/ulta_excel.py", "tools/ulta_word.py",
    "tools/dashboard.py", "tools/whiteboard.py",
    "guides/excel.md", "guides/word.md", "guides/sites.md", "guides/ui-screens.md", "guides/dashboards.md",
    "modules/ultawordtableguard",
    "modules/ultabranddeliverables/scripts/kit/data",
    "modules/ultabranddeliverables/scripts/kit/whiteboard",
    "modules/ultabranddeliverables/scripts/kit/templates/Ulta Beauty Word template.docx",
    "modules/ultabranddeliverables/scripts/kit/html",                       # HTML slide decks (not PowerPoint)
    "modules/ultabranddeliverables/references/gallery/deck-layouts",        # reference pictures for people, read by no code
    "modules/ultabranddeliverables/references/gallery/diagrams",
    "modules/ultabranddeliverables/references/gallery/index.html",
    "modules/ultabranddeliverables/references/gallery/gallery.json",
    "modules/ultapowerpointvalidator/examples",                             # worked examples, read by no code, not in its manifest
    # no ARB: the ARB template, its slide map and the Concept ARB intake module
    "modules/ultabranddeliverables/scripts/kit/templates/ARB Template - v3.6 as of 9-1-26.pptx",
    "modules/ultabranddeliverables/scripts/kit/template-map-ARB36.md",
    "modules/pptintentdiscovery",
] + [f"tools/ooxml_schemas/ISO-IEC29500-4_2016/{x}.xsd" for x in (         # schemas no PowerPoint part needs (Word, VML, maths ...)
    "dml-wordprocessingDrawing", "shared-additionalCharacteristics", "shared-bibliography", "shared-customXmlDataProperties",
    "shared-customXmlSchemaProperties", "shared-documentPropertiesCustom", "shared-documentPropertiesExtended",
    "shared-documentPropertiesVariantTypes", "shared-math", "vml-main", "vml-officeDrawing", "vml-presentationDrawing",
    "vml-spreadsheetDrawing", "vml-wordprocessingDrawing", "wml", "xml")]
# The Studio's copies of shared tools: v140 plus Studio fixes that v141 does not have (title fit at 94% of the box, the
# takeaway line under the headline's own text, editable visual groups, an engine-safe icon lookup, sankey colours, "Avg"
# naming, a render check on any renderer). v141's own changes (BigQuery dashboards, the 99% estimate cap) are kept by
# leaving tokens.py, stamp.py and selftest.py as v141; lo/audience/onepager/bootstrap stay v141 because the Studio's
# versions never start LibreOffice unless a server administrator allows it, which would switch off a skill's render check.
STUDIO_TOOLS = ["build_deck.py", "validate_deck.py", "chart_advisor.py", "modern_charts.py", "look.py", "pictograms.py",
                "visual_spec.py", "review_deck.py", "deck_doctor.py", "meeting.py", "report_pack.py", "people.py",
                "controls.py", "walkthrough.py"]
STUDIO_ENGINE = ["page_to_spec.py", "build_from_storyboard.py", "family_rules.py", "central_slides.py", "slide_svg.py",
                 "narration.py", "themes.py", "svgraster.py", "process_library.py",
                 "template-map-STANDARD33.md",
                 "infographic/info.py", "infographic/templates.py", "infographic/ulta-logo.svg",   # not info-template.html: HTML pages (it calls the app's server)
                 "enterprise/steerco_pack.py", "enterprise/process_insights.py", "enterprise/common.py"]

KIT_REL = "modules/ultabranddeliverables/scripts/kit"
# self-test library cases (templates that build READY), and the library's minimum size
LIB_ONE, LIB_TWO, LIB_SEARCH = "sc-wh-cycle-count", ["rt-oc-fulfilment", "fi-pp-three-way-match"], ("cycle count", "sc-wh-cycle-count")
LIB_PICK = ("three-way match controls; cycle count swimlane; cutover timeline",   # one slide per request, each from its template
            ["fi-pp-three-way-match (", "sc-wh-cycle-count (", "pp-dl-cutover ("])
LIBRARY_MIN = 294


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def patch(path, old, new, count=1):
    s = path.read_text(encoding="utf-8")
    n = s.count(old)
    if n != count:
        sys.exit(f"PATCH STOP {path}: expected {count} x {old[:70]!r}, found {n}")
    path.write_text(s.replace(old, new), encoding="utf-8")


def rm(p):
    if p.is_dir():
        shutil.rmtree(p)
    elif p.exists():
        p.unlink()
    else:
        sys.exit(f"DROP STOP: {p} not in the source (the drop list is out of date)")


def build(upc, rk, out):
    if out.exists():
        shutil.rmtree(out)
    ign = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
    shutil.copytree(upc, out, ignore=ign)
    for rel in UPC_DROP:
        rm(out / rel)

    # ---- the Studio's fixed and extra tools
    for f in STUDIO_TOOLS:
        shutil.copy2(rk / "central" / "tools" / f, out / "tools" / f)
    # validate_deck's no-LibreOffice fallback draws slides with the Studio's slide_svg, found two folders up in the app
    patch(out / "tools/validate_deck.py", "sys.path.insert(0, str(Path(__file__).resolve().parents[2]))",
          "sys.path.insert(0, str(Path(__file__).resolve().parents[1] / \"studio\"))")
    # the Studio's lo.allowed() gate, as a skill sees it: LibreOffice is allowed unless switched off
    patch(out / "tools/lo.py", "\ndef soffice(", "\ndef allowed():\n    \"\"\"LibreOffice may be used (the Studio's gate, as a skill sees it: on unless ULTA_NO_LIBREOFFICE=1).\"\"\"\n"
          "    return os.environ.get(\"ULTA_NO_LIBREOFFICE\", \"\").strip().lower() not in (\"1\", \"true\", \"yes\")\n\n\ndef soffice(")
    patch(out / "tools/lo.py", "def soffice():\n    return shutil.which(\"soffice\") or shutil.which(\"libreoffice\")",
          "def soffice():\n    if not allowed():   # ULTA_NO_LIBREOFFICE=1: no render (batch builds); the gate then says UNVERIFIED, never PASS\n"
          "        return None\n    return shutil.which(\"soffice\") or shutil.which(\"libreoffice\")")

    # ---- the Studio's Eco engine in studio/, its central/ paths pointed at this skill's root
    eng = out / "studio"
    for f in STUDIO_ENGINE:
        (eng / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(rk / f, eng / f)
    up = "os.path.dirname(os.path.dirname(os.path.abspath(__file__)))"
    bfs = eng / "build_from_storyboard.py"
    # one icon set for both engines (the kit's folder, refreshed below with the Studio's superset)
    patch(bfs, "ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons')",
          f"ICON_DIR = os.path.join({up}, *'{KIT_REL}/icons'.split('/'))")
    patch(bfs, "os.path.join(kit, 'icons', ", "os.path.join(ICON_DIR, ")
    patch(eng / "infographic/info.py", "os.path.join(KIT, 'icons'", f"os.path.join(os.path.dirname(KIT), *'{KIT_REL}/icons'.split('/')", 3)
    patch(bfs, "os.path.join(os.path.dirname(os.path.abspath(__file__)), 'central', 'fonts')", f"os.path.join({up}, 'fonts')")
    patch(bfs, "os.path.join(os.path.dirname(os.path.abspath(__file__)), 'central', 'tools')", f"os.path.join({up}, 'tools')", 3)
    patch(eng / "slide_svg.py", "os.path.join(os.path.dirname(os.path.abspath(__file__)), 'central', 'fonts')", f"os.path.join({up}, 'fonts')")
    cs = eng / "central_slides.py"
    patch(cs, "TOOLS = os.path.join(HERE, 'central', 'tools')", "TOOLS = os.path.join(os.path.dirname(HERE), 'tools')")
    patch(cs, "os.path.join(HERE, 'central', 'brands', 'ulta', 'modern-sample.json')",
          "os.path.join(os.path.dirname(HERE), 'brands', 'ulta', 'modern-sample.json')")
    # the library lives at the skill root; templates are Presentation Central's own (one copy of each .pptx)
    patch(eng / "process_library.py", "DIRS = [os.path.join(HERE, 'library')]", "DIRS = [os.path.join(os.path.dirname(HERE), 'library')]")
    patch(eng / "page_to_spec.py", "tdir = tdir or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')",
          f"tdir = tdir or os.path.join({up}, *'{KIT_REL}/templates'.split('/'))")
    kit_tpl = "*'" + KIT_REL + "/templates'.split('/')"
    patch(eng / "enterprise/common.py", "'--templates', os.path.join(KIT, 'templates')",
          f"'--templates', os.path.join(os.path.dirname(KIT), {kit_tpl})")
    sp_ = eng / "enterprise/steerco_pack.py"
    patch(sp_, "'--templates', os.path.join(C.KIT, 'templates')", f"'--templates', os.path.join(os.path.dirname(C.KIT), {kit_tpl})")
    patch(sp_, "os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'central', 'tools')",
          "os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'tools')")
    patch(sp_, "os.path.join(C.KIT, 'central', 'tools', 'compliance.py')", "os.path.join(os.path.dirname(C.KIT), 'tools', 'compliance.py')")
    for f in STUDIO_ENGINE:
        if f.endswith(".py") and re.search(r"'central',\s*'", (eng / f).read_text(encoding="utf-8")):
            sys.exit(f"PATH STOP: studio/{f} still names a central/ folder")

    # ---- engine fixes found by building all 147 library decks through Presentation Central's delivery gate
    # (1) table cell borders in schema order (a:lnL a:lnR a:lnT a:lnB, then the fill): written after python-pptx's
    #     <a:noFill/>, or each inserted at index 0 (reversed), PowerPoint may offer to repair the file
    patch(bfs, "                for side in ('a:lnL', 'a:lnR', 'a:lnT', 'a:lnB'):\n"
               "                    ln_ = etree.SubElement(tcPr, A + side[2:], w='0'); etree.SubElement(ln_, A + 'noFill')",
          "                for k_, side in enumerate(('a:lnL', 'a:lnR', 'a:lnT', 'a:lnB')):   # schema order: borders before the fill\n"
          "                    ln_ = etree.Element(A + side[2:], w='0'); etree.SubElement(ln_, A + 'noFill'); tcPr.insert(k_, ln_)")
    patch(bfs, "                for side in ('lnL', 'lnR', 'lnT', 'lnB'):\n                    for old in pr.findall('a:' + side, NS): pr.remove(old)",
          "                for side in ('lnB', 'lnT', 'lnR', 'lnL'):   # each inserted first: lnL lnR lnT lnB, the schema's order\n"
          "                    for old in pr.findall('a:' + side, NS): pr.remove(old)")
    # (1b) the flow tables' body grey is the template's neutral, not a colour of its own
    patch(bfs, "'3D3532'", "'404040'", 3)
    # (1c) table rows per slide estimated at the template's own type size (16 pt on the actions table), never stepping down
    #      to 9 pt to save a slide: a long table continues on a "(cont.)" slide, as Presentation Central's standard asks
    patch(eng / "page_to_spec.py",
          "    g12 = chunk_rows(data, n, kind)\n    if len(g12) <= 1 or kind != 'actions': return g12, None\n"
          "    g9 = chunk_rows(data, n, kind, pt=9)\n    return (g9, 9) if len(g9) < len(g12) else (g12, None)",
          "    return chunk_rows(data, n, kind, pt=16 if kind == 'actions' else None), None   # ULTA SlideGlam: the template's 16 pt")
    # (1d) a rating grid repeats its scale words and a template its [placeholders]: not filler
    patch(out / "tools/validate_deck.py", "            seen = [v for v in vals if len(v) >= 3]",
          "            seen = [v for v in vals if len(v) >= 3 and not RATING.match(v)]   # a rating grid repeats its scale words")
    patch(out / "tools/validate_deck.py", "\nREPEAT_OK = ",
          "\nRATING = re.compile(r\"(?i)^\\s*(\\[[^\\]]{1,24}\\]|high|medium|low|strong|moderate|weak|none|partial|full|yes|no|n/?a|done|open|"
          "closed|on track|at risk|late|green|amber|red|good|fair|poor|planned|in progress|complete|not started|must|should|could|won't"
          "|(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\\.? \\d{1,2},? \\d{4}|\\d{4}-\\d{2}-\\d{2}|q[1-4] \\d{4}"
          "|[+\\-\\u2212]?[$€£]?\\d[\\d,.]*\\s?(?:%|[kmb]|h|hrs?|hours?|days?|weeks?|pts?)?)\\s*$\")   # scale words, placeholders, dates and figures (signed too) are data\n"
          "STATUS_COLOURS = {\"00B050\", \"0BA03E\", \"FFC000\", \"FF0000\"}   # the brand's status palette (brand.json)\n"
          "STATUS_MARKS = set(\"●○■□▲▼◆◇★►◀▶◄•\")   # dot, square, arrow ... (brand_colours.MARKS)\n"
          "REPEAT_OK = ")
    # (1f) a template infographic may mark status in its text colour (the fidelity gate already allows status marks)
    patch(out / "tools/validate_deck.py", '                       or (st[3] not in rco and not (inherit_white and str(st[3]).upper() in ("FFFFFF", "BG1", "LT1"))))]',
          '                       or (st[3] not in rco and not (inherit_white and str(st[3]).upper() in ("FFFFFF", "BG1", "LT1"))\n'
          '                           and not (i in INFO and str(st[3]).upper() in STATUS_COLOURS)))]')
    # (1e) picture clearance: an ADDED pictogram (the Studio's table-head and card icons) is measured like any picture -
    #      it passes when it covers no text; a MOVED template picture still fails at once, as before
    vd = out / "tools/validate_deck.py"
    patch(vd, '                    old = pics.get(ob["key"])\n'
              '                    if old is None or (old["rect"] != ob["rect"] and i not in LIST):   # a shortened list: icons move with\n'
              '                        return "FAIL", [], f"picture {ob[\'key\']} on slide {i} was moved or added"   # their column or row\n'
              '                    area = sum(fit.overlap(l["rect"], ob["rect"]) for l in cur.get("lines", []))\n'
              '                    old_area = sum(fit.overlap(l["rect"], old["rect"]) for l in before.get("lines", []))',
          '                    old = pics.get(ob["key"])\n'
          '                    if old is not None and old["rect"] != ob["rect"] and i not in LIST:   # a shortened list: icons move with\n'
          '                        return "FAIL", [], f"picture {ob[\'key\']} on slide {i} was moved"   # their column or row\n'
          '                    area = sum(fit.overlap(l["rect"], ob["rect"]) for l in cur.get("lines", []))\n'
          '                    old_area = sum(fit.overlap(l["rect"], old["rect"]) for l in before.get("lines", [])) if old is not None else 0.0   # added: measured')
    # (1g) the takeaway line keeps Presentation Central v141's place under the headline: the Studio's v6.37.1 placement
    #      (below the headline's measured descenders) leaves the cards and metrics layouts no clear space, so their takeaway
    #      went to the notes only and a two-line summary was no longer flagged - v141's own self-test asserts both
    patch(out / "tools/build_deck.py",
          "            # v6.37.1 under the headline's own text: at 0.58 in a 36 pt headline's descenders ran into the line (a 36 pt line is 0.63 in)\n"
          "            hpt = explicit_or_inherited(head)\n"
          "            hl = max(1, _lines(head.text_frame.text, int(w * 0.94), int(hpt * 12700), BRAND.font(\"heading\"), _B.metrics_for(BRAND)))\n"
          "            text_end = head.top + Emu_(head.text_frame.margin_top) + int(hl * hpt * HEAD_LINE_EM / 72 * IN)\n"
          "            top = max(head.top + int(SUMMARY_TOP * IN), text_end + int(HEAD_GAP_IN * IN))\n",
          "            top = head.top + int(SUMMARY_TOP * IN)   # ULTA SlideGlam: v141's place (see dev/build_skill.py, 1g)\n")
    # (1h) a status dot only for a status: the whole cell is the status word, or the word and then a note ("At risk - vendor",
    #      "Done (Mar 3)", "Late by 2 days"); a label that starts with one ("Late changes", "Failed messages", "Live or drop")
    #      is a label, and a red or green dot beside it misreads the table
    patch(bfs, "        if low in words or any(low.startswith(w + ' ') for w in words):",
          "        if low in words or any(re.match(re.escape(w) + r'(\\s*[-\\u2013:(,;]|\\s+\\d|\\s+(?:by|until|since)\\b)', low) for w in words):   # (1h)")
    # (1j) a heading inside a text box keeps the template box's own face, made bold (b=1): the Studio switched it to the
    #      Medium face, which the type standard maps to Circular Bold, at a size (15 pt) the standard has no role for, so
    #      the gate failed every two-box slide with card headings ("formatting not in the template box")
    patch(bfs, "            for tag in ('latin', 'cs'):           # the template's bold style = b=1 + the Medium face of the same family\n"
               "                f = rpr.find(f'a:{tag}', NS)\n"
               "                if f is not None and f.get('typeface', '').endswith(' Book'):\n"
               "                    f.set('typeface', f.get('typeface')[:-5] + ' Medium')\n",
          "            # (1j) the template box's own face, bold by b=1 (the Medium face became Circular Bold at a size off the type standard)\n")
    # (1k) a figure in a template text box is made bold, not orange: the template's boxes hold black text only (the gate's
    #      "write into the existing runs" rule); figures keep their emphasis, drawn slides keep their colours
    patch(eng / "page_to_spec.py", "        return f'{{{accent}}}**{tok}**{{/}}'",
          "        return f'**{tok}**'   # (1k) bold, in the box's own colour")
    # (1l) the scorecard's two lists (lowlights, highlights) come from the page: its "Lowlight:" / "Highlight:" lines, else
    #      the KPIs themselves by status (off target = lowlight); the Studio left both empty, so every scorecard slide kept
    #      the template's empty rows ("emptied template structure") - nothing is invented, only the page's own figures
    patch(eng / "family_rules.py",
          "    grp = {}\n    for k, l in enumerate(plain(x) for x in lines):\n"
          "        lab, body = split_label(l); p = [x.strip() for x in body.split('|')] if lab else []\n"
          "        if len(p) < 4: return None\n",
          "    grp, lows, highs = {}, [], []\n    for k, l in enumerate(plain(x) for x in lines):\n"
          "        lab, body = split_label(l)\n"
          "        if lab in ('lowlight', 'lowlights', 'highlight', 'highlights'):   # (1l) the page's own notes for the two lists\n"
          "            (lows if lab.startswith('low') else highs).append(body.strip()); continue\n"
          "        p = [x.strip() for x in body.split('|')] if lab else []\n"
          "        if len(p) < 4: return None\n")
    patch(eng / "family_rules.py",
          "    return {'scorecard': {'columns': ['Prior', 'Target', 'Actual'], 'note': 'vs target', 'groups': [{'name': g, 'kpis': v} for g, v in grp.items()],\n"
          "                          'lowlights': [], 'highlights': []}}",
          "    if not lows and not highs:                       # (1l) else the KPIs by status: off target -> lowlights, on target -> highlights\n"
          "        for row in (r for v in grp.values() for r in v):\n"
          "            name, st = row[0][:1].upper() + row[0][1:], str(row[4]).strip().lower()\n"
          "            (lows if st in ('red', 'amber', 'at risk', 'off track') else highs if st in ('green', 'on track', 'done') else []).append(f'{name} {row[3]} vs {row[2]} target')\n"
          "    return {'scorecard': {'columns': ['Prior', 'Target', 'Actual'], 'note': 'vs target', 'groups': [{'name': g, 'kpis': v} for g, v in grp.items()],\n"
          "                          'lowlights': lows[:5] or ['No measure off target'], 'highlights': highs[:5] or ['No measure on target yet']}}")
    # (2b) the structure-check copy also leaves out the Studio's named overlays (pictograms, the takeaway line), as it
    #      leaves out Presentation Central's summary layer: additions on top of the template's shapes, not changed shapes;
    #      the picture clearance check still measures every pictogram on the real deck
    patch(vd, '        if re.match(r"ppt/slides/slide\\d+\\.xml$", n) and (b"ULTA summary" in d or b"ULTA decision" in d):\n'
              '            x = etree.fromstring(d)\n'
              '            for nv in list(x.iter("{%s}cNvPr" % NS["p"])):\n'
              '                if nv.get("name") in ("ULTA summary", "ULTA decision"):\n',
          '        if re.match(r"ppt/slides/slide\\d+\\.xml$", n) and any(k in d for k in (b"ULTA summary", b"ULTA decision", b"ULTA takeaway", b"ULTA icon ")):\n'
          '            x = etree.fromstring(d)\n'
          '            for nv in list(x.iter("{%s}cNvPr" % NS["p"])):\n'
          '                if nv.get("name") in ("ULTA summary", "ULTA decision", "ULTA takeaway") or (nv.get("name") or "").startswith("ULTA icon "):   # (2b)\n')
    # (1m) the contrast pass leaves a status mark alone: an amber dot (FFC000) on a white cell sits under 3:1 and was turned
    #      black, so "Amber" lost its colour and the gate saw black text it did not expect; the dot is a mark (the brand
    #      rule: status colours on marks only) and the word beside it says the status in text
    patch(bfs, "        for r in holder.findall('.//a:r', NS):\n            rpr = r.find('a:rPr', NS)\n"
               "            if rpr is None: rpr = r.makeelement(A + 'rPr', {}); r.insert(0, rpr)\n",
          "        for r in holder.findall('.//a:r', NS):\n            rpr = r.find('a:rPr', NS)\n"
          "            t_, c_ = r.find('a:t', NS), r.find('a:rPr/a:solidFill/a:srgbClr', NS)\n"
          "            if t_ is not None and (t_.text or '').strip() and set(t_.text.strip()) <= set('●○■□▲▼◆◇★►◀▶◄•') \\\n"
          "                    and c_ is not None and (c_.get('val') or '').upper() in ('00B050', '0BA03E', 'FFC000', 'FF0000'):\n"
          "                continue                       # (1m) a status mark keeps its colour: it is the mark's message\n"
          "            if rpr is None: rpr = r.makeelement(A + 'rPr', {}); r.insert(0, rpr)\n")
    # (1n) a template infographic (scorecard, OGSM, house, quad, funnel, donut, map) is filled by Presentation
    #      Central's filler on the template's own slide, as in build_deck: the Studio first cleared every region it did not
    #      fill itself, so the filler found the OGSM's row labels (Objective, Goals ...), the scorecard's Highlights and
    #      Lowlights headers and the goal numbers already gone ("emptied template structure")
    patch(bfs, "        for key, sh in regions.items():\n            if key in fills or key in keep:\n                continue\n            if sh.has_table:\n",
          "        c_ = sd.get('central') if isinstance(sd.get('central'), dict) else {}\n"
          "        tmpl_info = c_.get('family') == 'infographic'   # (template timelines keep the clean-up: their filler expects it)\n"
          "        for key, sh in regions.items():\n            if key in fills or key in keep or tmpl_info:   # (1n) the filler works on the template's own slide\n"
          "                continue\n            if sh.has_table:\n")
    # (1o) a takeaway headline computed from the data only when it fits the template's one-line headline: the Studio
    #      allowed 60 characters, so "1,450 hours saved a month, $520K cost saved a year" failed "does not fit one line at
    #      the standard 36 pt" on every deck it wrote; longer, the author's own heading stays
    patch(eng / "family_rules.py",
          "    return out if len(out) <= 60 else (say[:1].upper() + say[1:] if len(say) <= 60 else None)",
          "    return out if len(out) <= 42 else (say[:1].upper() + say[1:] if len(say) <= 42 else None)   # (1o) one line at 36 pt")
    # (1p) a card header that inherits its size from the template (24 pt in the display serif) is measured at 24 pt when
    #      an icon is added beside it: the Studio assumed 18 pt for any inherited size and wrote 18 pt into every card
    #      title, which the type-scale check fails ("had to shrink to 18 pt - the template sets it at 24 pt")
    patch(bfs, "        avail = (tbl.columns[c].width - 2 * pad) / 914400; words = cell.text.split() or ['']\n        pt = _run_pt(cell, 18.0)\n",
          "        avail = (tbl.columns[c].width - 2 * pad) / 914400; words = cell.text.split() or ['']\n"
          "        pt = _run_pt(cell, 24.0 if serif else 18.0)   # (1p) an inherited serif header is the template's 24 pt\n")
    # (1i) a status mark is a mark, not text: the content gate skips a run that is only a dot, square or arrow in a status
    #      colour, as the brand colours gate already does ("status colours on marks only"); the words beside it are checked
    patch(vd, '                continue\n            rpr = r.find("a:rPr", NS)\n            lat = rpr.find("a:latin", NS) if rpr is not None else None\n',
          '                continue\n            rpr = r.find("a:rPr", NS)\n'
          '            if set(t.text.strip()) <= STATUS_MARKS and str(run_colour(rpr)).upper() in STATUS_COLOURS:\n'
          '                continue                           # a status mark: the brand colours gate checks it (marks only)\n'
          '            lat = rpr.find("a:latin", NS) if rpr is not None else None\n')
    # (2) the Studio's named overlays on a template slide (auto pictograms beside template text, the takeaway line under
    #     the headline) are additions like Presentation Central's own summary layer, not changed template shapes
    patch(out / "tools/template_infographics.py",
          '            if nm in ("ULTA summary", "ULTA decision"):       # the summary layer: added above and below the template\'s shapes\n                continue',
          '            if nm in ("ULTA summary", "ULTA decision", "ULTA takeaway") or nm.startswith("ULTA icon "):   # overlays: summary layer, Studio takeaway, pictograms\n                continue')

    # ---- the library's three new domains, in the picker after the Studio's nine
    patch(eng / "process_library.py",
          "    ('Infographics', 'bar-chart', 'Big numbers, scorecards, shares, rankings, funnels, maps and plans'),\n]",
          "    ('Infographics', 'bar-chart', 'Big numbers, scorecards, shares, rankings, funnels, maps and plans'),\n"
          "    ('Technology Operations', 'server', 'Incidents, problems, monitoring, changes and releases, service requests, access and service levels'),   # ULTA SlideGlam\n"
          "    ('Data and AI', 'database', 'Data governance, quality and master data, analytics products, AI use cases, responsible AI, agent reviews'),\n"
          "    ('People and Change', 'users', 'Organisation design, roles and skills, workforce plans, change impact, adoption and champions'),\n]")

    # ---- the process library (Markdown pages); previews are drawn on demand, not shipped
    shutil.copytree(rk / "library", out / "library", ignore=shutil.ignore_patterns("previews", "__pycache__"))
    rm(out / "library/enterprise-architecture/review-and-decide/ea-rd-arb-submission.md")   # no ARB

    # ---- one icon set for both engines: the Studio's is a superset of the kit's
    kit_icons = out / KIT_REL / "icons"
    shutil.rmtree(kit_icons); shutil.copytree(rk / "icons", kit_icons)

    # ---- the Word and ARB templates leave the kit's template manifest with their files
    man_p = out / KIT_REL / "templates" / "manifest.json"
    man = json.loads(man_p.read_text(encoding="utf-8"))
    for tid, t in list(man["templates"].items()):
        if str(t.get("file", "")).lower().endswith(".docx") or tid.upper().startswith("ARB") or "ARB" in str(t.get("file", "")):
            del man["templates"][tid]

    # ---- no ARB: bootstrap no longer requires the ARB template; the diagram standard's panel and hint name no board;
    #      the storyboard and review modules lose their Concept ARB sections
    bs = out / "tools/bootstrap.py"
    patch(bs, 'ARB_SHA = "611a8d59ccd6aeff0f10b7a9b07e307579871ef2d195e680ec1c3f45d200311c"\n', "")
    patch(bs, '    arb = KIT / "kit" / "templates" / "ARB Template - v3.6 as of 9-1-26.pptx"\n'
              '    if arb.exists() and sha(arb) == ARB_SHA:\n'
              '        print(f"PASS  ARB template v3.6 (22 slides): {arb}")\n'
              '    else:\n'
              '        print("FAIL  ARB Template v3.6 missing or changed"); hard_fail = True\n\n', "")
    ed = out / "tools/enterprise_diagram.py"
    patch(ed, "Key Design Decisions & ARB Review Evidence", "Key Design Decisions & Review Evidence", 2)
    patch(ed, "Key Design Decisions &amp; ARB Review Evidence", "Key Design Decisions &amp; Review Evidence")
    patch(ed, "ARB reviewers expect KDD-001", "reviewers expect KDD-001")
    for mod, head in (("executivepresentationstoryboarder", "# Requested Concept ARB coverage"),
                      ("executivepresentationreviewer", "# Requested Concept ARB acceptance")):
        p_ = out / "modules" / mod / "MODULE.md"
        s_ = p_.read_text(encoding="utf-8")
        if head not in s_:
            sys.exit(f"PATCH STOP {p_}: no '{head}' section")
        p_.write_text(s_[:s_.index(head)].rstrip() + "\n", encoding="utf-8")
    patch(out / "modules/executivepresentationstoryboarder/MODULE.md",
          " Concept/Design ARB content requirements apply only to the requested review type.", "")
    man_p.write_text(json.dumps(man, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # ---- PowerPoint schemas only: a part whose schema is not shipped (a Word file) is skipped, never a crash
    oc = out / "tools/ooxml_check.py"
    patch(oc, "def _schema(name):\n    if name not in _CACHE:",
          "def _schema(name):\n    if not (DIR / name).exists():                      # ULTA SlideGlam ships the PowerPoint schemas only\n"
          "        return None\n    if name not in _CACHE:")
    patch(oc, "            else:\n                continue\n            try:\n                x = _resolve_mc(",
          "            else:\n                continue\n            if sc is None:\n                continue\n            try:\n                x = _resolve_mc(")
    kd = out / "modules/ultabranddeliverables"
    patch(kd / "MODULE.md", "one picture per style in `references/gallery/diagrams/`)",
          "style pictures are not shipped in ULTA SlideGlam: draw a small sample to see one)")
    patch(kd / "references/diagram-styles.md", "`gallery/diagrams/` holds a picture of each one (01-bands.png ... 17-cloud.png).",
          "(ULTA SlideGlam does not ship the style pictures: draw a small sample to see one.)")

    # ---- PowerPoint only: the tools that offered a Word copy or checked the site publisher keep working without them
    patch(out / "tools/audience.py", "        import ulta_word; ulta_word.brand(p, made=True); made.append(p)",
          "        made.append(p)   # ULTA SlideGlam: PowerPoint only - the Word copy is plain .docx (no Word letterhead tool shipped)")
    patch(out / "tools/brand_colours.py", "    import ulta_word\n    return set(ulta_word.WORD_PALETTE)",
          "    try:\n        import ulta_word\n    except ImportError:   # ULTA SlideGlam ships no Word tools\n        return set()\n    return set(ulta_word.WORD_PALETTE)")

    # ---- its own working folders: the 40-layout reference cache and the fontconfig live under the temp folder by
    # skill name, so this skill and Presentation Central installed side by side never read each other's cache
    patch(out / "tools/full_template.py", '/ "ulta-presentation-central" / f"Ulta Beauty PPT Standard-40-', f'/ "{NAME}" / f"Ulta Beauty PPT Standard-40-')
    patch(out / "tools/lo.py", 'Path(tempfile.gettempdir()) / "ulta-presentation-central" / "fontconfig"', f'Path(tempfile.gettempdir()) / "{NAME}" / "fontconfig"')
    patch(out / "tools/doctor.py", '"skill": "ulta-presentation-central"', f'"skill": "{NAME}"')

    # ---- self-test: PowerPoint features only, plus the process library
    st = out / "tools/selftest.py"
    for call in ("editable_pages", "bq_demo", "ui_screens", "page_scripts"):   # HTML pages, BigQuery dashboards, UI screens
        patch(st, f"    rows.append({call}(w))\n", "")
    patch(st, 'def run(name, cmd, cwd, expect="READY", tokens=True, check=None):\n    t0 = time.time()\n',
          'def run(name, cmd, cwd, expect="READY", tokens=True, check=None):\n'
          '    tool = next((Path(str(c)) for c in cmd if str(c).endswith(".py")), None)\n'
          '    if tool is not None and not tool.exists():          # Word, Excel, dashboards, sites, whiteboards: not in this skill\n'
          '        return (name, True, "SKIP", "not part of this PowerPoint skill", 0.0)\n'
          '    t0 = time.time()\n')
    patch(st, "\ndef slides(p):",
          "\ndef library_checks(w):\n"
          "    \"\"\"The process library: every page lints clean and application-agnostic; templates build READY on their own and\n"
          "    as one deck of chapters; search finds a template by its words.\"\"\"\n"
          "    rows, t0 = [], time.time()\n"
          "    r = subprocess.run([PY, str(T / \"playbook.py\"), \"check\", \"--agnostic\"], capture_output=True, text=True, timeout=240)\n"
          "    m = re.search(r\"(\\d+) templates, (\\d+) problem\", r.stdout)\n"
          "    n, bad = (int(m.group(1)), int(m.group(2))) if m else (0, -1)\n"
          f"    rows.append((\"process library (every page lints clean)\", n >= {LIBRARY_MIN} and bad == 0, \"-\", f\"{{n}} templates, {{bad}} problem(s)\", round(time.time() - t0, 1)))\n"
          "    rows.append(run(\"library deck (one template)\", [T / \"playbook.py\", \"build\", LIB_ONE, \"--out\", w / \"lib-one.pptx\"], w))\n"
          "    rows.append(run(\"library deck (templates as chapters)\", [T / \"playbook.py\", \"build\", *LIB_TWO, \"--out\", w / \"lib-two.pptx\"], w))\n"
          "    t0 = time.time()\n"
          "    r = subprocess.run([PY, str(T / \"playbook.py\"), \"search\", *LIB_SEARCH[0].split()], capture_output=True, text=True)\n"
          "    rows.append((\"library search\", LIB_SEARCH[1] in r.stdout, \"-\", (r.stdout.strip().splitlines() or ['no output'])[-1][:60], round(time.time() - t0, 1)))\n"
          "    t0 = time.time()\n"
          "    r = subprocess.run([PY, str(T / \"playbook.py\"), \"pick\", LIB_PICK[0], \"--out\", str(w / \"picked.md\"), \"--title\", \"Picked\"], capture_output=True, text=True)\n"
          "    page = (w / \"picked.md\").read_text(encoding=\"utf-8\") if (w / \"picked.md\").exists() else \"\"\n"
          "    rows.append((\"library pick (one slide per request, any template)\", all(f\"template {i}\" in page for i in LIB_PICK[1]), \"-\",\n"
          "                 f\"{page.count(chr(10) + '## ')} slides from {len(LIB_PICK[1])} templates\", round(time.time() - t0, 1)))\n"
          "    return rows\n\n\ndef slides(p):")
    patch(st, "    import importlib.util\n    tools = {k: bool(shutil.which(k)) for k in (\"soffice\", \"pdftoppm\")}\n",
          "    rows.extend(library_checks(w))\n"
          "    skipped = [r[0] for r in rows if r[2] == \"SKIP\"]\n"
          "    rows = [r for r in rows if r[2] != \"SKIP\"]\n"
          "    import importlib.util\n    tools = {k: bool(shutil.which(k)) for k in (\"soffice\", \"pdftoppm\")}\n")
    patch(st, "          + (f\" | work folder {w}\" if w.exists() else \" | work folder removed\"))\n",
          "          + (f\" | work folder {w}\" if w.exists() else \" | work folder removed\"))\n"
          "    if skipped:\n"
          "        print(f\"not part of this PowerPoint skill (not run): {', '.join(skipped)}\")\n")
    patch(st, "\nT = Path(__file__).resolve().parent\n",
          f"\nT = Path(__file__).resolve().parent\nLIB_ONE, LIB_TWO, LIB_SEARCH, LIB_PICK = {LIB_ONE!r}, {LIB_TWO!r}, {LIB_SEARCH!r}, {LIB_PICK!r}   # library cases\n")

    # the chart test keeps its PowerPoint half (every chart kind with axis ids PowerPoint reads; an old deck refused and
    # healed); the dashboard deck and the Excel workbook it also checked are not part of this skill
    patch(st, '    r = subprocess.run([PY, "-I", str(T / "dashboard.py"), "build", str(w / "fill.csv"), "--out", str(w / "fill"), "--grain", "month",\n'
              '                        "--charts", "paired:Region@Units Ordered&Units Shipped; combo:@Units Shipped&Fill Rate; "\n'
              '                                    "pareto:Category@Net Sales; bar:Category@Net Sales", "--deck", "--excel"],\n'
              '                       capture_output=True, text=True, cwd=w, timeout=900)\n'
              '    deck, book, bad = w / "fill.pptx", w / "fill.xlsx", []\n'
              '    if not deck.exists() or not book.exists():\n'
              '        return (name, False, "-", "BAD no deck or workbook: " + (r.stdout + r.stderr)[-150:], round(time.time() - t0, 1))\n'
              '    import data_slides, ooxml_check, ulta_excel\n',
          '    deck, book, bad = None, None, []                     # ULTA SlideGlam: chart decks only (no dashboard, no workbook)\n'
          '    import data_slides, ooxml_check\n')
    patch(st, '    for f in (w / "kinds.pptx", deck):\n', '    for f in [w / "kinds.pptx"] + ([deck] if deck else []):\n')
    patch(st, '            f"deck: {len(kinds)} chart kinds and the dashboard deck\'s charts with axis ids PowerPoint reads, a v139 deck "\n'
              '            f"refused and healed; workbook: "\n'
              '            f"every series stores its name, categories and values, {len(combo)} combo lines on their own axes"\n',
          '            f"deck: {len(kinds)} chart kinds with axis ids PowerPoint reads, a v139 deck refused and healed"\n')
    patch(st, '    with zipfile.ZipFile(book) as zb:\n        cp = ulta_excel.cache_problems(zb)\n',
          '    cp, combo = [], ["-", "-"]\n    if book:\n      with zipfile.ZipFile(book) as zb:\n        cp = ulta_excel.cache_problems(zb)\n')
    # safety rules for a skill that publishes nothing and makes PowerPoint only
    sr = out / "tools/safety_rules.py"
    patch(sr, '    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")\n    site = (TOOLS / "site.py").read_text(encoding="utf-8")\n',
          '    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")\n'
          '    if not (TOOLS / "site.py").exists():                # ULTA SlideGlam publishes nothing: no page may say it publishes by default\n'
          '        for name, t in [("SKILL.md", skill)] + [(f"guides/{g.name}", g.read_text(encoding="utf-8")) for g in sorted((ROOT / "guides").glob("*.md"))]:\n'
          '            for m in DEFAULT_PUBLISH.finditer(t):\n'
          '                bad.append(f"{name}:{t.count(chr(10), 0, m.start()) + 1}: {m.group(0)!r}")\n'
          '        return bad\n'
          '    site = (TOOLS / "site.py").read_text(encoding="utf-8")\n')
    patch(sr, 'CAPABILITIES = {"decks": ("deck", "powerpoint"), "infographics and one-pagers": ("infographic", "one-pager"),\n'
              '                "dashboards": ("dashboard",), "diagrams": ("diagram",), "whiteboards": ("whiteboard",),\n'
              '                "UI and app screens": ("screen",), "Word documents": ("word",),\n'
              '                "Excel workbooks": ("excel",), "ChatGPT Sites": ("chatgpt site",)}',
          'CAPABILITIES = {"decks": ("deck", "powerpoint"), "infographics and one-pagers": ("infographic", "one-pager"),   # ULTA SlideGlam\n'
          '                "diagrams": ("diagram",), "process flows": ("process flow", "swimlane"), "the process library": ("library",)}')

    # ---- identity: every file this skill makes names it (Producer, SkillVersion)
    patch(out / "tools/stamp.py", 'SKILL_VERSION = "v141"', f'SKILL_VERSION = "{VERSION}"')
    patch(out / "tools/stamp.py", 'PRODUCER = "Ulta Presentation Central"', f'PRODUCER = "{PRODUCER}"')

    # ---- this skill's own files (SKILL.md, guides, tools/playbook.py, new library pages, trimmed self-test ...)
    if OVERRIDES.exists():
        for src in sorted(OVERRIDES.rglob("*")):
            if src.is_file() and "__pycache__" not in src.parts:
                dst = out / src.relative_to(OVERRIDES)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)

    # ---- size: the approved templates slimmed (XML byte-identical; oversized pictures re-encoded), every pin moved
    sys.path.insert(0, str(DEV))
    import slim_templates
    slim_templates.main(out)

    # ---- the guides name this skill
    for g in sorted((out / "guides").glob("*.md")):
        s = g.read_text(encoding="utf-8")
        if "ULTA Presentation Central instructions" in s:
            g.write_text(s.replace("ULTA Presentation Central instructions", f"{PRODUCER} instructions"), encoding="utf-8")

    # ---- integrity: the SHA-256 of every file shipped (bootstrap checks it)
    files = {}
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name != "integrity.json" and "__pycache__" not in p.parts:
            files[p.relative_to(out).as_posix()] = sha(p)
    (out / "integrity.json").write_text(json.dumps({"algorithm": "sha256", "files": files}, indent=0) + "\n", encoding="utf-8")
    n = len(files); size = sum((out / k).stat().st_size for k in files)
    print(f"BUILT {out}  {n} files  {size / 1e6:.1f} MB unpacked")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--upc", required=True); ap.add_argument("--studio", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    build(Path(a.upc).resolve(), Path(a.studio).resolve(), Path(a.out).resolve())
