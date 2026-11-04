---
id: sc-wh-yard
domain: Supply Chain
l1: Warehouse & Inventory
l2: Yard and dock appointments
summary: Booking inbound and outbound dock slots, checking trailers in and out, assigning doors and keeping the yard moving without detention.
systems: Yard management, Dock scheduling, WMS, TMS
tags: yard management, dock appointment, door assignment, trailer, detention, check-in, live unload
order: 411
---
# Yard and dock appointments

## What yard and dock cover
### Purpose
- Trucks arrive when the DC can work them
- Doors, trailers and labour used evenly
### In scope
- Inbound and outbound dock appointments
- Check-in, door moves and check-out
### Outcome
- Shorter waits and less detention cost
- Receiving and shipping plans that hold

## Appointments decide when trucks arrive
Layout: swimlane handoffs
- Carrier: Books a dock slot
- Yard team: Checks the slot and PO
- Yard team: Arrived within the window?
- Yard team: If yes, assigns a door
- Yard team: If no, reschedules or works it in
- Receiving: Unloads and closes the door
- Yard team: Releases the trailer

## Rules every carrier follows
| Rule | Standard | Owner |
|---|---|---|
| Booking lead time | At least [n] hours before arrival | Carrier |
| Arrival window | [n] minutes either side of the slot | Transportation |
| Live or drop | Set by load type and door plan | Yard team |
| Detention clock | Starts at the booked time | Transportation |

## Systems and data for the yard
| Step | What the system does | Records it keeps |
|---|---|---|
| Book | Offers slots by door and load type | Appointment |
| Check in | Records arrival and trailer | Gate log, trailer number |
| Assign | Sends the trailer to a door | Door assignment |
| Work | Links the door to the receipt or load | Receipt or load record |
| Check out | Records departure and seal | Gate log, seal number |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| On-time arrivals | Trucks inside their window | Appointments vs gate log |
| Truck turn time | Gate in to gate out | Gate log |
| Door utilization | Hours each door is worked | Door assignments |
| Detention cost | Charges for waiting trucks | Freight bills |

## Today and target
### Today
- Trucks arrive at once, then the dock is idle
- The yard is tracked on a whiteboard
### Target
- Every truck booked and checked in by system
- Truck turns inside [n] hours
