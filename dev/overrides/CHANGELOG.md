# ULTA SlideGlam - changelog

"Stamped" = the SkillVersion written into every file the skill builds (Producer "ULTA SlideGlam"). Each release is
packaged as `ulta-slideglam-<version>.zip`; the skill folder inside is always `ulta-slideglam`. Newest first.

| Version | Name | Date | In one line |
|---|---|---|---|
| v1.4 | Clear Slides | 2026-11-04 | No boxes of bullets: sentence lists become icon rows, phase lists become chevrons |
| v1.3 | Variety | 2026-11-04 | Never two slides in a row that look the same; icon rows; calmer drawn pictures |
| v1.2 | Quality Pass | 2026-11-04 | All 294 library decks rendered and read: no empty template slides, every shape filled |
| v1.1 | Expert Review | 2026-11-04 | The skill's presentation expert on every build; a real 2 x 2 matrix; 5-word swimlane steps |
| v1.0 | First Release | 2026-11-03 | Presentation Central + Deliverable Studio in one PowerPoint skill, 294 ready-made decks |

## v1.4 "Clear Slides" - 2026-11-04
A deck built from content prepared in ChatGPT showed two slides that were boxes of bullets (six journey steps; five
scenarios whose text was too long for the numbered style it asked for).
- A list of 3-6 sentences with no names becomes icon rows with the sentence on the row - numbered down
  a spine under a heading that names a sequence (journey, steps, process, from ... to ...), unnumbered otherwise;
  "Label: text" lines whose labels are phase words (Discover, Design, Pilot, Measure, Decide ...) become chevrons; a
  process whose text is too long for the style asked for falls back to chevrons, then to rows (a sentence a step),
  never to a box of bullets; never rows after rows. The review names any box of bullets left (`EXPERT text:`), and
  SKILL.md says never to deliver one.

## v1.3 "Variety" - 2026-11-04
A deck written by another assistant read as one table after another (two identical card slides, then four table
slides in a row), and the drawn hexagons and hub looked loud.
- Icon rows, `Layout: process list`: a set that is not a sequence (paths, controls, safeguards, tests) as white rows -
  an icon, the name, its line and a caption - in one accent, without numbers or the connecting spine. Over a table
  it takes a row each (first cell the name, the second its line, later columns as the caption under their headers).
