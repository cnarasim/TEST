# Architecture diagrams

Part of the ULTA Presentation Central instructions: SKILL.md's rules for every deliverable, token rules and checks apply here too.

## Architecture diagrams - ULTA Enterprise Diagram Standards v0.7.0
Only for a standalone architecture diagram (no deck asked for), or when the user asks for draw.io, the ULTA Enterprise Diagram Standard(s) or an ARB / C1-C3 submission diagram (even when it names a vendor platform). A diagram inside a PowerPoint deck is a guides/decks.md `diagram` slide in one of the native styles.
The standard is in `brands/ulta/diagram_standard.json`; never draw these with the deck diagram or one-pager engines.
1. Write arch.json (format at the top of `tools/enterprise_diagram.py`): `zones` (kind dmz | saas | core | downstream; a zone
   can sit `"above"` the zone it feeds), `systems` (zone, state existing | modified | new | retire | future, shape rect |
   cylinder | diamond; `row` is optional - without it each zone is laid out from its own flows), `flows` (step 1.0, 1.1, 2.0 … in order, from,
   to, type sync | async | optional | rejection, desc = the sentence for the Flow Legend), `kdd` and `evidence`.
   Names 1-4 words; sub-labels a few words. Only the user's systems and facts - for a vendor's standard process with no
   Ulta detail, write "Conceptual … (not Ulta's configured solution)" in the subtitle. Gate 1 or 2 from the request.
2. `python {SKILL_DIR}/tools/enterprise_diagram.py arch.json --out /mnt/data/out/<Name>` - lays out zones and gutters,
   routes every connector with a full corner list, places numbered badges, runs the Step 8b geometry audit and the 28
   Step 13 checks plus a legibility audit (no line through a zone title, no text past its box, badges clear of lines,
   borders and arrowheads). On NEEDS CORRECTION nothing is written: apply the printed fix (shorten a name, move a
   support system to row 1, split the view) and run again. Re-running on the same --out keeps the Created date.
   The kit's arch.json (`ulta-kit diagram`: zones[].title, nodes[].label, keep/changed, badge, opt/reject)
   is accepted as is. More than ~25 systems or ~30 flows in one view: split it (C2 overview + C3 per zone).
3. `show()` the PNG; deliver the files on the FILES line that the user needs: the editable .drawio, the .png and the .pdf
   (the .svg and .html are working files). The same diagram on a slide of a deck: a diagram slide in the deck's
   storyboard (guides/deck-layouts.md, "Any diagram in a deck"), native and editable in PowerPoint.
