---
id: ea-pr-technology-lifecycle
domain: Enterprise Architecture
l1: Portfolio and Rationalisation
l2: Technology lifecycle and standards
summary: Which technologies are standard, on trial, contained or retiring, how a new one gets approved, and the support dates we track.
systems: Architecture repository, Application inventory, Contract register
tags: technology lifecycle, technology standards, tech radar, end of support, adopt, retire, version currency
order: 406
---
# Technology lifecycle and standards

## What the lifecycle covers
### Purpose
- Clear standards for what teams build on
- No system left on an unsupported version
### In scope
- Languages, platforms, products and versions
- Trials, standards, containment and retirement
### Outcome
- Fewer technologies to support and secure
- Upgrades planned before support ends

## Every technology has one state
| State | What it means | Rule |
|---|---|---|
| Adopt | Our standard for new work | Use by default |
| Trial | Tested in a limited scope | Use only in the trial |
| Contain | Supported, not for new work | Plan the move off |
| Retire | End of support is set | Move off by the date |

## A technology moves through five steps
Layout: process cycle
- Propose: a need the standards do not meet
- Trial: time-boxed, with success measures
- Adopt: added to the standards list
- Contain: replaced by a better standard
- Retire: moved off before support ends

## New technology starts as a trial
Layout: swimlane handoffs
- Delivery team: Proposes a new technology
- Design authority: A standard already fits?
- Design authority: If yes, points to the standard
- Design authority: If no, approves a trial
- Delivery team: Reports the trial results
- Design authority: Decides adopt or stop

## Dates we track for every product
| Date | Tracked as | Owner |
|---|---|---|
| Vendor end of support | Date per product and version | Technology owner |
| Our retirement date | [n] months before end of support | Enterprise architecture |
| Upgrade window | Planned release to stay supported | Application owner |
| Licence renewal | Date and notice period | Procurement |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Supported versions | Systems on a supported version | Application inventory |
| Contained in new work | New projects on contained tech | Design reviews |
| Retirements on time | Moves done before end of support | Retirement plan |
| Trial decisions | Trials decided by their end date | Trial log |
