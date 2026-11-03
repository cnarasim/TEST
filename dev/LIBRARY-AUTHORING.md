# Writing process library templates (ULTA SlideGlam)

The process library is a set of ready-made Ulta decks. Each template is ONE Markdown page; the skill builds it on the
approved Ulta PowerPoint template with rules (no AI) and checks it with Presentation Central's delivery gate. A person
picks a template, then adapts it with their own facts. So a template must be (1) right about the process, (2) short
enough to sit at the template's type sizes, (3) neutral about vendors, and (4) honest: no invented facts.

## Where things are
- Built skill to check with (read-only, do not edit; `python3 dev/build_skill.py ... --out <dir>` makes it): `<built skill>`
- Existing templates (read them, copy their style): `<built skill>/library/<domain>/<l1>/<id>.md`
- Write templates to: `/home/user/TEST/dev/overrides/library/<domain-folder>/<l1-folder>/<id>.md`
  (to tighten an EXISTING template, copy it to the same relative path there and edit the copy)
- Check: `python3 dev/verify_templates.py --skill <built skill> <files or folder>` (lint + a governed build of each page)

## Front matter (all fields required)
```
---
id: sc-wh-putaway                 file name without .md; prefix = domain code + L1 code; lower case, digits, dashes
domain: Supply Chain              one of the domains below (exact spelling)
l1: Warehouse & Inventory         the end-to-end process (reuse an existing L1 name of the domain when it fits)
l2: Putaway and slotting          the sub-process: what a person ticks in the picker (2-5 words)
summary: One sentence on what the deck explains (under 160 characters).
systems: WMS, ERP inventory        KINDS of system only (ERP, WMS, OMS, POS, TMS, PIM, CRM, planning system, ...)
tags: putaway, slotting, ...       5-8 search words people would type
order: 406                         L1 x 100 + position (look at the domain's other templates; avoid duplicates)
---
```
Domains and folders: Retail `retail/` (rt-) · Supply Chain `supply-chain/` (sc-) · Finance `finance/` (fi-) ·
Enterprise Architecture `enterprise-architecture/` (ea-) · Programs and Projects `programs-and-projects/` (pp-) ·
Proposals `proposals/` (pr-) · Strategy `strategy/` (st-) · Timelines and Roadmaps `timelines-and-roadmaps/` (tl-) ·
Infographics `infographics/` (ig-) · NEW: Technology Operations `technology-operations/` (to-) · Data and AI
`data-and-ai/` (da-) · People and Change `people-and-change/` (pc-). The L1 folder is the L1 name in kebab case
(`Warehouse & Inventory` -> `warehouse-inventory`).

## The page
`# Title` (= l2, sentence case), an optional one-line intro under it, then one `## Heading` per slide (6-9 slides).
A `## Heading` is the slide's takeaway, not a topic: "Counters count, inventory control approves", not "Roles".
Under a heading, choose ONE body:
- **Cards**: `### Name` sub-headings (2-3 of them), each with 2 bullets -> three coloured cards.
  The classic opener: `## What <process> covers` with `### Purpose`, `### In scope`, `### Outcome`.
- **A table**: a Markdown table (header row + 3-5 rows, 2-4 columns). Classic process tables:
  `| Step | What the system does | Records it keeps |`, `| Control | How it works | Owner |`, `| KPI | What it measures | Data source |`.
