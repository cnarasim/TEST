#!/usr/bin/env python3
"""Check library templates the way the skill will build them: lint, then a governed build of each page.

    python3 dev/verify_templates.py [--skill DIR] [--jobs 3] <file.md | folder> [...]

Lint errors (fail the page): front matter (id = file name, domain, l1, l2, summary, tags, order; systems optional),
"# Title", application-agnostic wording (no product names, transaction codes or table names).
Lint warnings (the authoring guide's margins; they fail a page only with --strict, which new pages should pass):
plain punctuation (no em or en dashes; the build replaces any left), at least three "## " slides, and the size rules
that keep text at the template's type sizes:
  slide heading <= 42 characters    card bullet (under ###) <= 52    table: <= 5 rows, cell <= 64 (first column <= 30)
  swimlane step <= 40               process / timeline line <= 70
Build: the page body -> tools/playbook.py page (render check off for speed; --render runs it) -> status, FAIL lines, Standards Match.
The gate is the measure: a page is OK when it has no lint error, no FAIL line and builds READY (or DRAFT where no
renderer is installed). Exit 0 only when every page is OK.
"""
import argparse, concurrent.futures as cf, os, re, subprocess, sys, tempfile
from pathlib import Path

DEFAULT_SKILL = "/tmp/claude-0/-home-user-TEST/12dcbf9d-aee8-5751-826b-81ab99be96ee/scratchpad/build/ulta-slideglam"
REQ = ("id", "domain", "l1", "l2", "summary", "tags", "order")   # systems: optional (strategy pages name none)
LIMITS = dict(heading=42, card=52, rows=5, cell=64, first_cell=30, swim=40, line=70)


