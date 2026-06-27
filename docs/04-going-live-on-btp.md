# 04 — Going live on SAP BTP (optional next step)

This project runs fully offline. When you're ready to touch the *real* SAP
services, here's the path. None of it is required to learn from the code.

> Heads-up: exact console wording and free-tier availability change over
> time. Always confirm against current SAP Help Portal / SAP Discovery
> Center docs. Treat the steps below as the shape, not gospel.

## 0. Get an account
- Sign up for an **SAP BTP trial** (free) or use a **BTP free-tier** global
  account. You'll land in the **BTP Cockpit**.

## 1. Entitlements + instances
In the BTP Cockpit, add entitlements and create instances for:
- **SAP AI Core** (the runtime) — pick the free/`standard`-style plan if
  available on trial.
- **SAP AI Launchpad** (the UI) — subscribe to the SaaS app.

Then create a **service key** for AI Core. It contains the credentials your
SDK needs (client id/secret, token URL, AI API URL).

## 2. Configure local credentials
The SDKs read `AICORE_*` environment variables (or a config file). From the
service key:

```bash
export AICORE_AUTH_URL="https://<your-subaccount>.authentication.<region>.hana.ondemand.com"
export AICORE_CLIENT_ID="<clientid>"
export AICORE_CLIENT_SECRET="<clientsecret>"
export AICORE_BASE_URL="https://api.ai.<region>.aws.ml.hana.ondemand.com/v2"
export AICORE_RESOURCE_GROUP="default"
```

Install the SDKs (do this in a real venv, not this offline repo):

```bash
pip install ai-core-sdk generative-ai-hub-sdk
```

## 3. Generative AI Hub — the quickest win
1. In AI Launchpad / AI Core, create a **deployment** for a foundation
   model (e.g. `gpt-4o`) in the Generative AI Hub.
2. Then this project's GenAI path calls it directly — just flip the
   provider:

   ```bash
   export GENAI_PROVIDER=sap
   python3 -m sap_ai_retail enrich --provider sap
   ```

   `SapGenAIHubProvider` in `genai_hub.py` lazily imports
   `gen_ai_hub.proxy.native.openai` and calls the real model. Your
   `product_enrichment.py` code is unchanged.

## 4. Forecasting as a real AI Core scenario (bigger lift)
To run the forecasting half for real, you'd:
1. Put your **training code** (today's `forecasting.py`, beefed up) in a
   **Docker image**, push it to a registry AI Core can read.
2. Write an **Argo workflow template** (training) + a **serving template**
   (KServe) and commit them to a **Git repo**.
3. Register **connections** (Git, Docker, object store) in AI Core.
4. Create a **configuration**, run an **execution** (training), inspect
   metrics, then create a **deployment** (serving).
5. Drive it all with `ai-core-sdk` or the AI Launchpad UI.

This is exactly the seven-noun model from `03-architecture-mapping.md`,
now backed by real infrastructure.

## 5. Where to learn more
- **SAP Help Portal** — "SAP AI Core" and "Generative AI Hub".
- **SAP Discovery Center** — service pages with "Get Started" missions.
- **SAP Customer Activity Repository / Unified Demand Forecast** docs — the
  production version of the forecasting use case.
- **SAP Developer Tutorials** (developers.sap.com) — hands-on AI Core /
  Gen AI Hub walkthroughs.

When network access and an account are available, ask me to help wire up
any one of these steps concretely.
