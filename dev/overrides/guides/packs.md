# Packs and data - decks made from files

Part of the ULTA PPT Studio instructions: SKILL.md's rules for every deck, token rules and checks apply here too. Every
tool below builds on the Ulta template, runs the checks and prints its files; deliver every .pptx it names (companion
.xlsx or .drawio files the tools write may go with it). Outputs go to `/mnt/data/out` (on Claude: your working folder).

| The user has / wants | Run |
|---|---|
| A spreadsheet or CSV: "chart my data" | `python {SKILL_DIR}/tools/chart_advisor.py data.xlsx [--sheet S]` recommends charts (rank, chart, why); `--build /mnt/data/out/<Name>.pptx [--pick 1,3]` builds them. Headlines state facts computed from the data. Order header + items files: pass both. |
| A KPI workbook: monthly or quarterly business review | `python {SKILL_DIR}/tools/report_pack.py kpis.xlsx --title "Customer Operations MBR" --period "October 2026" --out /mnt/data/out/Ops-MBR [--owner "Name"] [--classification internal]` (sheet KPIs: KPI, Actual, Target, Prior, Unit, Better, Owner, Commentary, Group). Next period: same command, new file. |
| Several workstream decks: one steering committee pack | `python {SKILL_DIR}/studio/enterprise/steerco_pack.py A.pptx B.pptx C.pptx --out /mnt/data/out/SteerCo --title "Transformation steering committee" [--date "..."] [--classification internal]` |
| A tracker export (Jira, ServiceNow, Smartsheet, Azure DevOps, Excel): weekly status | `python {SKILL_DIR}/tools/status_from_export.py export.csv --project "<name>" --lead "<name>" --out /mnt/data/out/<Name>-Status` (RAG rules are written into the notes; next week, same command) |
| A RACI or a team list | `python {SKILL_DIR}/tools/people.py raci raci.xlsx --title "<Project> RACI" --out /mnt/data/out/RACI` (checks one A and at least one R per activity); `people.py org team.csv --title "..." --out /mnt/data/out/Org` (Name, Title, Reports to) |
| Meeting notes or a transcript | `python {SKILL_DIR}/tools/meeting.py prep transcript.vtt --out /mnt/data/out/mtg`, read `mtg-cues.txt`, write `meeting.json` (decisions, actions with owners and dates), then `meeting.py build meeting.json --out /mnt/data/out/Team-Sync` |
| Screenshots with a red box around what to click: a how-to deck | `python {SKILL_DIR}/tools/walkthrough.py marks s1.png s2.png ...` then `walkthrough.py build guide.json --out /mnt/data/out/<Name>` (deliver the .pptx) |
| An event log (case, step, time): what really happens in a process | `python {SKILL_DIR}/studio/enterprise/process_insights.py events.xlsx --out /mnt/data/out/O2C --title "Order to cash" [--reference "A > B > C"] [--target-days 5]` (`--sample order-to-cash` shows it on a sample log) |
| A list of flows (systems, teams, hand-offs): diagram plus register | `python {SKILL_DIR}/tools/diagram_pack.py flows.txt --title "..." --out /mnt/data/out/<Name>` (`A → B: what [type=...; owner=...]` per line) |
| Any deck: a score and a fix list, or a rebuild on the template | `python {SKILL_DIR}/tools/review_deck.py Deck.pptx`; `python {SKILL_DIR}/tools/deck_doctor.py Deck.pptx [--fix /mnt/data/out/<Name>.pptx]` |

Rules that matter here:
- Every number on a slide comes from the user's file; the tools compute headlines from the data. Never add figures.
- Sample data is used only when the user asks for an example, and is labelled as sample in the deck.
- A tool that prints a FAIL: fix the input (a column name, a missing value) and run it again; never edit the .pptx.
