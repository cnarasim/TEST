# 03 — How this demo maps to real SAP AI Core

Side-by-side: the local code vs. what you'd actually wire up on SAP BTP.

## The forecasting scenario (classic ML)

```
LOCAL (this repo)                      SAP AI CORE
------------------------------------   ------------------------------------
data.generate_sales()              ->  POS data landing in CAR / object
data/retail_sales.csv                  store (S3) registered as a DATASET
                                       artifact + CONNECTION

forecasting.DemandForecaster.fit() ->  Training code in a Docker image,
(called by                             described by an Argo WORKFLOW
 run_training_execution)                template in Git -> an EXECUTION
                                       produces a MODEL artifact

forecasting.backtest()             ->  Offline metrics logged to the
                                       execution; gate before promotion

pipeline.serve_forecast()          ->  A DEPLOYMENT: a KServe server
                                       exposing an inference endpoint

cli.py subcommands                 ->  ai-core-sdk / ai_api_client_sdk
                                       (or the AI Launchpad UI)

tenant="default" argument          ->  RESOURCE GROUP
```

### What the real training container looks like
Same three moves your `run_training_execution` makes, just containerized:

1. **Read inputs** from the mounted object-store path (your CSV → a
   parquet dataset).
2. **Fit + evaluate** (your `DemandForecaster` → e.g. gradient boosting,
   SAP HANA PAL, or a time-series library).
3. **Write the model artifact** back to the object store so a deployment
   can load it.

AI Core runs that container as an **execution** defined by an Argo
**workflow template** committed to a **Git** repo it syncs from.

## The GenAI scenario (Generative AI Hub)

```
LOCAL (this repo)                      SAP GENERATIVE AI HUB
------------------------------------   ------------------------------------
genai_hub.GenAIHubClient (mock)    ->  gen_ai_hub.proxy.* SDK
client.complete(system, user)      ->  chat.completions.create(...)
product_enrichment.SYSTEM_PROMPT   ->  a managed PROMPT (versioned in
 + *_prompt() builders                 the Prompt Registry / Orchestration)
MockProvider                       ->  a real FOUNDATION MODEL deployment
                                       (e.g. gpt-4o) you create in AI Core
(none yet)                         ->  GROUNDING (RAG), DATA MASKING,
                                       CONTENT FILTERING in orchestration
```

The whole point of `GenAIHubClient` is that **only the provider changes**.
`provider="mock"` runs offline; `provider="sap"` calls the real hub once
the SDK + credentials are present (`SapGenAIHubProvider`). Your business
code (`product_enrichment.py`) never changes.

## The vocabulary cheat-sheet

- **Scenario** = use case. We have two: demand-forecast, catalog-enrichment.
- **Execution** = a training run (ours: `run_training_execution`).
- **Artifact** = an input dataset or an output model.
- **Deployment** = a live inference endpoint (ours: `serve_forecast`).
- **Configuration** = the recipe (workflow + params + inputs) for a run.
- **Resource group** = tenant isolation (ours: the `tenant` arg).
- **Connection** = link to Git / Docker registry / object store.

Once these seven nouns feel obvious, the AI Core console and SDK stop being
mysterious — they're just CRUD over exactly these.
