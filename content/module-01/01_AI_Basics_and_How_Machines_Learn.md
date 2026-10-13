# 01 — AI Basics & How Machines Learn

**Kanchan · AI Foundation · Module 01 · Topic 01 of 02 (not timeboxed)**  
**Concepts + practical application · Free, offline-first**

> **Memory sentence:** **Choose the problem first. Use rules when rules are enough.**

## 1. Problem, objectives and readiness

**Real scenario:** A Linux/DevOps team faces high disk usage, repeated error logs, support tickets and requests to draft incident updates. A colleague says, “Let's use AI for all of it.” Is that a sensible design?

**Outcome:** After studying this topic, you can:
1. Explain **AI, Machine Learning (ML), Deep Learning (DL) and Generative AI (GenAI)** without mixing them up.
2. Identify **supervised, unsupervised and reinforcement learning**.
3. Explain **dataset, labels, model, parameters/weights, training, inference and foundation models**.
4. Match common DevOps tasks to an appropriate approach—and state when **human approval** is needed.

**5W+H:** What—AI methods; Why—solve the *right* problem; Who—engineers/trainers; Where—DevOps incident workflows; When—before selecting a model; How—classify, test and review.

**Learning rule:** Study until the concept, examples, and assessment can be explained independently. The TOC's scheduled session time is not a cap on material depth or practice.

**Prerequisites / check:** Basic technical awareness, paper or text editor. No Python, paid API, GPU, account or production access required. Use only **synthetic** incident examples.

## 2. Real-life analogy and Memory Hooks

Imagine an organization where people have different responsibilities. It is a memory aid, **not** a literal hierarchy of job titles.

| Concept | Recall tag | What it means |
|---|---|---|
| **AI** | ☂️ **Umbrella** | Broad field of intelligent-computing approaches; includes rules and learning |
| **ML** | 🎓 **Apprentice** | Learns patterns from examples |
| **DL** | 🎂 **Layer Cake** | A family of ML methods using multi-layer neural networks |
| **GenAI** | 🎨 **Creative Studio** | Generates text, images, code or other content |
| **Training** | 🏋️ **Gym** | Adjusts learned model parameters from data |
| **Inference** | 🏟️ **Match Day** | Applies an already trained model to new input |

**Recall twice, without reading:**  
**Umbrella → Apprentice → Layer Cake → Creative Studio**  
**Gym → Match Day**

**Important distinction:** AI is broader than ML; DL is a form of ML. GenAI is an output-focused category, not simply “another DL layer.” Modern LLM-based GenAI often uses DL.

## 3. Understand once; apply many times

**Which technique fits?**

| Approach | What is available? | DevOps example |
|---|---|---|
| **Fixed rule (no learning needed)** | A known condition | Alert when disk usage exceeds 90% |
| **Supervised ML** | Examples **with correct labels** | Predict ticket priority from previously labeled tickets |
| **Unsupervised ML** | Data **without target labels** | Cluster similar error messages |
| **Reinforcement learning** | Actions with **reward feedback** | Learn a policy in a *simulated* resource-allocation environment |
| **GenAI** | A request for generated content | Draft a maintenance note; engineer checks it |

**Model vocabulary, using one example:** A **dataset** is a collection of incidents. A **feature** is an input such as disk utilization; a **label** might be “high severity.” An ML **model** uses learned numerical **parameters (weights)**, adjusted during **training**. At **inference**, the model uses its learned parameters to make a prediction about a new incident. A **foundation model** has been broadly pretrained and can support multiple tasks through suitable interfaces and adaptation.

~~~mermaid
flowchart LR
    A[Labeled sample incidents] --> B[Training: Gym]
    B --> C[Model with learned weights]
    C --> D[Inference: Match Day]
    E[New incident] --> D
    D --> F[Prediction to check]
~~~

**Progressive depth:** **Beginner:** identify rule versus learning versus generation. **Engineering:** distinguish training data, labels and unseen inputs. **Advanced awareness:** evaluate on separate held-out cases; avoid data leakage, unsupported predictions and unaudited operational actions.

**Watch out:** A normal prompt to an existing LLM is **not** weight training. A fluent generated answer is not proof that the answer is correct.

## 4. Practice in one continuous DevOps case

### Lab A — Choose the tool, not the buzzword

**Task:** Complete **Approach + Why + Risk/approval** for all five scenarios. Reuse the five approaches from Section 3; more than one tool may be involved, but choose the simplest suitable starting point.

