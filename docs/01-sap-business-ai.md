# 01 — SAP Business AI, in plain terms

This is the conceptual half of the project. Read it once, then look at the
code — the modules are named to match these terms.

## The big picture

**SAP Business AI** is SAP's umbrella brand for AI across its whole
portfolio. It comes in three flavors:

1. **Embedded AI** — AI features baked directly into SAP apps (S/4HANA,
   SuccessFactors, Ariba, Concur, SAP Commerce Cloud…). You don't build
   it; you switch it on. Example: predictive accruals, lead scoring.
2. **Joule** — SAP's generative-AI *copilot*. A natural-language assistant
   embedded across SAP apps that can answer questions, navigate, and
   increasingly *take actions* (agentic workflows) on your behalf.
3. **Custom AI on SAP BTP** — when you want to build/extend your own
   models and LLM apps. This is where **SAP AI Core**, **SAP AI
   Launchpad**, and the **Generative AI Hub** live. **This project is a
   local rehearsal of this third flavor.**

## SAP BTP — the platform underneath

**SAP Business Technology Platform (BTP)** is SAP's cloud platform (think:
SAP's equivalent of a hyperscaler's app platform) for extending and
integrating SAP. The AI services run as BTP services. To follow along for
real you'd use a **BTP account** (a free *BTP trial* or *BTP free tier*
works to start).

## The three custom-AI building blocks

### SAP AI Core
The runtime. A Kubernetes-based service that **trains** and **serves**
models. Key nouns you'll meet (and which this repo mirrors in
`pipeline.py`):

| Concept            | Meaning                                                        |
|--------------------|----------------------------------------------------------------|
| **Scenario**       | A named ML use case (e.g. "demand-forecast").                  |
| **Workflow / Executable** | A pipeline template (an Argo workflow for training, or a KServe serving template), stored in **Git**. |
| **Configuration**  | Binds a workflow + parameters + input data for a run.          |
| **Execution**      | One training run. Produces a model **artifact**.               |
| **Deployment**     | A running inference endpoint serving a model.                  |
| **Resource group** | Tenant/isolation boundary inside one AI Core instance.         |
| **Connections**    | Pointers to your **Git** repo, **Docker** registry, and **object store** (S3) where data + models live. |

The mental model: *AI Core is GitOps for ML.* You describe training and
serving as templates in Git; AI Core executes them on Kubernetes.

### SAP AI Launchpad
The **UI / control tower** (a BTP SaaS app) to manage AI Core — browse
scenarios, launch executions, watch deployments, manage prompts — often
across several AI runtimes at once.

### Generative AI Hub
The **LLM gateway** inside AI Core/Launchpad. One governed entry point to
many **foundation models** (OpenAI, Anthropic, Google, plus open-source),
with extras enterprises need:

- **Prompt management** (versioned, reusable prompts)
- **Orchestration** (templating, model routing, **grounding/RAG**)
- **Data masking** (strip PII before it hits a model)
- **Content filtering** (block unsafe in/out)

Python access is via the **`generative-ai-hub-sdk`** package
(`gen_ai_hub.proxy.*`). In this repo, `genai_hub.py` mimics its shape with
an offline mock so it runs with no account.

## Where retail fits

See `02-sap-retail.md`. The short version: SAP's retail products generate
exactly the data (POS sales, catalogs, customers) that these AI services
turn into forecasts, recommendations, and generated content. This project
demos two of those: **demand forecasting** and **GenAI catalog
enrichment**.

## A 4-step learning path

1. **Run it.** `python3 -m sap_ai_retail pipeline` — see ingest → train →
   GenAI end to end.
2. **Read the code** in `sap_ai_retail/`, matching each module to the
   nouns above.
3. **Map it to SAP** with `03-architecture-mapping.md`.
4. **Go live** (optional) with `04-going-live-on-btp.md` on a BTP trial.
