# 02 — LLM Building Blocks & Model Choices

**Module 01 — AI, ML, Deep Learning & Generative AI Foundations**  
**Topic 02 of 02 · Kanchan · Beginner → Engineering → Advanced awareness**

> **Understand the input, the model's limits and the evidence before trusting its output.**

---

## 1. Problem Statement

A DevOps support team wants an AI assistant for Linux incidents. A user pastes a long runbook, expects a precise explanation, and asks whether the solution should use a hosted or local model. Without understanding transformers, tokens, context, embeddings and model trade-offs, the team may choose a costly or unreliable solution.

**Engineering question:** What can the model actually process, how do we check it, and what deployment choice fits the team's constraints?

## 2. Learning Objectives

After this topic, explain and apply:
1. **Transformer** and **attention** at a conceptual level.
2. **Tokens** and **context windows** without confusing them with words or permanent memory.
3. **Embeddings** and semantic similarity, including their limitations.
4. **Multimodal AI**, **LLM versus SLM** and **foundation model** terminology.
5. **Hosted, local, proprietary, open-weight and open-source** model decisions.
6. A reproducible context-limit demonstration, response comparison and defensible model choice.

**Prerequisites:** Topic 01 and simple command-line familiarity. Python is optional; paper-based and illustrative alternatives are included. No paid API or GPU required.

## 3. 5W + H Framework

### What?
The elements of modern language-model inference: tokens, attention, context windows, output generation, embeddings and runtime choices.

### Why?
Incorrect assumptions about context, truth, privacy, infrastructure requirements and cost can make AI applications unreliable.

### When?
Before choosing a language model, building an assistant, connecting organizational data or promising a deployment architecture.

### Where?
Documentation search, incident assistance, technical Q&A, text plus image use cases and AI-powered support systems.

### Who?
Developers, cloud/DevOps specialists, AI platform engineers, security reviewers and instructors explaining LLM systems.

### How?
Prepare a safe request → check its size → send it to an appropriate model → validate the response → compare quality and operating constraints.

## 4. Real-Life Analogy

Picture an engineer using a **desk and library**:

- The **spotlight** illuminates relevant items on the desk: an analogy for attention.
- A document is broken into **Lego pieces**: an analogy for model tokens.
- The desk has a limited **whiteboard**: the available context window.
- A library's **meaning-based catalog** locates related articles: an analogy for embeddings.
- The engineer still checks facts; a well-written answer is not necessarily true.

These are memory aids, not literal mathematical definitions of model internals.

## 5. Memory Hook

**Interview Master Plan rule:** **Real-life picture → action phrase → precise technical mapping → short trace → interview trap → memory lock.** This is more than a list of memorable labels.

### Hook A — Library Desk: Token, Context and Attention

**Picture it:** An engineer at a library desk breaks a document into **Lego pieces**, arranges only what fits on a **whiteboard**, and shines a **spotlight** on relevant relationships.

**Say the action phrase:** **"Break into Pieces → Fit the Board → Relate the Pieces → Check the Answer."**

| Action | Precise meaning |
|---|---|
| **Break into Pieces** | A named model's tokenizer maps text into model-specific tokens |
| **Fit the Board** | The model interaction has a limited token context; systems handle excess input differently |
| **Relate the Pieces** | Transformer attention models relationships between representations |
| **Check the Answer** | Generated output needs separate factual and safety verification |

**Trace:** For the phrase "disk usage 95 percent": the tokenizer produces model-specific tokens (not necessarily four words); those tokens must fit the model's current context capacity; a model generates an answer using learned relationships; a reviewer checks diagnostics and uncertainty.

**Interview answer:** "A model-specific tokenizer converts text to tokens; the context window limits what is available; attention helps represent relationships. None of these guarantees a correct answer."

**Trap:** "Is one whitespace word always one token, or is the context window permanent memory?" **No to both.** Our Python example counts words **only**.

### Hook B — Meaning GPS: Embeddings and Retrieval

**Picture it:** You search an enormous library with **Meaning GPS** instead of matching exact titles. Nearby shelf locations suggest related runbooks, but you still open and verify the document.

**Say the action phrase:** **"Encode Meaning → Find Neighbors → Read Sources → Verify Facts."**

| Action | Engineering mapping |
|---|---|
| **Encode Meaning** | A suitable embedding model represents text as vectors |
| **Find Neighbors** | Similarity search returns likely relevant passages |
| **Read Sources** | The application supplies approved retrieved context when appropriate |
| **Verify Facts** | Check authorization, provenance, freshness and factual support |

**Trace:** Query "server almost out of space" can retrieve a document titled "filesystem capacity alerts" without exact shared keywords. It is a **hypothetical retrieval example**, not an executed search or proof that a result is correct.

