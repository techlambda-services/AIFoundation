# Module 01 — AI, Machine Learning, Deep Learning & Generative AI Foundations

> **Program:** Common AI Foundation · **Module:** 01 of 05 · **Duration:** 2 hours · **Level:** Beginner → Professional → Advanced awareness  
> **Delivery:** Instructor-led, practical-first · **Learning mix:** 36 minutes concepts (30%) + 84 minutes applied practice (70%)  
> **Source alignment:** Part A, Module 1, of *Kanchan — 30-Hour AI Foundation + AI Infrastructure & Agentic AI TOC*. This lesson covers **only the Common AI Foundation**, not the 20-hour specialization.  
> **Memory Book master hook:** **UMBRELLA → APPRENTICE → LAYER CAKE → CREATIVE STUDIO**.

## 01. Problem / Context

A Linux/DevOps team receives recurring incidents: a disk-space alert, suspicious log spikes, a customer asking for a clear explanation, and a request to draft a runbook. Someone proposes, “Use AI for everything.” That is not yet an engineering plan.

**Problem:** Which tasks need fixed rules, learned predictions, generation, search, or human judgment? How do we choose without confusing the AI techniques, exposing company information, or claiming untested accuracy?

**Module outcome:** Explain the AI landscape correctly and justify an AI approach for common technical problems.

## 02. Objectives / Learning Outcomes

By the end of this two-hour session, the learner can:

1. Differentiate **AI, ML, Deep Learning and Generative AI**, including areas of overlap.
2. Explain **supervised, unsupervised and reinforcement learning** using a workplace example for each.
3. Describe **datasets, training, inference, models, parameters and weights**, and why a prompt does not normally retrain a model.
4. Give a conceptual explanation of **foundation models, transformers, tokens and context windows**.
5. Explain **embeddings, multimodal AI, LLMs and SLMs**, and choose between hosted and local models at a high level.
6. Complete the three source-TOC exercises: **model response comparison**, **token/context experiment**, and **Linux/DevOps AI use-case map**.
7. Explain model limits, privacy risks, quality checks and appropriate human review.

**Success standard:** Complete all three labs, score at least 8/10 on MCQs, and explain the three central memory hooks in the teach-back.

## 03. Prerequisites

**Knowledge:** Basic programming logic, browser use and technical troubleshooting concepts. Prior statistics or neural network training is **not** required.

**Equipment/software:** Laptop, browser, text editor; Python 3.10+ recommended for the offline token/context exercise. Optional: access to two chat models and their approved documentation. No paid cloud, GPU or Kubernetes environment is necessary.

**Zero-assumption preparation check:**

1. Confirm the laptop and browser work.
2. If running Lab 2 code, open a terminal and run **python --version** (or **python3 --version**).
3. Confirm access to a text editor and permission to save plain-text evidence.
4. For real model comparisons, confirm both models are accessible and use **synthetic prompts only**.
5. If model access is blocked, perform the **explicitly illustrative offline comparison** instead and label it accordingly.

## 04. 5W + H

| Question | Answer |
|---|---|
| **What?** | The AI family, ways models learn, and the building blocks of contemporary language systems. |
| **Why?** | To select suitable solutions and avoid overengineering, security risk and exaggerated performance claims. |
| **Who?** | Developers, infrastructure engineers, technical trainers, analysts and solution designers. |
| **Where?** | Support operations, document search, ticket routing, knowledge assistance and content preparation. |
| **When?** | Before selecting a model, architecture, vendor, dataset or automation boundary. |
| **How?** | Analogy → concept → architecture/mind map → worked example → guided labs → validation → evidence → assessment. |

## 05. What / Why / How

**What:** AI is the broad field of computer-based intelligent behavior; ML is an approach that learns from data, DL is a family of ML techniques involving multi-layer neural networks, and GenAI focuses on creating content. Modern LLM-based GenAI is commonly built using deep learning.

**Why:** A threshold alert, a machine-learned incident classifier, and an LLM-drafted explanation solve different parts of a problem. A reliable system may use all three, with human approval for risky action.

**How:** Learn one concept, connect it with an everyday memory hook, explain it in engineering terms, then apply it to a synthetic technical example.

## 06. Memory Hook Book — Fast Recall

