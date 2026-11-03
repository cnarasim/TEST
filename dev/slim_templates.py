#!/usr/bin/env python3
"""Slim the approved Ulta templates for the skill package, provably without touching the design.

    python3 dev/slim_templates.py <skill dir>            rewrites the templates in place, records PROVENANCE, re-pins hashes

Per template (.pptx):
  - every XML part (slides, layouts, master, theme, rels, content types) is copied byte for byte: layouts, positions,
    fonts and colours cannot change; the script verifies this after writing and stops otherwise
  - a JPEG photo over 1 MB is re-encoded at 2400 px on its long edge (180 dpi across the full 13.33 in slide) at quality 85
  - a PNG is re-saved losslessly (optimize) only when that is smaller; vector art (EMF, SVG) is never touched
Then every place that pins a template's SHA-256 (brand.json, the kit's template manifest, the validator's approved
reference hash, and the chain of hashes that pin the validator itself) is moved from the old hash to the new one, and
assets/templates/PROVENANCE.json records both hashes, so the slim file is traceable to the approved original.
"""
import hashlib, io, json, re, sys, zipfile
from pathlib import Path

from PIL import Image

LONG_EDGE, JPEG_Q, JPEG_MIN = 2400, 85, 1_000_000
TEMPLATES = ["modules/ultabranddeliverables/scripts/kit/templates/Ulta Beauty PPT Standard.pptx",
             "assets/templates/Ulta Beauty PPT Standard_Curated.pptx"]
TEXT_EXT = {".py", ".json", ".md", ".txt", ".yaml", ".yml"}


def sha_b(b):
    return hashlib.sha256(b).hexdigest()


def slim(path):
    src = path.read_bytes()
    zin = zipfile.ZipFile(io.BytesIO(src))
    changes, buf = [], io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            name = info.filename.lower()
            new = data
            if name.startswith("ppt/media/") and name.endswith((".jpg", ".jpeg")) and len(data) > JPEG_MIN:
                im = Image.open(io.BytesIO(data)); w, h = im.size
                k = min(1.0, LONG_EDGE / max(w, h))
                im2 = im.convert("RGB").resize((round(w * k), round(h * k)), Image.LANCZOS) if k < 1 else im.convert("RGB")
                b = io.BytesIO(); im2.save(b, "JPEG", quality=JPEG_Q, optimize=True, progressive=True)
                if len(b.getvalue()) < len(data):
                    new = b.getvalue(); changes.append({"part": info.filename, "from": [w, h, len(data)], "to": [*im2.size, len(new)]})
            elif name.startswith("ppt/media/") and name.endswith(".png"):
                im = Image.open(io.BytesIO(data)); b = io.BytesIO(); im.save(b, "PNG", optimize=True)
                if len(b.getvalue()) < len(data) * 0.97:
                    new = b.getvalue(); changes.append({"part": info.filename, "from": [*im.size, len(data)], "to": [*im.size, len(new)]})
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.compress_type = zipfile.ZIP_STORED if name.endswith((".jpg", ".jpeg", ".png")) else zipfile.ZIP_DEFLATED
            zi.external_attr = info.external_attr
            zout.writestr(zi, new)
    out = buf.getvalue()
    # proof: every non-media part is byte-identical, every part is still there, in the same order
    a, b = zipfile.ZipFile(io.BytesIO(src)), zipfile.ZipFile(io.BytesIO(out))
    if a.namelist() != b.namelist():
        sys.exit(f"STOP {path.name}: part list changed")
    for n in a.namelist():
        if not n.startswith("ppt/media/") and a.read(n) != b.read(n):
            sys.exit(f"STOP {path.name}: {n} changed")
    return src, out, changes


REFERENCE_PICTURES = ["modules/ultabranddeliverables/references/gallery", "modules/ultabranddeliverables/scripts/kit/infographic/samples"]


