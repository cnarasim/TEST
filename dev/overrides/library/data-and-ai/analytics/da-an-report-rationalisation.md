---
id: da-an-report-rationalisation
domain: Data and AI
l1: Analytics
l2: Report rationalisation
summary: Cutting a sprawl of reports down to a trusted set: inventory, usage, overlap, a keep, merge or retire decision, and the move.
systems: BI dashboards, Data platform, Data catalog
tags: report rationalisation, BI, dashboards, report inventory, usage, retire reports, self-service
order: 202
---
# Report rationalisation

## What report rationalisation covers
### Purpose
- Fewer reports, each one trusted
- People find the answer in one place
### In scope
- Reports, dashboards and scheduled extracts
- Usage, overlap, owners and definitions
### Outcome
- Less time reconciling conflicting numbers
- Lower cost to run and support reports

## Five steps from sprawl to a trusted set
Layout: process chevrons
- Inventory: every report, owner and source
- Measure: usage over the last [n] months
- Group: reports that answer the same question
- Decide: keep, merge, rebuild or retire
- Move: users to the kept report, then switch off

## Usage and value decide each report
Layout: matrix
- Keep: high use, high value - certify and maintain
- Merge: high use, overlapping - combine into one
- Rebuild: low use, high value - fix and promote
- Retire: low use, low value - switch off after notice

## Owners confirm before anything retires
Layout: swimlane handoffs
- Analytics team: Proposes the decision
- Report owner: Agrees with the decision?
- Report owner: If yes, signs it off
- Report owner: If no, gives the business reason
- Analytics team: Moves users and data
- Analytics team: Switches the report off

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Reports retired | Reports switched off | Report inventory |
| Certified reports | Reports on governed data | BI catalog |
| Active use | Users of the kept reports | Usage logs |
| Run cost | Cost to refresh and support | Platform costs |

## Today and target
### Today
- Thousands of reports, many unused
- Three versions of the same sales number
### Target
- A short list of certified reports
- One number for each business question