| Concept | Hook | Meaning you must recall | Real-world illustration |
|---|---|---|---|
| **AI** | ☂️ **UMBRELLA** | Broad collection of techniques for intelligent-seeming tasks | Rules, search and learning all sit underneath |
| **ML** | 👨‍🎓 **APPRENTICE** | Finds patterns from example data | Learns ticket categories from historical labeled tickets |
| **DL** | 🎂 **LAYER CAKE** | Multi-layer neural networks learn representations | A neural model recognizes complex patterns |
| **GenAI** | 🎨 **CREATIVE STUDIO** | Creates content from learned patterns | Drafts an incident summary |
| **Supervised** | 🗝️ **ANSWER KEY** | Learns from examples that have labels | Ticket → known category |
| **Unsupervised** | 🧦 **SORTING SOCKS** | Finds groups/structure without target labels | Groups similar log messages |
| **Reinforcement** | 🎮 **GAME POINTS** | Learns action policies using reward feedback | Optimizes a simulated resource policy |
| **Training** | 🏋️ **GYM** | Adjusts model weights during learning | Train a classifier on approved examples |
| **Inference** | 🏟️ **MATCH DAY** | Uses existing learned weights on new input | Classify a new ticket |
| **Parameters / weights** | 🎚️ **CONTROL KNOBS** | Learned numeric values shaping behavior | Values updated during training |
| **Transformer / attention** | 🔦 **SPOTLIGHT** | Connects relevant positions in context | Resolves which earlier phrase matters |
| **Tokens** | 🧱 **LEGO** | Model-specific pieces of input/output | A word may be one or several tokens |
| **Context window** | 🧑‍🏫 **WHITEBOARD** | Finite working space for an interaction | Very long history may not fit |
| **Embeddings** | 🧭 **MEANING GPS** | Numeric representation for similarity | Find related knowledge articles |
| **Multimodal** | 👀 **MULTIPLE SENSES** | Work with more than one modality where supported | Text plus images |
| **Hosted / local** | 🍽️ **RESTAURANT / HOME KITCHEN** | Provider runs infrastructure vs you run it | Hosted API vs locally installed runtime |
| **LLM / SLM** | 🚚 **TRUCK / SCOOTER** | Often higher capacity vs lower resource needs; benchmark first | Broad reasoning vs narrower on-device task |

**Three memory chains to rehearse aloud:**

- **Umbrella → Apprentice → Layer Cake → Creative Studio** = AI → ML → DL → GenAI.
- **Gym → Match Day** = training changes learned parameters; inference uses them.
- **Spotlight → Lego → Whiteboard → Meaning GPS** = attention → tokens → context → embeddings.

> **Accuracy note:** These are mental models, not scientific definitions. Generative techniques are not universally confined to transformers, and GenAI overlaps with other AI categories.

## 07. Real-Life Analogy

Imagine running a company:

- The **company** is AI.
- The **apprentice** (ML) learns how to classify requests by studying past examples.
- The **specialist team with layers** (DL) learns complex patterns from large sets of examples.
- The **creative studio** (GenAI) writes a draft email or produces a new design.
- The **gym** is the learning/training period, while **match day** is solving a fresh task using current abilities.
- A **whiteboard** can hold only so much information at once; that resembles the finite working context of an LLM.

Ask learners: **Is a company’s creative studio the entire company?** No. Likewise, generative AI is not all of AI.

## 08. Beginner Explanation

**Artificial Intelligence:** Computer systems that perform tasks associated with perception, prediction, planning or language.

**Machine Learning:** Systems learn patterns from data rather than relying exclusively on manually written rules.

**Deep Learning:** ML using neural networks with multiple layers. Deep learning is powerful for text, speech and images, but not required for all business automation.

**Generative AI:** Produces new text, code, image, audio or other content, depending on the model. Fluency does not guarantee correctness.

**Training vs inference:** During training, model weights are adjusted. During ordinary inference, the trained model processes the new request. Sending a prompt usually does not change the model’s learned weights.

**Tokens and context:** A model generally processes token units rather than whitespace-separated words. Its context is limited; it does not guarantee long-term memory or perfect recall.

**Embeddings:** Convert content into numerical vectors so a system can estimate relatedness, which is useful in semantic search.

## 09. Professional / Engineering Explanation

### 09.01 Learning paradigms

