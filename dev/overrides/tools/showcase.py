"""The skill's own showcase picture: real outputs of this skill on the Ulta template - a deck's variety, the process
library, flows and retail diagrams, an infographic one-pager slide, chart my data, an architecture slide, a pack, a
reviewed deck. The ONLY picture to show for "what can you do", "show examples", "what does it look like" - one tile per
capability, numbered 1-8 like the answer's list (guides/capabilities.md). Never web, stock or generated images.

    python tools/showcase.py [--out /mnt/data/out/showcase.png]
"""
import shutil, sys
from pathlib import Path

src = Path(__file__).resolve().parent.parent / "assets" / "showcase.png"
out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else (
    Path("/mnt/data/out/showcase.png") if Path("/mnt/data").exists() else Path("showcase.png"))
out.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out)
print(f"PICTURE {out}")
print("1 Decks (every template layout, a PDF or another deck rebuilt on the template, other ways to show any slide) · "
      "2 Library of ready-made decks · 3 Process flows, swimlanes and retail diagrams · 4 Infographic one-pager slides · "
      "5 Chart my data and report packs · 6 Architecture slides · 7 Packs from your files · 8 Review and repair")
