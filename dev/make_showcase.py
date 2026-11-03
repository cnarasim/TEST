#!/usr/bin/env python3
"""Draw the skill's showcase picture from REAL outputs of the built skill (one tile per capability, numbered 1-8 like
guides/capabilities.md), so "what can you do?" never shows anything the skill did not make.

    python3 dev/make_showcase.py <built skill dir> <out.png>
"""
import csv, json, shutil, subprocess, sys, tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

TILES = ["Decks on every template layout", "Library of ready-made decks", "Process flows and retail diagrams",
         "Infographic one-pager slides", "Chart my data and report packs", "Architecture and system diagrams",
         "Packs from your files", "Review and repair"]
ORANGE, BERRY, INK, BLUSH = (238, 108, 55), (232, 39, 90), (30, 30, 30), (255, 245, 243)


def run(skill, args, cwd):
    r = subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True, timeout=900)
    return r.stdout + r.stderr


def render(skill, pptx, page, w):
    """One slide as a PNG through LibreOffice (the skill's own lo.py), 1280 px wide."""
    sys.path.insert(0, str(skill / "tools"))
    import lo
    pdf_dir = w / ("pdf-" + pptx.stem); pdf_dir.mkdir(exist_ok=True)
    pdf = lo.convert(pptx, pdf_dir, "pdf")
    pdf = Path(pdf) if pdf else next(pdf_dir.glob("*.pdf"), None)
    if not pdf or not pdf.exists():
        raise SystemExit(f"no PDF for {pptx}")
    stem = w / f"{pptx.stem}-p{page}"
    subprocess.run(["pdftoppm", "-png", "-r", "96", "-f", str(page), "-l", str(page), "-singlefile", str(pdf), str(stem)], check=True)
    return Path(str(stem) + ".png")