| Paradigm | Training signal | Typical scenario | Caution |
|---|---|---|---|
| Supervised | Labeled input/output examples | Incident severity classification | Inconsistent labels weaken the model |
| Unsupervised | Input data without target labels | Grouping similar incident messages | Clusters are not guaranteed meaningful |
| Reinforcement | Actions, outcomes and rewards | Simulated resource allocation policy | Reward design can create unintended behavior |

**Important:** A tool-using LLM is not automatically a reinforcement-learning system.

### 09.02 From data to a model

**Data collection → cleaning/labeling → training → validation/test → saved trained model → inference → monitoring.**

- **Dataset:** Input examples and, where applicable, expected labels.
- **Parameters/weights:** Values learned from training.
- **Hyperparameters:** Training configuration selected by developers.
- **Foundation model:** Broad pretrained model that can support many tasks.
- **Transformer:** Widely used neural architecture that incorporates attention.
- **Inference:** Applying existing model weights to a new request.
- **Evaluation:** Assessing task accuracy, robustness, safety, latency and cost against evidence.

### 09.03 Language-model request flow

1. Application creates a prompt and determines allowed context.
2. A compatible tokenizer encodes the input into tokens.
3. The model processes token representations through neural layers, often transformer layers with attention.
4. The model generates output tokens iteratively.
5. The application validates format, risk and factual support before displaying or acting on the answer.

### 09.04 Hosted, local and open models

- **Hosted:** Quick initial integration, provider-operated infrastructure; requires cost, data-sharing and availability review.
- **Local:** More direct runtime control; requires hardware, maintenance and security controls. Local does not automatically mean secure.
- **Open weight vs open source:** Publicly accessible weights do not necessarily mean all code, training data or commercial usage rights are open. Check licenses.
- **LLM vs SLM:** Labels for larger and smaller language models are approximate; select by benchmark results, required quality, latency, privacy and compute budget.

## 10. Advanced Explanation / Engineering Trade-offs

- **Training data leakage:** Never use held-out evaluation items to train a system you then claim to have tested independently.
- **Inference vs RAG vs fine-tuning:** Ordinary prompts provide context; retrieval fetches external information at request time; fine-tuning changes model parameters.
- **Attention is not truth:** It weighs relationships among token representations; factual validation and citations require system-level evidence.
- **Long context is not perfect recall:** A model may fit information in the context window and still fail to use it reliably.
- **Tokenization differs:** Character count, word count, bytes and real model token count are not interchangeable.
- **Embedding similarity is not verification:** Two passages may be close in vector space but outdated, unauthorized or incorrect.
- **Multimodal is capability-specific:** Not every model supports every image, audio or video input/output format.
- **Model size is not a score:** A smaller model may perform better on a narrow workload, but this must be measured.

## 11. Architecture / Visualization

### AI family mental model

~~~mermaid
flowchart TD
    A[AI - Big Umbrella] --> B[Rules, search and planning]
    A --> C[Machine Learning - Apprentice]
    C --> D[Classical ML]
    C --> E[Deep Learning - Layer Cake]
    E --> F[Transformer language models]
    F --> G[Modern LLM-based GenAI - Creative Studio]
    E --> H[Other deep models]
~~~

**Scope note:** This depicts a common modern path to LLM-based GenAI, not an exhaustive set diagram for all generative systems.

### Training versus inference

~~~mermaid
flowchart LR
    D[Approved training examples] --> T[Training: Gym]
    T --> W[Learned parameters / checkpoint]
    W --> I[Inference: Match Day]
    Q[New prompt or request] --> I
    I --> O[Output]
    O --> V[Application validation and human review]
~~~

### LLM interaction

~~~mermaid
flowchart LR
    U[User request] --> A[Application privacy checks]
    A --> K[Tokenizer - Lego]
    K --> C[Context - Whiteboard]
    C --> M[Model / Attention - Spotlight]
    M --> R[Generated result]
    R --> V[Validate result]
~~~

## 12. Mind Map

~~~mermaid
mindmap
  root((Module 01 AI Foundation))
    AI - UMBRELLA
      Rules
      Machine Learning - APPRENTICE
        Supervised - ANSWER KEY
        Unsupervised - SORTING SOCKS
        Reinforcement - GAME POINTS
        Deep Learning - LAYER CAKE
      GenAI - CREATIVE STUDIO
    Lifecycle
      Dataset
      Training - GYM
      Weights - KNOBS
      Inference - MATCH DAY
    LLM Building Blocks
      Transformer - SPOTLIGHT
      Tokens - LEGO
      Context - WHITEBOARD
      Embeddings - MEANING GPS
      Multimodal - MULTIPLE SENSES
    Model Selection
      Hosted vs Local
      Open weight vs Proprietary
      LLM vs SLM
    Evidence
      Model comparison
      Token/context experiment
      Linux/DevOps use-case map
