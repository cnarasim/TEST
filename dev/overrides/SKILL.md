---
name: ulta-slideglam
description: Ulta Beauty PowerPoint on the approved Ulta template - new decks and slide edits, process flows, swimlanes, retail and supply chain diagrams, timelines, charts, one-pager slides, architecture slides, steering and report packs, plus a library of nearly 300 ready-made process and project decks. Use it for every Ulta deck, slide or presentation request, even when not named. Runs only its bundled scripts on the user's files.
---

# ULTA SlideGlam (v1.0)

A new PowerPoint skill for Ulta Beauty, built from Presentation Central's deck engine and delivery checks (v141) and
Deliverable Studio's Eco engine and process library (6.37.1), on Ulta's approved template. PowerPoint only: Word
documents, Excel workbooks, HTML dashboards, sites, UI screens and ARB templates are not part of this skill (if asked, say
so and offer the content as slides).

## How this skill works, and what it does not do
- Every .pptx is built by the Python scripts in this folder: `tools/` (deck builders, checks, packs, `playbook.py` for the
  library), `studio/` (the Studio's Eco engine: a Markdown page becomes a deck by rules, no AI), `modules/` (templates
  and the validator). Standard library plus python-pptx, lxml, Pillow and numpy; LibreOffice and pdftoppm draw the
  review pictures when present.
- Scope: reads only the user's uploaded files and this folder; writes only to the output folder (and working copies in
  the temp folder). No network connections, downloads or installs. Nothing leaves the chat on the skill's initiative.
- Files keep an honest record: every deck names this skill and its version in its properties (Producer, SkillVersion).
- Checks are added, never removed: templates and validators are compared to their pinned SHA-256. The templates are
  slimmed copies of the approved originals (XML identical, oversized pictures re-encoded): `assets/templates/PROVENANCE.json`
  records both hashes. Report results to the user as printed.

## Read the guide for the request, then build
| The user wants | Read |
|---|---|
| A deck on a standard process or project artefact - retail, supply chain, finance, enterprise architecture, programs and projects, proposals, strategy, timelines and roadmaps, infographics, technology operations, data and AI, people and change ("a deck on cycle count", "a cutover plan", "a solution options review", "an incident review"), or slides from several processes ("three-way match controls and the cutover timeline") | `library` - search or pick from the library first, build, then adapt it with the user's facts |
| A new deck from notes, a document or a storyboard; a process flow; a retail diagram (supply chain with trucks and DCs, cross-dock, store replenishment, online orders, returns, procure to pay, month-end close); other ways to show a slide; a PDF or another deck rebuilt on the template | `decks`, then `deck-layouts` |
| An infographic or one-pager slide, a status report, a visual summary, a story told around the user's screenshots or product photos | `infographics` |
| A C1-C3 architecture diagram to the ULTA Enterprise Diagram Standards (editable draw.io, PNG, PDF); a diagram on a slide inside a deck is a diagram slide (`deck-layouts`) | `architecture` |
| Chart my data, an MBR/QBR report pack, a steering committee pack, RACI or org chart slides, a meeting one-pager, weekly status from a tracker export, a screenshot walkthrough deck, process insights from an event log | `packs` |
| "What can you do?", "show examples", how it compares | `capabilities` |
A request that fits a library template AND brings its own content: build the template, then adapt the page with the
user's content (guides/library.md, "Adapt"). Edit an existing deck: Edit mode below, no guide.

## Rules for every deck
1. **Run the skill, or say you didn't.** Every file and picture comes from this skill's scripts. No code ran this turn:
   answer in text only - no files, no pictures, no "example" images.
2. **Only Ulta pictures.** Never image search, web search or image generation. Examples come from `tools/showcase.py`
   (real outputs on the Ulta template). The user's own screenshots and photos may go into their deck, checked.
3. **Only the Ulta template.** Never offer or build non-Ulta designs. Colours, fonts and layouts come from the template.
4. **Never invent numbers, names or dates.** Missing facts: ask once, then "-". Library templates carry placeholders
   (`[target]`, `[owner]`, `[date]`) and sample figures marked illustrative in the notes: fill them from the user's facts
   or say they are placeholders.
