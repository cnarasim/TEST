# SAP AI for Retail — hands-on starter

A small, **dependency-free** Python project that teaches the core ideas of
**SAP Business AI** by building two of the most common retail use cases and
mapping every piece back to the real SAP services (SAP AI Core, Generative
AI Hub, Customer Activity Repository).

It runs **100% locally with the Python standard library** — no `pip
install`, no SAP account, no network. You learn the *shape* of an SAP AI
workflow first; `docs/04` shows how to go live on SAP BTP when you're ready.

## What's inside

| Use case | What it does | Real SAP analog |
|----------|--------------|-----------------|
| **Demand forecasting** | Fits a trend + weekly-seasonality model per store/product and forecasts future unit sales. | SAP **Unified Demand Forecast** (in Customer Activity Repository) |
| **GenAI product enrichment** | Auto-generates product descriptions and categories from sparse catalog data. | SAP **Generative AI Hub** (in SAP AI Core) |

The code is deliberately named after SAP AI Core's vocabulary
(scenario / execution / artifact / deployment / resource group) so the
concepts stick. See `docs/`.

## Quickstart

```bash
# Run the whole flow: ingest -> train -> GenAI enrich
python3 -m sap_ai_retail pipeline

# Just the forecast for one store/product (note the weekend peaks!)
python3 -m sap_ai_retail forecast --store STORE-ONLINE --sku SKU-1004 --horizon 7

# Just the GenAI catalog enrichment (offline mock by default)
python3 -m sap_ai_retail enrich

# (Re)generate the synthetic sales dataset
python3 -m sap_ai_retail generate-data

# Run the tests
python3 -m unittest discover -s tests
```

Requires only Python 3.9+ (developed on 3.11). No third-party packages.

## Project layout

```
sap_ai_retail/
  data.py               synthetic POS sales  (analog: CAR / Demand Data Foundation)
  forecasting.py        demand model         (analog: Unified Demand Forecast)
  genai_hub.py          LLM gateway + mock   (analog: Generative AI Hub SDK)
  product_enrichment.py GenAI catalog copy
  pipeline.py           ties it together     (analog: an AI Core scenario)
  cli.py / __main__.py  command-line entry point
tests/                  stdlib unittest suite
docs/
  01-sap-business-ai.md     concepts: BTP, AI Core, Launchpad, Gen AI Hub, Joule
  02-sap-retail.md          S/4HANA Retail, CAR/UDF, Commerce Cloud + where AI fits
  03-architecture-mapping.md  this demo  <->  real SAP AI Core, side by side
  04-going-live-on-btp.md     real setup steps on an SAP BTP trial
data/retail_sales.csv     generated sample data (committed for convenience)
```

## Suggested learning path

1. **Read `docs/01`** for the SAP Business AI landscape (10 min).
2. **Run `python3 -m sap_ai_retail pipeline`** and watch the three stages.
3. **Read the code** in `sap_ai_retail/`, matching it to the vocabulary.
4. **Read `docs/02` and `docs/03`** to connect it to real SAP retail + AI Core.
5. **Optional:** follow `docs/04` to run the GenAI half against a real
   model on an SAP BTP trial (flip `--provider sap`).

> This is a learning scaffold, not production code. The forecaster and the
> GenAI "model" are intentionally tiny and transparent so every line is
> readable. The value is the end-to-end *shape* and the SAP mapping.
