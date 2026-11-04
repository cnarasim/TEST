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
NAME, PRODUCER, VERSION = "ulta-slideglam", "ULTA SlideGlam", "v1.4"   # release name: "Clear Slides" (CHANGELOG.md)

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
LIB_REVIEW = ("# Update\n\n## Milestones\n- Design signed off: Mar 15, 2027\n- Pilot in 20 stores: May 1, 2027\n"
              "- Wave 1 live: Jul 15, 2027\n- All stores live: Oct 1, 2027\n\n## Risks\n- Data quality in the item master\n"
              "- Store staffing in peak: [owner]\n- Vendor readiness for ASNs\n")   # the expert review must see 3 things on this page
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


MATRIX_NEW = "    elif kind == 'matrix':   # (1q) a 2 x 2 read as a matrix: row and column labels in the author's own words, the first quadrant (the one to act on) strong, the rest a light tint\n        def descr_(it):\n            t_ = str(it.get('text', '') or '')\n            parts_ = [p_.strip() for p_ in t_.split(' - ', 1)[0].split(',') if p_.strip()] if ' - ' in t_ else []\n            return parts_ if len(parts_) == 2 else None\n        ds = [descr_(it) for it in items[:4]]\n        full = len(items) >= 4 and all(ds)\n        rows_l = (ds[0][0], ds[2][0]) if full and ds[0][0].lower() == ds[1][0].lower() and ds[2][0].lower() == ds[3][0].lower() else None\n        cols_l = (ds[0][1], ds[1][1]) if full and ds[0][1].lower() == ds[2][1].lower() and ds[1][1].lower() == ds[3][1].lower() else None\n        lab_w = Inches(1.6) if rows_l else 0; lab_h = Inches(0.5) if cols_l else 0\n        gx = Inches(0.9) + lab_w; gw = Inches(12.4) - gx; gap = Inches(0.16); gh = avail - lab_h\n        cw = (gw - gap) / 2; ch = (gh - gap) / 2\n        STRONG, TINT = 'D01381', 'FDE1D2'\n        for k, it in enumerate(items[:4]):\n            x = gx + (k % 2) * (cw + gap); y = top0 + (k // 2) * (ch + gap)\n            sh = seg(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, ch, STRONG if k == 0 else TINT); sh.name = f'ULTA graphic {k + 1}'\n            geom = sh._element.find('.//a:prstGeom', NS); av = geom.find('a:avLst', NS)\n            if av is None: av = etree.SubElement(geom, A + 'avLst')\n            for g in list(av): av.remove(g)\n            etree.SubElement(av, A + 'gd', name='adj', fmla='val 8000')\n            tf = sh.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE   # the text is IN the quadrant\n            tf.margin_left = tf.margin_right = Inches(0.35); tf.margin_top = tf.margin_bottom = Inches(0.2)\n            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT; r = p.add_run(); r.text = str(it.get('title', '')).strip(); r.font.size = Pt(22); r.font.bold = True; r.font.name = FONT_HEAD\n            r.font.color.rgb = RGBColor.from_string('FFFFFF' if k == 0 else STRONG)\n            body = str(it.get('text', '') or '').strip()\n            if (rows_l or cols_l) and ' - ' in body: body = body.split(' - ', 1)[1].strip()   # the axes say the rest\n            if body:\n                p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.LEFT; p2.space_before = Pt(6); r2 = p2.add_run(); r2.text = body[:1].upper() + body[1:]; r2.font.size = Pt(16); r2.font.name = FONT_BODY\n                r2.font.color.rgb = RGBColor.from_string('FFFFFF' if k == 0 else '000000')\n        def axis_label(x, y, w, h, text, align, name):\n            tb = slide.shapes.add_textbox(int(x), int(y), int(w), int(h)); tb.name = name\n            tf_ = tb.text_frame; tf_.word_wrap = True; tf_.vertical_anchor = MSO_ANCHOR.MIDDLE\n            tf_.margin_left = tf_.margin_right = Inches(0.05)\n            p_ = tf_.paragraphs[0]; p_.alignment = align; r_ = p_.add_run(); r_.text = text[:1].upper() + text[1:]\n            r_.font.size = Pt(16); r_.font.bold = True; r_.font.name = FONT_BODY; r_.font.color.rgb = RGBColor.from_string('404040')\n        def axis_line(x1, y1, x2, y2, name):\n            from pptx.enum.shapes import MSO_CONNECTOR as MC_\n            ln = slide.shapes.add_connector(MC_.STRAIGHT, int(x1), int(y1), int(x2), int(y2)); ln.name = name\n            ln.line.color.rgb = RGBColor.from_string('D9D9D9'); ln.line.width = Pt(1.5)\n        if rows_l:\n            for j, lab in enumerate(rows_l):\n                axis_label(Inches(0.9), top0 + j * (ch + gap), lab_w - Inches(0.3), ch, lab, PP_ALIGN.RIGHT, f'ULTA graphic row label {j + 1}')\n            axis_line(gx - Inches(0.14), top0, gx - Inches(0.14), top0 + gh, 'ULTA graphic axis rows')\n        if cols_l:\n            for j, lab in enumerate(cols_l):\n                axis_label(gx + j * (cw + gap), top0 + gh + Inches(0.14), cw, lab_h - Inches(0.1), lab, PP_ALIGN.CENTER, f'ULTA graphic column label {j + 1}')\n            axis_line(gx, top0 + gh + Inches(0.08), gx + gw, top0 + gh + Inches(0.08), 'ULTA graphic axis columns')\n"


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
    # (1q) the 2 x 2 matrix reads as a matrix, not four equal blocks: the row and column labels come from the author's own
    #      words ("- Do now: high value, ready - pilot this quarter": rows high value / lower value, columns ready / not
    #      ready), the first quadrant (the one to act on) in the strong colour and the others in the light tint, larger type
    src_ = bfs.read_text(encoding="utf-8")
    a_, b_ = src_.index("    elif kind == 'matrix':"), src_.index("    elif kind == 'hub':")
    patch(bfs, src_[a_:b_], MATRIX_NEW)
    # (2c) the package check also catches a connector glued to a shape that is not on the slide (a slide edited by hand or
    #      by another tool after the build; PowerPoint drops the glue or offers a repair) - one more check, none removed
    patch(out / "tools/ooxml_check.py",
          '                if dup:\n                    out.append((n, 0, f"shape id {\', \'.join(dup[:3])} used twice on the slide"))\n',
          '                if dup:\n                    out.append((n, 0, f"shape id {\', \'.join(dup[:3])} used twice on the slide"))\n'
          '                glued = [c.get("id") for c in y.iter(f"{{{A}}}stCxn", f"{{{A}}}endCxn") if c.get("id") not in ids]\n'
          '                if glued:                        # (2c)\n'
          '                    out.append((n, 0, f"a connector is glued to shape {glued[0]}, which is not on the slide"))\n')
    # (1r) a template timeline (Gantt, roadmap, milestones, call-outs) only when its filler takes the data: tried first on a
    #      scratch copy of the template slide; refused (a roadmap holds 7 months or quarters, a Gantt 3 workstreams ...),
    #      the section is drawn as the 'lanes' timeline (any span) - the Studio kept the template slide with its sample
    #      shapes emptied, a roadmap of blank bars
    patch(eng / "central_slides.py", "    c = {'family': fam, 'style': style, 'data': data, 'headline': head}\n",
          "    if fam == 'timeline' and (fam, style) in TI.TEMPLATE_STYLES and not _template_takes(TI, style, data, head):   # (1r)\n"
          "        notes = (notes + ' - ' if notes else '') + f'drawn as lanes: the plan does not fit the {style.replace(\"-\", \" \")} slide'\n"
          "        style = 'lanes'\n"
          "    c = {'family': fam, 'style': style, 'data': data, 'headline': head}\n")
    patch(eng / "central_slides.py", "\ndef to_spec_slide(cs, roles=None):",
          "\ndef _template_takes(TI, style, data, head):\n"
          "    \"\"\"(1r) True when the template timeline's filler takes the data (tried on a scratch copy of its template slide).\"\"\"\n"
          "    try:\n"
          "        import brand as _B\n"
          "        from pptx import Presentation\n"
          "        sl = Presentation(str(_B.current().template)).slides[TI.TEMPLATE_STYLES[('timeline', style)] - 1]\n"
          "        probs = TI.fill(sl, 'timeline', style, {'timeline': data, 'style': style, 'headline': head}) or []\n"
          "    except Exception:                                  # noqa: BLE001  unknown: the filler decides at build time\n"
          "        return True\n"
          "    return not probs                                  # any problem (over capacity, a label too long): not taken\n"
          "\n\ndef to_spec_slide(cs, roles=None):")
    # (1s) a takeaway computed from the data goes after the author's heading or not at all (never in its place), and it
    #      states a fact from the data (the last milestone and its date, the largest share, the leader), never a count:
    #      "3 teams, 3 tasks, milestone Dec 31" replaced "Transition in three stages", and "What comes next: 2 teams,
    #      3 tasks" or "Order to cash: 8 steps, 4 teams" tell the audience nothing the slide does not show
    patch(eng / "family_rules.py",
          "    return out if len(out) <= 42 else (say[:1].upper() + say[1:] if len(say) <= 42 else None)   # (1o) one line at 36 pt",
          "    return out if len(out) <= 42 else None   # (1o) one line at 36 pt; (1s) never the count in place of the heading")
    patch(eng / "family_rules.py",
          "            parts = ([f'{len(groups)} teams'] if len(groups) > 1 else []) + ([f'{len(tasks)} tasks'] if tasks else [])",
          "            parts = []   # (1s) the last milestone and its date; never a count of teams or tasks")
    patch(eng / "family_rules.py",
          "            say = f'{len(st)} steps, {len(data.get(\"lanes\") or [])} teams' + (f', {dec} decision' + ('s' if dec > 1 else '') if dec else '')",
          "            say = None   # (1s) a count of steps and teams is not a takeaway")
    # (2d) a template infographic keeps its labels: three or more of its template slide's text shapes left with no text
    #      fail the content gate (a filler that refused the data leaves the template's shapes empty)
    patch(vd, '        ref = shape_facts(etree.fromstring(rz.read(rparts[src - 1]))) if src else {}\n',
          '        ref = shape_facts(etree.fromstring(rz.read(rparts[src - 1]))) if src else {}\n'
          '        if i in INFO and src:                          # (2d) the template infographic kept its labels\n'
          '            had = {nv_.get("name") for sp_ in etree.fromstring(rz.read(rparts[src - 1])).iter("{%s}sp" % NS["p"])\n'
          '                   for nv_ in [sp_.find(".//p:cNvPr", NS)] if nv_ is not None and text_of(sp_).strip()}\n'
          '            empty = [nv_.get("name") for sp_ in x.iter("{%s}sp" % NS["p"]) for nv_ in [sp_.find(".//p:cNvPr", NS)]\n'
          '                     if nv_ is not None and nv_.get("name") in had and sp_.find(".//p:txBody", NS) is not None\n'
          '                     and not text_of(sp_).strip()]\n'
          '            if len(empty) >= 3:\n'
          '                fails.append(f"slide {i}: the template infographic kept {len(empty)} of its shapes with no text "\n'
          '                             f"(\'{empty[0]}\' ...) - the data did not fit this layout: give each item the detail its box shows "\n'
          '                             f"(a funnel: \'Stage: detail\'), or use a drawn style (a timeline: lanes)")\n')
    # (1t) a section that is only asks (Decision / Ask / Next step, 3 or 4 lines) becomes the template's three cards (or the
    #      label table for 4), each ask a card titled by its label: the Studio set them as three bullets in one wide box, a
    #      mostly empty slide that closed 56 library decks
    patch(eng / "page_to_spec.py",
          "            # a section that is only asks (two strips would overwrite each other in one box): all of them as the body, in order; they also reach the asks slide\n",
          "            # a section that is only asks (two strips would overwrite each other in one box): all of them as the body, in order; they also reach the asks slide\n"
          "            pairs_ = [(lab, body) for lab, body in callouts] + [split_label(l.replace(H, '', 1) if l.startswith(H) else l) for l in rest]\n"
          "            if infographics and len(pairs_) in (3, 4) and all(lab and body for lab, body in pairs_):   # (1t) the asks as cards\n"
          "                cards_ = [(lab[:1].upper() + lab[1:], [body]) for lab, body in pairs_]\n"
          "                if infographic(cards_, head, note, 'cards' if len(cards_) == 3 else 'table', takeaway):\n"
          "                    if overflow and appendix and appendix[-1][0] == headline: appendix.pop()\n"
          "                    return\n")
    # (1u) the template funnel shows each stage's detail in the box beside it: a stage written without one (no "Stage:
    #      detail") is reported, as a name over 3 words already is - the Studio left the four boxes white
    patch(out / "tools/template_infographics.py",
          '        if _words(det) > 14:\n            P_.append(f"funnel detail',
          '        if not det.strip():                                             # (1u)\n'
          '            P_.append(f"funnel stage \'{lead[:24]}\' has no detail for the box beside it - write \'Stage: detail\'")\n'
          '        if _words(det) > 14:\n            P_.append(f"funnel detail')
    #      ... and the same asks written as bullets ("- Decision: ...", a named list the engine keeps as a list): the list
    #      router dropped every Decision / Ask / Next step line, found no list and left one wide box of three bullets
    patch(eng / "page_to_spec.py",
          "        lines = [l for l in raw if l.strip() and split_label(l)[0] not in TAKEAWAY_LABELS + CALLOUT_LABELS]\n",
          "        lines = [l for l in raw if l.strip() and split_label(l)[0] not in TAKEAWAY_LABELS\n"
          "                 and (split_label(l)[0] not in CALLOUT_LABELS or l.startswith('\u2022 '))]   # (1t) a bulleted ask is a list item\n")
    # (1v) every hand-off keeps its number: when no stretch of its line is free (short flows between close steps), the
    #      number sits on the receiving step's top corner (left, else right), then the sending step's - the panel lists
    #      every hand-off, so a number missing from the drawing left the reader unable to match one (66 library slides)
    sw = out / "tools/swimlanes.py"
    patch(sw, "\ndef _p_handoffs(plan, m, box):",
          "\ndef _corner_spot(rb, ra, d, avoid, taken):\n"
          "    \"\"\"(1v) A number badge centred on a step's top corner: the receiving step's left, then right, then the sending\n"
          "    step's; None when every corner touches another step or badge.\"\"\"\n"
          "    pad = int(0.03 * IN)\n"
          "    for own in (rb, ra):\n"
          "        if not own:\n"
          "            continue\n"
          "        for cx in (own[0], own[2]):\n"
          "            r = (cx - d // 2, own[1] - d // 2, cx + d // 2, own[1] + d // 2)\n"
          "            if any(q_ != own and r[0] < q_[2] + pad and r[2] > q_[0] - pad and r[1] < q_[3] + pad and r[3] > q_[1] - pad\n"
          "                   for q_ in list(avoid) + list(taken)):\n"
          "                continue\n"
          "            return r\n"
          "    return None\n"
          "\n\ndef _p_handoffs(plan, m, box):")
    patch(sw, "        r = _badge_spot(pts, bd, avoid, taken)\n        if r is None:\n"
              "            plan.problems.append(f\"no room for hand-off number {n}",
          "        r = _badge_spot(pts, bd, avoid, taken)\n"
          "        if r is None:                                   # (1v) on a step's corner\n"
          "            r = _corner_spot(rects.get(b), rects.get(a), bd, avoid, taken)\n"
          "        if r is None:\n"
          "            plan.problems.append(f\"no room for hand-off number {n}")
    # (1w) a dated line's closing parenthesis names its team only when it is a name (1-3 words, the timeline's workstream
    #      limit); a longer one is the item's detail: "(two features moved to phase 2)" became a lane of that name, and on
    #      a story line a short detail vanished as an unused team while a long one stayed in brackets
    patch(eng / "family_rules.py",
          "        g = re.search(r'\\(([^()]{2,30})\\)\\s*$', rest) or re.search(r'\\[([^\\[\\]]{2,30})\\]', rest)\n"
          "        if g:\n"
          "            word = g.group(1).strip()\n"
          "            if word.lower() in STATUS: it['status'] = STATUS[word.lower()]\n",
          "        g = re.search(r'\\(([^()]{2,90})\\)\\s*$', rest) or re.search(r'\\[([^\\[\\]]{2,30})\\]', rest)   # (1w)\n"
          "        if g:\n"
          "            word = g.group(1).strip()\n"
          "            if word.lower() in STATUS: it['status'] = STATUS[word.lower()]\n"
          "            elif len(word.split()) > 3 or len(word) > 30: it['text'] = word   # (1w) a sentence: the detail, not a team\n")
    # (1y) a page's SIPOC: "Layout: swimlane sipoc" over "Suppliers: ...", "Inputs: ...", "Process: step, step, step",
    #      "Outputs: ...", "Customers: ..." lines fills the five columns (the page reader made lanes of the five labels
    #      and the drawing showed four empty columns); and a big number may carry months or years ("14 months")
    patch(eng / "family_rules.py",
          "        data = timeline(lines, groups) if fam == 'timeline' else swimlane(lines, explicit=True)\n",
          "        data = timeline(lines, groups) if fam == 'timeline' else (sipoc(lines) if style == 'sipoc' else swimlane(lines, explicit=True))   # (1y)\n")
    patch(eng / "family_rules.py", "\n# ---------------------------------------------------------------- template infographics\n",
          "\nSIPOC_KEYS = {'supplier': 'suppliers', 'suppliers': 'suppliers', 'input': 'inputs', 'inputs': 'inputs', 'process': 'process',\n"
          "              'steps': 'process', 'output': 'outputs', 'outputs': 'outputs', 'customer': 'customers', 'customers': 'customers'}\n"
          "\n\ndef sipoc(lines):\n"
          "    \"\"\"(1y) \\\"Suppliers: a, b\\\" ... \\\"Process: step, step, step\\\" ... \\\"Customers: ...\\\" -> {'lanes', 'steps', 'sipoc'}; None\n"
          "    unless the process has 3-7 steps and the suppliers and customers are named.\"\"\"\n"
          "    got = {}\n"
          "    for raw in lines:\n"
          "        lab, body = split_label(plain(raw))\n"
          "        k = SIPOC_KEYS.get(str(lab or '').strip().lower())\n"
          "        if k and body:\n"
          "            got[k] = [x.strip(' .')[:1].upper() + x.strip(' .')[1:] for x in re.split(r',\\s*|\\s+and\\s+', body) if x.strip(' .')]\n"
          "    proc = got.pop('process', [])\n"
          "    if not 3 <= len(proc) <= 7 or not got.get('suppliers') or not got.get('customers'): return None\n"
          "    steps = [{'id': f's{k + 1}', 'lane': 'Process', 'text': _short(t, 5)} for k, t in enumerate(proc)]\n"
          "    steps[0]['kind'] = 'start'; steps[-1]['kind'] = 'end'\n"
          "    return {'lanes': ['Process'], 'steps': steps, 'sipoc': got}\n"
          "\n# ---------------------------------------------------------------- template infographics\n")
    patch(out / "tools/template_infographics.py",
          r'BIG = re.compile(r"^[~<>≈]?[-+]?[$€£]?\d[\d,.]*\s?(%|x|k|m|bn|b|pts?|min|h|hrs|days?|wks?|weeks?|M|K|B)?$',
          r'BIG = re.compile(r"^[~<>≈]?[-+]?[$€£]?\d[\d,.]*\s?(%|x|k|m|bn|b|pts?|min|h|hrs|days?|wks?|weeks?|months?|mos?|years?|yrs?|M|K|B)?$')
    # (1z) the milestones slide finds its event circles and year labels by shape, not by their sample text: the page
    #      engine clears a template timeline's sample text before the filler runs, so the filler found no circle ("9
    #      events at most") and left the slide's 11 shapes empty - every library milestone slide failed the gate
    patch(out / "tools/template_infographics.py",
          '    circles = [s for s in shapes if s.width > 0.8 * IN and s.has_text_frame and s.text_frame.text.strip() == "Event"]\n'
          '    years = sorted((s for s in shapes if s.has_text_frame and s.text_frame.text.strip() == "YEAR"), key=lambda s: s.left)\n',
          '    circles = [s for s in shapes if 0.8 * IN < s.width < 1.3 * IN and abs(s.width - s.height) < 0.05 * IN   # (1z) by shape\n'
          '               and s.has_text_frame and s.text_frame.text.strip() in ("Event", "")]\n'
          '    years = sorted((s for s in shapes if s.has_text_frame and s.text_frame.text.strip() in ("YEAR", "")\n'
          '                    and 0.8 * IN < s.width < 1.0 * IN and s.height < 0.35 * IN), key=lambda s: s.left)\n')
    # (1aa) a KPI card keeps the words around its number: "5 against a target of 0", "9 days per claim", "4.6 of 5
    #      (from 4.2)" lost everything but the number and a signed change; the rest is now the card's caption (shown
    #      beside the change, or under the number when there is none), and a card without a trend line is sized to its
    #      content (2.6 in, not 3.6 in of mostly empty card)
    patch(eng / "family_rules.py",
          "            v = (NUM.search(body) or [body])[0]; d = re.search(r'\\(([-+▲▼][^()]+)\\)', body)\n"
          "            its.append({'label': lab, 'value': v.strip(), **({'delta': d.group(1)} if d else {})})\n",
          "            m_ = NUM.search(body); v = m_.group(0) if m_ else body; d = re.search(r'\\(([-+▲▼][^()]+)\\)', body)\n"
          "            before = body[:m_.start()].strip(' ,:') if m_ else ''   # (1aa) the words around the number\n"
          "            after = (body[m_.end():] if m_ else '').replace(d.group(0), ' ') if d else (body[m_.end():] if m_ else '')\n"
          "            after = re.sub(r'\\s+', ' ', re.sub(r'[()]', ' ', after)).strip(' ,;:')\n"
          "            if before and len(before + ' ' + v.strip()) <= 9: v = before + ' ' + v.strip(); before = ''\n"
          "            vs = ', '.join(x for x in ((before + ' ' + v.strip()) if before else '', after) if x)\n"
          "            its.append({'label': lab, 'value': v.strip(), **({'delta': d.group(1)} if d else {}), **({'vs': vs} if vs else {})})\n")
    mc = out / "tools/modern_charts.py"
    patch(mc, "    gap = int(0.25 * IN); cw = (w - gap * (n - 1)) / n; ch = min(h, int(3.6 * IN)); y0 = y + (h - ch) / 2\n",
          "    gap = int(0.25 * IN); cw = (w - gap * (n - 1)) / n\n"
          "    ch = min(h, int((3.6 if any(len(it.get('trend') or []) >= 2 for it in items[:n]) else 2.6) * IN))   # (1aa)\n"
          "    y0 = y + (h - ch) / 2\n")
    patch(mc, "        if it.get(\"vs\"):\n            text(sl, x + pad + bw + 0.1 * IN, by, w - 2 * pad - bw, bh, it[\"vs\"], 10, MUTED, BODY, \"l\", \"m\")\n",
          "        if it.get(\"vs\"):\n            text(sl, x + pad + bw + 0.1 * IN, by, w - 2 * pad - bw, bh, it[\"vs\"], 10, MUTED, BODY, \"l\", \"m\")\n"
          "    elif it.get(\"vs\"):                                  # (1aa) the words around the number, under it\n"
          "        text(sl, x + pad, by, w - 2 * pad, 0.6 * IN, it[\"vs\"], 12, MUTED, BODY, \"l\", \"t\")\n")
    # (1ab) a one-lane process (a page's SIPOC) does not print its lane name under every step ("Route / Process")
    patch(out / "tools/swimlanes.py",
          "        if two:                                         # owner team as a second, smaller line\n",
          "        if two and len(m[\"lanes\"]) > 1:                # owner team as a second, smaller line; (1ab) one lane: none\n")
    # (1ac) an input or output of the "process io" picture keeps up to 6 words: it was cut at 4 mid-phrase ("Cost per user
    #      per" for "Cost per user per year"); the drawing's own fit check reports one that does not fit its box
    patch(eng / "family_rules.py",
          "        if d['title'].strip().lower() in ('input', 'inputs'): ins.append({'title': _short(d['text'], 4), 'text': ''}); continue\n"
          "        if d['title'].strip().lower() in ('output', 'outputs'): outs.append({'title': _short(d['text'], 4), 'text': ''}); continue\n",
          "        if d['title'].strip().lower() in ('input', 'inputs'): ins.append({'title': _short(d['text'], 6), 'text': ''}); continue   # (1ac)\n"
          "        if d['title'].strip().lower() in ('output', 'outputs'): outs.append({'title': _short(d['text'], 6), 'text': ''}); continue\n")
    # (1ad) three labelled lines with a repeated label ("Ask", "Ask", "Next step") are two boxes, one per label, its lines
    #      under its heading: as three cards the title row repeated a word, which the gate refuses (numbering does not
    #      help: the duplicate check ignores figures); the closing-asks cards (1t) need three different labels
    patch(eng / "page_to_spec.py",
          "        if all(labs):\n            if len(labs) == 3 and 'cards3' in R and all(len(b) <= 220 for _, b in labs):\n",
          "        if all(labs) and len(labs) == 3 and len({t.lower() for t, _ in labs}) == 2 and 'two_col' in R:   # (1ad) two boxes\n"
          "            grp_ = {}\n"
          "            for t_, b_ in labs: grp_.setdefault(t_, []).append(b_)\n"
          "            (t1_, b1_), (t2_, b2_) = list(grp_.items())\n"
          "            bl_ = lambda bs: ['• ' + x for x in bs] if len(bs) > 1 else bs\n"
          "            return put({'source': R['two_col'], 'fills': {'title': head, 'text1': ['## ' + t1_] + bl_(b1_), 'text2': ['## ' + t2_] + bl_(b2_)}, 'notes': note2})\n"
          "        if all(labs):\n            if len(labs) == 3 and 'cards3' in R and all(len(b) <= 220 for _, b in labs):\n")
    patch(eng / "page_to_spec.py",
          "            if infographics and len(pairs_) in (3, 4) and all(lab and body for lab, body in pairs_):   # (1t) the asks as cards\n",
          "            if infographics and len(pairs_) in (3, 4) and all(lab and body for lab, body in pairs_) \\\n"
          "                    and len({lab.lower() for lab, _ in pairs_}) == len(pairs_):   # (1t) the asks as cards; (1ad) labels differ\n")
    patch(eng / "page_to_spec.py",
          "            cs, _ = synth_cards([(None, items)], 'cards')\n"
          "            return put({'source': R['cards3'], 'fills': {'title': head, 'table': card_rows([t for t, _ in cs], [ls for _, ls in cs])},",
          "            cs, _ = synth_cards([(None, items)], 'cards')\n"
          "            if len({str(t).lower() for t, _ in cs}) == 2 and 'two_col' in R:   # (1ad) a repeated label: two boxes\n"
          "                grp_ = {}\n"
          "                for t_, ls_ in cs: grp_.setdefault(t_, []).extend(ls_)\n"
          "                (t1_, b1_), (t2_, b2_) = list(grp_.items())\n"
          "                bl_ = lambda bs: ['• ' + x for x in bs] if len(bs) > 1 else bs\n"
          "                return put({'source': R['two_col'], 'fills': {'title': head, 'text1': ['## ' + t1_] + bl_(b1_), 'text2': ['## ' + t2_] + bl_(b2_)}, 'notes': note2})\n"
          "            return put({'source': R['cards3'], 'fills': {'title': head, 'table': card_rows([t for t, _ in cs], [ls for _, ls in cs])},")
    # (1ae) variety: two slides in a row never look the same when the content can be told another way, with nothing lost.
    #      A table straight after a label table is drawn as hexagons (or a hub, alternating), each row a shape with its
    #      first cell as the name and the other cells as its line, later columns under their header ("Control: Legal
    #      review"); three cards straight after three cards become a hub. "Layout: table" or "Layout: cards" keeps the
    #      author's form. The Studio drew every Markdown table as the same label table, so a deck written by another
    #      assistant read as one table after another.
    patch(eng / "page_to_spec.py",
          "            t_hint = hints.get(headline.strip()) or hints.get(section.strip())\n",
          "            t_hint = hints.get(headline.strip()) or hints.get(section.strip())\n"
          "            prev_ = next((s_ for s_ in reversed(slides) if s_.get('kind') != 'divider'), None)   # (1ae) variety\n"
          "            if not t_hint and infographics and 2 <= ncol <= 4 and 3 <= len(data) <= 6 and prev_ is not None \\\n"
          "                    and prev_.get('source') in (R.get('actions'), R.get('grid6')) and 'two_col' in R and all(len(' '.join(r)) <= 150 for r in data):\n"
          "                t_hint = 'fam:process list'\n"
          "                warnings.append(f'variety: the table \"{head_title}\" follows a label table - drawn as icon rows (\"Layout: table\" keeps a table)')\n")
    patch(eng / "page_to_spec.py",
          "[' · '.join(f'{header[j]}: {c}' if j < len(header) and header[j] and len(data) <= 4 else c for j, c in enumerate(r[1:], 1) if c and c.strip())]",
          "[' · '.join(f'{header[j]}: {c}' if 2 <= j < len(header) and header[j] else c for j, c in enumerate(r[1:], 1) if c and c.strip())]")
    patch(eng / "page_to_spec.py",
          "        if 'cards3' in R and len(titled) == 3 and (hint == 'cards' or",
          "        prev_c = next((s_ for s_ in reversed(slides) if s_.get('kind') != 'divider'), None)   # (1ae) cards after cards: a hub\n"
          "        if hint != 'cards' and 'cards3' in R and 'two_col' in R and len(titled) == 3 and prev_c is not None \\\n"
          "                and prev_c.get('source') == R['cards3'] and family_slide('fam:process list', ['\\u2022 ' + h_ + ': ' + re.sub(r'^[\\u2022\\u2013]\\s*', '', ls_[0]) + (' (' + '; '.join(re.sub(r'^[\\u2022\\u2013]\\s*', '', l_) for l_ in ls_[1:]) + ')' if len(ls_) > 1 else '') for h_, ls_ in titled if ls_], None, head, head, note, takeaway, []):\n"
          "            warnings.append(f'variety: \"{head}\" follows three cards - drawn as icon rows (\"Layout: cards\" keeps the cards)')\n"
          "            return True\n"
          "        if 'cards3' in R and len(titled) == 3 and (hint == 'cards' or")
    patch(eng / "page_to_spec.py",
          "                if t_hint == 'text' or not infographic(row_cards, head_title, note_t, t_hint):\n",
          "                if t_hint == 'hub' and header and header[0].strip() and len(header[0].strip()) <= 22 and infographic(row_cards, head_title, note_t, t_hint):\n"
          "                    slides[-1]['graphic']['hub'] = header[0].strip()   # (1ae) the hub's centre names its rows\n"
          "                    continue\n"
          "                if t_hint == 'text' or not infographic(row_cards, head_title, note_t, t_hint):\n")
    # (1af) a step named "Source", "Result", "Outcome", "Centre", "Input" or "Output" stays a step unless the style uses that
    #      role (diverge: source, converge: result, cycle: centre, io: inputs and outputs): a seven-step snake lost its
    #      "Source" step to the diverge style's source box, which the snake never draws
    patch(eng / "family_rules.py",
          "        k = ROLE_KEYS.get(d['title'].strip().lower())\n        if k and d.get('text'):\n",
          "        k = ROLE_KEYS.get(d['title'].strip().lower())\n"
          "        if k and style not in (None, '', 'auto') and style != {'result': 'converge', 'source': 'diverge', 'center': 'cycle'}.get(k):\n"
          "            k = None                                   # (1af) a step of this style, not a role it never draws\n"
          "        io_ = style in (None, '', 'auto', 'io')\n"
          "        if k and d.get('text'):\n")
    patch(eng / "family_rules.py",
          "        if d['title'].strip().lower() in ('input', 'inputs'): ins.append(",
          "        if io_ and d['title'].strip().lower() in ('input', 'inputs'): ins.append(")
    patch(eng / "family_rules.py",
          "        if d['title'].strip().lower() in ('output', 'outputs'): outs.append(",
          "        if io_ and d['title'].strip().lower() in ('output', 'outputs'): outs.append(")
    # (1ag) the drawn hub, hexagons and cycle in the brand's calm infographic look: one accent, light fills, dark words.
    #      The Studio cycled the four saturated step colours over every shape (white words on magenta, pink, red and
    #      orange), put a black disc in the hub's centre and coloured each legend name differently - loud next to the
    #      template's own slides. Now: hexagons in the light peach tint with dark names; hub and cycle nodes white with an
    #      accent ring and an accent number; the hub's centre the one strong accent; legend names dark, one size larger
    bfs_ = eng / "build_from_storyboard.py"
    patch(bfs_, "            sh = seg(MSO_SHAPE.OVAL, px - d / 2, py - d / 2, d, d, FLOW_COLORS[k % 4]); label(sh, str(k + 1), 15); sh.name = f'ULTA graphic {k + 1}'\n"
                "        hub = seg(MSO_SHAPE.OVAL, cx - hr, cy - hr, 2 * hr, 2 * hr, '000000'); label(hub, str(graphic.get('hub') or '')[:40], 12); hub.name = 'ULTA graphic hub'\n",
                "            sh = seg(MSO_SHAPE.OVAL, px - d / 2, py - d / 2, d, d, 'FFFFFF'); sh.line.color.rgb = RGBColor.from_string(FLOW_COLORS[0]); sh.line.width = Pt(2.25)   # (1ag)\n"
                "            label(sh, str(k + 1), 15, color=FLOW_COLORS[0]); sh.name = f'ULTA graphic {k + 1}'\n"
                "        hub = seg(MSO_SHAPE.OVAL, cx - hr, cy - hr, 2 * hr, 2 * hr, FLOW_COLORS[0]); label(hub, str(graphic.get('hub') or '')[:40], 13); hub.name = 'ULTA graphic hub'\n")
    patch(bfs_, "                sh = seg(MSO_SHAPE.HEXAGON, x0 + j * hw * 0.92, y0 + ri * (hh * 0.88), hw, hh, FLOW_COLORS[k % 4]); sh.name = f'ULTA graphic {k + 1}'\n"
                "                label(sh, str(it.get('title', '')) if names_fit else str(k + 1), hex_pt if names_fit else 18); k += 1\n",
                "                sh = seg(MSO_SHAPE.HEXAGON, x0 + j * hw * 0.92, y0 + ri * (hh * 0.88), hw, hh, 'FDE1D2'); sh.name = f'ULTA graphic {k + 1}'   # (1ag)\n"
                "                sh.line.color.rgb = RGBColor.from_string('FFFFFF'); sh.line.width = Pt(2)\n"
                "                label(sh, str(it.get('title', '')) if names_fit else str(k + 1), hex_pt if names_fit else 18, color='000000' if names_fit else FLOW_COLORS[0]); k += 1\n")
    patch(bfs_, "            sh = seg(MSO_SHAPE.OVAL, x, y, d, d, FLOW_COLORS[k % 4]); label(sh, str(k + 1), 16); sh.name = f'ULTA graphic {k + 1}'\n",
                "            sh = seg(MSO_SHAPE.OVAL, x, y, d, d, 'FFFFFF'); sh.line.color.rgb = RGBColor.from_string(FLOW_COLORS[0]); sh.line.width = Pt(2.25)   # (1ag)\n"
                "            label(sh, str(k + 1), 16, color=FLOW_COLORS[0]); sh.name = f'ULTA graphic {k + 1}'\n")
    patch(bfs_, "            cells.append([[[((f'{k_ + 1}. ' if num else '') + t_, True, FLOW_COLORS[k_ % 4], size)]], [[(body, False, '404040', size - 1)]]])\n",
                "            cells.append([[[((f'{k_ + 1}. ' if num else '') + t_, True, '000000', size)]], [[(body, False, '404040', size - 1)]]])   # (1ag) one ink\n")
    for old_, new_ in (("        legend(lx, y0, lw, [lh] * n, items, 12 if n <= 4 else 11, num=True)\n    elif kind == 'roadmap':",
                        "        legend(lx, y0, lw, [lh] * n, items, 13 if n <= 4 else 12, num=True)\n    elif kind == 'roadmap':"),
                       ("        legend(lx, ly0, lw, [lh] * n, items, 12 if n <= 4 else 11, num=not names_fit)\n",
                        "        legend(lx, ly0, lw, [lh] * n, items, 13 if n <= 4 else 12, num=not names_fit)\n")):
        patch(bfs_, old_, new_)
    # (1ah) a takeaway line under a one-line headline sits in the headline box's lower half only when there is content
    #      below to make room for; on a drawn slide (nothing below yet) it goes under the box - the two-column slide's
    #      headline is not top-anchored, so "How we rank" sat on "Must-haves first"
    patch(bfs_, "    if headline_lines(ttxt, title.width or 0, tsize, glyph=0.64) <= 1:\n        y = title.top + Inches(0.56)",
                "    if headline_lines(ttxt, title.width or 0, tsize, glyph=0.64) <= 1 and body:   # (1ah)\n        y = title.top + Inches(0.56)")
    # (1ai) icon rows for a set that is not a sequence: "Layout: process list" draws the vertical style's white rows (an
    #      icon, the name, its line, a caption) without numbers or the connecting spine, every row in the one accent.
    #      The variety rule (1ae) and the expert review use it: hexagons and a hub keep the meaning in a legend away from
    #      the shapes. A table under any "Layout: process ..." line becomes the steps, a row each (first cell the name,
    #      the second its line, the third its caption under its header).
    patch(eng / "family_rules.py",
          "    st = rest.strip().replace(' ', '-')\n    its = retail_items(lines)\n",
          "    st = rest.strip().replace(' ', '-')\n"
          "    unordered = word == 'process' and st in ('list', 'rows', 'icon-rows')   # (1ai) icon rows: a set, not steps\n"
          "    if unordered: st = 'vertical'\n"
          "    its = retail_items(lines)\n")
    patch(eng / "family_rules.py",
          "        P = process_data(st, its)\n        if not P['steps'] or (len(P['steps']) < 2 and st != 'io'): return None",
          "        P = process_data(st, its)\n        if unordered: P['unordered'] = True\n"
          "        if not P['steps'] or (len(P['steps']) < 2 and st != 'io'): return None")
    fl_ = out / "tools/flows.py"
    patch(fl_, '    C.line(sx, by + h / 2, sx, by + bh - h / 2, colour=ND.ROSE_TINT, width=4.0, name="process spine")\n',
          '    unordered = bool(D.get("unordered"))                 # (1ai) a set, not steps: no spine, no numbers, one accent\n'
          '    if not unordered:\n'
          '        C.line(sx, by + h / 2, sx, by + bh - h / 2, colour=ND.ROSE_TINT, width=4.0, name="process spine")\n')
    patch(fl_, '        _badge(C, sx, y + h / 2, d, i, i + 1, name=f"Step {i + 1} number", icon=s["icon"])\n'
               '        C.rect(x, y, bx + bw - x, h, ND.WHITE, r=0.08, name=f"Step {i + 1} card")\n'
               '        C.rect(x, y, _in(0.08), h, _colour(i), r=None, name=f"Step {i + 1} colour")\n',
          '        if not unordered:\n'
          '            _badge(C, sx, y + h / 2, d, i, i + 1, name=f"Step {i + 1} number", icon=s["icon"])\n'
          '        elif s["icon"]:\n'
          '            C.dot(sx, y + h / 2, d, _colour(0), name=f"Item {i + 1} icon")\n'
          '            PG.icon(C, s["icon"], sx, y + h / 2, d * 0.56, colour=ND.WHITE, bg=_colour(0))\n'
          '        C.rect(x, y, bx + bw - x, h, ND.WHITE, r=0.08, name=f"Step {i + 1} card")\n'
          '        C.rect(x, y, _in(0.08), h, _colour(0) if unordered else _colour(i), r=None, name=f"Step {i + 1} colour")\n')
    # a table under a process Layout line: its rows are the steps
    patch(eng / "page_to_spec.py",
          "            if t_hint in ('cards', 'steps', 'bands', 'text') + GRAPHIC_KINDS and 3 <= len(data) <= 8 and ncol >= 2:\n",
          "            if str(t_hint or '').startswith('fam:process') and 3 <= len(data) <= 8 and ncol >= 2:   # (1ai) rows as steps\n"
          "                def cap_(r):   # the later columns under their headers, one caption (one column when two run long)\n"
          "                    xs = [(f'{header[j].strip()}: ' if j < len(header) and header[j].strip() else '') + r[j].strip() for j in range(2, len(r)) if r[j].strip()]\n"
          "                    c = ' \u00b7 '.join(xs) if len(' \u00b7 '.join(xs)) <= 60 else (xs[0] if xs else '')\n"
          "                    return f' ({c})' if c else ''\n"
          "                raw_ = ['\\u2022 ' + f\"{r[0].strip()}: {r[1].strip()}\" + cap_(r) for r in data if r and r[0].strip()]\n"
          "                note_t = note + ' — table: ' + ' | '.join(' / '.join(r) for r in rows)\n"
          "                if family_slide(t_hint, raw_, [(None, raw_)], head_title, headline, note_t, None, []):\n"
          "                    continue\n"
          "            if t_hint in ('cards', 'steps', 'bands', 'text') + GRAPHIC_KINDS and 3 <= len(data) <= 8 and ncol >= 2:\n")
    #      ... and a caption in brackets may run to 60 characters ("(Safeguard: Human approval for commitments)" stayed
    #      in the line, brackets and all, and the longest line set every row's text smaller)
    patch(eng / "family_rules.py", "OWNER = re.compile(r'^(.*?\\S)\\s*\\(([^()]{2,40})\\)\\s*$')",
          "OWNER = re.compile(r'^(.*?\\S)\\s*\\(([^()]{2,60})\\)\\s*$')   # (1ai) a caption up to 60 characters")
    # (1aj) the variety rule on labelled lists too: three "Label: text" lines after three cards, or 3-6 after a label
    #      table, become icon rows instead of the same cards or table again
    patch(eng / "page_to_spec.py",
          "        if all(labs):\n            if len(labs) == 3 and 'cards3' in R and all(len(b) <= 220 for _, b in labs):\n",
          "        prev_l = next((s_ for s_ in reversed(slides) if s_.get('kind') != 'divider'), None)   # (1aj) variety\n"
          "        if all(labs) and 3 <= len(labs) <= 6 and prev_l is not None and 'two_col' in R and all(len(b) <= 150 for _, b in labs) \\\n"
          "                and prev_l.get('source') == (R.get('cards3') if len(labs) == 3 else R.get('actions')) \\\n"
          "                and family_slide('fam:process list', ['• ' + f'{t}: {b}' for t, b in labs], None, head, head, note2, tk, []):\n"
          "            warnings.append(f'variety: \"{head}\" follows the same layout - drawn as icon rows')\n"
          "            return True\n"
          "        if all(labs):\n            if len(labs) == 3 and 'cards3' in R and all(len(b) <= 220 for _, b in labs):\n")
    #      ... and the page reader knows the name: "Layout: process list" (or rows) is a family line like the other styles
    patch(eng / "page_to_spec.py", "process (chevrons|arrow|numbered|cycle|snake|vertical|phases|pipeline|io|converge|diverge))$'",
          "process (chevrons|arrow|numbered|cycle|snake|vertical|phases|pipeline|io|converge|diverge|list|rows))$'")
    # (1ak) no text dumps: a list of steps or points is drawn, not boxed.
    #      - Sentences with no names (3-6, no "Label:"): icon rows, the sentence on the row - numbered down a spine under a
    #        heading that names a sequence (journey, steps, process, from ... to ...), unnumbered otherwise. The Studio set
    #        "Employee submits a guided purchasing request" and five more as one box of bullets or a numbered table.
    #      - "Label: text" lines whose labels are phase words (Discover, Design, Pilot, Measure, Decide ...) or under a
    #        sequence heading: chevrons, the label in the arrow.
    #      - A process whose text is too long for the style asked for (chevrons, numbered: a sentence each) falls back to the
    #        vertical rows, which hold a sentence a step, before chevrons or snake - and never to a box of bullets.
    patch(out / "tools/flows.py",
          "    missing = [s for s in st if not s[\"title\"]]\n",
          "    missing = [s for s in st if not s[\"title\"]]\n"
          "    if style == \"vertical\" and len(missing) == len(st):   # (1ak) rows with no names: the sentence is the row\n"
          "        missing = []\n")
    patch(out / "tools/flows.py",
          "    tw = _in(2.7)\n    x2 = x + _in(0.2) + tw\n",
          "    tw = _in(2.7) if any(s[\"title\"] for s in st) else 0   # (1ak) no names: the sentence takes the whole row\n"
          "    x2 = x + _in(0.2) + tw\n")
    patch(eng / "family_rules.py",
          "    if unordered: st = 'vertical'\n    its = retail_items(lines)\n",
          "    if unordered: st = 'vertical'\n    its = retail_items(lines)\n"
          "    if word == 'process' and st == 'vertical' and its and not any(split_label(plain(l))[0] for l in lines if plain(l)):\n"
          "        its = [{'title': '', 'text': plain(l)} for l in lines if plain(l)]   # (1ak) sentences with no names: rows of the sentence\n")
    patch(eng / "family_rules.py",
          "            style = 'chevrons' if len(P['steps']) <= 6 else 'snake'\n            if FL.lint({'process': P, 'style': style}): return None\n",
          "            style = 'chevrons' if len(P['steps']) <= 6 else 'snake'\n"
          "            if FL.lint({'process': P, 'style': style}):\n"
          "                if len(P['steps']) <= 6 and not FL.lint({'process': dict(P, unordered=unordered), 'style': 'vertical'}):\n"
          "                    P['unordered'] = unordered; style = 'vertical'   # (1ak) a sentence a step: the rows hold it\n"
          "                else: return None\n")
    # the list router: sentences -> icon rows; phase-word labels -> chevrons
    patch(eng / "page_to_spec.py",
          "        prev_l = next((s_ for s_ in reversed(slides) if s_.get('kind') != 'divider'), None)   # (1aj) variety\n",
          "        seq_h = bool(re.search(r'(?i)\\bfrom\\b.+\\bto\\b|\\bsteps?\\b|\\bprocess\\b|\\bflow\\b|\\blifecycle\\b|\\bjourney\\b|\\bhow (?:we|it|to)\\b|\\bstages?\\b|\\bphases?\\b', head))\n"
          "        prev_v = next((s_ for s_ in reversed(slides) if s_.get('kind') != 'divider'), None)\n"
          "        rows_before = isinstance((prev_v or {}).get('central'), dict) and prev_v['central'].get('style') == 'vertical'   # never rows after rows\n"
          "        if 3 <= len(items) <= 6 and not any(labs) and not rows_before and 'two_col' in R and all(len(x) <= 120 for x in items) \\\n"
          "                and family_slide('fam:process vertical' if (seq_h or numbered) else 'fam:process list', ['\\u2022 ' + x for x in items], None, head, head, note2, tk, []):\n"
          "            return True                                        # (1ak) sentences: icon rows, never a box of bullets\n"
          "        PHASE_W = {'discover', 'define', 'design', 'build', 'test', 'pilot', 'deploy', 'launch', 'measure', 'decide', 'scale', 'plan', 'assess',\n"
          "                   'prepare', 'adopt', 'sustain', 'analyse', 'analyze', 'implement', 'validate', 'train', 'operate', 'improve', 'learn', 'gather',\n"
          "                   'write', 'rank', 'approve', 'order', 'receive', 'pay', 'request', 'route', 'source', 'review', 'run', 'go-live', 'hypercare'}\n"
          "        if all(labs) and 3 <= len(labs) <= 6 and 'two_col' in R and (seq_h or all(t.strip().lower() in PHASE_W for t, _ in labs)) \\\n"
          "                and all(len(b) <= 120 for _, b in labs) \\\n"
          "                and family_slide('fam:process chevrons', ['\\u2022 ' + f'{t}: {b}' for t, b in labs], None, head, head, note2, tk, []):\n"
          "            return True                                        # (1ak) named steps in order: chevrons\n"
          "        prev_l = next((s_ for s_ in reversed(slides) if s_.get('kind') != 'divider'), None)   # (1aj) variety\n")
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
          "    t0 = time.time()\n"
          "    (w / \"weak.md\").write_text(LIB_REVIEW, encoding=\"utf-8\")\n"
          "    r = subprocess.run([PY, str(T / \"playbook.py\"), \"review\", str(w / \"weak.md\")], capture_output=True, text=True)\n"
          "    seen = [k for k in (\"a timeline\", \"name a topic\", \"placeholders\") if k in r.stdout]\n"
          "    rows.append((\"library expert review (dates, topic headings, placeholders)\", len(seen) == 3, \"-\",\n"
          "                 f\"{len(seen)} of 3 findings: {', '.join(seen) or 'none'}\", round(time.time() - t0, 1)))\n"
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
          f"\nT = Path(__file__).resolve().parent\nLIB_ONE, LIB_TWO, LIB_SEARCH, LIB_PICK = {LIB_ONE!r}, {LIB_TWO!r}, {LIB_SEARCH!r}, {LIB_PICK!r}   # library cases\n"
          f"LIB_REVIEW = {LIB_REVIEW!r}\n")

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