~~~

## 13. Core Concepts and Glossary

| Term | Precise meaning | Memory cue |
|---|---|---|
| Rules-based automation | Explicit logic that does not learn weights | Rulebook |
| Dataset | Examples used in building or evaluating models | Practice material |
| Label | Expected output paired with a supervised example | Answer key |
| Feature | Measurable input to a model | Clue |
| Training | Adjust model parameters using an objective and data | Gym |
| Inference | Use the trained model to predict/generate | Match day |
| Foundation model | Broadly pretrained reusable model | Library |
| Transformer | Neural architecture using attention among other parts | Spotlight |
| Token | Unit used by a compatible model tokenizer | Lego |
| Context window | Bounded interaction context, measured in model tokens | Whiteboard |
| Embedding | Learned numeric representation of content | Meaning GPS |
| Multimodal | Support for multiple data modalities | Multiple senses |
| LLM/SLM | Large/small language-model descriptions, not fixed standards | Truck/scooter |

## 14. Tools, KPIs and Measurements

**Tools:** Python (standard library), browser, text editor, optional hosted models, optional vendor-compatible tokenizer.

**For comparison:** record model identifier, date, exact prompt, output, response accuracy against independently checked facts, clarity, safety, and apparent limitations. Quality judgments without evidence should be marked subjective.

**For context lab:** calculate actual characters/bytes/whitespace-separated words; demonstrate truncation using an explicit **toy word limit**. Do **not** rename word counts as token counts. Real token counts require a tokenizer matched to the selected model.

**For use-case decisions:** record problem type, chosen technique, rationale, risk, human approval and what evidence would validate the design.

## 15. Worked Example — Linux Disk Alert

**Synthetic alert:** A host reports 95% disk usage.

| Technique | What it does | Suitable use |
|---|---|---|
| Rules | Trigger an alert if disk usage exceeds a threshold | Predictable operations check |
| Supervised ML | Classify severity from labeled historical examples | Repeated triage |
| Unsupervised ML | Group recurring anomalous patterns | Explore unknown patterns |
| GenAI | Write an explanation or draft runbook | Help an engineer understand the situation |
| Human approval | Review/delete/restore decisions | Prevent unsafe changes |

**Decision:** A language model may draft remediation advice but must not execute a destructive disk-cleanup command solely because its text says to do so.

## 16. Real Project / Application Usage

**Teaching project:** “AI-Aware DevOps Support Triage” using **synthetic** logs and runbooks. Module 01 produces a **decision map and evidence**, not a production agent. In Module 03, learners implement a Python API; Module 04 covers embeddings and RAG implementations.

## 17. Scenario / Case Study

Your team needs to: (a) alert on CPU > 90%, (b) group unknown error messages, (c) classify tickets with labels, (d) draft explanations, and (e) reboot a production machine.

Discuss which task fits a rule, supervised ML, unsupervised ML, GenAI or a human-controlled workflow. **Expected:** (a) rules; (b) clustering/anomaly analysis; (c) supervised ML; (d) optional GenAI; (e) approved operational automation/human authorization, not free-form LLM execution.

## 18. Session Delivery Plan — 120 Minutes

| Minutes | Type | Activity | Artifact |
|---|---|---|---|
| 00–12 | Theory (12) | AI family, objectives, memory hooks | Concept explanation |
| 12–36 | Hands-on (24) | Lab A: DevOps use-case mapping | Decision table |
| 36–48 | Theory (12) | Training, inference, transformers, tokens | Mental model |
| 48–72 | Hands-on (24) | Lab B: Token/context experiment | CLI output |
| 72–84 | Theory (12) | Embeddings, multimodal, hosted/local, LLM/SLM | Trade-off comparison |
| 84–108 | Hands-on (24) | Lab C: Compare two responses | Scoring worksheet |
| 108–120 | Practice/Assessment (12) | Quiz, viva, evidence review | Answer sheet |
| **Total** | **Theory 36** | **Applied 84** | **30% / 70%** |

