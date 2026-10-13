# Suggested delivery plan — 15 sessions × 2 hours

**Status:** PROPOSED, subject to TOC correction approval and dry-run of labs. The session schedule is for planning **only**; module/topic content is not capped by scheduled hours.

| Session | Time allocation | Planned focus |
|---|---|---|
| 01 | M01 2h | AI/ML/DL/GenAI, tokens, model comparison |
| 02 | M02 2h | Prompting, structured outputs, safety |
| 03 | M03 2h | Python LLM API and FastAPI |
| 04 | M04 2h | Embeddings, search, basic RAG |
| 05 | M05 2h | Foundation architecture and capstone checkpoint |
| 06 | M06 2h | Local model, routing, fallback, gateway |
| 07 | M07 2h | Dockerized AI serving and health checks |
| 08 | M07 1h + M08 1h | Inference performance; production RAG retrieval |
| 09 | M08 2h | RAG evaluation, access filtering, security |
| 10 | M09 2h | Tool-calling, agent state and checkpoints |
| 11 | M09 1h + M10 1h | Approval/retries; MCP server/client |
| 12 | M10 2h | MCP authorization, portable tools, A2A concepts |
| 13 | M11 2h | LLMOps/AgentOps, evals, telemetry, guardrails |
| 14 | M12 2h | Kubernetes/CI-CD/rollback/FinOps |
| 15 | M13 2h | Integrate, demonstrate and teach back |

**Total:** 30h = 10h common foundation + 20h specialization.

## Contact-hour target
In scheduled delivery, target a **30% theory / 70% application** blend. The schedule does not restrict content depth, reference explanations, practice volume or remediation. Finish by verified objectives and evidence, not an arbitrary fixed-length file.

## Progressive capstone milestones
1. S03: Python AI API with environment-variable configuration; verify success/error paths.
2. S04–05: minimal documented RAG and architecture diagram.
3. S06–08: local/hosted routing, container service, health endpoint and measured latency.
4. S09: retrieval comparison, small golden evaluation set, metadata isolation.
5. S10–12: stateful tool workflow with human approval and an MCP integration.
6. S13–14: evaluation/trace evidence, threat checklist, K8s/CI-CD/rollback design.
7. S15: run integrated demonstration, explain trade-offs, conduct trainer teach-back.

## Evidence and exit requirements
Every lab should produce: README instructions, reproducible source/config (no secrets), expected output, actual output, verification command or screenshot, known limitation and next step. No module is **DONE** without evidence of its lab and stated learning outcome.

## Delivery risk gates
- Confirm Python, Docker and Git installed and functioning before session 1.
- Test model/API access independently; provide mocked response mode and local/hosted alternatives.
- For 8 GB RAM or CPU-only machines, use small quantized models or instructor demo rather than promise local vLLM/Triton/GPU performance.
- Check data privacy, secret handling, prompt injection boundaries and tool permissions before any external/system integration.