def lint(path, LIB):
    """(meta, body, errors, warnings): errors fail the page; warnings (sizes, dashes, a short page) are the authoring
    guide's margins and fail it only when the build shows the problem too (the gate is the measure)."""
    probs, warns = [], []
    text = path.read_text(encoding="utf-8")
    meta, body = LIB.parse(str(path))
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    raw = dict(l.split(":", 1) for l in (m.group(1).splitlines() if m else []) if ":" in l)
    raw = {k.strip().lower(): v.strip() for k, v in raw.items()}
    for k in REQ:
        if not raw.get(k):
            probs.append(f"front matter: no '{k}'")
    if raw.get("id") and raw["id"] != path.stem:
        probs.append(f"id '{raw['id']}' differs from the file name '{path.stem}'")
    if not body.lstrip().startswith("# "):
        probs.append('the page does not start with "# Title"')
    if len(re.findall(r"^##\s+\S", body, re.M)) < 3:
        warns.append("fewer than three '## ' slides")
    hits = LIB.vendor_terms(text)
    if hits:
        probs.append("not application-agnostic: " + ", ".join(dict.fromkeys(hits)))
    if "—" in text or "–" in text:
        warns.append("em or en dash: use a hyphen, a colon or a comma (the build replaces them)")
    section, layout, in_card, table = None, None, False, []
    def flush_table():
        if not table:
            return
        rows = [r for r in table if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
        data = rows[1:]
        if len(data) > LIMITS["rows"]:
            warns.append(f"'{section}': table has {len(data)} rows (at most {LIMITS['rows']}: split it or keep the top ones)")
        for r in rows:
            cells = [c.strip() for c in r.strip().strip("|").split("|")]
            for j, c in enumerate(cells):
                lim = LIMITS["first_cell"] if j == 0 else LIMITS["cell"]
                if len(c) > lim:
                    warns.append(f"'{section}': cell over {lim} chars: '{c[:50]}...' ({len(c)})")
        table.clear()
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("|"):
            table.append(s); continue
        flush_table()
        if s.startswith("## "):
            section, layout, in_card = s[3:].strip(), None, False
            if len(section) > LIMITS["heading"]:
                warns.append(f"slide heading over {LIMITS['heading']} chars: '{section}' ({len(section)})")
        elif s.startswith("### "):
            in_card = True
        elif s.lower().startswith("layout:"):
            layout, in_card = s.split(":", 1)[1].strip().lower(), False
        elif s.startswith(("- ", "* ")):
            item = s[2:].strip()
            if layout and layout.startswith("swimlane"):
                step = item.split(":", 1)[1].strip() if ":" in item else item
                core = re.sub(r"(?i)^if (yes|no)\s*,?\s*", "", step)
                if len(core.split()) > 5:                # the engine shows the first 5 words of a step and drops the rest
                    probs.append(f"'{section}': swimlane step over 5 words (the slide would show only the first 5): '{step}'")
                if len(step) > LIMITS["swim"]:
                    warns.append(f"'{section}': swimlane step over {LIMITS['swim']} chars: '{step[:45]}...'")
            elif layout:
                if len(item) > LIMITS["line"]:
                    warns.append(f"'{section}': line over {LIMITS['line']} chars: '{item[:45]}...'")
            elif in_card and len(item) > LIMITS["card"]:
                warns.append(f"'{section}': card bullet over {LIMITS['card']} chars: '{item[:45]}...' ({len(item)})")
    flush_table()
    return meta, body, probs, warns


def build(skill, path, meta, body, render=False, keep=None):
    with tempfile.TemporaryDirectory(prefix="ulta-verify-") as d:
        page = Path(d) / "page.md"
        page.write_text(body, encoding="utf-8")
        out = Path(d) / f"{path.stem}.pptx"
        env = dict(os.environ) if render else dict(os.environ, ULTA_NO_LIBREOFFICE="1")   # --render: the full check, READY
        r = subprocess.run([sys.executable, "-I", f"{skill}/tools/playbook.py", "page", str(page), "--out", str(out),
                            "--title", (meta or {}).get("l2") or path.stem], capture_output=True, text=True, env=env, timeout=900)
        o = r.stdout + r.stderr
        st = "READY" if re.search(r"^READY", o, re.M) else "NOT BUILT" if re.search(r"NOT (BUILT|WRITTEN)", o) else \
             "CRASH" if "Traceback" in o else ("DRAFT (no renderer)" if "no renderer here" in o else "DRAFT (review)") \
             if "VERIFICATION INCOMPLETE" in o else "NEEDS CORRECTION"
        fails = list(dict.fromkeys(l.strip() for l in o.splitlines() if l.strip().startswith("FAIL")))
        checks = list(dict.fromkeys(l.strip()[6:] for l in o.splitlines() if l.strip().startswith("CHECK ")))
        sheet = Path(d) / f"{path.stem}_validation" / "contact-sheet.png"
        if keep and sheet.exists():
            import shutil as _sh
            Path(keep).mkdir(parents=True, exist_ok=True); _sh.copy2(sheet, Path(keep) / f"{path.stem}.png")
        if st in ("NOT BUILT", "CRASH"):
            fails.append(o.strip().splitlines()[-1][:300] if o.strip() else "no output")
        m = re.search(r"Standards Match (\d+)%[^-·]*(?:- fix: ([^·]+))?", o)
        return st, fails, (m.group(1) if m else "?"), (m.group(2).strip() if m and m.group(2) else ""), checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+"); ap.add_argument("--skill", default=os.environ.get("ULTA_SKILL", DEFAULT_SKILL))
    ap.add_argument("--jobs", type=int, default=3); ap.add_argument("--lint-only", action="store_true")
    ap.add_argument("--strict", action="store_true", help="size and dash warnings fail too (for new pages)")
    ap.add_argument("--render", action="store_true", help="render each deck (LibreOffice): READY instead of DRAFT")
    ap.add_argument("--keep", help="folder to keep each deck's contact sheet in (<id>.png), for the visual review")
    a = ap.parse_args()
    sys.path.insert(0, f"{a.skill}/studio")
    import process_library as LIB
    files = []
    for p in map(Path, a.paths):
        files += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    files = [f for f in files if not f.name.lower().startswith("readme")]
    linted = [(f, *lint(f, LIB)) for f in files]
    results = {}
    if not a.lint_only:
        with cf.ThreadPoolExecutor(a.jobs) as ex:
            futs = {ex.submit(build, a.skill, f, meta, body, a.render, a.keep): f for f, meta, body, _, _w in linted if meta}
            for fu in cf.as_completed(futs):
                results[futs[fu]] = fu.result()
    bad = 0
    for f, meta, body, probs, warns in linted:
        st, fails, pct, fix, checks = results.get(f, ("not built", [], "?", "", []))
        ok = not probs and (a.lint_only or (not fails and st in ("READY", "DRAFT (no renderer)", "DRAFT (review)")))
        if a.strict:
            ok, probs = ok and not warns, probs + warns
            warns = []
        bad += 0 if ok else 1
        print(f"{'OK ' if ok else 'FIX'} {f.stem}  [{st}, Standards Match {pct}%{', open: ' + fix if fix else ''}]")
        for p in probs:
            print(f"    lint: {p}")
        for w in warns:
            print(f"    warn: {w}")
        for l in fails[:12]:
            print(f"    {l[:240]}")
        for l in checks[:6]:
            print(f"    check: {l[:240]}")
    print(f"{len(files)} template(s), {bad} to fix")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
