# ULTA SlideGlam - changelog

"Stamped" = the SkillVersion written into every file the skill builds (Producer "ULTA SlideGlam").

## v1.0 - a new PowerPoint skill: Presentation Central + Deliverable Studio, a bigger library, a smaller package

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
(`.ulta.json`: drawn visuals, template infographics, shortened lists), Presentation Central's finishing (template run
styles, fit, accessibility, type scale, plain punctuation), the delivery gate, a stamp and the RESULT line.

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