def optimize_pictures(skill):
    """Reference thumbnails and sample pictures (shown in the chat, never placed in a deck) as 256-colour PNGs when that
    saves at least 15%: flat slide renders, so the palette version looks the same. Returns bytes saved."""
    saved = 0
    for d in REFERENCE_PICTURES:
        for f in sorted((skill / d).rglob("*.png")):
            data = f.read_bytes()
            im = Image.open(io.BytesIO(data)).convert("RGBA")
            q = im.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.Dither.NONE)
            b = io.BytesIO(); q.save(b, "PNG", optimize=True)
            if len(b.getvalue()) < len(data) * 0.85:
                f.write_bytes(b.getvalue()); saved += len(data) - len(b.getvalue())
    return saved


def main(skill):
    skill = Path(skill).resolve()
    print(f"reference pictures: {optimize_pictures(skill) / 1024:.0f} KB saved")
    moves, prov = {}, {"note": "Slimmed for the skill package by dev/slim_templates.py: XML parts byte-identical to the approved "
                       "original; only oversized raster pictures re-encoded. source_sha256 is the approved original.", "templates": []}
    for rel in TEMPLATES:
        p = skill / rel
        src, out, changes = slim(p)
        if not changes:
            print(f"unchanged {p.name}"); continue
        old, new = sha_b(src), sha_b(out)
        p.write_bytes(out)
        moves[old] = new
        prov["templates"].append({"file": rel, "source_sha256": old, "sha256": new, "source_bytes": len(src), "bytes": len(out),
                                  "changed_parts": changes})
        print(f"{p.name}: {len(src) / 1e6:.2f} MB -> {len(out) / 1e6:.2f} MB ({len(changes)} picture(s) re-encoded)")
    # the 53-layout reference the gate compares with (the 33 template slides + the curated layouts) is rebuilt from the
    # slim base byte for byte by tools/full_template.py and pinned by its own hash (brand.json layouts.combined_sha256)
    if moves:
        import importlib
        sys.path.insert(0, str(skill / "tools"))
        for m in ("brand", "full_template"):
            sys.modules.pop(m, None)
        BR = importlib.import_module("brand"); FT = importlib.import_module("full_template")
        b = BR.current()
        old_c = (b.get("layouts") or {}).get("combined_sha256")
        if old_c:
            rows = sorted((r for r in FT.collection()["slides"] if r["new"]), key=lambda r: r["source"])
            new_c = sha_b(FT.build(b.base_template, FT.template(), rows))
            moves[old_c] = new_c
            prov["combined_reference"] = {"source_sha256": old_c, "sha256": new_c}
            print(f"40-layout reference re-pinned {old_c[:12]} -> {new_c[:12]}")
        sys.path.remove(str(skill / "tools"))
    # re-pin: replace each old hash by its new one wherever it is written (and a template's recorded byte count next to
    # it); files whose bytes change that way are pinned elsewhere in turn (validator <- its clearance gate <- the module
    # manifest), so repeat until nothing moves
    sizes = {f'"bytes": {t["source_bytes"]}': f'"bytes": {t["bytes"]}' for t in prov["templates"]}
    for _ in range(8):
        files = [f for f in skill.rglob("*") if f.is_file() and f.suffix in TEXT_EXT and f.name != "integrity.json"]
        before = {f: sha_b(f.read_bytes()) for f in files}
        touched = []
        for f in files:
            s = f.read_text(encoding="utf-8")
            t = s
            for o, n in list(moves.items()) + list(sizes.items()):
                t = t.replace(o, n)
            if t != s:
                f.write_text(t, encoding="utf-8"); touched.append(f)
        new_moves = {before[f]: sha_b(f.read_bytes()) for f in touched}
        new_moves = {o: n for o, n in new_moves.items() if o != n and o not in moves}
        if not new_moves:
            break
        moves.update(new_moves)
    (skill / "assets/templates/PROVENANCE.json").write_text(json.dumps(prov, indent=1) + "\n", encoding="utf-8")
    print(f"re-pinned {len(moves)} hash(es)")


if __name__ == "__main__":
    main(sys.argv[1])
