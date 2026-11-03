---
id: tl-ps-release-calendar
domain: Timelines and Roadmaps
l1: Plans and Schedules
l2: Release calendar
summary: The year's release dates across teams: release types, the windows we plan around, the steps every release follows, booking a slot and release health.
systems: Change calendar, Ticketing tool, Project plan
tags: release calendar, release schedule, change freeze, deployment window, release management, calendar
order: 206
---
# Release calendar

## Releases on the calendar
Layout: timeline calendar
- Spring release: Feb 28, 2027 (All systems)
- Summer release: May 16, 2027 (All systems)
- Back-to-school release: Aug 1, 2027 (Digital)
- Pre-holiday release: Oct 10, 2027 (All systems)
- Holiday freeze starts: Nov 1, 2027 (All systems)
- January release: Jan 23, 2028 (All systems)
> Notes: example dates; the last release before the freeze carries fixes only.

## Three kinds of release
| Type | What it carries | How often | Approves |
|---|---|---|---|
| Major | New capabilities, process changes | Quarterly | Change advisory board |
| Minor | Fixes and small changes | Monthly | Release manager |
| Emergency | Urgent fixes for live issues | When needed | Emergency change approver |

## Windows we plan around
Layout: gantt
- Spring beauty event: Mar 2027 to Apr 2027 (Business)
- Fall beauty event: Sep 2027 to Sep 2027 (Business)
- Holiday freeze: Nov 2027 to Jan 2028 (Technology)
- Year-end close: Jan 2028 to Feb 2028 (Finance)
- Pre-holiday release: Oct 10, 2027 (Technology)
> Notes: example dates; no major release lands inside an event, a freeze or a close.

## Every release follows the same steps
| Step | When | Owner |
|---|---|---|
| Code freeze for the release | Ten days before | Release manager |
| Regression testing passed | Three days before | Test lead |
| Change board approval | Two days before | Change advisory board |
| Deploy in the overnight window | Release night, 23:00 to 04:00 | Technology operations |
| Business checks and sign-off | Release morning, 06:00 | Business owners |

## How a release slot is booked
Layout: swimlane handoffs
- Product owner: Requests a change slot
- Release manager: Checks freezes and clashes
- Release manager: Is the slot free?
- Release manager: If yes, books it on the calendar
- Product owner: If no, takes the next free slot
- Change advisory board: Approves the release

## Release health
Layout: kpi cards
- Releases on the planned date: 9 of 10
- Changes rolled back: 1 this year
- Incidents after release: 3, down from 8
> Notes: illustrative figures from the ticketing tool.

## Who needs to know
| Audience | What they hear | When |
|---|---|---|
| Store teams | What changes and when to expect it | One week before |
| Service desk | Release notes and known issues | Three days before |
| Business owners | Checks to run after the release | Two days before |
| Leaders | A summary and any risk | Release day |
