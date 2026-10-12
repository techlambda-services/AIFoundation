# AIFoundation — Techlambda AI Training

A **reusable AI Foundation** curriculum with an extension track for **Kanchan Bangani — AI Infrastructure & Agentic Systems**. This repository is initialized as a planning and learning-artifact source of truth, not yet a finished application or training package.

## Curriculum at a glance

| Track | Modules | Proposed live hours | Intended audience |
|---|---|---:|---|
| Common AI Foundation | M01–M05 | 10 | Technical trainers and engineers starting AI |
| Kanchan specialization | M06–M13 | 20 | Experienced Linux/DevOps/Python/Docker/Kubernetes trainers |
| **Combined** | **M01–M13** | **30** | **15 × 2-hour live sessions** |

**Important TOC issue:** The original supplied Word TOC is labeled 30 hours, but its explicit module durations add up to **32 hours**. [Course alignment](docs/COURSE-ALIGNMENT.md) proposes reducing M07 and M08 from 4h to 3h each, subject to source-document approval. This repository does **not** claim that the Word TOC has been updated.

## Navigate the project

- [Course alignment and duration correction proposal](docs/COURSE-ALIGNMENT.md)
- [15-session training delivery plan](docs/DELIVERY-PLAN.md)
- [Techlambda teaching and validation standard](docs/TRAINING-STANDARD.md)
- [Progressive capstone architecture](docs/CAPSTONE-ARCHITECTURE.md)
- [Course checkpoint: current status and next task](COURSE-STATE.md)
- [Hands-on lab directory and implementation status](labs/README.md)

## Learning path

1. **Foundation:** AI/ML/GenAI → LLMs/prompts/safety → Python APIs → embeddings/RAG → foundational architecture.
2. **Specialization:** local model routing → serving/inference → production-minded RAG → agent state/approval → MCP/interoperability → AgentOps/LLMOps → K8s/CI-CD/FinOps → final teach-back.
3. **Progressive capstone:** AI Infrastructure & Agentic Operations Assistant, built and verified across sessions rather than created entirely in the last session.

## Principles

- Train with **30% theory / 70% demonstrable practice**, tracked session by session.
- Explain with real-life analogies; grow Beginner → Professional → Advanced.
- Prefer local/free/reproducible tooling, with safe hosted fallbacks.
- Require validation commands, expected outputs, learner evidence, and measurable assessments.
- Never store API secrets, client data, production credentials or unrestricted administrative agents in this repository.
- Distinguish proposed plans from tested code, and don't mark tasks complete before proof.

## Current state

**Planning baseline only.** The source TOC still requires duration reconciliation; course notes, runnable labs, CI and capstone code are not yet implemented. See [COURSE-STATE.md](COURSE-STATE.md) for evidence-based progress.

Maintained under Techlambda. The corporate Word TOC supplied for review remains the reference source until corrections are approved.
