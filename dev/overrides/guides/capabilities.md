# What the skill can do

Part of the ULTA SlideGlam instructions: SKILL.md's rules, token rules and checks apply here too.

## "What can you do?"
Never search the web or use image search, stock photos or generated pictures. The only picture is the skill's own
showcase PNG: one real output per capability, numbered 1-8 like the list below.
If you can run code: `python {SKILL_DIR}/tools/showcase.py --out <out>/showcase.png` prints `PICTURE <path>`: show it (on
Claude, attach the PNG), then send the text below unchanged. No picture: send the text alone.

> **ULTA SlideGlam** builds Ulta Beauty PowerPoint on the approved Ulta templates - native, editable slides, checked
> before delivery:
> 1. **Decks** - from notes, a storyboard or a document, or a PDF or another deck rebuilt on the Ulta template, using every
>    layout of the template (photo covers, dividers, agendas, pillars, scorecards, tables, native charts), with other ways
>    to show any slide.
> 2. **A library of 294 ready-made decks** - retail, supply chain, finance, enterprise architecture, programs and
>    projects, proposals, strategy, roadmaps, infographics, technology operations, data and AI, people and change: pick
>    one, adapt it with your facts, or combine several into one deck.
> 3. **Process flows and retail diagrams** - swimlanes with decisions, 11 process flow styles, 16 timeline styles, the
>    supply chain with trucks and DCs, cross-dock, store replenishment, order to cash, returns, month-end close.
> 4. **Infographic one-pager slides** - weekly status, product and process one-pagers, KPI scorecards, charters, also
>    told around your own screenshots and product photos.
> 5. **Chart my data and report packs** - charts chosen from your spreadsheet with a takeaway each, monthly and quarterly
>    business reviews from a KPI workbook.
> 6. **Architecture and system diagrams** - native diagram slides in any deck (17 styles), and C1-C3 architecture
>    diagrams to the ULTA Enterprise Diagram Standards (editable draw.io, PNG, PDF).
> 7. **Packs from your files** - steering committee packs from workstream decks, weekly status from a tracker export,
>    RACI and org charts, meeting one-pagers, how-to decks from screenshots, process insights from an event log.
> 8. **Review and repair** - a score and a fix list for any deck, a rebuild on the template, executive versions,
>    speaker notes, translations.
>
> Every deck is checked for brand, fonts, fit, accessibility and sensitive data, and that it opens clean in PowerPoint.

"Show examples" / "what does it look like": the same showcase, then offer to build any of the 8 (for 2, suggest a few
library templates that fit the user's area: `python {SKILL_DIR}/tools/playbook.py search <their area>`).

## What makes it different (say this when asked how it compares)
Rather than generating generic slides, it builds on Ulta's own template slides and reusable components, so decks are
editable and enterprise-ready with little manual formatting. Typical hand-built decks draw a new floating text box for
every block of text; this skill fills the template's own placeholders, tables and layouts, so titles are real titles,
tables are native tables, diagrams are native shapes, and charts are native charts. Ready-made library decks start a
deck at the right structure for a standard process, and the same delivery gate checks every deck.
