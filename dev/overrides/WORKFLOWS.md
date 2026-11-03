# ULTA SlideGlam - workflows reference
Read only the section a request needs. SKILL.md rules (no waiting, edit mode, decks, checks) still apply.

## A. Workflows (one command each; read the tool's header for options)
| User asks for | Run | Then |
|---|---|---|
| A ready-made deck for a standard process or project artefact | `tools/playbook.py search <words>`, then `build <id> --out …` or `md <id>` + edit + `page` (guides/library.md) | Fix FAILs in the page and rebuild |
| PDF slides or a non-branded deck → Ulta template | `tools/convert_deck.py <file> --out … --build` | Fix only the FIX/FAIL slides in the storyboard and rebuild. A PDF chart becomes a picture: ask for its data to make it native |
| Deck from a Word/PDF/long document | `tools/doc_outline.py <doc> --out outline.md`: read the outline, pull only the sections you need (`--section S7`), then write the storyboard (guides/decks.md) with "Source: <doc> p.N" in the notes | Never paste whole sections onto slides |
| Executive version, appendix | `tools/audience.py exec <deck> --out … [--keep 1,3,6]` | A one-pager from the deck's own facts; with `--keep` the deck reordered with an Appendix section |
| Speaker notes / timing | `tools/audience.py notes <deck> --minutes 20` | |
| PDF handout or e-mail text | `tools/audience.py export <deck> --pdf --email` | PowerPoint skill: no Word narrative is offered |
| Process / system / hand-off diagram with a register | `tools/diagram_pack.py flows.txt --title … --out …` (`A → B: what [type=…; owner=…]`) | Deliver the deck and the .drawio (the register .xlsx may go with it) |
| Packs from files (chart my data, MBR/QBR, steering committee, weekly status, RACI, org chart, meeting, walkthrough, process insights) | guides/packs.md | |
| Translate a deck | `tools/translate.py prepare <deck> --lang es` writes `<deck>-es.json`; replace each value with its translation (keep numbers, names and codes); `translate.py apply <deck> <deck>-es.json --lang es` | Report any SHRUNK HARD lines |
| Approved slides (disclaimer, company overview) | `tools/library.py add <approved.pptx> --slide N --key <name>`; in a storyboard: `{"library":"<name>"}` | Inserted unchanged; the validator fails the deck if one is edited (this is the approved slide library, not the process library) |
| Native table on its own slide | storyboard `{"table":{"rows":[[…],[…]]}}` or `{"table":{"from":"x.csv"}}` | |
All of these run the checks SKILL.md lists (sensitive data, accessibility, classification, stamp) and write to `/mnt/data/out`.

## B. Enterprise controls (automatic; report them, don't skip them)
Every deck build, edit and fix runs all four. The status table shows the results.
- **Sensitive data.** Secrets, passwords, keys, SSNs and card numbers are a FAIL: never deliver the file; remove the item
  and rebuild. E-mail addresses, phone numbers, IP addresses and internal host names are REVIEW: list them for the user
  and keep them only if they confirm.
- **Classification.** The template's Microsoft Purview label (Ulta: "Business Use") is kept. One-pagers and diagrams
  inherit it too. The skill never invents or changes a Purview label: a different one is applied by the user in PowerPoint.
- **Accessibility.** Alt text, the decorative flag and table header rows are added automatically (`tools/a11y.py fix`).
  A FAIL blocks delivery. On the slides the tools draw, words are made readable on what they sit on.
- **Version stamp.** Every file gets a version, owner, brand, check result, slide hash and change log in its properties,
  plus a `<file>.audit.json`. `python {SKILL_DIR}/tools/stamp.py verify <file>` shows the stamp and whether the slides
  changed since.

## C. A new or second template (brand)
Everything template-specific lives in a brand profile: template file, theme colours, fonts, slide roles, logo. Decks are
built on the active brand's own slides. Diagrams and infographics are drawn by the kit and moved onto the brand by
`ulta_conform.py`. The process library's pages build on the Ulta template.
- The user uploads a template: `python {SKILL_DIR}/tools/brand_import.py /mnt/data/<file>.pptx --name <short-name> --use`
  (add `--fonts <folder of .ttf/.otf>` and `--logo <file>` if they were uploaded too). Show its summary in at most 6 lines.
- Switch brands: `python {SKILL_DIR}/tools/brand.py use <name>`; `brand.py list` shows the brands available.
- Fonts without uploaded font files are measured with a similar bundled font: that measurement is APPROXIMATE.
- To make a brand permanent: zip `/mnt/data/brands/<name>` for the user; they add it to `brands/` and re-upload the skill.