**Interview answer:** "Embeddings help retrieve semantically related material; similarity is a ranking signal, not proof of truth, permission or recency."

**Trap:** "Does embedding similarity certify that a runbook is safe?" **No.** This topic introduces the concept; the real RAG implementation belongs to Module 04.

### Hook C — Restaurant vs Home Kitchen: Hosted vs Local

**Picture it:** At a **restaurant**, someone else cooks and manages the kitchen; in a **home kitchen**, you control ingredients and equipment but do all the upkeep.

**Say the action phrase:** **"Provider Runs → Verify Terms; We Run → Maintain and Secure."**

| Decision | Engineering meaning |
|---|---|
| **Provider Runs** | Hosted model API; provider operates model infrastructure |
| **Verify Terms** | Check cost, service reliability and data-handling requirements |
| **We Run** | Locally hosted model; your team controls deployment runtime |
| **Maintain and Secure** | Your team owns compute planning, patching, access and incident response |

**Trace:** For a sensitive internal ticket assistant: list data policy, hardware and availability requirements; compare an approved hosted option against a supported local runtime; select only after task-level tests.

**Interview answer:** "Hosted can reduce operational burden; local offers hosting control but adds infrastructure responsibility. Neither is automatically private, secure or cheaper."

**Trap:** "Does open-weight mean open-source, or local mean automatically secure?" **No to both.** Examine the license and actual controls.

### Hook D — Truck vs Scooter: LLM, SLM and Multimodal

**Picture it:** A moving team chooses a **truck** or **scooter** based on the load and route, not the biggest vehicle available. If the task includes images, the driver also needs working **eyes**, not just a larger engine.

**Say the action phrase:** **"Check the Load → Match Capabilities → Test the Route."**

| Action | Precise mapping |
|---|---|
| **Check the Load** | Define task, volume, privacy and expected quality |
| **Match Capabilities** | Evaluate LLM/SLM size and supported text/image/audio modalities |
| **Test the Route** | Compare task accuracy, latency, memory, price and failure cases |

**Trace:** For one small synthetic text-classification task, a suitably evaluated SLM might be enough. For an image-plus-text incident screenshot, verify that the model actually supports image input, regardless of size.

**Interview answer:** "Model size is a resource trade-off, not a guarantee of task accuracy; multimodal ability depends on documented capabilities."

**Trap:** "Does every large language model see screenshots?" **No.**

**Memory lock — without reading:** Describe **Break → Fit → Relate → Check**, **Encode → Find → Read → Verify**, **Provider Runs / We Run**, and **Check Load → Match → Test**. Apply each to a new, synthetic incident assistant and defend one trap in a 30-second answer.

## 6. Visualization

**Interview Master Plan mind map** — the recall routes are related, not one mandatory sequential pipeline.

~~~text
LLM interaction
├─ Break into Pieces — tokenizer
├─ Fit the Board — context window
├─ Relate the Pieces — attention / transformer
└─ Check the Answer — application validation

Optional knowledge retrieval
└─ Meaning GPS — Encode → Find → Read → Verify

Choose a model/runtime
├─ Restaurant vs Home Kitchen — hosted vs local
└─ Truck vs Scooter — LLM vs SLM + multimodal capabilities
~~~


~~~mermaid
flowchart LR
  USER[Question and approved context] --> TOKEN[Model-compatible tokenizer]
  TOKEN --> CONTEXT[Tokens within context budget]
  CONTEXT --> MODEL[Language model, often Transformer]
  MODEL --> ANSWER[Generated output]
  ANSWER --> CHECK[Check format, facts and safety]
  DOCS[Approved documents] --> EMBED[Embeddings / similarity search]
  EMBED -. optional retrieved evidence .-> CONTEXT
~~~

**Scope:** Optional retrieval is previewed here; implementation of embeddings and RAG belongs to **Module 04**.

## 7. Simple Explanation

- A **transformer** is a popular neural-network architecture used in many LLMs. Attention helps the network relate parts of its input.
- A **token** is a unit of text determined by a specific tokenizer. One word can contain multiple tokens.
- A **context window** is a bounded amount of token information available during a model interaction. It is **not permanent memory**.
- An **embedding** is a numeric vector representing some aspects of meaning. Nearby vectors can support search for related documents.
- **Multimodal** means a model supports multiple modalities (such as text and images) to the extent that specific model's capabilities allow.
- **LLM** and **SLM** roughly refer to larger and smaller language models; naming boundaries vary.

## 8. Engineering Explanation

**Transformer:** Attention computes relationships among token representations. It can help with contextual prediction but does not guarantee factuality, citation quality or safe decisions.

**Tokenizer/context:** Model-specific tokenization and context budgets matter for prompts, attached material, retrieval and generated output. A long document may exceed available context, or fit but still be used poorly. Some systems truncate, reject, summarize or split input—do not presume a particular product's behavior.

