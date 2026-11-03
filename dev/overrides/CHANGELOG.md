# Ulta DeckCraft - changelog

"Stamped" = the SkillVersion written into every file the skill builds (Producer "Ulta DeckCraft").

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

**The process library**: the Studio's 147 templates plus this skill's new ones in the same Markdown format, three new
domains (Technology Operations, Data and AI, People and Change), `tools/playbook.py` (list, search, show, md, build, page,
check). A library deck is held to the same standard as every deck: the Eco build is followed by a build record
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
- Gate refinements, each the same intent applied to the Studio's output: rating words, [placeholders], dates and figures
  may repeat across a table row; a template infographic may mark status in the brand's status colours; the Studio's named
  overlays (pictograms, the takeaway line) are additions like the summary layer; an added pictogram passes the picture
  clearance check when it covers no text (a moved template picture still fails).
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