## 19. Hands-on Lab A — DevOps Use-Case Map (24 Minutes)

**Goal:** Decide *whether and where* AI techniques are useful.

**Instructions:** Copy the table, complete **Technique**, **Why**, **Risk** and **Approval** for all five tasks, then compare with the facilitator guidance.

| Synthetic task | Recommended baseline | Why? | Risk / approval |
|---|---|---|---|
| Alert when CPU exceeds threshold | Rules | Fixed measurable criterion | Human checks action |
| Cluster similar error lines | Unsupervised ML | Similarity without explicit labels | No automated destructive action |
| Categorize tickets from labeled examples | Supervised ML | Historical labels available | Verify low-confidence classifications |
| Draft a maintenance notice | GenAI (optional) | Produces readable language | Human reviews before sending |
| Restart a critical service | Rules-based authorized workflow | Controlled operational action | Explicit privileged approval |

**Learner challenge:** Propose one task **where GenAI should not be used** and explain why.

**Expected output:** Saved use-case map with at least five rows and sensible decision boundaries.

**Validation:** Every row has a plausible technique, a rationale, and a risk/approval statement. Explain why the “restart” row must not be an autonomous LLM action.

**Evidence:** Completed decision table and one sentence: “I avoided GenAI for ___ because ___.”

## 20. Hands-on Lab B — Tokens and Context Windows (24 Minutes)

**Goal:** Understand input-length limits without confusing words with real model tokens.

**Steps:** Create a file named **module1_context_lab.py** with the following standard-library Python code. Run **python module1_context_lab.py** (or **python3 module1_context_lab.py**).

~~~python
import json

text = (
    "Disk usage is 95 percent. Review the filesystem safely. "
    "Check which service owns large files. Do not delete data "
    "without an approved change."
)

words = text.split()
toy_word_budget = 12
visible_words = words[-toy_word_budget:]

report = {
    "characters": len(text),
    "utf8_bytes": len(text.encode("utf-8")),
    "whitespace_words": len(words),
    "toy_word_budget": toy_word_budget,
    "toy_visible_text": " ".join(visible_words),
    "toy_words_dropped": max(0, len(words) - toy_word_budget),
    "actual_model_tokens": None,
    "token_note": (
        "Not measured: true tokens require a tokenizer "
        "compatible with a named model."
    ),
}

print(json.dumps(report, indent=2))
assert report["toy_words_dropped"] == max(0, len(words) - toy_word_budget)
assert report["actual_model_tokens"] is None
assert len(visible_words) <= toy_word_budget
~~~

**Interpret:** Which information disappeared when the **toy word budget** was applied? Change the budget from **12** to **24**, rerun and compare. Explain why this is *only a word-budget demonstration* and **not** a measurement of any model's token window.

**Optional real tokenizer experiment:** Use the documentation/tokenizer associated with a specific model and report its model name and **actual measured token count**. Do not estimate tokens by relabeling the output above.

**Expected:** Program prints JSON counts with **actual_model_tokens: null**. For this 23-word sample, budget **12** retains 12 words and drops **11**; budget **24** retains all 23 words and drops **0**. Both executions must pass the assertions.

**Validation:** All assertions pass; the learner identifies the removed part of the sample and states why “whiteboard” does not mean permanent memory.

**Troubleshooting:** If **python** is not recognized, try **python3**. If files cannot be created, use a Python interactive shell or perform the exact word-truncation exercise manually and label evidence “manual”.

**Evidence:** Terminal output for 12 and 24, and a two-sentence reflection.

## 21. Hands-on Lab C — Model Comparison (24 Minutes)

**Goal:** Compare responses using reproducible criteria rather than “I liked the answer.”

**Common synthetic prompt (use exactly for each real model):**

> A Linux server reports disk usage of 95%. Explain likely causes in at most 120 words, suggest three **read-only** diagnostic checks, state what you cannot know without logs, and avoid destructive commands. Return the result as three numbered points plus one caution.

**Real-model mode:** Submit the same prompt to two accessible models. Record model/product names, date, relevant settings (if known), and their **actual** answers. Verify proposed diagnostic commands against authoritative Linux documentation before marking them correct.

**Offline fallback — illustrative training examples, NOT real model measurements:**

