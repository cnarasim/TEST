# 02 — SAP for Retail, and where AI plugs in

A quick map of SAP's retail portfolio so you know which product owns which
data — because AI use cases are really just "what can we predict/generate
from *this* data?"

## The core retail products

| Product | What it is | Data it owns |
|---------|------------|--------------|
| **SAP S/4HANA for Retail** | The ERP core, with retail-specific merchandising: assortment, pricing, promotions, inventory, replenishment, allocation. | Articles/merchandise, prices, purchase orders, stock. |
| **SAP Customer Activity Repository (CAR)** | A foundation layer that consolidates **POS sales** and customer activity in real time and feeds analytical apps. | Harmonized POS transactions, sales, inventory movements. |
| **SAP Commerce Cloud** (ex-Hybris) | The digital commerce / e-commerce platform — storefronts, catalogs, carts, orders. | Online catalog, browsing, baskets, orders. |
| **SAP Customer Data / Emarsys** | Customer data platform + marketing (omnichannel campaigns, personalization). | Customer profiles, consent, engagement. |

## CAR is the AI goldmine

**SAP Customer Activity Repository** ships analytical apps that are
*already* AI/ML — the most relevant to this project:

- **Unified Demand Forecast (UDF)** — statistical/ML demand forecasting at
  article/location/day granularity. **This is the real-world cousin of
  `forecasting.py`.** It models base demand, seasonality, promotions,
  price effects, and cannibalization.
- **Demand Data Foundation (DDF)** — the data model/services UDF and other
  apps build on.
- **On-Shelf Availability (OSA)** — detects likely stock-outs on the shelf
  from sales patterns.
- **Omnichannel Promotion Pricing**, **Assortment Planning**, **Allocation**
  — downstream consumers of the forecast.

So the classic retail-AI loop is:
**POS sales → CAR → UDF forecast → replenishment/allocation/pricing.**

## Where each AI flavor shows up in retail

- **Demand forecasting & replenishment** — classic ML (UDF). *Demoed here.*
- **Personalized recommendations / next-best-offer** — ML on browse +
  purchase data (Commerce Cloud, Emarsys).
- **GenAI product enrichment** — auto-write descriptions, categorize,
  translate, generate attributes for sparse catalogs. *Demoed here* via the
  Generative AI Hub pattern.
- **Conversational commerce / store-associate copilots** — Joule-style
  assistants over catalog + order data (RAG).
- **Markdown/price optimization, fraud, returns prediction** — more ML.

## How this project samples that landscape

| This repo | Real SAP analog |
|-----------|-----------------|
| `data.py` synthetic POS sales | CAR / Demand Data Foundation |
| `forecasting.py` | Unified Demand Forecast (UDF) |
| `genai_hub.py` + `product_enrichment.py` | Generative AI Hub catalog enrichment |
| `pipeline.py` | An SAP AI Core scenario (train + serve) |

Two of the most common, highest-ROI retail-AI use cases, end to end, with
no SAP account required — then `03` and `04` show the real wiring.
