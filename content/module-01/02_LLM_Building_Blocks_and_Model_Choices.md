# 02 — LLM Building Blocks & Model Choices
**Kanchan · Module 01 · Topic 02 of 02 (not timeboxed)**  
**Concepts + practical application · Browser + optional Python**

> **Remember:** Understand what goes in, what the model can see, and why its answer still needs checking.

## 1. The problem and learning goal

A team wants an assistant to explain Linux errors. It must choose a model, manage long input and avoid unsafe recommendations.

After this hour, you should be able to explain **transformers, tokens, context windows, embeddings and multimodal AI**; compare **hosted/local/open-weight** approaches and **LLMs/SLMs**; and score model responses against clear criteria.

**Learning rule:** Follow concepts and practice by understanding, not by a fixed one-hour limit.

**Prerequisites:** Module 01 Topic 01. Two accessible chat models are **optional**. Free offline examples are provided.

**5W+H:** Model building blocks (what) help technical teams (who) choose safer AI support assistants (why/where), before integration (when), using measured context and model comparisons (how).

## 2. Memory Hooks

| Concept | Memory Hook | Plain-English meaning |
|---|---|---|
| Transformer / attention | 🔦 **Spotlight** | Learns relationships among positions in a sequence |
| Tokens | 🧱 **Lego Pieces** | Model-specific chunks of text; **not necessarily words** |
| Context window | 🧑‍🏫 **Whiteboard** | Limited space for tokens the model can consider |
| Embeddings | 🧭 **Meaning GPS** | Vectors that help find semantically related content |

**Recall:** **Spotlight → Lego → Whiteboard → Meaning GPS**.

These are learning analogies, not literal descriptions of model internals. An open-weight model is not automatically open-source or unrestricted.

## 3. Follow one request

~~~mermaid
flowchart LR
    U[Question] --> T[Tokenizer]
    T --> C[Tokens in Context]
    C --> M[Model, often a Transformer]
    M --> O[Generated Tokens]
    O --> V[Check Result Before Use]
    K[Optional Knowledge Search via Embeddings] -. extra context .-> C
~~~

- **Transformer:** widely used architecture with attention mechanisms; attention does not guarantee truth.
- **Tokens / context:** a tokenizer splits input into model-specific units; model context has a token limit and is not permanent memory.
- **Embeddings:** numeric vectors for similarity; useful for searching documentation, but similarity is not factual proof.
- **Multimodal:** a model may accept text and images or other media, **only where its capabilities allow**.
- **Hosted:** quicker startup; evaluate provider access, confidentiality, availability and cost.
- **Local:** more runtime control; requires installation, compute, updates and security.
- **LLM vs SLM:** larger is not automatically better. Compare tested quality, speed, memory needs and price.
- **Open-weight models:** available weights have license conditions; they are not automatically unrestricted, fully open-source or secure.

**Depth progression:** Beginner: understand tokens and input limits. Engineer: use the named model's tokenizer and measure accuracy. Advanced awareness: long context and retrieval can still introduce stale or unauthorized information.

**Decision rule:** Start with task + data sensitivity + evidence of quality; then choose the simplest model/runtime that meets the need.

## 4. Do it yourself

### Lab A — What fits on the Whiteboard?
This is a **toy word-budget experiment**, **not** a measurement of real model tokens.

If Python is available, run this short program (otherwise split the sentence into words by hand):

~~~python
words = "Disk usage is 95 percent. Review logs first. Never delete files without approval.".split()
for limit in (6, 20):
    visible = words[-limit:]
    print(f"budget={limit}; words={len(words)}; retained={len(visible)}; dropped={len(words)-len(visible)}")
    print(" ".join(visible))
~~~

**Expected:** there are 13 whitespace-separated words. With budget 6, **6 remain and 7 drop**. With budget 20, **all 13 remain**. Explain what context was lost at budget 6.

**Important:** Real context handling is model/application-specific. To count **real tokens**, use a tokenizer compatible with a **named model**; this example cannot tell you the model's token count or context length.

**If blocked:** No Python? Do it on paper; label evidence as *manual*.

**Optional real-token check:** Use a tokenizer compatible with one named model and record its measured token count. Do not treat this toy word count as real tokens.

### Lab B — Compare two model answers
Use the **same synthetic prompt** in two models, if available:

> A Linux server is at 95% disk usage. State what is known, suggest three read-only diagnostic checks, avoid destructive commands, and say what evidence is missing. Keep it under 120 words.

Record the model names and actual outputs. If real models are unavailable, use the examples below **only as illustrative practice, not real model results**:

- **Illustrative A:** "Delete old files now. Backups must be the cause."
- **Illustrative B:** "Check filesystem usage with read-only diagnostics such as df -h and du, and review permitted log evidence. The cause is unknown without further data. Do not remove files without approval."

For each answer, rate **0 = not satisfied, 1 = satisfied**:

| Check | A (0/1) | B (0/1) |
|---|---|---|
| Clearly separates facts from guesses | | |
| Gives safe, useful diagnostics | | |
| Follows the requested format | | |
| Avoids unauthorized changes | | |

**Expected insight:** A makes an unsupported claim and unsafe suggestion. B is a better starting point, but it **does not fully meet** the request for three clearly distinct checks; review real answers against the prompt rather than assuming they passed.

**Safety:** No confidential logs or live credentials; verify commands before using them.

### Lab C — Choose the deployment approach
A small internal incident assistant has sensitive input and modest hardware. Write **two sentences**:
1. Hosted or local model, and **why** (privacy, hardware, effort, licensing).
2. LLM or SLM, and **what would you measure** before deciding?

**Check:** Any choice is acceptable if constraints and evaluation plan are explicit. Do not claim local means automatically secure or small means automatically inaccurate.

## 5. Check your understanding and submit

Answer aloud:
1. Are tokens always whole words? **No.**
2. Is the context window permanent memory? **No.**
3. Do similar embeddings guarantee a true answer? **No.**
4. Can every multimodal model process every modality? **No.**
5. Is open-weight identical to unrestricted open-source? **No.**

Submit **02_LLM_Concepts_Evidence.md** (or one page):
- Word-budget outputs for 6 and 20, with the limitation clearly stated.
- Two model responses or *clearly marked illustrative* comparison, plus the four scores.
- Your two-sentence model-selection decision and the five answers above.

**Assessment (10 points):** Correct word-budget outputs and limitations (3); scored answer comparison with reasons (4); defended model choice (2); memory-chain teach-back (1). **Pass: at least 8/10**; claims about live testing or tokens must match actual evidence.

**Troubleshooting:** Python unavailable → manual word count. Models unavailable → clearly label example responses illustrative. Answers conflict → verify claims independently, never guess.

**Done when:** you explain the four-part memory chain, demonstrate the word-budget limitation, score both outputs fairly and defend one model choice. Trainer review and **actual learner evidence** are required before marking this topic passed.

**Next:** Module 02 — LLMs, Prompt Engineering & Responsible AI.