- **Illustrative Response A:** “Delete old files immediately; the disk is obviously full because backups were misconfigured.” **Problems:** unsupported cause; destructive recommendation; no safe diagnostics.
- **Illustrative Response B:** “Investigate filesystem usage with read-only checks such as df and du; inspect permitted logs and ownership. Cause cannot be confirmed without system evidence. Do not delete or change files without authorization.” **Advantages:** qualified uncertainty and safe intent; commands still need environment-specific review.

**Rubric (1 = weak, 5 = strong):**

| Criterion | Model/Example A | Model/Example B | What justifies the rating? |
|---|---:|---:|---|
| Factual correctness and uncertainty | | | Independently verified facts vs guesses |
| Instruction/format following | | | Three points, ≤ 120 words, caution |
| Operational safety | | | No destructive actions, review boundaries |
| Usefulness and clarity | | | Diagnostic reasoning and concise steps |
| **Total / 20** | | | An *exercise score*, not a universal benchmark |

**Expected:** Two clearly identified responses, a scored table, written justification and selection for the stated scenario. If using the offline fallback, label the entire artifact **ILLUSTRATIVE — NOT LIVE MODEL RESULTS**.

**Validation:** Criterion ratings are justified; unsupported causes are penalized; scoring is explicitly subjective/limited where independent verification is unavailable.

**Evidence:** Prompt, responses, filled rubric and recommendation.

## 22. Expected Outputs and Validation Checklist

| Evidence item | Minimum acceptable result | Pass condition |
|---|---|---|
| Lab A — Use-case map | Five mapped tasks + one avoid-GenAI example | Appropriate categories and approval reasoning |
| Lab B — Context experiment | JSON run at two toy budgets | Assertions pass; no fake “actual token” count |
| Lab C — Model comparison | Two outputs + justified scoring | Sources identified as live or illustrative |
| Quiz | 10 answers | At least 8 correct |
| Teach-back | Memory chains and one architecture choice | Technically accurate, safety-aware |

**Trainer note:** No lab should be marked **VALIDATED** until its observed output/evidence is reviewed. Sample instructions alone do not prove successful learner execution.

## 23. Evidence / Submission

Suggested filename: **Module01_Evidence_<learner-id>.md** (replace placeholder with a non-sensitive ID).

~~~markdown
# Module 01 Evidence
- Date:
- Mode: real-model / illustrative-offline
- Lab A use-case map: completed / incomplete
- Lab B word-context experiment: commands, outputs, what changed
- Lab C model comparison: exact prompt, responses, rubric
- Quiz score: __ / 10
- Teach-back: UMBRELLA→APPRENTICE→LAYER CAKE→CREATIVE STUDIO
- Biggest misunderstanding corrected:
- Trainer validation: pending / passed / needs retry
~~~

Share using the approved training evidence location. **Never include API keys, confidential logs, user credentials or sensitive operational details.**

## 24. Mini Project

**AI-Aware Technical Support Decision Map:** Create a one-page architecture showing input → rule/ML/GenAI decision → human approval and review → output. Annotate which stages need a real model and which can remain deterministic.

This is an **architecture exercise**, not the final Python API capstone (that belongs to Module 05, built progressively after Module 03).

## 25. Research / Learning Notebook

Write one question for each item: (a) a real business use of classical ML, (b) a real LLM use case, (c) a tokenizer for a named model, (d) a privacy/licensing difference between one hosted and one local model. Cite documentation, distinguish verified facts from guesses, and record limitations.

## 26. Decision Scenarios

**Scenario 1:** “All alarms should be sent to a language model.” Explain the cost, reliability and approval issues and where simple threshold logic suffices.

**Scenario 2:** “We gave the model a document; it has been trained on it.” Explain prompt context vs retrieval vs fine-tuning.

**Scenario 3:** “The larger model is always better.” Define an evaluation plan comparing task accuracy, latency, privacy, cost and failure modes.

## 27. Common Mistakes

- **AI, ML, DL and GenAI are synonyms.** They are different, related concepts.
- **Every AI problem needs a generative model.** Some need only reliable rules.
- **Prompt = training.** Ordinary prompting does not normally update weights.
- **Words = tokens.** Tokenization is specific to the model and encoding.
- **Context = permanent memory.** A finite context window is not persistent memory.
- **Attention = factual evidence.** Attention does not validate truth or sources.
- **Embedding similarity = accuracy.** Relatedness cannot establish correctness or permission.
- **Local deployment = automatic privacy/compliance.** Local systems still require security.
- **Any open-weight model is unrestricted.** License and usage permissions vary.