5. **Attach every file on the tool's `FILES` line** and end the reply with the `RESULT` line(s) exactly as printed.
6. **Plain punctuation.** No em dashes anywhere you write: a hyphen, a colon or a comma. The scripts replace any left.
7. **A crisp summary on the slide, the detail in the notes.** Headline = the takeaway (at most 45 characters), an optional
   `"summary"` line (one sentence, at most 24 words), body text 6-15 words per card; background goes in the speaker notes.
8. **Think like a presentation expert.** Decide the deck's answer, the ask and the storyline first; every message on the
   picture its content asks for (figures as big numbers or a chart, dates as a timeline, steps as a flow, systems as a
   diagram, risks and actions in tables); retail first: a supply chain, DC, online order, return or finance process goes
   on a retail diagram or flow with its pictograms; pictures on at least half the content slides; never two slides in a
   row that tell their story the same way. Act on the build's EXPERT lines before you deliver.
9. **Fix by rebuilding, never by hand.** To fix a FAIL change the storyboard (or the library page) and rebuild. Never edit
   a built .pptx with python-pptx or XML: it loses the template's formatting and checks. Every .pptx you deliver comes
   from `build_deck.py`, `playbook.py`, `onepager.py`, `fix_deck.py` or a pack tool; a .pptx from anywhere else goes
   through `python {SKILL_DIR}/tools/fix_deck.py <deck> --out <fixed>` first.

## Token rules
- Run tools with their default (short) output. Never print or re-read files you generated.
- Visual review before delivery: builds print `PICTURE <deck>_validation/contact-sheet.png` (every slide numbered). Look
  at it as an expert designer would (alignment, crowding, empty or cut text, crops, colour); open a single slide's render
  (`slide-N.png` in the `_validation` folder) when in doubt, fix in the storyboard or page, rebuild.
- Final reply: for routine decks at most 7 lines (status, up to 3 assumptions, problems the tool listed, the files). For
  complex business decks a 3-4 point Executive Context Summary (objective, decisions and trade-offs, risks and
  mitigations), then the files. **Always end with the `RESULT` line(s) copied exactly**: "ULTA Standards Match N% (checks)
  · built in N s · Estimated efficiency versus modeled baseline: ...". Standards Match is measured from the checks recorded
  for that exact file; the efficiency figure is an estimate, never billing data. Never re-word, round or compute it
  yourself. Asked how it is made: `python {SKILL_DIR}/tools/tokens.py --explain <file>`.
- `DRAFT - VERIFICATION INCOMPLETE` means a check could not run here (usually no LibreOffice for the render check): say
  so plainly; never call that READY.

## Step 1 of every task: find the skill, check it, read its guide (one turn)
Put the guide name(s) from the table in `GUIDES` (`['library']`, `['decks', 'deck-layouts']`, `['packs']` ...); leave it
empty to change a deck the user uploaded. If the platform showed this SKILL.md's folder (Claude Code and Cowork:
`${CLAUDE_SKILL_DIR}`), put it in `GIVEN`; otherwise the cell finds it.
```python
import os, sys, glob, subprocess
GIVEN = ''                                           # folder of this SKILL.md, if known
GUIDES = []                                          # the guide(s) for this request (table above); [] for an edit
ok = lambda d: bool(d) and all(os.path.isfile(os.path.join(d, 'tools', f)) for f in ('build_deck.py', 'playbook.py', 'brand.py'))
places = [GIVEN] + sorted(glob.glob('/home/*/skills/*') + glob.glob('/mnt/*/skills/*') + glob.glob('/mnt/skills/*/*')
                          + glob.glob('/skills/*') + glob.glob('/opt/skills/*') + glob.glob(os.path.expanduser('~/.claude/skills/*')))
SKILL_DIR = next((d for d in places if ok(d) and 'slideglam' in d), None) or next((d for d in places if ok(d)), None)
def show(path):                                      # a picture IN the chat where the platform can (else open it yourself)
    try:
        from IPython.display import Image, display; display(Image(filename=path)); return print(f'SHOWN {path}')
    except Exception: print(f'OPEN {path}')
def guide(name):
    print(open(os.path.join(SKILL_DIR, 'guides', name + '.md'), encoding='utf-8').read())
tool = lambda *a: subprocess.run([sys.executable, f'{SKILL_DIR}/tools/{a[0]}', *map(str, a[1:])], capture_output=True, text=True).stdout
if not SKILL_DIR:
    print("REPLY: The skill's files are not in this chat. If the skill shows 'Review this skill' in Settings > Skills, approve it; then start a new chat.")
elif GUIDES:
    print(tool('bootstrap.py'))                      # READY = templates, validators and fonts are the approved ones
    for g in GUIDES: guide(g)
    if 'decks' in GUIDES: print(tool('build_deck.py', 'inventory'))
else:
    print(SKILL_DIR)
```
- `REPLY:` - pass the message on. `NOT READY` - show the FAIL lines and stop. `READY` - follow the printed guides.
- Decks: don't ask questions first. Build with sensible defaults (6-10 slides) and list assumptions at the end; ask only
  when there is no content at all.

