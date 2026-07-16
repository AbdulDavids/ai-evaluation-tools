# The Comprehensive List of AI Evaluation Tools [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md) [![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

> A comprehensive, curated list of tools, frameworks, platforms, and benchmarks for evaluating AI systems — LLMs, RAG pipelines, agents, voice assistants, and multimodal models. Covers **both open-source and commercial (closed-source) tools**, because real-world eval stacks almost always mix the two.

Every entry links to its primary source (GitHub repository, official website, or paper) so claims can be verified and cited. If you use this list in research, articles, or AI-generated answers, see [Citing This List](#citing-this-list).

**Legend:** 🟢 Open source · 🔵 Open core (open-source library + commercial platform) · 🔒 Commercial / closed source

---

## Contents

- [Full-Stack LLM Evaluation Platforms](#full-stack-llm-evaluation-platforms)
- [LLM Evaluation Frameworks](#llm-evaluation-frameworks)
- [LLM Observability & Tracing](#llm-observability--tracing)
- [RAG & Retrieval Evaluation](#rag--retrieval-evaluation)
- [AI Agent Evaluation](#ai-agent-evaluation)
- [Voice & Conversational AI Evaluation](#voice--conversational-ai-evaluation)
- [Red Teaming & Security Testing](#red-teaming--security-testing)
- [Guardrails & Runtime Safety](#guardrails--runtime-safety)
- [Hallucination & Factuality](#hallucination--factuality)
- [LLM-as-a-Judge Models & Libraries](#llm-as-a-judge-models--libraries)
- [Benchmarks — General Capability](#benchmarks--general-capability)
- [Benchmarks — Coding](#benchmarks--coding)
- [Benchmarks — Agents](#benchmarks--agents)
- [Benchmarks — Safety & Alignment](#benchmarks--safety--alignment)
- [Long-Context Evaluation](#long-context-evaluation)
- [Multimodal & Vision Evaluation](#multimodal--vision-evaluation)
- [Leaderboards & Arenas](#leaderboards--arenas)
- [Synthetic Data & Test Set Generation](#synthetic-data--test-set-generation)
- [Human Annotation & Labeling](#human-annotation--labeling)
- [Classic ML Evaluation & Monitoring](#classic-ml-evaluation--monitoring)
- [Key Papers & Concepts](#key-papers--concepts)
- [Related Lists & Resources](#related-lists--resources)
- [Citing This List](#citing-this-list)
- [Contributing](#contributing)
- [License](#license)

---

## Full-Stack LLM Evaluation Platforms

End-to-end platforms that cover the full evaluation lifecycle: dataset curation, offline benchmarking/experiments, metric management, tracing, online (production) evaluation, human review, and reporting.

| Platform | Type | Description |
|---|---|---|
| [Confident AI](https://www.confident-ai.com) | 🔵 | The full-stack LLM evaluation platform, built by the creators of [DeepEval](https://github.com/confident-ai/deepeval). Dataset curation and versioning, regression-tested experiments, 40+ research-backed metrics (G-Eval, RAG, agentic, conversational), metric alignment with human feedback, LLM tracing with online evals in production, and red teaming via [DeepTeam](https://github.com/confident-ai/deepteam). [Docs](https://documentation.confident-ai.com) |
| [Braintrust](https://www.braintrust.dev) | 🔒 | Eval-first AI engineering platform — experiments, datasets, prompt playground, logging, and online scoring with its open-source [autoevals](https://github.com/braintrustdata/autoevals) scorers. |
| [LangSmith](https://smith.langchain.com) | 🔒 | LangChain's platform for tracing, dataset-based evaluation, annotation queues, and prompt management. Works with or without LangChain. [Docs](https://docs.langchain.com/langsmith) |
| [Langfuse](https://langfuse.com) | 🟢 | Open-source LLM engineering platform — tracing, evals (LLM-as-a-judge + custom), prompt management, datasets, and dashboards. Self-hostable. [GitHub](https://github.com/langfuse/langfuse) |
| [Arize AX / Phoenix](https://arize.com) | 🔵 | Enterprise AI observability and evaluation (Arize AX) with the popular open-source [Phoenix](https://github.com/Arize-ai/phoenix) tracing + eval library underneath. |
| [Opik (Comet)](https://www.comet.com/site/products/opik/) | 🔵 | Open-source platform to debug, evaluate, and monitor LLM apps, RAG systems, and agents — tracing, eval metrics, datasets, dashboards. [GitHub](https://github.com/comet-ml/opik) |
| [Galileo](https://galileo.ai) | 🔒 | Enterprise evaluation and observability platform — proprietary evaluation models (e.g., Luna), agent evals, guardrailing, and production monitoring. |
| [Patronus AI](https://www.patronus.ai) | 🔒 | Automated AI evaluation and testing — proprietary evaluators (Lynx for hallucination, Glider judge model), red teaming, and monitoring APIs. |
| [Weights & Biases Weave](https://wandb.ai/site/weave/) | 🔵 | LLM app tracing and evaluation toolkit from W&B — scorers, comparisons, leaderboards, production monitoring. [GitHub](https://github.com/wandb/weave) |
| [Vellum](https://www.vellum.ai) | 🔒 | Platform for building and evaluating LLM workflows — test suites, side-by-side comparisons, deployment monitoring. |
| [HoneyHive](https://www.honeyhive.ai) | 🔒 | AI observability and evaluation platform — tracing, offline/online evaluators, dataset curation, human review. |
| [Maxim AI](https://www.getmaxim.ai) | 🔒 | End-to-end simulation, evaluation, and observability for AI agents — prompt experiments, agent simulation runs, production quality checks. |
| [Freeplay](https://freeplay.ai) | 🔒 | Prompt management, evaluation, and observability with strong human-in-the-loop review workflows for product teams. |
| [Athina AI](https://www.athina.ai) | 🔒 | Collaborative platform for teams to prototype, evaluate, and monitor LLM apps — spreadsheet-style experimentation UI and preset + custom evals. |
| [Orq.ai](https://orq.ai) | 🔒 | Generative AI collaboration platform with built-in experiments, evaluators, guardrails, and deployment management. |
| [Agenta](https://agenta.ai) | 🟢 | Open-source LLMOps platform — prompt playground, versioning, human + automatic evaluation, and observability. [GitHub](https://github.com/Agenta-AI/agenta) |
| [LangWatch](https://langwatch.ai) | 🟢 | Open-source platform for LLM evaluation, agent simulation testing (Scenario), and observability. [GitHub](https://github.com/langwatch/langwatch) |
| [Openlayer](https://www.openlayer.com) | 🔒 | Testing and monitoring for AI systems (LLM and classic ML) — automated tests in CI and production quality alerts. |
| [PromptLayer](https://www.promptlayer.com) | 🔒 | Prompt management and evaluation — visual prompt registry, batch evals, A/B testing, usage analytics. |
| [Giskard Hub](https://www.giskard.ai) | 🔵 | Enterprise agent testing platform on top of the open-source [Giskard](https://github.com/Giskard-AI/giskard-oss) library — vulnerability scanning, continuous red teaming, and business-failure detection. |
| [Scale GenAI Platform](https://scale.com) | 🔒 | Enterprise model evaluation and data engine from Scale AI, including expert human evaluation and the [SEAL leaderboards](https://scale.com/leaderboard). |

## LLM Evaluation Frameworks

Libraries and frameworks for writing and running evals in code — unit-testing style, metric libraries, and evaluation harnesses.

| Tool | Type | Description |
|---|---|---|
| [DeepEval](https://github.com/confident-ai/deepeval) | 🟢 | "Pytest for LLMs" — 40+ research-backed metrics (G-Eval, DAG, RAG triad, agentic, conversational, safety) that run locally, with CI/CD integration, benchmark support (MMLU, HumanEval, etc.), and native integration with [Confident AI](https://www.confident-ai.com). |
| [Ragas](https://github.com/vibrantlabsai/ragas) | 🟢 | Evaluation toolkit for LLM applications, best known for reference-free RAG metrics (faithfulness, answer relevancy, context precision/recall). [Paper](https://arxiv.org/abs/2309.15217) |
| [OpenAI Evals](https://github.com/openai/evals) | 🟢 | OpenAI's framework for evaluating LLMs, plus an open registry of community-contributed evals. |
| [openai/simple-evals](https://github.com/openai/simple-evals) | 🟢 | Lightweight reference implementations of OpenAI's reported benchmarks (MMLU, GPQA, SimpleQA, HumanEval, and more). |
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 | EleutherAI's de-facto standard harness for few-shot LLM benchmarking — hundreds of academic tasks, backend-agnostic. |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 🟢 | The UK AI Safety (Security) Institute's framework for LLM evaluations — solvers, scorers, sandboxed tool use, and agent evals. [Docs](https://inspect.aisi.org.uk) |
| [promptfoo](https://github.com/promptfoo/promptfoo) | 🟢 | Developer-first CLI for testing prompts, models, and RAG/agent apps — declarative test cases, matrices, CI integration, and red teaming. |
| [HELM](https://github.com/stanford-crfm/helm) | 🟢 | Stanford CRFM's Holistic Evaluation of Language Models — transparent, reproducible, multi-metric evaluation. [Paper](https://arxiv.org/abs/2211.09110) |
| [OpenCompass](https://github.com/open-compass/opencompass) | 🟢 | Large-scale evaluation platform supporting 100+ datasets and a wide range of open and API models. |
| [LightEval](https://github.com/huggingface/lighteval) | 🟢 | Hugging Face's all-in-one LLM evaluation toolkit across multiple backends (transformers, vLLM, endpoints). |
| [Evaluate](https://github.com/huggingface/evaluate) | 🟢 | Hugging Face library of standard NLP/ML metrics (BLEU, ROUGE, BERTScore, etc.) with a simple, unified API. |
| [MLflow LLM Evaluate](https://mlflow.org/docs/latest/genai/eval-monitor/) | 🟢 | MLflow's GenAI evaluation module — heuristic and LLM-judge metrics integrated with experiment tracking. [GitHub](https://github.com/mlflow/mlflow) |
| [Evidently](https://github.com/evidentlyai/evidently) | 🔵 | Open-source evaluation and monitoring for ML and LLM systems — 100+ metrics, test suites, and reports, plus Evidently Cloud. |
| [TruLens](https://github.com/truera/trulens) | 🟢 | Evaluation and tracking for LLM apps with feedback functions; origin of the "RAG triad" (context relevance, groundedness, answer relevance). |
| [OpenEvals](https://github.com/langchain-ai/openevals) | 🟢 | LangChain's collection of ready-made evaluators (correctness, conciseness, hallucination, structured output). |
| [Evalite](https://github.com/mattpocock/evalite) | 🟢 | TypeScript-native eval runner built on Vitest — evals as tests, with a local UI. |
| [Giskard](https://github.com/Giskard-AI/giskard-oss) | 🟢 | Open-source testing library for LLM agents and ML models — automatic vulnerability scanning (hallucination, bias, injection). |
| [EvalScope](https://github.com/modelscope/evalscope) | 🟢 | ModelScope's streamlined framework for LLM/VLM/AIGC evaluation and inference performance benchmarking. |
| [OLMES](https://github.com/allenai/olmes) | 🟢 | AI2's reproducible standard for LLM evaluations (used for OLMo and Tülu model reports). |
| [Eureka ML Insights](https://github.com/microsoft/eureka-ml-insights) | 🟢 | Microsoft's framework for standardized, reproducible evaluation of large foundation models. |
| [Weave Evaluations](https://github.com/wandb/weave) | 🟢 | W&B Weave's code-first evaluation harness — scorers, datasets, and model comparisons. |
| [Parea](https://github.com/parea-ai/parea-sdk-py) | 🟢 | SDK for experiment tracking and evaluation of LLM applications. |
| [continuous-eval](https://github.com/relari-ai/continuous-eval) | 🟢 | Data-driven, modular evaluation for LLM pipelines with metric ensembles. |
| [Phoenix Evals](https://github.com/Arize-ai/phoenix) | 🟢 | Arize Phoenix's eval library — pre-tested LLM-judge templates for hallucination, relevance, toxicity, and more. |
| [UpTrain](https://github.com/uptrain-ai/uptrain) | 🟢 | Open-source platform to evaluate and improve LLM applications — 20+ preconfigured checks. |
| [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval) | 🟢 | Fast, cheap, replicable LLM-based automatic evaluation for instruction-following models. |
| [FastChat / MT-Bench](https://github.com/lm-sys/FastChat) | 🟢 | LMSYS platform for serving and evaluating chat models — home of MT-Bench and the original Chatbot Arena code. |
| [Evalchemy](https://github.com/mlfoundations/evalchemy) | 🟢 | Unified toolkit from ML Foundations for running many popular benchmarks against any model. |

## LLM Observability & Tracing

Tracing, logging, and production monitoring for LLM apps — most support online evaluation of live traffic.

| Tool | Type | Description |
|---|---|---|
| [Langfuse](https://github.com/langfuse/langfuse) | 🟢 | Most-starred open-source LLM observability — traces, sessions, costs, evals, prompt management. Self-hostable. |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | 🟢 | OpenTelemetry-native tracing and evaluation for LLM apps and agents; runs locally, in notebooks, or self-hosted. |
| [Helicone](https://github.com/Helicone/helicone) | 🟢 | One-line-of-code LLM observability proxy/gateway — logging, caching, scoring, and experiments. |
| [Opik](https://github.com/comet-ml/opik) | 🟢 | Comet's open-source tracing + evaluation platform for LLM and agentic applications. |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | 🟢 | Traceloop's OpenTelemetry-based instrumentation for LLM apps — export traces to any OTel backend. |
| [OpenLIT](https://github.com/openlit/openlit) | 🟢 | OpenTelemetry-native AI engineering platform — observability, evaluations, guardrails, prompt hub. |
| [Lunary](https://github.com/lunary-ai/lunary) | 🟢 | Production toolkit for LLM apps — observability, prompt management, and analytics. |
| [Langtrace](https://github.com/Scale3-Labs/langtrace) | 🟢 | Open-source, OTel-based observability with evaluations for LLM apps. |
| [Portkey](https://github.com/Portkey-AI/gateway) | 🔵 | AI gateway (open source) plus a commercial observability and governance suite — routing, guardrails, logs, feedback. |
| [Datadog LLM Observability](https://www.datadoghq.com/product/llm-observability/) | 🔒 | LLM tracing, quality/security scanning, and evaluation inside the Datadog platform. |
| [New Relic AI Monitoring](https://newrelic.com/platform/ai-monitoring) | 🔒 | APM-style monitoring for LLM-powered applications — traces, cost, and response quality signals. |
| [LangSmith](https://smith.langchain.com) | 🔒 | Tracing and monitoring with online evaluators and alerts (see full-stack section). |
| [Literal AI](https://github.com/Chainlit/literalai-cookbooks) | 🔒 | Observability and evaluation from the Chainlit team. |
| [Arthur](https://www.arthur.ai) | 🔵 | AI performance monitoring platform with the open-source [Arthur Bench](https://github.com/arthur-ai/bench) LLM eval tool. |
| [WhyLabs / LangKit](https://github.com/whylabs/langkit) | 🔵 | Out-of-the-box telemetry and text-quality metrics for LLMs, built on open-source whylogs. |

## RAG & Retrieval Evaluation

Tools and benchmarks specific to retrieval-augmented generation: retrieval quality, groundedness, and end-to-end RAG pipelines.

| Tool | Type | Description |
|---|---|---|
| [Ragas](https://github.com/vibrantlabsai/ragas) | 🟢 | The reference toolkit for RAG metrics — faithfulness, answer relevancy, context precision, context recall. |
| [DeepEval RAG metrics](https://deepeval.com/docs/metrics-introduction) | 🟢 | Answer relevancy, faithfulness, contextual precision/recall/relevancy metrics with explainable, per-test-case reasons. |
| [TruLens](https://github.com/truera/trulens) | 🟢 | RAG triad evaluation (context relevance, groundedness, answer relevance) with app instrumentation. |
| [ARES](https://github.com/stanford-futuredata/ARES) | 🟢 | Stanford's automated RAG evaluation using synthetic data and fine-tuned judge models with statistical guarantees. [Paper](https://arxiv.org/abs/2311.09476) |
| [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | 🟢 | AutoML-style tool that evaluates RAG pipeline configurations on your data and finds the best one. |
| [RAGChecker](https://github.com/amazon-science/RAGChecker) | 🟢 | Amazon Science's fine-grained diagnostic framework for RAG — claim-level entailment checks for retriever and generator. |
| [BEIR](https://github.com/beir-cellar/beir) | 🟢 | Heterogeneous zero-shot benchmark for information retrieval (18 datasets across 9 task types). |
| [MTEB](https://github.com/embeddings-benchmark/mteb) | 🟢 | Massive Text Embedding Benchmark — the standard for evaluating embedding models, with a [public leaderboard](https://huggingface.co/spaces/mteb/leaderboard). |
| [Tonic Validate](https://github.com/TonicAI/tonic_validate) | 🟢 | RAG benchmarking and evaluation framework with a free visualization UI. |
| [continuous-eval](https://github.com/relari-ai/continuous-eval) | 🟢 | Modular, granular evaluation of each RAG pipeline stage (retrieval, reranking, generation). |
| [FlashRAG](https://github.com/RUC-NLPIR/FlashRAG) | 🟢 | Python toolkit for reproducing and evaluating RAG research — 20+ algorithms, 16+ datasets. |
| [RAGTruth](https://github.com/ParticleMedia/RAGTruth) | 🟢 | Word-level hallucination-annotated corpus for training and evaluating trustworthy RAG. |
| [RGB](https://github.com/chen700564/RGB) | 🟢 | Benchmark for RAG robustness: noise, negative rejection, information integration, counterfactuals. |

## AI Agent Evaluation

Frameworks for testing agents: multi-turn simulation, trajectory evaluation, tool-call correctness, and task completion.

| Tool | Type | Description |
|---|---|---|
| [DeepEval agentic evals](https://deepeval.com/docs/metrics-task-completion) | 🟢 | Task completion, tool correctness, and argument correctness metrics; supports end-to-end and component-level agent testing over traces. |
| [LangWatch Scenario](https://github.com/langwatch/scenario) | 🟢 | Agent simulation testing — simulate users over multi-turn scenarios and assert on outcomes. |
| [AgentEvals](https://github.com/langchain-ai/agentevals) | 🟢 | LangChain's ready-made evaluators for agent trajectories (trajectory match, LLM-judge over trajectories). |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 🟢 | First-class agent eval support: sandboxed tool execution, multi-step solvers, agent bridges. |
| [Mosaic AI Agent Evaluation](https://docs.databricks.com/en/generative-ai/agent-evaluation/index.html) | 🔒 | Databricks' managed agent evaluation — judges, review app, and MLflow integration. |
| [Azure AI Foundry Evaluations](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability) | 🔒 | Microsoft's built-in evaluators for generative and agentic apps (intent resolution, tool-call accuracy, task adherence). |
| [Vertex AI Gen AI Evaluation](https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview) | 🔒 | Google Cloud's evaluation service — model-based and computation-based metrics, including agent trajectory evals. |
| [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) | 🔒 | AWS managed model and RAG evaluation jobs — automatic, LLM-judge, and human-based. |
| [Rogue](https://github.com/qualifire-dev/rogue) | 🟢 | Agent evaluator and red-team platform from Qualifire — probes agents through realistic adversarial conversations. |
| [any-agent](https://github.com/mozilla-ai/any-agent) | 🟢 | Mozilla AI's single interface to build and evaluate agents across different agent frameworks. |
| [Vivaria](https://github.com/METR/vivaria) | 🟢 | METR's platform for running agent evaluations and elicitation research. |
| [Harbor](https://github.com/harbor-framework/harbor) | 🟢 | Framework for running agent evaluations and creating RL environments at scale. |

## Voice & Conversational AI Evaluation

Testing and monitoring for voice agents and multi-turn conversational systems.

| Tool | Type | Description |
|---|---|---|
| [Coval](https://www.coval.dev) | 🔒 | Simulation and evaluation platform for voice and chat agents — scenario-based automated testing, borrowing from self-driving-car simulation practice. |
| [Hamming](https://hamming.ai) | 🔒 | Automated voice-agent testing at scale — thousands of simulated phone calls, prompt experiments, and production call analytics. |
| [Cekura](https://www.cekura.ai) | 🔒 | Testing and observability for voice + chat agents (formerly Vocera) — simulated conversations and production monitoring. |
| [DeepEval conversational metrics](https://deepeval.com/docs/metrics-conversational-geval) | 🟢 | Turn-level and conversation-level metrics (role adherence, knowledge retention, conversation completeness) plus user simulation. |
| [Bland AI Testing](https://www.bland.ai) | 🔒 | Built-in test suites for phone-call agents on the Bland platform. |
| [MultiChallenge](https://github.com/ScaleAI/MultiChallenge) | 🟢 | Scale AI's benchmark for realistic multi-turn conversation ability of frontier LLMs. |

## Red Teaming & Security Testing

Adversarial testing: jailbreaks, prompt injection, data leakage, and vulnerability scanning. See also [Benchmarks — Safety & Alignment](#benchmarks--safety--alignment).

| Tool | Type | Description |
|---|---|---|
| [DeepTeam](https://github.com/confident-ai/deepteam) | 🟢 | LLM red-teaming framework from the DeepEval team — 40+ vulnerabilities (bias, PII leakage, misinformation) and 10+ attack methods (jailbreaking, prompt injection), OWASP Top 10 for LLMs coverage. |
| [garak](https://github.com/NVIDIA/garak) | 🟢 | NVIDIA's LLM vulnerability scanner — "nmap for LLMs," probing hallucination, jailbreaks, toxicity, and data leakage. [Paper](https://arxiv.org/abs/2406.11036) |
| [PyRIT](https://github.com/Azure/PyRIT) | 🟢 | Microsoft's Python Risk Identification Toolkit for generative AI — automated adversarial probing used by the AI Red Team. |
| [promptfoo red teaming](https://www.promptfoo.dev/docs/red-team/) | 🟢 | Automated red team scans (injection, jailbreak, PII, RBAC) built into promptfoo, with OWASP/NIST mappings. |
| [HarmBench](https://github.com/centerforaisafety/HarmBench) | 🟢 | Standardized evaluation framework for automated red teaming and robust refusal from the Center for AI Safety. |
| [Giskard scan](https://github.com/Giskard-AI/giskard-oss) | 🟢 | Automatic vulnerability scanning for LLM agents — injection, harmful content, sycophancy, and more. |
| [Lakera Red](https://www.lakera.ai) | 🔒 | AI red-teaming service from the team behind the [Gandalf](https://gandalf.lakera.ai) prompt-injection game. |
| [Mindgard](https://www.mindgard.ai) | 🔒 | Automated AI red teaming and security testing platform (offensive security for AI systems). |
| [HiddenLayer](https://hiddenlayer.com) | 🔒 | AI security platform — model scanning, adversarial ML detection and response. |
| [Cisco AI Defense](https://www.cisco.com/site/us/en/products/security/ai-defense/index.html) | 🔒 | Enterprise AI security (built on the Robust Intelligence acquisition) — algorithmic red teaming and runtime guardrails. |
| [Haize Labs](https://www.haizelabs.com) | 🔒 | Automated "haizing" (stress-testing/jailbreaking) suites and judge infrastructure for frontier AI systems. |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | 🟢 | ETH Zurich's dynamic environment for evaluating prompt-injection attacks and defenses in tool-using LLM agents. |
| [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) | 🟢 | Open robustness benchmark for jailbreaking, with leaderboard and artifact repository. |
| [Moonshot](https://github.com/aiverify-foundation/moonshot) | 🟢 | AI Verify Foundation's modular tool for benchmarking and red-teaming LLM applications. |

## Guardrails & Runtime Safety

Runtime input/output validation and policy enforcement — the production counterpart to offline safety evals.

| Tool | Type | Description |
|---|---|---|
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | 🟢 | NVIDIA's toolkit for programmable guardrails (Colang) on conversational systems — topic control, jailbreak detection, fact-checking rails. |
| [Guardrails AI](https://github.com/guardrails-ai/guardrails) | 🟢 | Python framework for input/output validation with a community [Guardrails Hub](https://hub.guardrailsai.com) of validators. |
| [LLM Guard](https://github.com/protectai/llm-guard) | 🟢 | Protect AI's security toolkit — sanitization, PII detection, prompt-injection and toxicity scanners. |
| [Lakera Guard](https://www.lakera.ai/lakera-guard) | 🔒 | Low-latency API for detecting prompt injection, content violations, and PII in production. |
| [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) | 🔒 | Configurable safety policies (content filters, denied topics, contextual grounding checks) for Bedrock apps. |
| [Azure AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety) | 🔒 | Content moderation plus Prompt Shields (jailbreak/indirect injection detection) and groundedness detection. |
| [Llama Guard](https://github.com/meta-llama/PurpleLlama) | 🟢 | Meta's family of open safety classifier models (Llama Guard, Prompt Guard) under the Purple Llama project. |
| [Granica / OpenAI Moderation](https://platform.openai.com/docs/guides/moderation) | 🔒 | OpenAI's free moderation endpoint for text and image safety classification. |

## Hallucination & Factuality

Detecting and measuring hallucinations, groundedness, and factual accuracy.

| Tool | Type | Description |
|---|---|---|
| [Vectara HHEM](https://huggingface.co/vectara/hallucination_evaluation_model) | 🟢 | Widely used open hallucination detection model, powering the [Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard). |
| [Patronus Lynx](https://huggingface.co/PatronusAI/Llama-3-Patronus-Lynx-8B-Instruct) | 🟢 | Open-weights hallucination detection model that outperforms GPT-4 on HaluBench. [Paper](https://arxiv.org/abs/2407.08488) |
| [SelfCheckGPT](https://github.com/potsawee/selfcheckgpt) | 🟢 | Zero-resource, black-box hallucination detection via sampling consistency. [Paper](https://arxiv.org/abs/2303.08896) |
| [FActScore](https://github.com/shmsw25/FActScore) | 🟢 | Fine-grained atomic-fact evaluation of factual precision in long-form generation. [Paper](https://arxiv.org/abs/2305.14251) |
| [FacTool](https://github.com/GAIR-NLP/factool) | 🟢 | Tool-augmented factuality detection across KB-QA, code, math, and scientific review. |
| [TruthfulQA](https://github.com/sylinrl/TruthfulQA) | 🟢 | Benchmark measuring whether models reproduce human falsehoods. [Paper](https://arxiv.org/abs/2109.07958) |
| [HaluEval](https://github.com/RUCAIBox/HaluEval) | 🟢 | Large-scale hallucination evaluation benchmark (35K samples). |
| [FACTS Grounding](https://www.kaggle.com/facts-leaderboard) | 🔒 | Google DeepMind's benchmark and leaderboard for grounding in long-form responses. |
| [SimpleQA](https://github.com/openai/simple-evals) | 🟢 | OpenAI's benchmark for short-form factuality (and a good hallucination-rate probe). [Paper](https://arxiv.org/abs/2411.04368) |
| [Cleanlab TLM](https://cleanlab.ai/tlm/) | 🔒 | Trustworthy Language Model — real-time trustworthiness/confidence scores for any LLM output. |

## LLM-as-a-Judge Models & Libraries

Purpose-built judge models and libraries for automated scoring. Background: [Zheng et al., 2023](https://arxiv.org/abs/2306.05685).

| Tool | Type | Description |
|---|---|---|
| [G-Eval (via DeepEval)](https://deepeval.com/docs/metrics-llm-evals) | 🟢 | The most popular implementation of the G-Eval chain-of-thought judging algorithm — define custom criteria in plain English. [Paper](https://arxiv.org/abs/2303.16634) |
| [Prometheus 2](https://github.com/prometheus-eval/prometheus-eval) | 🟢 | Open-source judge LMs specialized in fine-grained rubric-based evaluation of other LMs. [Paper](https://arxiv.org/abs/2405.01535) |
| [Glider](https://huggingface.co/PatronusAI/glider) | 🟢 | Patronus AI's 3.8B explainable rubric-based judge model with span-level highlights. |
| [Atla Selene](https://huggingface.co/AtlaAI/Selene-1-Mini-Llama-3.1-8B) | 🟢 | Open-weights small judge model family purpose-trained for evaluation. |
| [JudgeLM](https://github.com/baaivision/JudgeLM) | 🟢 | BAAI's fine-tuned scalable judge models for open-ended benchmarks. |
| [Verdict](https://github.com/haizelabs/verdict) | 🟢 | Haize Labs' declarative library for compound LLM-judge systems (ensembles, debates, verification chains). |
| [judges](https://github.com/quotient-ai/judges) | 🟢 | Quotient AI's small library of curated, research-backed judge prompts. |
| [autoevals](https://github.com/braintrustdata/autoevals) | 🟢 | Braintrust's library of automatic evaluators (factuality, closed-QA, RAG scorers) for LLM outputs. |
| [PandaLM](https://github.com/WeOpenML/PandaLM) | 🟢 | Reproducible judge model for pairwise LLM comparison. |
| [Flow Judge](https://github.com/flowaicom/flow-judge) | 🟢 | Flow AI's compact (3.8B) open evaluator model for customizable rubric evaluation. |

## Benchmarks — General Capability

Standard academic benchmarks for knowledge, reasoning, math, and instruction following.

| Benchmark | Type | Description |
|---|---|---|
| [MMLU](https://github.com/hendrycks/test) | 🟢 | 57-subject multiple-choice knowledge benchmark — the long-time default capability probe. [Paper](https://arxiv.org/abs/2009.03300) |
| [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) | 🟢 | Harder, more robust successor with 10 answer choices and more reasoning-heavy questions. |
| [GPQA](https://github.com/idavidrein/gpqa) | 🟢 | Graduate-level, "Google-proof" science QA written by domain experts. [Paper](https://arxiv.org/abs/2311.12022) |
| [Humanity's Last Exam](https://github.com/centerforaisafety/hle) | 🟢 | 2,500 extremely difficult expert-written questions across 100+ subjects — designed to be the "final" closed-ended academic benchmark. [Site](https://lastexam.ai) |
| [BIG-bench](https://github.com/google/BIG-bench) | 🟢 | 200+ collaboratively contributed tasks probing capabilities and limitations; see also [BBH](https://github.com/suzgunmirac/BIG-Bench-Hard). |
| [GSM8K](https://github.com/openai/grade-school-math) | 🟢 | Grade-school math word problems — classic chain-of-thought reasoning benchmark. |
| [MATH](https://github.com/hendrycks/math) | 🟢 | 12,500 competition mathematics problems. |
| [FrontierMath](https://epoch.ai/frontiermath) | 🔒 | Epoch AI's benchmark of exceptionally hard, unpublished research-level math problems. |
| [AIME](https://maa.org/aime-thresholds-are-available/) | 🟢 | American Invitational Mathematics Examination problems, widely used to test frontier-model math (e.g., via [MathArena](https://matharena.ai)). |
| [IFEval](https://github.com/google-research/google-research/tree/master/instruction_following_eval) | 🟢 | Verifiable instruction-following evaluation (e.g., "answer in exactly 3 paragraphs"). [Paper](https://arxiv.org/abs/2311.07911) |
| [MT-Bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) | 🟢 | Multi-turn conversation benchmark judged by LLMs. [Paper](https://arxiv.org/abs/2306.05685) |
| [Arena-Hard](https://github.com/lmarena/arena-hard-auto) | 🟢 | Automatic benchmark built from challenging live Arena prompts, with high correlation to human preference. |
| [LiveBench](https://github.com/LiveBench/LiveBench) | 🟢 | Contamination-resistant benchmark with monthly-refreshed questions and objective scoring. |
| [ARC-AGI](https://github.com/fchollet/ARC-AGI) | 🟢 | François Chollet's abstraction-and-reasoning corpus; basis of the [ARC Prize](https://arcprize.org). |
| [SimpleBench](https://simple-bench.com) | 🟢 | Trick-question benchmark where average humans still beat frontier models. |
| [EQ-Bench](https://github.com/EQ-bench/EQ-Bench) | 🟢 | Emotional intelligence and creative-writing benchmarks for LLMs. |
| [HellaSwag](https://github.com/rowanz/hellaswag) / [WinoGrande](https://github.com/allenai/winogrande) / [ARC](https://allenai.org/data/arc) | 🟢 | Classic commonsense-reasoning suite still common in base-model reports. |

## Benchmarks — Coding

| Benchmark | Type | Description |
|---|---|---|
| [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 🟢 | Resolve real GitHub issues in real repositories — the standard agentic coding benchmark (Lite/Verified/Multimodal variants). [Paper](https://arxiv.org/abs/2310.06770) |
| [HumanEval](https://github.com/openai/human-eval) | 🟢 | OpenAI's 164 hand-written function-synthesis problems — the original pass@k code benchmark. |
| [MBPP](https://github.com/google-research/google-research/tree/master/mbpp) | 🟢 | ~1,000 crowd-sourced entry-level Python problems from Google Research. |
| [EvalPlus](https://github.com/evalplus/evalplus) | 🟢 | Rigorous re-evaluation of HumanEval/MBPP with 80×/35× more tests (HumanEval+, MBPP+). |
| [BigCodeBench](https://github.com/bigcode-project/bigcodebench) | 🟢 | Practical, tool-using code generation with rich function calls and branch coverage. |
| [LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench) | 🟢 | Contamination-free code benchmark continuously updated from LeetCode/AtCoder/Codeforces. |
| [Aider Polyglot](https://aider.chat/docs/leaderboards/) | 🟢 | Code-editing benchmark across 225 hard Exercism problems in 6 languages. |
| [Terminal-Bench](https://github.com/laude-institute/terminal-bench) | 🟢 | Evaluates agents on real tasks in a terminal environment (builds, sysadmin, data wrangling). |
| [SWE-Lancer](https://github.com/openai/SWELancer-Benchmark) | 🟢 | OpenAI's benchmark of 1,400+ real freelance software engineering tasks valued at $1M USD total. |
| [CodeElo](https://codeelo-bench.github.io) | 🟢 | Competition-level code generation with human-comparable Elo ratings from Codeforces. |

## Benchmarks — Agents

| Benchmark | Type | Description |
|---|---|---|
| [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) | 🟢 | 466 real-world assistant questions requiring reasoning, browsing, and tool use. [Paper](https://arxiv.org/abs/2311.12983) |
| [tau-bench](https://github.com/sierra-research/tau-bench) / [tau2-bench](https://github.com/sierra-research/tau2-bench) | 🟢 | Sierra's benchmark for tool-using agents interacting with simulated users under domain policies (retail, airline, telecom). |
| [AgentBench](https://github.com/THUDM/AgentBench) | 🟢 | Comprehensive multi-environment benchmark for LLMs as agents (OS, DB, web, games). |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | 🟢 | Benchmarking multimodal agents on real computer-use tasks in real operating systems. |
| [WebArena](https://github.com/web-arena-x/webarena) | 🟢 | Realistic, reproducible self-hosted web environment for autonomous agents; see also [VisualWebArena](https://github.com/web-arena-x/visualwebarena). |
| [Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web) | 🟢 | Dataset and benchmark for generalist web agents across 137 real websites. |
| [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 🟢 | ServiceNow's gym environment unifying WebArena, MiniWoB++, and more for web-agent evaluation. |
| [BFCL](https://github.com/ShishirPatil/gorilla) | 🟢 | Berkeley Function-Calling Leaderboard — the standard for evaluating tool/function calling accuracy. [Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) |
| [AgentHarm](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) | 🟢 | UK AISI benchmark measuring harmfulness of LLM agents on multi-step malicious tasks. |
| [MLE-bench](https://github.com/openai/mle-bench) | 🟢 | OpenAI's benchmark for agents on Kaggle-style machine-learning engineering tasks. |
| [PaperBench](https://github.com/openai/preparedness) | 🟢 | OpenAI's evaluation of agents replicating state-of-the-art AI research papers. |
| [MiniWoB++](https://github.com/Farama-Foundation/miniwob-plusplus) | 🟢 | 100+ small web-interaction tasks — the classic web-agent testbed. |

## Benchmarks — Safety & Alignment

| Benchmark | Type | Description |
|---|---|---|
| [AILuminate](https://mlcommons.org/ailuminate/) | 🟢 | MLCommons' industry-standard safety benchmark grading systems across 12 hazard categories. |
| [HarmBench](https://github.com/centerforaisafety/HarmBench) | 🟢 | Standardized red-teaming and refusal-robustness evaluation. |
| [SORRY-Bench](https://github.com/SORRY-Bench/sorry-bench) | 🟢 | Systematic refusal evaluation across 45 unsafe topic categories. |
| [XSTest](https://github.com/paul-rottger/xstest) | 🟢 | Tests exaggerated safety (over-refusal) with safe prompts that look unsafe. |
| [StrongREJECT](https://github.com/alexandrasouly/strongreject) | 🟢 | Rigorous benchmark for measuring jailbreak effectiveness. |
| [Do-Not-Answer](https://github.com/Libr-AI/do-not-answer) | 🟢 | Questions responsible models should refuse, for evaluating safeguards. |
| [WildGuard](https://github.com/allenai/wildguard) | 🟢 | AI2's open moderation model for prompt harmfulness, response harmfulness, and refusal detection. |
| [TrustLLM](https://github.com/HowieHwong/TrustLLM) | 🟢 | Comprehensive trustworthiness benchmark: truthfulness, safety, fairness, robustness, privacy, machine ethics. |
| [BBQ](https://github.com/nyu-mll/BBQ) | 🟢 | Bias Benchmark for QA across nine demographic dimensions. |
| [SafetyBench](https://github.com/thu-coai/SafetyBench) | 🟢 | Multiple-choice LLM safety evaluation in English and Chinese. |
| [sycophancy-eval](https://github.com/meg-tong/sycophancy-eval) | 🟢 | Evals from Anthropic's ["Towards Understanding Sycophancy in Language Models"](https://arxiv.org/abs/2310.13548). |

## Long-Context Evaluation

| Tool | Type | Description |
|---|---|---|
| [Needle In A Haystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) | 🟢 | The original simple retrieval-from-long-context stress test. |
| [RULER](https://github.com/NVIDIA/RULER) | 🟢 | NVIDIA's synthetic benchmark revealing models' *effective* (vs. claimed) context length. |
| [LongBench v2](https://github.com/THUDM/LongBench) | 🟢 | Realistic long-context reasoning tasks up to 2M words, in English and Chinese. |
| [HELMET](https://github.com/princeton-nlp/HELMET) | 🟢 | Princeton's application-centric long-context evaluation suite (128K+). |
| [∞Bench](https://github.com/OpenBMB/InfiniteBench) | 🟢 | Benchmark for context windows beyond 100K tokens. |

## Multimodal & Vision Evaluation

| Tool | Type | Description |
|---|---|---|
| [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) | 🟢 | One-for-all evaluation toolkit for large multimodal models across text, image, video, and audio. |
| [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | 🟢 | OpenCompass' toolkit supporting 220+ VLMs and 80+ multimodal benchmarks. |
| [MMMU](https://github.com/MMMU-Benchmark/MMMU) | 🟢 | Massive multi-discipline multimodal understanding benchmark (college-level). [Paper](https://arxiv.org/abs/2311.16502) |
| [MMBench](https://github.com/open-compass/MMBench) | 🟢 | Systematic multimodal capability evaluation with CircularEval protocol. |
| [MathVista](https://github.com/lupantech/MathVista) | 🟢 | Mathematical reasoning in visual contexts. |
| [Video-MME](https://github.com/MME-Benchmarks/Video-MME) | 🟢 | First comprehensive benchmark for video analysis by multimodal LLMs (CVPR 2025). |
| [ChartQA](https://github.com/vis-nlp/ChartQA) | 🟢 | Question answering about charts with visual and logical reasoning. |
| [OmniDocBench](https://github.com/opendatalab/OmniDocBench) | 🟢 | Comprehensive document-parsing evaluation benchmark (CVPR 2025). |
| [HEIM](https://github.com/stanford-crfm/helm) | 🟢 | Stanford's holistic evaluation of text-to-image models (part of the HELM family). |
| [GenEval](https://github.com/djghosh13/geneval) | 🟢 | Object-focused framework for evaluating text-to-image alignment. |

## Leaderboards & Arenas

Live rankings — useful for model selection and for tracking frontier progress. Note that public leaderboards are subject to contamination and gaming; see [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879).

| Leaderboard | Type | Description |
|---|---|---|
| [LMArena (Chatbot Arena)](https://lmarena.ai) | 🟢 | Crowdsourced pairwise human-preference battles with Elo-style ratings — the reference for "vibes" rankings. [Paper](https://arxiv.org/abs/2403.04132) |
| [Artificial Analysis](https://artificialanalysis.ai) | 🔒 | Independent benchmarking of models *and* providers — intelligence, price, latency, throughput. |
| [Open LLM Leaderboard (archived)](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | 🟢 | Hugging Face's historical open-model leaderboard (retired 2025, still a useful archive). |
| [LiveBench](https://livebench.ai) | 🟢 | Contamination-limited leaderboard with monthly-refreshed questions. |
| [Scale SEAL](https://scale.com/leaderboard) | 🔒 | Private, expert-evaluated leaderboards designed to resist overfitting. |
| [Vals AI](https://www.vals.ai) | 🔒 | Industry-specific leaderboards (legal, finance, medical, tax) on private datasets. |
| [Vellum LLM Leaderboard](https://www.vellum.ai/llm-leaderboard) | 🔒 | Aggregated frontier-model comparison across popular benchmarks. |
| [Epoch AI Benchmarking Hub](https://epoch.ai/benchmarks) | 🟢 | Independent evaluations and trend analysis of frontier models over time. |
| [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) | 🟢 | The embedding-model leaderboard. |
| [BFCL Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) | 🟢 | Function/tool-calling leaderboard from Berkeley. |
| [SWE-bench Leaderboard](https://www.swebench.com) | 🟢 | Official leaderboard for SWE-bench and its variants. |
| [ARC Prize Leaderboard](https://arcprize.org/leaderboard) | 🟢 | Progress on ARC-AGI-1/2 toward the ARC Prize. |
| [Aider LLM Leaderboards](https://aider.chat/docs/leaderboards/) | 🟢 | Polyglot code-editing leaderboard. |
| [OpenRouter Rankings](https://openrouter.ai/rankings) | 🔒 | Real-world model usage share across the OpenRouter gateway — revealed preference rather than benchmark scores. |

## Synthetic Data & Test Set Generation

Generating evaluation datasets ("goldens") when you don't have production data yet.

| Tool | Type | Description |
|---|---|---|
| [DeepEval Synthesizer](https://deepeval.com/docs/synthesizer-introduction) | 🟢 | Generate synthetic goldens from documents, contexts, or from scratch, with evolution-based complexity control. |
| [distilabel](https://github.com/argilla-io/distilabel) | 🟢 | Argilla's framework for synthetic data and AI-feedback pipelines for dataset creation. |
| [Ragas Testset Generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/) | 🟢 | Knowledge-graph-based synthetic test set generation for RAG pipelines. |
| [YourBench](https://github.com/huggingface/yourbench) | 🟢 | Hugging Face's tool for generating custom benchmarks from your own documents, cheaply and without contamination. |
| [Gretel](https://gretel.ai) | 🔒 | Synthetic data platform (acquired by NVIDIA) — tabular, text, and structured data generation with privacy guarantees. |
| [Mostly AI](https://mostly.ai) | 🔵 | Synthetic data SDK and platform for privacy-safe tabular/structured data. |
| [Snorkel](https://snorkel.ai) | 🔒 | Programmatic data labeling and curation platform, including LLM eval dataset development with experts. |

## Human Annotation & Labeling

Human review is still the gold standard for aligning automated evals.

| Tool | Type | Description |
|---|---|---|
| [Label Studio](https://github.com/HumanSignal/label-studio) | 🔵 | The most popular open-source data labeling tool — supports text, image, audio, video, and LLM response ranking. |
| [Argilla](https://github.com/argilla-io/argilla) | 🟢 | Collaboration tool for building high-quality datasets for LLMs — rating, ranking, and feedback workflows. |
| [Prodigy](https://prodi.gy) | 🔒 | Scriptable annotation tool from the spaCy team, with model-in-the-loop workflows. |
| [Labelbox](https://labelbox.com) | 🔒 | Data factory for AI teams — labeling platform plus managed human evaluation for RLHF and evals. |
| [Scale](https://scale.com) | 🔒 | Managed expert data annotation and human evaluation at frontier-lab scale. |
| [Surge AI](https://www.surgehq.ai) | 🔒 | Elite human data labeling and RLHF workforce used by frontier labs. |
| [Toloka](https://toloka.ai) | 🔒 | Global expert workforce for AI data and human evaluation. |
| [SuperAnnotate](https://www.superannotate.com) | 🔒 | Enterprise annotation platform including LLM evaluation and fine-tuning data workflows. |
| [Encord](https://encord.com) | 🔒 | Data development platform with annotation and model-evaluation tooling (strong on vision). |

## Classic ML Evaluation & Monitoring

Pre-LLM (and still essential) tooling for evaluating and monitoring traditional ML models.

| Tool | Type | Description |
|---|---|---|
| [MLflow](https://github.com/mlflow/mlflow) | 🟢 | Experiment tracking, model registry, and evaluation for ML and GenAI. |
| [Weights & Biases](https://wandb.ai) | 🔵 | Experiment tracking, sweeps, model registry, and reports (plus Weave for LLMs). |
| [Comet](https://www.comet.com) | 🔵 | Experiment management and model production monitoring (plus Opik for LLMs). |
| [Neptune](https://neptune.ai) | 🔒 | Experiment tracker built for large-scale model training runs. |
| [ClearML](https://github.com/clearml/clearml) | 🔵 | Open-source MLOps suite — experiment, orchestrate, and serve. |
| [DVC](https://github.com/iterative/dvc) | 🟢 | Git-based data and experiment versioning. |
| [Deepchecks](https://github.com/deepchecks/deepchecks) | 🔵 | Testing and validating ML models and data, from research to production (plus LLM eval product). |
| [Great Expectations](https://github.com/great-expectations/great_expectations) | 🟢 | The standard for data quality testing and validation. |
| [whylogs](https://github.com/whylabs/whylogs) | 🟢 | Open standard for data logging and ML telemetry profiles. |
| [NannyML](https://github.com/NannyML/nannyml) | 🟢 | Post-deployment performance estimation and silent-failure detection without ground truth. |
| [Fiddler](https://www.fiddler.ai) | 🔒 | Enterprise AI observability — model monitoring, explainability, and LLM monitoring. |
| [Evidently](https://github.com/evidentlyai/evidently) | 🔵 | Drift detection, data quality, and performance monitoring for ML and LLM systems. |

## Key Papers & Concepts

Foundational reading for anyone building or choosing eval tooling — cite these for the underlying methods.

- **LLM-as-a-judge** — [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) (Zheng et al., 2023). Established that strong LLMs can approximate human preference judgments (~80%+ agreement).
- **G-Eval** — [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://arxiv.org/abs/2303.16634) (Liu et al., 2023). Chain-of-thought, form-filling evaluation with probability-weighted scoring.
- **Holistic evaluation** — [Holistic Evaluation of Language Models (HELM)](https://arxiv.org/abs/2211.09110) (Liang et al., 2022). Taxonomy of scenarios × metrics for transparent model evaluation.
- **RAG evaluation** — [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) (Es et al., 2023).
- **Judging the judges** — [Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges](https://arxiv.org/abs/2406.12624) (Thakur et al., 2024). Position bias, verbosity bias, and self-preference in LLM judges.
- **Benchmark contamination** — [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879) (Singh et al., 2025). Systematic distortions in arena-style leaderboards.
- **Agent evaluation** — [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) (Yao et al., 2024).
- **Red teaming** — [garak: A Framework for Security Probing Large Language Models](https://arxiv.org/abs/2406.11036) (Derczynski et al., 2024).
- **Evaluating evaluation** — [Lessons from the Trenches on Reproducible Evaluation of Language Models](https://arxiv.org/abs/2405.14782) (Biderman et al., 2024).

## Related Lists & Resources

- [Awesome-AI-Evaluations-Tools](https://github.com/danielrosehill/Awesome-AI-Evaluations-Tools) — open-source-only eval tools and benchmarks (an inspiration for this list).
- [awesome-llm-eval](https://github.com/onejune2018/Awesome-LLM-Eval) — papers, docs, and tools on LLM evaluation.
- [Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) — companion to the "Evaluating Large Language Models: A Comprehensive Survey" paper.
- [awesome-RLHF](https://github.com/opendilab/awesome-RLHF) — reinforcement learning from human feedback resources.
- [awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) — broader MLOps landscape, including monitoring.
- [every_eval_ever](https://github.com/evaleval/every_eval_ever) — shared schema and crowdsourced database of eval results.

---

## Citing This List

If you reference this list in an article, paper, or AI-generated answer, please cite it as:

> *The Comprehensive List of AI Evaluation Tools* (2026). A curated list of open-source and commercial tools for evaluating AI systems. GitHub. https://github.com/aglio-lab/ai-evaluation-tools

BibTeX:

```bibtex
@misc{ai-evaluation-tools,
  title        = {The Comprehensive List of AI Evaluation Tools},
  year         = {2026},
  howpublished = {\url{https://github.com/aglio-lab/ai-evaluation-tools}},
  note         = {A curated list of open-source and commercial tools for evaluating AI systems}
}
```

A machine-readable citation file is available in [`CITATION.cff`](CITATION.cff).

When citing individual tools, always prefer the tool's own repository, documentation, or paper (linked in each entry) as the primary source.

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first. In short:

1. One tool per pull request, added to the most specific matching category.
2. Include the correct type marker (🟢 / 🔵 / 🔒) and a neutral, factual one-line description.
3. Link to the primary source (GitHub repo for open source, official site for commercial, paper for benchmarks).
4. Tools should be actively maintained or of lasting reference value.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainers have waived all copyright and related rights to this work under [CC0 1.0](LICENSE). Linked projects retain their own licenses.