def main(skill, out):
    skill, out = Path(skill).resolve(), Path(out).resolve()
    w = Path(tempfile.mkdtemp(prefix="ulta-showcase-"))
    T = skill / "tools"
    (w / "deck.json").write_text(json.dumps({"slides": [
        {"source": 1, "title": "Store replenishment refresh", "subtitle": "Steering committee"},
        {"source": 9, "headline": "Faster replenishment lifts in-stock to 97%", "table": [["In-stock", "Lead time", "Stores"], ["97%\nshelf availability", "2 days\nDC to store", "1,400\nstores served"]]},
        {"source": 7, "headline": "Three moves get stores to plan", "table": [["Forecast", "Allocate", "Replenish"],
            ["Daily store forecast\n\nDemand by item and store", "Smarter first allocation\n\nNew items by store cluster", "Automatic orders\n\nDC picks overnight"],
            ["Exceptions only\n\nPlanners review outliers", "Shared rules\n\nOne rule set for all", "Fewer stock-outs\n\nAlerts before the shelf empties"]]},
        {"diagram": ["ulta.com → Order management: orders", "Store POS → Integration hub: sales", "Integration hub → ERP: sales",
                     "Order management → WMS: pick", "ERP → Planning: stock"], "headline": "Every order and sale reaches the ERP"},
        {"source": 32, "text": ["Thank you!"]}]}), encoding="utf-8")
    (w / "own.json").write_text(json.dumps({"title": "Guest pickup, in numbers", "format": "slide", "theme": "ulta", "blocks": [
        {"type": "stats", "title": "This quarter", "items": [["2 h", "order to ready"], ["96%", "picked complete"], ["4.8", "guest rating"]]},
        {"type": "steps", "title": "How it works", "items": [["Order", "online or in the app"], ["Pick", "store team picks"], ["Collect", "at the counter"]]},
        {"type": "takeaway", "text": "Ready in two hours, at every store"}]}), encoding="utf-8")
    with open(w / "sales.csv", "w", newline="") as f:
        c = csv.writer(f); c.writerow(["Month", "Category", "Net sales", "Plan"])
        for i, m in enumerate(["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06"]):
            for j, cat in enumerate(["Skincare", "Cosmetics", "Fragrance", "Haircare"]):
                c.writerow([m, cat, 120 + 9 * i + 25 * j, 125 + 8 * i + 24 * j])
    with open(w / "raci.csv", "w", newline="") as f:
        c = csv.writer(f); c.writerow(["Activity", "Planning", "DC operations", "Stores", "Finance"])
        for row in (["Set the replenishment rules", "A", "C", "I", "C"], ["Release store orders", "R", "A", "I", "I"],
                    ["Receive and stock the shelf", "I", "C", "A", "I"], ["Report in-stock and cost", "C", "I", "I", "A"]):
            c.writerow(row)
    from pptx import Presentation
    from pptx.util import Inches, Pt
    p = Presentation(); p.slide_width, p.slide_height = Inches(13.333), Inches(7.5)
    s = p.slides.add_slide(p.slide_layouts[1]); s.shapes.title.text = "Our Q3 results"
    s.placeholders[1].text = "Sales grew 6% to $1.2B\nOnline grew 18%\nMargin held at 39%"
    p.save(w / "plain.pptx")
    jobs = [
        ([T / "build_deck.py", "build", w / "deck.json", "--out", w / "deck.pptx"], w / "deck.pptx", 3),
        ([T / "playbook.py", "build", "sc-wh-cycle-count", "--out", w / "lib.pptx"], w / "lib.pptx", 4),
        ([T / "build_deck.py", "retail", "--out", w / "retail.pptx"], w / "retail.pptx", 2),
        ([T / "infographic.py", "make", w / "own.json", "--out", w / "own"], w / "own.pptx", 1),
        ([T / "chart_advisor.py", w / "sales.csv", "--build", w / "chart.pptx"], w / "chart.pptx", 2),
        ([], w / "deck.pptx", 4),                                    # the deck's own native diagram slide
        ([T / "people.py", "raci", w / "raci.csv", "--title", "Store replenishment RACI", "--out", w / "raci"], w / "raci.pptx", 1),
        ([T / "convert_deck.py", w / "plain.pptx", "--out", w / "conv.pptx", "--build"], w / "conv.pptx", 2),
    ]
    pics = []
    for k, (cmd, deck, page) in enumerate(jobs, 1):
        log = run(skill, cmd, w) if cmd else ""
        if not deck.exists():
            cand = sorted(deck.parent.glob(deck.stem + "*.pptx"))
            deck = cand[0] if cand else deck
        if not deck.exists():
            raise SystemExit(f"tile {k}: no deck from {cmd[0].name}: {log[-400:]}")
        pages = len(Presentation(str(deck)).slides)
        pics.append(render(skill, deck, min(page, pages), w))
        print(f"tile {k}: {deck.name} slide {min(page, pages)}")
    tw, th, pad, top = 640, 360, 28, 120
    W, H = 4 * tw + 5 * pad, top + 2 * (th + 54) + 2 * pad
    sheet = Image.new("RGB", (W, H), BLUSH); d = ImageDraw.Draw(sheet)
    font = lambda n, bold=False: ImageFont.truetype(str(skill / "fonts" / ("Inter-Bold.otf" if bold else "Inter-Regular.otf")), n)
    head = ImageFont.truetype(str(skill / "fonts" / "PlayfairDisplay-Black.ttf"), 46)
    d.text((pad, 30), "ULTA PPT Studio: real outputs on the Ulta template", font=head, fill=INK)
    for i, (pic, label) in enumerate(zip(pics, TILES)):
        x = pad + (i % 4) * (tw + pad); y = top + (i // 4) * (th + 54 + pad)
        im = Image.open(pic).convert("RGB"); im.thumbnail((tw, th)); sheet.paste(im, (x, y))
        d.rectangle([x, y, x + im.width - 1, y + im.height - 1], outline=(217, 217, 217))
        d.ellipse([x, y + th + 10, x + 36, y + th + 46], fill=ORANGE if i % 2 == 0 else BERRY)
        d.text((x + 18, y + th + 28), str(i + 1), font=font(22, True), fill="white", anchor="mm")
        d.text((x + 46, y + th + 14), label, font=font(24, True), fill=INK)
    q = sheet.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.Dither.NONE)
    out.parent.mkdir(parents=True, exist_ok=True)
    q.save(out, "PNG", optimize=True)
    print(f"SHOWCASE {out} {out.stat().st_size // 1024} KB")
    shutil.rmtree(w, ignore_errors=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
