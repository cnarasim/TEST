#!/usr/bin/env python3
"""Check library templates the way the skill will build them: lint, then a governed build of each page.

    python3 dev/verify_templates.py [--skill DIR] [--jobs 3] <file.md | folder> [...]

Lint (fast, no build): front matter (id = file name, domain, l1, l2, summary, systems, tags, order), "# Title", at least
three "## " slides, application-agnostic wording (no product names, transaction codes or table names), plain punctuation
(no em or en dashes), and the size rules that keep text at the template's type sizes:
  slide heading <= 42 characters    card bullet (under ###) <= 52    table: <= 5 rows, cell <= 64 (first column <= 30)
  swimlane step <= 40               process / timeline line <= 70
Build: the page body -> tools/playbook.py page (render check off for speed) -> status, the FAIL lines, Standards Match.
Prints one block per template; exit 0 only when every template has no lint problem, no FAIL line and builds READY
(or DRAFT where no renderer is installed).
"""
import argparse, concurrent.futures as cf, os, re, subprocess, sys, tempfile
from pathlib import Path

DEFAULT_SKILL = "/tmp/claude-0/-home-user-TEST/12dcbf9d-aee8-5751-826b-81ab99be96ee/scratchpad/build/ulta-deckcraft"
REQ = ("id", "domain", "l1", "l2", "summary", "systems", "tags", "order")
LIMITS = dict(heading=42, card=52, rows=5, cell=64, first_cell=30, swim=40, line=70)


def lint(path, LIB):
    probs = []
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
        probs.append("fewer than three '## ' slides")
    hits = LIB.vendor_terms(text)
    if hits:
        probs.append("not application-agnostic: " + ", ".join(dict.fromkeys(hits)))
    if "—" in text or "–" in text:
        probs.append("em or en dash: use a hyphen, a colon or a comma")
    section, layout, in_card, table = None, None, False, []
    def flush_table():
        if not table:
            return
        rows = [r for r in table if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
        data = rows[1:]
        if len(data) > LIMITS["rows"]:
            probs.append(f"'{section}': table has {len(data)} rows (at most {LIMITS['rows']}: split it or keep the top ones)")
        for r in rows:
            cells = [c.strip() for c in r.strip().strip("|").split("|")]
            for j, c in enumerate(cells):
                lim = LIMITS["first_cell"] if j == 0 else LIMITS["cell"]
                if len(c) > lim:
                    probs.append(f"'{section}': cell over {lim} chars: '{c[:50]}...' ({len(c)})")
        table.clear()
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("|"):
            table.append(s); continue
        flush_table()
        if s.startswith("## "):
            section, layout, in_card = s[3:].strip(), None, False
            if len(section) > LIMITS["heading"]:
                probs.append(f"slide heading over {LIMITS['heading']} chars: '{section}' ({len(section)})")
        elif s.startswith("### "):
            in_card = True
        elif s.lower().startswith("layout:"):
            layout, in_card = s.split(":", 1)[1].strip().lower(), False
        elif s.startswith(("- ", "* ")):
            item = s[2:].strip()
            if layout and layout.startswith("swimlane"):
                step = item.split(":", 1)[1].strip() if ":" in item else item
                if len(step) > LIMITS["swim"]:
                    probs.append(f"'{section}': swimlane step over {LIMITS['swim']} chars: '{step[:45]}...'")
            elif layout:
                if len(item) > LIMITS["line"]:
                    probs.append(f"'{section}': line over {LIMITS['line']} chars: '{item[:45]}...'")
            elif in_card and len(item) > LIMITS["card"]:
                probs.append(f"'{section}': card bullet over {LIMITS['card']} chars: '{item[:45]}...' ({len(item)})")
    flush_table()
    return meta, body, probs


def build(skill, path, meta, body):
    with tempfile.TemporaryDirectory(prefix="ulta-verify-") as d:
        page = Path(d) / "page.md"
        page.write_text(body, encoding="utf-8")
        out = Path(d) / f"{path.stem}.pptx"
        env = dict(os.environ, ULTA_NO_LIBREOFFICE="1")
        r = subprocess.run([sys.executable, "-I", f"{skill}/tools/playbook.py", "page", str(page), "--out", str(out),
                            "--title", (meta or {}).get("l2") or path.stem], capture_output=True, text=True, env=env, timeout=900)
        o = r.stdout + r.stderr
        st = "READY" if re.search(r"^READY", o, re.M) else "NOT BUILT" if re.search(r"NOT (BUILT|WRITTEN)", o) else \
             "CRASH" if "Traceback" in o else "DRAFT (no renderer)" if "VERIFICATION INCOMPLETE" in o else "NEEDS CORRECTION"
        fails = list(dict.fromkeys(l.strip() for l in o.splitlines() if l.strip().startswith("FAIL")))
        if st in ("NOT BUILT", "CRASH"):
            fails.append(o.strip().splitlines()[-1][:300] if o.strip() else "no output")
        m = re.search(r"Standards Match (\d+)%[^-·]*(?:- fix: ([^·]+))?", o)
        return st, fails, (m.group(1) if m else "?"), (m.group(2).strip() if m and m.group(2) else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+"); ap.add_argument("--skill", default=os.environ.get("ULTA_SKILL", DEFAULT_SKILL))
    ap.add_argument("--jobs", type=int, default=3); ap.add_argument("--lint-only", action="store_true")
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
            futs = {ex.submit(build, a.skill, f, meta, body): f for f, meta, body, _ in linted if meta}
            for fu in cf.as_completed(futs):
                results[futs[fu]] = fu.result()
    bad = 0
    for f, meta, body, probs in linted:
        st, fails, pct, fix = results.get(f, ("not built", [], "?", ""))
        ok = not probs and (a.lint_only or (not fails and st in ("READY", "DRAFT (no renderer)")))
        bad += 0 if ok else 1
        print(f"{'OK ' if ok else 'FIX'} {f.stem}  [{st}, Standards Match {pct}%{', open: ' + fix if fix else ''}]")
        for p in probs:
            print(f"    lint: {p}")
        for l in fails[:12]:
            print(f"    {l[:240]}")
    print(f"{len(files)} template(s), {bad} to fix")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
