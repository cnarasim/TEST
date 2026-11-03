# ULTA SlideGlam - how the skill is built

`ulta-slideglam` is one PowerPoint skill made from two Ulta sources, reproducibly, by the scripts in this folder.
Current as of 2026-11-03: python-pptx 1.0.2, LibreOffice and pdftoppm present for render checks, resvg not installed.

| Source | Version | Taken |
|---|---|---|
| ULTA Presentation Central (skill zip) | v141 | tools, modules, guides, brands, fonts, assets (PowerPoint parts) |
| ULTA Deliverable Studio (Mac app runtime-kit) | 6.37.1 | Eco engine (`studio/`), process library, Studio fixes to shared tools, extra PPT tools |

## Build, check, package
```bash
python3 dev/build_skill.py --upc <ulta-presentation-central dir> --studio "<.../Contents/Resources/runtime-kit>" --out ulta-slideglam
python3 -I ulta-slideglam/tools/bootstrap.py              # READY = templates, validators, fonts are the pinned ones
python3 ulta-slideglam/tools/selftest.py                  # every PowerPoint feature + the process library
python3 dev/verify_templates.py --skill ulta-slideglam ulta-slideglam/library    # lint + governed build per template
python3 dev/make_showcase.py ulta-slideglam dev/overrides/assets/showcase.png     # the capabilities picture (then rebuild)
python3 dev/package.py ulta-slideglam dist                # dist/ulta-slideglam.zip, upload-ready (folder at the top level)
```

## What the build does (`build_skill.py`)
1. Copies Presentation Central v141 and drops what is not PowerPoint (`UPC_DROP`: Word, Excel, dashboards, sites, UI
   screens, BigQuery demo, HTML decks, reference galleries, examples, non-PowerPoint XSDs).
2. Takes the Studio's fixed copies of shared tools and its extra PowerPoint tools (`STUDIO_TOOLS`), and its Eco engine
   into `studio/` with every `central/` path pointed at the skill root (`STUDIO_ENGINE` + patches).
3. Applies named patches; each states the exact text it replaces and how often it must occur, so a changed source stops
   the build instead of being patched wrongly. Engine fixes and gate refinements are explained inline and in
   `overrides/CHANGELOG.md`.
4. Copies `overrides/` (SKILL.md, guides, WORKFLOWS, CHANGELOG, `tools/playbook.py`, `tools/showcase.py`, new library pages).
5. Slims the templates (`slim_templates.py`: XML byte-identical, oversized pictures re-encoded, every hash pin moved,
   `assets/templates/PROVENANCE.json` keeps the approved originals' SHA-256) and the reference thumbnails.
6. Writes `integrity.json` (SHA-256 of every shipped file), which bootstrap checks.

## The process library
Pages are Markdown with front matter (`overrides/library/<domain>/<l1>/<id>.md` for this skill's additions and
tightened copies). Rules for writing them: `LIBRARY-AUTHORING.md`. `verify_templates.py` lints a page and builds it
through the same gate as every deck; a page is done when it prints OK.