**Embeddings:** Compare representations to retrieve likely relevant content. Similarity is **not proof** that information is correct, current or authorized. Retrieval systems must also check access and provenance.

**Model choices:**

| Choice | Advantages | What to verify |
|---|---|---|
| Hosted API | Easier start, provider runs infrastructure | Data policy, availability, latency, usage cost |
| Local runtime | More direct control over hosting | Hardware, patching, security, model capacity |
| Proprietary | Vendor-managed interfaces may simplify support | Data terms, portability, price |
| Open-weight | Weights available under a specific license | License, runtime security, allowed usage |
| Open-source | Rights granted under an applicable license for published components | Which *components* are open; model/data rights may differ |
| LLM vs SLM | Possible trade-offs in quality and resource needs | Benchmark the actual task, not only model size |

**Advanced awareness:** Long context is not guaranteed long-range recall; output can hallucinate; model licenses and multimodal support vary. For sensitive workflows use least privilege, appropriate data access controls and evidence-based evaluation.

## 9. Real Project Usage

**Project:** A DevOps runbook assistant receives a synthetic Linux alert and seeks a safe explanation.

1. User submits a synthetic alert: "disk utilization 95%".
2. The application selects permitted runbook text if retrieval is used.
3. The chosen hosted or local model produces a suggested explanation.
4. Application checks that diagnostic guidance is read-only and factual claims are qualified.
5. Human operator approves any consequential production changes.

**Decision:** A model is a component of an application, not its safety or authorization boundary.

## 10. Python Example

This short **standard-library** example demonstrates an **illustrative word budget**, not model tokens and not real LLM context handling.

**Save** as `topic02_context_budget.py`; run `python topic02_context_budget.py` or `python3 topic02_context_budget.py`.

~~~python
text = (
    "Disk usage is 95 percent. Review logs first. "
    "Never delete files without approval."
)
words = text.split()

def apply_word_budget(items, budget):
    if budget <= 0:
        raise ValueError("Budget must be positive")
    return items[-budget:]

print("words:", len(words))
for budget in (6, 20):
    retained = apply_word_budget(words, budget)
    print("budget:", budget, "kept:", len(retained),
          "dropped:", len(words) - len(retained))
    print("visible:", " ".join(retained))

assert len(words) == 13
assert len(apply_word_budget(words, 6)) == 6
assert len(apply_word_budget(words, 20)) == 13

try:
    apply_word_budget(words, 0)
except ValueError:
    print("negative budget test: passed")
else:
    raise AssertionError("Zero budget must fail")
~~~

**Expected numbers:** 13 whitespace-separated words; budget 6 keeps **6** and drops **7**; budget 20 keeps **13** and drops **0**; the zero-budget negative test passes.

**Do not claim:** these counts are actual model token counts. For actual counts, identify a **named model and compatible tokenizer**, and use its published limits.

## 11. Complexity Discussion

A word-budget slicing example is deliberately simple; it does not benchmark an LLM. Real inference can vary by model size, hardware, prompt length, generated length, batching and load.

Common model-choice trade-offs:
- **Latency:** time before/during generation.
- **Throughput:** requests or tokens handled over time.
- **Quality:** correctness and usefulness on representative tasks.
- **Cost:** compute, API tokens, storage, operations and monitoring.
- **Privacy/security:** access boundaries, vendor policies and operational controls.

**Choose a model by a small benchmark and documented constraints**, not by the assumption that larger, local or open-weight is automatically best.

## 12. Hands-on Exercise

### Exercise A — Context and tokens
Run the Python example; capture expected versus actual word counts. Identify which words disappear at budget 6. Then answer: **Why does this not measure real tokens?**

**Optional advanced validation:** Use an official compatible tokenizer for a named model. Record the model, exact text and real measured token count. Do not guess.

**Fallback:** If Python is unavailable, count the sample by hand and mark it **manual**.

### Exercise B — Compare model responses

Submit this **same synthetic prompt** to two accessible models, if available:

> A Linux server reports 95% disk usage. Provide three read-only diagnostic checks, state which cause is unknown without evidence, and avoid destructive actions. Use under 120 words.

Record exact prompt, names/settings (if available), actual answers and date. No company secrets.

If models are unavailable, use these **clearly illustrative examples**, not invented live-model results:

- **A:** "Delete old files. Backups are definitely the cause." *(unsupported and destructive)*.
- **B:** "Review filesystem usage with read-only diagnostics such as df -h and du, and inspect permitted logs. The cause is not confirmed. Do not remove files without approval." *(safer, but does not list three distinct diagnostic steps as requested)*.