- The engine never draws two label tables, two grid tables or two sets of three cards in a row when the content can
  be told another way with nothing lost: the second becomes icon rows (a table of 3-6 rows, a list of 3-6 "Label:
  text" lines, three cards). `Layout: table` / `Layout: cards` keeps the author's form.
- The expert review names slides in a row that look the same (`EXPERT variety:`) and decks with fewer than a third of
  their content slides drawn (`EXPERT pictures:`), each with the Layout: line to use, never the look the run already
  has; steps in order written as a list get `Layout: process chevrons|snake`; a current and future state pair and the
  closing asks are left as they are. SKILL.md: a variety or pictures line means the deck is not finished.
- The drawn hub, hexagons and cycle in the brand's calm infographic look: light peach fills with dark names, white
  nodes with an accent ring, one accent in the hub's centre (not black), legend names in one ink and a size larger;
  the Studio cycled four saturated colours over every shape. The library's 44 hexagon and hub sections of 3-6 items
  are icon rows now (the infographics shapes showcase keeps its shapes).
- A takeaway line on a drawn slide sits under the headline box, not in it ("How we rank" overlapped "Must-haves
  first"); a caption in brackets may run to 60 characters.
- A step named Source, Result, Outcome, Centre, Input or Output stays a step unless the style draws that role (a
  seven-step snake lost its "Source" step to the diverge style's source box).
- Library: all 294 decks pass the variety and pictures checks (45 flagged before): sections told as icon rows, cards
  and tables alternated, two lanes timelines in a row split (a vertical timeline, icon rows).

## v1.2 "Quality Pass" - 2026-11-04
Every library deck rendered and its contact sheet and engine warnings read: 7 failing decks and 178 warnings before,
none after.
- A template timeline (Gantt, roadmap, milestones, call-outs) is used only when its filler takes the data, tried first
  on a scratch copy of the template slide; otherwise the section is drawn as the lanes timeline (any span). The Studio
  kept the template slide with its labels emptied - a roadmap of blank bars - and the gate now fails a template
  infographic that keeps three or more of its text shapes empty.
- A headline computed from the data is added after the author's heading or not at all, never in its place, and a
  timeline grouped by periods (Year 1, Q3, Wave 2) is not counted as "teams".
- Library builds print the engine's own warnings as CHECK lines (they were only in the build log).
- The milestones template finds its event circles and year labels by shape: the page engine clears a template
  timeline's sample text first, so the filler found no circle and every milestone slide kept 11 empty shapes.
- A template timeline is used only when its filler takes the data with no problem at all (a name too long for its
  circle, more events than it holds); otherwise the section is drawn as lanes.
- Swimlane hand-off numbers always show: with no free stretch of line, the number sits on the receiving step's
  corner (66 numbers were missing; the side panel listed hand-offs the drawing did not number).
- The template funnel reports a stage written without its detail (the four boxes beside the funnel stayed white),
  and the gate's empty-shape FAIL says what to write (`
- Stage: detail`).
- Closing asks written as bullets ("
- Decision: ...", "
- Ask: ...", "
- Next step: ...") become three cards; the list
  reader dropped every ask line and left one wide box of three bullets. Three lines that repeat a label ("Ask",
  "Ask", "Next step") become two boxes, one per label (three cards would repeat a title, which the gate refuses).
- A headline computed from the data states a fact (the last milestone and its date, the largest share), never a
  count: "What comes next: 2 teams, 3 tasks" and "8 steps, 4 teams" are gone.
- A dated line's closing parenthesis is its team only when it is a name (1-3 words); a sentence there is the item's
  detail ("(two features moved to phase 2)" had become a lane).
- A page's SIPOC (`Suppliers:`, `Inputs:`, `Process: step, step, step`, `Outputs:`, `Customers:`) fills the five
  columns; they were drawn empty.
- KPI cards keep the words around the number ("5 against a target of 0", "9 days per claim") as a caption and are
  sized to their content; big-number cards accept months and years ("14 months").
- Library content: 52 headings over 42 characters shortened (they printed smaller than the deck's other titles; the
  verifier now fails a longer one), 50 swimlane steps and decisions shortened to fit their boxes (about 24 characters,
  no word over 10 letters), and 30 pages fixed for their layout's rules: explicit Now / Next / Later columns (the
  columns followed today's date and showed two empty), countdowns that end at the go-live, 2-5 swimlane lanes, phases
  named in 1-3 words, plans longer than 24 months drawn as phases, shorter OGSM measures and house goals.

## v1.1 "Expert Review" - 2026-11-04
- Every library build, and `playbook.py review page.md` before one, runs Presentation Central's expert review
  (tools/deck_expert.py) with its advice in page terms - the answer first, the ask last, the better picture for each
  section as its `Layout:` line - plus headings that name a topic instead of the takeaway, two sections packed on one
  slide, and placeholders left.
- The 2 x 2 matrix reads as a matrix: axis labels from the author's own row and column words, the quadrant to act on in
  the strong colour and the others in the light tint, larger type (the Studio drew four equal saturated blocks).
- Swimlane steps hold 5 words: the engine shows the first 5 and drops the rest, so 150 library steps that ran longer
  ("Funds and sets the success") were rewritten; the verifier and the expert review now flag a longer step.
- SKILL.md: runs on whatever model and mode the chat uses (the scripts build and check; never ask the user to switch
  models); attach only the files the FILES line names, after `stamp.py verify` says the slides are unchanged since the
  stamp.

## v1.0 "First Release" - 2026-11-03
A new PowerPoint skill: Presentation Central + Deliverable Studio, a bigger library, a smaller package.

**Made from**
- ULTA Presentation Central v141 (the skill): deck engine, layouts, flows, swimlanes, timelines, retail diagrams,
  infographic one-pagers, chart my data, architecture diagrams, edit / fix / convert / translate / audience tools, the
  delivery gate (validate_deck.py, the hash-pinned ulta_pptx_fit.py), accessibility, sensitive-data scan, stamp.
- ULTA Deliverable Studio 6.37.1 (the Mac app's runtime kit): the Eco page engine (`studio/`: page_to_spec, build_from_storyboard,
  family_rules, central_slides, slide_svg), the process library and its reader, steering committee packs, process insights,
  and the Studio's fixes to the shared tools - title fit at 94% of the box, a "Takeaway:" prefix said once, editable
  visual groups (visual_spec), an engine-safe icon lookup, sankey colours, "Avg" naming, a render check on any renderer -
  plus its extra tools: review_deck, deck_doctor, report_pack, people, meeting, walkthrough, controls.
- Not adopted: the Studio's lower takeaway-line placement (under the headline's measured descenders). It left the cards
  and metrics layouts no clear space, so their takeaway went to the notes only and a two-line summary was no longer
  flagged; Presentation Central v141's placement and its self-test assertions are kept.

**PowerPoint only** - not shipped: Word (ulta_word, the Word template, the Word table guard), Excel workbooks
(ulta_excel), HTML dashboards and BigQuery demo data, ChatGPT Sites, UI screens, HTML whiteboards, HTML slide decks, the
Studio's app, server, MCP, cloud deploy and AI-provider legs. No ARB: the ARB template v3.6, its slide map, the Concept
ARB intake module and the ARB submission library deck are not shipped; the architecture diagram standard keeps its
Key Design Decisions panel without naming a board. Guides, the self-test and the safety rules are scoped to PowerPoint;
the self-test lists any check it did not run.

**The process library**: 294 templates - the Studio's 146 (its 147 less the ARB submission deck) and 148 new ones in the
same Markdown format, three new
domains (Technology Operations, Data and AI, People and Change), `tools/playbook.py` (list, search, show, md, build, page,
check, pick). `pick` takes one request per slide ("three-way match controls; payment run KPIs; cutover timeline") and
returns the best slide for each from any template as one page, by rules: the topic words choose the template (a word
few templates use counts most), the other words choose its slide (heading, layout, text); each slide's notes name its
source. Content prepared elsewhere is written in the same page format and built with `page`. A library deck is held to the same standard as every deck: the Eco build is followed by a build record
(`.ulta.json`: drawn visuals, template infographics, shortened lists), Presentation Central's finishing (text inside
its drawn shapes, template run styles, fit, accessibility, type scale, plain punctuation), the delivery gate, a stamp and the RESULT line.

**Fixes found by building every library deck through the gate**
- Table cell borders written in schema order (PowerPoint could offer to repair the file).
- Flow tables' body grey is the template's neutral (#404040), not an off-palette colour.
- Long tables continue on "(cont.)" slides at the template's 16 pt instead of shrinking to 9 pt.
- Runs the engine left without a size or font take the template cell's own style (the gate's "write into the existing
  run" rule); a run's own status colour is kept.
- A two-box slide built as one wide box (the empty box removed, its neighbour widened) is recorded as a shortened slide,
  so the gate checks it with the template-fidelity rule (only the template's own shapes, same design) instead of
  failing it shape by shape; 13 strategy and proposal decks with a closing Decision / Ask slide were held back by this.
- `playbook.py` names the gate check that failed (the gate's table rows), not only "NEEDS CORRECTION".
- A status dot only for a status: the Studio marked any table cell that began with a status word ("Late changes",
  "Failed messages", "Live or drop") with a red or green dot; now the cell must be the status, or the status and a
  note ("At risk - vendor", "Done (Mar 3)", "Late by 2 days"). The content gate treats the dot itself as a mark,
  as the brand colour gate already did (status colours on marks only); the words beside it are still checked. The
  engine's contrast pass no longer turns an amber dot black (amber on white is under 3:1; the dot is a mark).
- Card headings inside the template's text boxes keep the box's own face, made bold: the Studio's Medium face became
  Circular Bold at 15 pt, a size the type standard has no role for, so every two-box slide with headings failed. Figures
  in those boxes are bold, not orange (the template's boxes hold black text).
- Card titles keep the template's 24 pt when an icon is placed beside them: the Studio measured an inherited header
  size as 18 pt and wrote 18 pt into every card title ("had to shrink - the template sets it at 24 pt").
- A headline the engine computes from the slide's figures is used only when it fits one line (42 characters); the
  Studio allowed 60, so several metric slides failed "does not fit one line at the standard 36 pt".
- Scorecards fill both lists: "Lowlight:" / "Highlight:" lines in the page, else the page's own KPIs by status (off
  target under Lowlights). The Studio left both empty, so every scorecard kept the template's empty rows.
- A template infographic (scorecard, OGSM, vision house, quad, funnel, donut, map) is filled on the template's own
  slide, as Presentation Central does: the Studio first cleared the regions it did not fill itself, so the OGSM lost its
  row labels (Objective, Goals, Strategies, Measurements) and the scorecard its Highlights and Lowlights headers.
- The same colour in the template's notation: a run that shows white as FFFFFF where the template cell says bg1 (or
  black as 000000 for tx1), or no colour of its own on an unchanged cell, takes the template run's colour as written.
- Gate refinements, each the same intent applied to the Studio's output: rating words, [placeholders], dates and figures
  (signed ones too: +0%, -1.8 pts) may repeat across a table row; a template infographic may mark status in the brand's status colours; the Studio's named
  overlays (pictograms, the takeaway line) are additions like the summary layer, in the fidelity check and in the
  structure check's copy; an added pictogram passes the picture clearance check when it covers no text (a moved template
  picture still fails).
- The 40-layout reference and the fontconfig cache live under the temp folder by this skill's name, so this skill and
  Presentation Central installed side by side never read each other's cache.
**Size**
- Templates slimmed by `dev/slim_templates.py`: every XML part byte-identical to the approved original, oversized
  pictures re-encoded (the cover photo at 2400 px, 180 dpi across the slide; PNGs losslessly re-saved). Every pin moved
  with it (brand.json, the template manifest, the validator's approved reference, the clearance gate's pin of the
  validator, the 40-layout reference) and `assets/templates/PROVENANCE.json` records the approved original's SHA-256.
  Ulta Beauty PPT Standard 4.12 MB -> 1.30 MB; every generated deck is about 2.5 MB smaller.
- One icon set for both engines, PowerPoint schemas only, reference thumbnails as 256-colour PNGs, no reference galleries,
  examples, changelog history or app files.
