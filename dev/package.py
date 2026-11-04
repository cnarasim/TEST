#!/usr/bin/env python3
"""Package the built skill as an upload-ready ZIP (the skill folder is the archive's top level) and check it.

    python3 dev/package.py <built skill dir> <out dir>      -> <out dir>/<name>-<version>.zip

Checks (stops on any): the folder name equals the SKILL.md `name`; exactly one SKILL.md; the description is 1-500
characters with no angle brackets (the upload limit the skill's own self-test enforces); integrity.json pins every
packaged file; no caches or OS litter. Prints the archive size and the largest entries.
"""
import hashlib, json, re, sys, zipfile
from pathlib import Path

SKIP_DIRS = {"__pycache__", ".pytest_cache"}
SKIP_FILES = {".DS_Store", "Thumbs.db"}


def main(src, out_dir):
    src, out_dir = Path(src).resolve(), Path(out_dir).resolve()
    text = (src / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        sys.exit("STOP: SKILL.md has no front matter")
    meta = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    name, desc = meta.get("name", "").strip(), meta.get("description", "").strip()
    if name != src.name:
        sys.exit(f"STOP: folder '{src.name}' differs from the skill name '{name}'")
    if not 0 < len(desc) <= 500 or "<" in desc or ">" in desc:
        sys.exit(f"STOP: description must be 1-500 characters without angle brackets ({len(desc)})")
    files = [p for p in sorted(src.rglob("*")) if p.is_file() and not (set(p.relative_to(src).parts) & SKIP_DIRS)
             and p.name not in SKIP_FILES and p.suffix != ".pyc"]
    skill_mds = [p for p in files if p.name == "SKILL.md"]
    if len(skill_mds) != 1:
        sys.exit(f"STOP: {len(skill_mds)} SKILL.md files (exactly one allowed)")
    integ = json.loads((src / "integrity.json").read_text(encoding="utf-8"))["files"]
    rel = {p.relative_to(src).as_posix(): p for p in files}
    missing = [k for k in rel if k != "integrity.json" and k not in integ]
    wrong = [k for k, v in integ.items() if k not in rel or hashlib.sha256(rel[k].read_bytes()).hexdigest() != v]
    if missing or wrong:
        sys.exit(f"STOP: integrity.json out of date - unpinned {missing[:3]}, changed or missing {wrong[:3]}")
    out_dir.mkdir(parents=True, exist_ok=True)
    ver = re.search(r"^# .*\((v\d+\.\d+)", text, re.M)          # the release in the SKILL.md heading
    zp = out_dir / (f"{name}-{ver.group(1)}.zip" if ver else f"{name}.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for k, p in rel.items():
            already = p.suffix.lower() in (".pptx", ".png", ".jpg", ".jpeg", ".otf", ".ttf", ".zip")
            z.write(p, f"{name}/{k}", compress_type=zipfile.ZIP_STORED if already else zipfile.ZIP_DEFLATED)
    z = zipfile.ZipFile(zp)
    big = sorted(z.infolist(), key=lambda i: -i.compress_size)[:8]
    unpacked = sum(i.file_size for i in z.infolist())
    print(f"PACKAGED {zp}  {zp.stat().st_size / 1e6:.2f} MB zipped, {unpacked / 1e6:.1f} MB unpacked, {len(z.infolist())} files")
    print("largest: " + "; ".join(f"{i.filename.split('/', 1)[1]} {i.compress_size // 1024} KB" for i in big))
    print(f"description {len(desc)} characters; top level: {sorted({k.split('/')[0] for k in rel})}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