Score each **0 or 1** for: (1) uncertainty/factual basis, (2) useful read-only checks, (3) exact format/instructions, (4) safe operational guidance.

**Expected insight:** A is unsafe and overconfident; B is safer but incomplete for the required three explicit checks. A score is specific to this task, not a universal model ranking.

### Exercise C — Choose a runtime

For a synthetic support assistant, compare **hosted vs local** and **LLM vs SLM** using quality, cost, privacy, latency and hardware constraints. Write a short decision with **one measurable acceptance test**. No choice is automatically correct.

## 13. Best Practices

- Use a model-compatible tokenizer before making real token/context claims.
- Verify the model's supported modalities, context limits and license from its documentation.
- Start small; compare models on the same synthetic task and evidence.
- Never place confidential data into unapproved prompts or public evidence files.
- Separate informative output from permission to execute operational actions.
- Record what was actually measured versus illustrative.

## 14. Common Mistakes

| Mistake | Correction |
|---|---|
| "One word equals one token" | Tokens depend on the tokenizer |
| "Context means permanent memory" | A window is bounded interaction context |
| "Attention guarantees correctness" | Verification is external to attention |
| "Similar embedding vectors prove truth" | Similarity is not validation or authorization |
| "All multimodal models handle any media" | Check each model's supported modalities |
| "Open weight means unrestricted" | Review component and weight licenses |
| "Local always means secure" | Security still depends on controls |
| "A larger model always performs better" | Benchmark the specific workload |

**Troubleshooting:** No Python? Use the manual exercise. No model account? Use explicitly illustrative responses. Different model outputs? Keep prompt/settings fixed and verify facts against independent evidence.

## 15. Interview Questions

1. **What does attention do in a transformer?** Helps model contextual relationships; does not prove truth.
2. **Why are tokens different from words?** Tokenization varies by model and encoding.
3. **What is a context window?** Bounded token capacity for an interaction, not durable memory.
4. **What is an embedding?** Vector representation used for tasks such as semantic similarity.
5. **How is multimodal capability determined?** By documented model-supported inputs/outputs.
6. **Why choose an SLM over an LLM?** Only if task-level evidence and operating constraints support it.
7. **What is the difference between open-weight and open-source?** Availability and license scope differ.
8. **What makes a model comparison fair?** Same prompt, recorded conditions, clear rubric, verified facts.
9. **Should retrieval results be trusted blindly?** No; check access, freshness and support.

## 16. Quick Revision

**Token/context/attention:** **Break into Pieces → Fit the Board → Relate the Pieces → Check the Answer**.  
**Embeddings:** **Encode Meaning → Find Neighbors → Read Sources → Verify Facts**.  
**Hosted/local:** **Provider Runs → Verify Terms; We Run → Maintain and Secure**.  
**Model sizing:** **Check the Load → Match Capabilities → Test the Route**.

**Memory-lock drill:** Hide the page; say each action phrase, map each verb to the correct technical action, explain one sample Linux incident and answer one interview trap. **A catchy label without a worked recall is incomplete.**

**One-line takeaway:** Choose and verify the model using the application's actual task, data and constraints.

## 17. Assignment

**Foundation:** Draw the request flow, label tokens, context and validation.  
**Applied:** Run or manually reproduce the context demonstration and evaluate two responses.  
**Interview:** Defend hosted/local and LLM/SLM choices for a synthetic Linux helpdesk.  
**Challenge:** Specify a small evaluation plan including failure cases, safe outputs and cost controls.

**Suggested 10-point rubric:** context demonstration and limitations **3**, comparison with evidence **3**, defensible architecture decision **2**, memory recall and safety **2**. **Recommended pass: 8/10** with accurate disclosure of real vs illustrative evidence.

## 18. Additional Reading

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — language-model concepts, tokenization and transformers.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — approachable attention architecture.
- [Python documentation](https://docs.python.org/3/) — standard-library exercise.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — AI system safety and governance.

## Completion Check

- [ ] Explain transformer, attention, tokens and context without confusing their roles.
- [ ] Explain embeddings and multimodal capabilities with appropriate limitations.
- [ ] Contrast hosted/local, open-weight/open-source and LLM/SLM.
- [ ] Complete context experiment and disclose that it is a word-budget example.
- [ ] Compare real or illustrative responses with correct labels and an honest rubric.
- [ ] Defend a model-choice decision using constraints and test criteria.
- [ ] Complete trainer teach-back and knowledge check without memorized definitions.

**Evidence file:** `02_LLM_Concepts_Evidence.md` — record actual output and observed limitations; instructor acceptance pending.

## Next Topic

**Module 02 — LLMs, Prompt Engineering & Responsible AI:** system/user/tool roles, reliable prompt design, structured outputs, grounding, privacy, prompt injection and human approval.