- **Today and target**: `### Today` and `### Target` (or `### Tomorrow`), 2 bullets each -> two contrast bands.
- **A Layout line** (exact spelling) over bullet lines:
  - `Layout: swimlane handoffs` - who does what. Lines `- Role: step`, roles reused (2-4 roles, 5-8 lines). A decision is
    a line ending with `?`, followed by `- Role: If yes, ...` and `- Role: If no, ...`. Other swimlane styles:
    `swimlane sipoc`, `swimlane lanes`, `swimlane columns`, `swimlane phased`, `swimlane blueprint`, `swimlane timed`, `swimlane systems`.
  - `Layout: process chevrons | numbered | arrow | cycle | snake | vertical | phases | pipeline | io | converge | diverge` -
    steps in order, `- Title: short detail` (chevrons 3-6, numbered 3-7, cycle 3-6, snake 5-10, phases 2-5, io/converge/diverge 2-5).
    Phases: `- Prepare: rehearsals; sign-offs (T-4 weeks)`.
  - `Layout: timeline quarters | lanes | status-roadmap | phases | sprints | now-next-later | countdown | storyline | vertical | calendar`
    and `timeline template-milestones | template-callouts | template-gantt | template-roadmap` - dated lines:
    `- Pilot in 40 stores: Apr 2027 to Jun 2027 (Stores)`, `- Go-live: Sep 6, 2027`, `- Q2 2027: Pilot`. Write a date range
    with "to" (the engine reads it), never with a dash.
  - `Layout: retail <starter>` with NO lines below (a ready-drawn retail diagram): cross-dock, dc-operations, import-flow,
    inbound-to-dc, inventory-count, markdown, merchandise-planning, month-end-close, omnichannel-fulfilment, order-to-cash,
    procure-to-pay, record-to-report, returns, store-replenishment, supply-chain, supply-chain-cross-dock, three-way-match,
    vendor-onboarding. Or `Layout: retail network | dc-flow | cross-dock | fulfilment | document-flow` over `- Title: text (Owner)` lines.
  - Numbers and strategy: `four numbers`, `kpi cards`, `scorecard`, `ranking`, `donut`, `rings`, `bubbles`, `treemap`,
    `sankey`, `slope`, `waffle`, `bullet`, `gantt`, `matrix`, `hexagons`, `pyramid`, `hub`, `cards`, `priorities house`,
    `OGSM`, `template funnel`. Find an existing template that uses the layout (`grep -rl "Layout: matrix" <built skill>/library`)
    and copy its line format exactly.
- `> Notes: ...` under a section goes to the speaker notes (detail, caveats, "example dates").

## Size rules (the gate holds the template's type sizes: 36 pt headlines, 14-24 pt cards, 16 pt tables)
- `## Heading` at most 42 characters (aim for 30-38). `# Title` at most 40.
- Card bullet (under `###`) at most 52 characters; 2 bullets per card; 2-3 cards.
- Tables: at most 5 data rows; first column at most 30 characters, other cells at most 64 (aim for 30-50).
- Swimlane step at most 40 characters; process / timeline line at most 70 (title part 1-3 words).
- Never repeat the same value across one table row unless it is a rating word (High/Medium/Low, Strong/Weak, Yes/No ...).
`verify_templates.py` lints these and then builds the page; a FAIL line from the build says what to shorten.

## Wording rules
- Application-agnostic: name KINDS of system (ERP, WMS, OMS, POS, TMS, PIM, CRM, planning system, integration platform,
  data platform, ticketing tool). Never a product or vendor (SAP, S/4HANA, Oracle, Manhattan, Blue Yonder, IBM, Salesforce,
  Workday, ServiceNow, Jira, Snowflake, Azure, AWS ...), a transaction code (VA01, F-28) or a table name (EKKO). EDI message
  numbers (EDI 850, 856, 810) and industry words (ASN, ATP, FEFO, RFID) are fine.
- Plain punctuation: no em dash (U+2014) and no en dash (U+2013) anywhere (date ranges use "to"). Use a hyphen, a colon
  or a comma. Straight quotes.
- No invented facts: use placeholders `[target]`, `[baseline]`, `[date]`, `[owner]`, `[n]` where a figure is unknown, or mark
  example numbers in a `> Notes: illustrative figures` line. Never name real people, vendors or brand partners.
- Ulta context where it helps (a beauty retailer: stores, DCs, ulta.com and the app, the loyalty program, salon services,
  prestige and mass brand partners, gift sets, testers), but keep each template reusable.
- Short, concrete, active sentences. One message per slide. US spelling is fine; keep the existing templates' tone.

## Done
Each of your files prints `OK` in `verify_templates.py` (no lint problem, no FAIL line, built READY, or DRAFT where no
renderer is installed). If a FAIL line remains that is
NOT about your text (an engine or check problem), leave it and list it in your final report with the template id.
Report: the files you wrote (paths), the verify summary line, and any residual non-content FAILs.
