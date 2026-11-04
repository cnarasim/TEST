---
id: st-tr-value-streams
domain: Strategy
l1: Transformation
l2: Value stream map
summary: One value stream end to end: its steps, work and wait time, where flow breaks, improvements ranked, the future state and the decision.
systems: Process mining tool, Workflow tool, ERP
tags: value stream map, VSM, lean, flow, lead time, waste, process improvement
order: 209
---
# Value stream map

One stream mapped end to end, from a brand partner's new item to the guest buying it.

## One stream from brand partner to guest
Layout: process arrow
- Agree: range and launch date
- Set up: item, price and content
- Order: purchase order to the brand
- Receive: at the DC and allocate
- Launch: on shelf and online

## Where the time goes in the stream
Layout: process list
| Step | Work time | Wait time | Right first time |
|---|---|---|---|
| Agree range | [n] hours | [n] days | [n]% |
| Set up item | [n] hours | [n] days | [n]% |
| Order | [n] hours | [n] days | [n]% |
| Receive and allocate | [n] hours | [n] days | [n]% |
| Launch | [n] hours | [n] days | [n]% |
> Notes: measure work and wait time by walking the stream or from process mining; lead time is all work plus all wait, flow efficiency is work divided by lead time.

## Flow breaks at waits, rework and handoffs
### Waiting
- Approvals queue for days
- Batches wait for the weekly run
### Rework
- Item data fixed after setup
- Missing content holds the launch
### Handoffs
- Five teams, four systems, e-mail between
- No one owns the end-to-end time

## Improvements ranked by lead time saved
| Improvement | Waste removed | Lead time effect | Owner |
|---|---|---|---|
| Setup and content in parallel | Waiting | High | Merchandising |
| One launch checklist | Rework | High | Brand partnerships |
| Daily, not weekly, allocation | Batching | Medium | Allocation |
| Single intake form | Handoffs | Medium | Item setup |
> Notes: example improvements; rank them on days of lead time saved, then on effort.

## The future state cuts the waiting
### Today
- Six handoffs and weekly batches
- Lead time measured by nobody
### Target
- One team owns the stream end to end
- Lead time cut by [target]%

## How we map and improve a stream
Layout: process numbered
- Choose: one stream and its owner
- Walk: the steps with the people doing them
- Measure: work, wait and quality
- Design: the future state
- Improve: one change at a time, then measure

## Give the stream one owner and fund it
- Decision: Name one owner for the end-to-end stream
- Ask: Fund the top two improvements this quarter
- Next step: Measure lead time again in [n] weeks