## 28. Best Practices

- Start with a precise task and expected measurable output.
- Choose the **simplest verified approach** first.
- Use synthetic examples during training.
- Validate model recommendations before acting.
- Record provider, model, prompt and conditions for comparisons.
- Treat unknown facts as unknown; do not invent evaluation results.
- Require explicit authorization for any operational change.
- Use small, evidence-driven experiments before architecture commitments.

## 29. Troubleshooting

| Symptom | Root cause to examine | Action |
|---|---|---|
| Learner confuses ML and GenAI | Overlapping terminology | Revisit company analogy and disk-alert case |
| No access to two LLMs | Account/network/provider unavailable | Switch to explicitly illustrative offline comparison |
| Python script does not run | Python missing, incorrect command or paste error | Check version, file name and indentation |
| Toy counts presented as tokens | Wrong interpretation of experiment | Require model-compatible tokenizer for actual token claims |
| Model responses disagree | Probabilistic generation, differing models or prompts | Record conditions; verify claims independently |
| Sensitive text in evidence | Inadequate data-handling checks | Stop submission; replace with synthetic data |
| Incomplete lab submission | No validation/output | Re-run and collect expected vs actual evidence |

## 30. Performance / Complexity / Trade-offs

Rules offer predictable decisions but limited adaptability. ML classifiers require appropriate data and validation. Generative models provide flexible language but can hallucinate and create operational/safety risks. A hosted model reduces infrastructure work but adds provider and data-handling considerations. Local models increase operations responsibility. Choose using **accuracy, latency, throughput, privacy, licensing, cost and governance**, not marketing labels.

## 31. Viva / Cross Questions / Interview Questions

1. **Is DL a subset of ML?** Yes, conventionally. **Is all AI ML?** No.
2. **Are GenAI and DL identical?** No; GenAI is an output-oriented category, and modern GenAI commonly uses DL.
3. **Why call supervised learning an answer key?** It uses labeled examples with target answers.
4. **Does a prompt retrain an LLM?** Usually not; a prompt modifies request context.
5. **Why are token limits not word limits?** A compatible tokenizer maps text to model-specific tokens.
6. **What does transformer attention guarantee?** It models token relationships; it does not guarantee truth.
7. **Are two close embedding vectors proof of factual accuracy?** No.
8. **Could a small model be preferable?** Yes, for suitable tested tasks and constraints.
9. **Should an LLM run a destructive Linux command autonomously?** No, not without strict permissions, controls and approval.
10. **How would you demonstrate Module 01 in an interview?** Explain one memory hook, show one lab and defend its limitations.

## 32. Quick Revision (One Minute)

**Family:** **Umbrella → Apprentice → Layer Cake → Creative Studio**.

**Learning types:** **Answer Key → Sorting Socks → Game Points**.

**Lifecycle:** **Gym → Match Day**.

**LLM mechanics:** **Spotlight → Lego → Whiteboard → Meaning GPS**.

**Deployment:** **Restaurant vs Home Kitchen**, **Truck vs Scooter**.

**One-sentence summary:** AI is the broad toolbox; select the right technique, explain how it works, test its output, and do not hand it unsafe authority.

## 33. MCQs — Knowledge Check (10 Points)

1. Which relationship is conventionally correct? **A)** DL is a subset of ML **B)** AI is a subset of GenAI **C)** All AI requires transformers **D)** GenAI equals every ML technique.
2. Supervised learning uses: **A)** no examples **B)** labeled targets **C)** only chat prompts **D)** only hand-written rules.
3. An unsupervised task is: **A)** predicting labeled severity **B)** clustering unlabeled log messages **C)** sending an email **D)** applying a CPU threshold.
4. Reinforcement learning learns primarily from: **A)** rewards/actions **B)** only labeled CSVs **C)** just a chat history **D)** character counts.
5. Ordinary model inference typically: **A)** retrains all weights **B)** applies learned weights **C)** creates labels automatically **D)** changes the model license.
6. Transformer attention primarily helps: **A)** guarantee truth **B)** make a system private **C)** model contextual relationships **D)** store permanent user memory.
7. Model context windows are generally measured in: **A)** minutes **B)** tokens **C)** screen lines **D)** spreadsheet rows.
8. Embeddings are primarily useful for: **A)** similarity-based search **B)** guaranteed source truth **C)** changing firewall settings **D)** encrypting credentials.
9. Which statement is sound? **A)** local models need no operations **B)** hosted models never transmit data **C)** choose LLM/SLM using task evaluation **D)** bigger models always win.
10. For a production disk-cleanup action, choose: **A)** unreviewed GenAI output **B)** permissive shell access to any agent **C)** a controlled process with authorization **D)** no audit records.

