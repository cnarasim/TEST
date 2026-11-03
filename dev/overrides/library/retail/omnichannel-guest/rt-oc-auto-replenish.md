---
id: rt-oc-auto-replenish
domain: Retail
l1: Omnichannel & Guest
l2: Auto-replenishment orders
summary: Guests subscribe to products they use up; orders are created, paid and shipped on their cadence, with reminders, skip, swap and pause.
systems: Subscription engine, OMS, Payments, CRM, WMS
tags: auto-replenishment, subscription, auto-ship, repeat order, cadence, recurring payment, skip
order: 412
---
# Auto-replenishment orders

## What auto-replenishment covers
### Purpose
- Never let a guest run out of a favorite
- Earn repeat sales without a new campaign
### In scope
- Sign-up, cadence, reminders and changes
- Scheduled orders, payment and stock-outs
### Outcome
- Orders created and paid on the due date
- Fewer cancels from surprise charges

## The schedule orders, the guest steers
Layout: swimlane handoffs
- Guest: Subscribes and picks a cadence
- Subscription engine: Sends the reminder
- Guest: Keep this delivery?
- Subscription engine: If yes, create the order
- Subscription engine: If no, move to the next date
- Payments: Charges the saved card
- DC: Picks and ships the order

## Systems and data for auto-replenishment
| Step | What the system does | Records it keeps |
|---|---|---|
| Subscription | Item, cadence and next date kept per guest | Subscription, next order date |
| Reminder | A message days before the order, with a skip link | Reminder log, guest changes |
| Order creation | The engine creates an OMS order on the due date | Customer order, subscription link |
| Payment | The saved card is authorized; declines retried | Authorization, decline and retry |

## Each cycle runs the same five steps
Layout: process cycle
- Remind: days before the due date
- Order: created on the due date
- Pay: the saved card authorized
- Ship: the DC picks, packs and ships
- Reset: next date from the cadence

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Reminder before charge | No order is created without a reminder first | Ecommerce team |
| Decline handling | Declined payments retried, then the guest is told | Payments team |
| Stock-out rule | Out-of-stock items skip this cycle; the guest is told | Omnichannel operations |
| Easy cancel | Cancel online as easily as signing up | Customer care |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Active subscriptions | Subscriptions with an upcoming order | Subscription records |
| Retention | Subscribers still active after [n] orders | Subscription history |
| Skip and cancel rate | Orders skipped and subscriptions ended | Guest changes |
| Payment success | Scheduled orders paid on the first try | Authorization results |

## Today and target
### Today
- Orders built by a nightly batch, no reminder
- Card declines cancel the order silently
### Target
- Reminders with one-click skip and swap
- Smart retries and a prompt to update the card
