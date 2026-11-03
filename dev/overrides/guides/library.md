# The process library - ready-made Ulta decks

Part of the Ulta DeckCraft instructions: SKILL.md's rules for every deck, token rules and checks apply here too.

## What it is
About 300 predefined decks, each one Markdown page in `library/<domain>/<l1>/<id>.md`, from the end-to-end process (L1)
to the sub-process (L2): **Retail** (merchandising, pricing and promotions, store operations, omnichannel and guest,
brand partners), **Supply Chain** (plan, source and procure, order to cash, warehouse and inventory, deliver),
**Finance** (procure to pay, cash and receivables, record to report, plan and perform), **Enterprise Architecture**
(assess, compare and select, design and standards, portfolio, review and decide, deliver and govern), **Programs and
Projects** (charter to closure), **Proposals**, **Strategy**, **Timelines and Roadmaps**, **Infographics**,
**Technology Operations** (incidents, problems, changes, releases, service levels), **Data and AI** (governance,
quality, master data, analytics, AI use cases, responsible AI, agent reviews) and **People and Change**. The pages are
application-agnostic: they name kinds of system (ERP, WMS, OMS, POS ...), never a product or a transaction code.
A build turns the page into a deck by rules (no AI): cover, the slides, closing; the same deck every time.

## Use it (one cell, then deliver)
1. **Find**: `python {SKILL_DIR}/tools/playbook.py search <words>` (`list` shows everything, `list --domain "Finance"` one
   domain). No match: build the deck the usual way (guides/decks.md).
2. **Build as is** when the user wants the standard view ("a deck on our cycle count process"):
   `python {SKILL_DIR}/tools/playbook.py build <id> --out /mnt/data/out/<Name>.pptx [--title "..."] [--owner "Name"] [--classification internal]`
   Several ids make one deck, a chapter per template (a divider and an agenda line each), in the order given.
3. **Adapt** when the user gives their own facts, names, dates, numbers or scope (most requests):
   `python {SKILL_DIR}/tools/playbook.py md <id> [<id> ...] --out /mnt/data/out/<Name>.md`, read the page, edit it with
   the user's content (keep one `## ` per slide and every `Layout:` line; replace generic lines and `[placeholders]`;
   delete sections that do not apply; add a section in the same style), then
   `python {SKILL_DIR}/tools/playbook.py page /mnt/data/out/<Name>.md --out /mnt/data/out/<Name>.pptx`.
4. **Review and deliver** like every deck: the status line, FAIL lines, `PICTURE` (look at the contact sheet), `FILES`,
   and the `RESULT` line copied exactly. Library pages carry placeholders and illustrative sample figures: tell the user
   which ones are still placeholders unless they gave you the facts.

## Fix a FAIL (edit the page, rebuild - never the .pptx)
- "headline ... does not fit one line" / "needs 2 lines": shorten that `## ` heading (aim for 30-38 characters).
- "had to shrink ... shorten it": shorten the bullets or table cells of that slide, or split the table (at most 5 rows).
- "repeats ... in several cells": give each cell its own words (rating words and dates may repeat).
- "cells empty ... emptied template structure": add the missing rows or columns, or use fewer columns.
- Anything else: the FAIL line names the fix; rebuild after each change.

## How a page is written (to adapt or add one)
- Front matter: `id`, `domain`, `l1`, `l2`, `summary`, `systems` (kinds of system), `tags`, `order`. `# Title`, then one
  `## Heading` per slide; the heading is the slide's takeaway (at most 42 characters).
- A body per slide: `### Name` cards (2-3, two short bullets each); a Markdown table (3-5 rows); `### Today` and
  `### Target` bands; or a `Layout:` line over its lines - `swimlane handoffs` (`- Role: step`, a question line then
  `- Role: If yes, ...` and `- Role: If no, ...`), `process chevrons | numbered | arrow | cycle | snake | vertical | phases |
  pipeline | io | converge | diverge`, `timeline quarters | lanes | status-roadmap | phases | sprints | now-next-later |
  countdown | storyline | vertical | calendar` (dated lines; ranges with "to"), `retail <starter>` (cross-dock,
  dc-operations, import-flow, inbound-to-dc, inventory-count, markdown, merchandise-planning, month-end-close,
  omnichannel-fulfilment, order-to-cash, procure-to-pay, record-to-report, returns, store-replenishment, supply-chain,
  supply-chain-cross-dock, three-way-match, vendor-onboarding), and `four numbers`, `kpi cards`, `scorecard`, `matrix`,
  `hexagons`, `pyramid`, `hub`, `ranking`, `donut`, `gantt`, `OGSM`, `priorities house`, `template funnel` ...
  Copy the line format from a library page that uses the layout.
- `> Notes: ...` under a section goes to the speaker notes.
- A team's own pages: a folder of pages with this front matter, named by `ULTA_LIBRARY_DIR` (several: separated by ':'),
  or added to `library/` before the skill is uploaded again. `python {SKILL_DIR}/tools/playbook.py check --agnostic`
  checks them (front matter, sections, no product names).