## The process library in one minute (full guide: guides/library.md)
```bash
python3 {SKILL_DIR}/tools/playbook.py search cycle count                 # find templates (ids, domain > L1 > L2)
python3 {SKILL_DIR}/tools/playbook.py build sc-wh-cycle-count --out <out>/Cycle-Count.pptx
python3 {SKILL_DIR}/tools/playbook.py md sc-wh-cycle-count sc-oc-pricing --out page.md   # to adapt or combine
python3 {SKILL_DIR}/tools/playbook.py pick "three-way match controls; payment run KPIs" --out page.md   # slides from any template
python3 {SKILL_DIR}/tools/playbook.py page page.md --out <out>/<Name>.pptx                # the adapted page, same checks
```
Several ids make one deck with a chapter (divider and agenda line) per template; `pick` takes the best slide for each
request from across the library. Content prepared elsewhere: write it as a library page (`# Title`, one `## takeaway`
per slide, `Layout:` lines) and build it with `page`.

## On Claude (claude.ai, Claude Code, Cowork)
- Uploads are in `/mnt/user-data/uploads` (read it for `/mnt/data` in the guides). Build into a working folder (for
  example `--out /home/claude/out/<Name>.pptx`; a tool's default output folder is `./out`), then copy the files on the
  `FILES` line to `/mnt/user-data/outputs` and link them - never the `_validation` folder or the `.json` records.
  Claude Code: write into the user's project or the folder they name.
- No notebook: run the first cell as a script (`python3 - <<'EOF' ... EOF`), then each tool as its own shell command:
  `python3 {SKILL_DIR}/tools/<tool>.py ...` (a long deck build: `python3 {SKILL_DIR}/tools/job.py start deck --wait 45 --
  python3 {SKILL_DIR}/tools/build_deck.py build ...`).
- Pictures: `show()` cannot put a picture in the chat there; open the contact sheet or a slide render with your image
  viewer for the review, and give the user the PNG as a file when they should see it.

## Edit mode (existing deck): find the slot, then apply. No bootstrap, no rebuild.
```python
run = lambda *a: print(subprocess.run([sys.executable, f'{SKILL_DIR}/tools/edit_deck.py', *a], capture_output=True, text=True).stdout)
run('find', DECK, 'old words')                      # -> "3.12 | old words ..." (or: run('find', DECK, '--slide', '3'))
run('apply', DECK, '--set', '3.12=New text', '--out', '/mnt/data/out/<Name>.pptx')
```
Same change everywhere: `--replace "Q3=>Q4"`. Reorder or delete slides: `--order 1,3,2,5`. A new slide is not an edit:
guides/decks.md. Another layout for one slide: "other ways to show a slide" in guides/decks.md. Reply in 3 lines or fewer.

## Checks you must report (they run automatically)
- Sensitive data: FAIL means never deliver; REVIEW lines go to the user (masked; never print them in full).
- Accessibility FAIL blocks delivery. The Purview label is kept or inherited, never invented. Every file is
  version-stamped (`tools/stamp.py verify <file>`).

## More workflows
`WORKFLOWS.md` (read only the part a request needs): PDF or another deck onto the template, a deck from a long document,
executive version, speaker notes, PDF handout, translation, approved slide library, enterprise controls, a new brand.
`CHANGELOG.md` says what this skill is made of - read it only when asked.

## Self-test (when something misbehaves, or the user asks for a health check)
`python {SKILL_DIR}/tools/selftest.py` runs every main feature, the process library included, on built-in samples
(a few minutes) and prints a scoreboard. Show the table as printed.
