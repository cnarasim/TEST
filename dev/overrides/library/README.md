# The process library (ULTA SlideGlam)

Ready-made, editable Ulta decks: one Markdown page per template, built on the approved Ulta template by the Studio's Eco
rules (no AI, the same deck every time) and checked by Presentation Central's delivery gate. 294 templates: 146 from
Deliverable Studio 6.37.1 (its 147 less the ARB submission deck) and 148 written for this skill, in twelve domains: Retail, Supply Chain, Finance, Enterprise
Architecture, Programs and Projects, Proposals, Strategy, Timelines and Roadmaps, Infographics, Technology Operations,
Data and AI, People and Change. Every page is application-agnostic: it names kinds of system (ERP, WMS, OMS, POS ...),
never a product, a transaction code or a table.

    python tools/playbook.py list | search <words> | show <id> | md <id> ... --out page.md | build <id> ... --out deck.pptx
    python tools/playbook.py pick "three-way match controls; cutover timeline" --out page.md   the best slide per request
    python tools/playbook.py page page.md --out deck.pptx      an adapted or new page, same checks
    python tools/playbook.py check --agnostic                  front matter, sections, no product names

## Add a template
1. Copy a template of the same kind (a process: `supply-chain/warehouse-inventory/sc-wh-cycle-count.md`; a strategy page:
   `strategy/strategy-on-a-page/st-sp-ogsm.md`) to `library/<domain>/<l1>/<your-id>.md`, or keep a team folder outside the
   skill and name it in `ULTA_LIBRARY_DIR` (several folders: separated by ':').
2. Front matter: `id` (the file name), `domain`, `l1` (the end-to-end process), `l2` (the sub-process), `summary`,
   `systems` (kinds of system), `tags` (search words), `order` (L1 x 100 + L2).
3. The page: `# Title`, then one `## Heading` per slide (the takeaway, at most 42 characters) with cards (`###`), a table
   (at most 5 rows), Today / Target bands, or a `Layout:` line over its lines (guides/library.md lists them). A
   `> Notes: ...` line goes to the speaker notes. Unknown figures stay `[target]`; sample figures are marked illustrative.
4. `python tools/playbook.py check --agnostic`, then `python tools/playbook.py build <your-id> --out check.pptx`: fix every
   FAIL line in the page until the build prints READY.
