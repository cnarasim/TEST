---
id: rt-so-store-inventory
domain: Retail
l1: Store Operations
l2: Store physical inventory and shrink
summary: Store counts by department or full store, recounts, posting and shrink analysis by cause.
systems: Store inventory app, ERP inventory, Loss prevention
tags: store inventory, shrink, count, loss prevention, physical inventory
order: 302
---
# Store physical inventory and shrink

## What this process covers
### Purpose
- Know what each store really has
- Find where shrink comes from
### In scope
- Department, cycle and full-store counts
- Recounts, posting and shrink analysis
### Outcome
- Store book stock that replenishment can trust
- Shrink by cause, store and department

## Stores count, loss prevention reads the result
Layout: swimlane handoffs
- Inventory control: Schedules the store count
- Store team: Counts with handhelds
- Store team: Variance over tolerance?
- Store team: If yes, recount the area
- Store team: If no, submit the count
- Inventory control: Posts the differences
- Loss prevention: Analyses shrink by cause

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Count list | Count lists by department or store | Count document |
| Count | Associates count with handhelds | Counted quantities |
| Differences | Approved differences adjust stock | Inventory adjustment |
| Value of shrink | Shrink by store, department and cause | Shrink report |
| Follow-up | Action plans for high-shrink stores | Loss prevention case |

## Five steps turn a physical count into accurate stock
Layout: retail inventory-count

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Count freeze | Sales and receipts cut off for the count | Store manager |
| Third-party count | Full-store counts by an independent team | Loss prevention |
| Recount rule | Departments over tolerance recounted | Inventory control |
| Shrink sign-off | Store shrink results signed by the district | District manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Shrink rate | Loss as a share of sales | Adjustments vs sales |
| Store inventory accuracy | Items whose count matched the book | Count results |
| Known vs unknown shrink | Shrink with and without a recorded cause | Recorded damage vs count loss |
| Count completion | Planned store counts done on time | Count schedule |

## Today and target
### Today
- One full count a year per store
- Shrink reported as one number
### Target
- Cycle counts on high-risk departments
- Shrink split by cause: damage, theft, process