**Answer key:** 1-A, 2-B, 3-B, 4-A, 5-B, 6-C, 7-B, 8-A, 9-C, 10-C.

**Passing threshold:** 8/10, plus all practical evidence and viva review. MCQ score alone is insufficient.

## 34. Subjective Questions

1. Explain AI vs ML vs DL vs GenAI with **one real-life analogy** and one DevOps use case.
2. Explain training vs inference, the role of weights and why an ordinary prompt does not amount to model training.
3. Contrast tokens, context windows and embeddings in a proposed document-search application.
4. Compare hosted versus local models for a customer-facing support task with sensitive information.
5. Propose a decision map for alerting, clustering, classification, response drafting and human-approved actions.

## 35. Assignment Levels (Foundation → Challenge)

- **Foundation:** Sketch the AI family and reproduce the three master memory chains.
- **Applied:** Complete the three labs, submit evidence and describe one failed assumption.
- **Interview:** Explain model selection for a synthetic DevOps support system in two minutes.
- **Challenge:** Design a privacy-safe, human-approved future AI assistant, clearly marking rules, models, retrieval, monitoring and approval boundaries; no deployment needed.

## 36. Assessment Rubric

| Criterion | Weight | Evidence |
|---|---:|---|
| Conceptual accuracy and memory-hook explanations | 25% | Viva + MCQ |
| Lab A use-case reasoning | 20% | Decision map |
| Lab B experiment and correct interpretation | 20% | Repeatable terminal output |
| Lab C comparison quality and limitations | 20% | Responses + scored rubric |
| Security, privacy, communication and reflection | 15% | Approval decisions, teach-back |
| **Total** | **100%** | |

Suggested acceptance: **≥ 80%**, 8/10 MCQ, and all three labs submitted. The trainer may request remediation where a safety-critical misunderstanding persists regardless of total score.

## 37. Definition of Done (DoD)

- [ ] All original TOC concepts taught at the intended foundation depth.
- [ ] Learner explains AI/ML/DL/GenAI and supervised/unsupervised/RL accurately.
- [ ] Learner distinguishes training from inference.
- [ ] Learner connects memory hooks to practical examples.
- [ ] Lab A: mapped five synthetic operational tasks, with safety checks.
- [ ] Lab B: observed two toy word-budget runs and stated real-token limitation.
- [ ] Lab C: compared two responses using evidence; real vs illustrative explicitly labeled.
- [ ] Quiz ≥ 8/10 and teach-back completed.
- [ ] Expected/actual evidence reviewed by trainer.
- [ ] No secrets or real sensitive data included.

## 38. Recommended Reading / References

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — ML terminology, supervised learning and evaluation.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — transformers, tokenizers and modern LLM concepts.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — conceptual architecture diagrams.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — responsible deployment and risk considerations.
- [Python Standard Library](https://docs.python.org/3/library/) — offline lab runtime.

Use provider-specific primary documentation for current token limits, available modalities, licenses and data-handling policies.

## 39. Key Takeaways

- **UMBRELLA / APPRENTICE / LAYER CAKE / CREATIVE STUDIO** captures the family of techniques.
- **GYM / MATCH DAY** distinguishes training from inference.
- **LEGO / WHITEBOARD / MEANING GPS** connects tokens, context and embeddings.
- Trust measurements and explicit evidence more than fluent model answers.
- For infrastructure decisions, preserve privacy, permission boundaries and human review.

## 40. Next Topic

**Module 02 — LLMs, Prompt Engineering & Responsible AI:** system/user/tool roles, zero/few-shot approaches, prompt templates, structured outputs, hallucination/grounding, prompt injection, privacy and human-in-the-loop. The Module 01 memory hooks remain prerequisite recall tags.

---
**Authoring note:** This is a complete **teaching manuscript and lab specification** based on the supplied Module 01 TOC. It is **not evidence** that any learner ran labs, that two real models were benchmarked, or that course delivery has already occurred.