| Scenario | Approach | Why? What must be checked? |
|---|---|---|
| A1. Trigger alert at 95% disk usage | | |
| A2. Discover groups of similar, unlabeled log entries | | |
| A3. Categorize tickets using historical labeled examples | | |
| A4. Draft a clear incident update | | |
| A5. Restart a critical production service | | |

**Self-check after attempting:** A1 **rule** (known threshold); A2 **unsupervised ML** (no target labels); A3 **supervised ML** (labels); A4 **GenAI optional**, with factual review; A5 **authorized operational workflow**, with permissions/approval—not an unconstrained LLM action. **No real operations are performed.**

**Expected evidence:** One completed five-row table with a rationale and a safety condition in each row.

### Lab B — Follow a ticket from Gym to Match Day

These are **made-up data** for understanding; **no ML model is trained or run here**.

| Ticket | Feature: disk/CPU utilization | Label: severity | Role |
|---|---|---|---|
| T1 | Disk 95% | High | Labeled example |
| T2 | Disk 30% | Low | Labeled example |
| T3 | CPU 96% | High | Labeled example |
| T4 | CPU 25% | Low | Labeled example |
| T5 | Disk 92% | Unknown | New input |

**Do these four tasks:**
1. Circle the **training examples**, underline their **labels**, and mark **T5** as new input.
2. Write the lifecycle in your own words: **labeled examples → training → learned model → new input → inference → prediction → verification**.
3. Mark **Training (T)** or **Inference (I)**: (a) changing model weights using T1–T4; (b) predicting a category for T5 using a trained model; (c) fine-tuning using approved examples; (d) asking a deployed LLM to summarize T5.
4. Imagine a model predicted “High” for T5. Can you claim **measured accuracy** from this worksheet? Explain why, and name one verification step.

**Self-check:** T1–T4 are *illustrative training data*; T5 is unseen input. (a) T, (b) I, (c) T, (d) I. The “High” prediction is **hypothetical**: compare predictions with independently labeled, held-out examples before making any accuracy claim. No weights are updated by this paper exercise.

**Expected evidence:** An annotated table, lifecycle and four T/I answers, plus the limitation of the hypothetical prediction.

### Lab C — Explain it like a corporate trainer

Using the same incident case, deliver a **brief teach-back** without looking at Section 2:

- Explain **Umbrella → Apprentice → Layer Cake → Creative Studio**.
- Explain **Gym → Match Day** using T1–T5.
- Defend **one place you would not use GenAI**.

Then answer two cross-questions: **Does a normal prompt retrain weights?** (No.) **Should a model-generated suggestion restart production without authorization?** (No.)

**Expected evidence:** Five lines of teach-back notes; a colleague or trainer can ask the two cross-questions. Practicing aloud alone is acceptable as preparation but is **not** independently observed validation.

## 5. Validate and finish — evidence and acceptance

**One submission:** `01_AI_Basics_Evidence.md` (or one page) with Lab A table, Lab B lifecycle/T-I answers, Lab C notes, and **one mistake corrected**.

**10-point assessment:**

| Check | Points | Pass evidence |
|---|---:|---|
| Lab A: five choices with sensible reasons and controls | 5 | 1 point per correct, reasoned scenario |
| Lab B: examples/new input + training/inference | 3 | 1 for data roles, 1 for four T/I answers, 1 for rejecting unverified accuracy |
| Lab C: memory chains and safe decisions | 2 | 1 for explaining concepts; 1 for approval boundary |
| **Total** | **10** | **Pass ≥ 8/10 AND A5 safety control correct** |

**Troubleshooting:** Confused by “ML” vs “GenAI”? Ask whether you need to *learn from labeled examples* or *generate content*. Not sure about “training”? Ask whether weights are being updated. Can't access any tools? All labs work with paper and synthetic data.

**Common mistakes:** Treating GenAI as all AI; assuming all AI needs learned weights; equating a prompt with model training; treating one hypothetical prediction as proven accuracy; giving an LLM permission to restart a server.

**Done when:** The learner submits evidence, explains the two recall chains, achieves the rubric threshold and correctly handles production authorization. **Lesson authoring is not proof of learner completion.**

**Optional reference:** [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

**Next topic:** [ LLM Building Blocks & Model Choices](02_LLM_Building_Blocks_and_Model_Choices.md).
