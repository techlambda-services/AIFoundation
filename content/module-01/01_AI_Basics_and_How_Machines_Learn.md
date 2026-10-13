# 01 — AI Basics & How Machines Learn

**Module 01 — AI, ML, Deep Learning & Generative AI Foundations**  
**Topic 01 of 02 · Kanchan · Beginner → Engineering → Advanced awareness**

> **Understand the problem first. Choose the simplest suitable approach second. Validate the result third.**

---

## 1. Problem Statement

A DevOps team handles server alerts, unknown log patterns, categorized incident tickets and maintenance updates. Someone proposes an LLM for every task. That may add cost, risk and errors without solving the real problem.

**Engineering question:** When should we use a fixed rule, a machine-learned prediction, generated language or an approval-controlled workflow?

## 2. Learning Objectives

After this topic, explain and demonstrate:
1. The difference between **AI, ML, Deep Learning and Generative AI**, including their overlap.
2. **Supervised, unsupervised and reinforcement learning** with one practical example each.
3. **Datasets, features, labels, models, parameters/weights and foundation models**.
4. **Training versus inference**, and why a normal prompt does not retrain a model.
5. A safe decision for Linux/DevOps use cases, supported by practical evidence.

**Prerequisites:** General software/Linux familiarity, text editor and basic Python if running the optional code. No paid API, GPU, production server or real company logs.

## 3. 5W + H Framework

### What?
**AI** is the broad field of systems performing tasks that require intelligent behavior. **ML** learns patterns from data; **DL** uses multi-layer neural networks. **GenAI** creates text, code, images or other content.

### Why?
Different problems need different solutions. A fixed disk-space threshold is easier with a rule; classifying hundreds of labeled tickets may justify supervised ML.

### When?
Decide **before** buying models, connecting sensitive data or authorizing operations.

### Where?
Operations monitoring, support-ticket triage, anomaly discovery, incident communications and knowledge assistance.

### Who?
Software engineers, SRE/DevOps teams, AI engineers, technical trainers and reviewers responsible for safe production changes.

### How?
Define the outcome → identify data and risks → choose a technique → validate against examples → obtain human authorization for risky actions.

## 4. Real-Life Analogy

Picture a company:

- **Company:** the broad AI discipline.
- **Apprentice:** ML learns to classify requests from past examples.
- **Specialist layer-cake team:** deep learning handles complex representations.
- **Creative studio:** GenAI drafts a new customer communication.
- **Gym:** a team learns during training.
- **Match day:** it applies learned skill to a new problem during inference.

This analogy is for recall, not a strict organizational chart: GenAI overlaps multiple AI approaches; contemporary LLM-based GenAI commonly uses deep learning.

## 5. Memory Hook

**Interview Master Plan rule:** **Real-life picture → action phrase → exact concept mapping → trace → interview trap → memory lock.** A name alone is not a memory hook.

### Hook A — Umbrella Office: AI vs ML vs DL vs GenAI

**Picture it:** A large office is sheltered under an **umbrella**. An **apprentice** learns how to sort tickets; a specialist builds a **layer cake** of learned representations; a **creative studio** writes a new incident update.

**Say the action phrase:** **"Cover All → Learn Examples → Stack Layers → Create Content."**

| Action | Exact engineering meaning |
|---|---|
| **Cover All** | **AI** is the broad discipline, including rules and ML |
| **Learn Examples** | **ML** fits patterns from datasets |
| **Stack Layers** | **DL** is ML using multi-layer neural networks |
| **Create Content** | **GenAI** generates text, code or media, often using DL |

**Trace:** For a disk incident: (1) an AI system could include a **fixed alert rule**; (2) ML could learn from labeled tickets; (3) a deep model could learn more complex text features; (4) a GenAI assistant could draft a reviewed incident summary. These are **alternative or overlapping capabilities**, not a required four-stage pipeline.

**Interview answer (20 seconds):** "AI is the umbrella. ML learns from examples, and DL is a neural-network family within ML. GenAI describes systems generating content; modern LLM-based GenAI commonly uses deep learning."

**Trap:** "Is all GenAI exactly one additional layer of DL?" **No.** The office story aids recall, not an exhaustive class hierarchy.

### Hook B — School, Socks, Game: Three Learning Signals

**Picture it:** A teacher checks an **answer key**; a child sorts unmarked **socks** into groups; a player changes moves based on **game points**.

**Say the action phrase:** **"Match Labels → Find Groups → Earn Rewards."**

| Action | Learning technique | Micro-scenario |
|---|---|---|
| **Match Labels** | Supervised learning | Use tickets with known "High"/"Low" severity |
| **Find Groups** | Unsupervised learning | Group previously unlabeled error messages |
| **Earn Rewards** | Reinforcement learning | Learn actions from reward in a **simulation** |

**Trace:** Ask "Do we have correct target labels?" → **Yes: supervised**. **No:** "Are we discovering structure?" → **Unsupervised**. "Are we choosing actions and receiving rewards?" → **Reinforcement**. These are diagnostic clues, not an automatic algorithm-selector.

**Interview answer:** "Supervised learning uses labeled examples; unsupervised learning finds structure without target labels; reinforcement learning learns policies from action-reward interaction."

**Trap:** "A chatbot receives a user's thumbs-up. Is it automatically training by reinforcement learning during this chat?" **No**; feedback collection and weight updates are separate processes.

### Hook C — Gym and Match Day: Model Lifecycle

**Picture it:** An athlete improves during **gym practice**, then plays a new opponent on **match day**. The coach reviews results to find weaknesses.

**Say the action phrase:** **"Examples In → Weights Change → New Case In → Prediction Out → Verify."**

| Action | Model lifecycle |
|---|---|
| **Examples In** | Collect a training dataset with features and, for supervised tasks, labels |
| **Weights Change** | Training fits model parameters |
| **New Case In** | Send previously unseen input to a trained model |
| **Prediction Out** | Inference applies the existing parameters |
| **Verify** | Compare with independent evidence or labeled test cases |

**Trace:** In the Topic 01 Python example, four labeled disk-use cases determine a threshold of **65** (toy **training**). The new **92%** usage produces **High** (**inference**); evaluate accuracy only with appropriate unseen labeled data.

**Interview answer:** "Training updates learned parameters using data; inference applies those parameters to fresh input. An ordinary prompt does not retrain a model."

**Trap:** "If the output sounds correct, is the model validated?" **No**—prediction quality requires testing.

**Memory lock — close the page:** Say **Cover All → Learn Examples → Stack Layers → Create Content**; **Match Labels → Find Groups → Earn Rewards**; **Examples In → Weights Change → New Case In → Prediction Out → Verify**. Explain one *new* DevOps example for each and answer the three traps without reading.

## 6. Visualization

**Interview Master Plan mind map** — see the relationships behind the recall phrases.

~~~text
AI — Cover All
├─ Rules: predefined decisions (no model training needed)
└─ ML — Learn Examples
   ├─ Supervised — Match Labels
   ├─ Unsupervised — Find Groups
   ├─ Reinforcement — Earn Rewards
   └─ DL — Stack Layers
        └─ Modern LLM-based GenAI often uses DL — Create Content

Model lifecycle — Gym → Match Day
Examples In → Weights Change → New Case In → Prediction Out → Verify
~~~


~~~mermaid
flowchart TB
  AI[AI — Umbrella] --> RULES[Rules and Search]
  AI --> ML[ML — Apprentice]
  ML --> CLASSIC[Classical ML]
  ML --> DL[Deep Learning — Layer Cake]
  DL --> LLM[Modern LLM-based GenAI]
  DATA[Labeled examples] --> TRAIN[Training — Gym]
  TRAIN --> MODEL[Model / learned parameters]
  MODEL --> PRED[Inference — Match Day]
  NEW[New ticket] --> PRED
~~~

**Important:** The left branch shows a common technical path, not an exhaustive definition of all possible generative systems.

## 7. Simple Explanation

- **Fixed rule:** You write an explicit condition such as disk usage above 90%.
- **Supervised ML:** Learn from examples with an **answer key** (ticket text and correct priority).
- **Unsupervised ML:** Group similar log lines without known category labels.
- **Reinforcement learning:** Learn how to act from **rewards**, often in a simulated environment.
- **GenAI:** Draft an incident report, then check it for unsupported claims.
- **Training:** Learn or adjust model parameters using data.
- **Inference:** Use an existing model on a new input; the ordinary prompt does not itself update model weights.

## 8. Engineering Explanation

**Dataset** = examples; **feature** = measurable input; **label** = supervised target; **model** = learned mapping; **weights/parameters** = learned numerical settings that influence outputs. A **foundation model** is broadly pretrained and can support multiple tasks with prompting, tools, retrieval or appropriate adaptation.

Example: From historical labeled incidents, train a classifier to predict severity. Evaluate it on **held-out, independently labeled incidents** that were not used to choose or train the model. After approval, run inference on a new ticket.

**Advanced awareness:** More data is not automatically better; representative examples, clean labels, held-out tests and monitoring matter. Reward feedback does not make every LLM agent a reinforcement-learning system.

## 9. Real Project Usage

**Synthetic project:** "AI-Aware DevOps Triage".

| Need | Sensible starting point | Production control |
|---|---|---|
| Alert when disk usage exceeds 90% | Fixed rule | Alert verification |
| Discover recurring unknown log patterns | Unsupervised clustering | Human review of cluster meaning |
| Predict a ticket category from labeled history | Supervised ML | Check misclassifications |
| Draft a maintenance update | GenAI, optional | Review factual statements |
| Restart a critical service | Approved deterministic workflow | Least privilege, change approval and audit |

**Case study decision:** AI-generated guidance may help diagnose an incident; it must not be granted unrestricted permissions to run destructive commands.

## 10. Python Example

A tiny **teaching-only** supervised model learns a threshold from labeled, synthetic disk-usage examples. It is deliberately not a neural network or a realistic production classifier.

**Save as** `topic01_threshold_model.py`; run `python topic01_threshold_model.py` (or `python3`). Python 3.x, standard library only.

~~~python
def train_threshold(examples):
    low = [usage for usage, label in examples if label == "Low"]
    high = [usage for usage, label in examples if label == "High"]
    if not low or not high or max(low) >= min(high):
        raise ValueError("Need separable labeled Low and High examples")
    return (max(low) + min(high)) / 2


def predict(usage, threshold):
    if not 0 <= usage <= 100:
        raise ValueError("Disk utilization must be 0..100")
    return "High" if usage >= threshold else "Low"


training_data = [(25, "Low"), (40, "Low"),
                 (90, "High"), (95, "High")]
threshold = train_threshold(training_data)
print("learned threshold:", threshold)
print("new ticket at 92%:", predict(92, threshold))
assert threshold == 65.0
assert predict(30, threshold) == "Low"
assert predict(92, threshold) == "High"

# Negative test: bad training data should fail clearly.
try:
    train_threshold([(95, "High")])
except ValueError:
    print("negative training test: passed")
else:
    raise AssertionError("Missing class should be rejected")
~~~

**Expected output:**
~~~text
learned threshold: 65.0
new ticket at 92%: High
negative training test: passed
~~~

**Interpretation:** The threshold is computed from examples during toy **training**. Calling `predict` uses that threshold at **inference**. The examples are too small to support accuracy claims; no real incident model is validated.

## 11. Complexity Discussion

For this teaching example, scanning **n** training examples to compute two class extrema takes **O(n)** time; each subsequent threshold prediction takes **O(1)** time. This is **not** a performance claim about neural networks, LLMs or production classifiers.

For real systems, also consider data labeling effort, quality of predictions, latency, monitoring, operational cost, confidentiality and risk of a mistaken action. A fixed rule is usually a better default when its behavior fully expresses the requirement.

## 12. Hands-on Exercise

### Exercise A — Choose the approach
Complete these five rows **before** viewing the expected direction below.

| Scenario | Your technique | Why? | Risk / human approval |
|---|---|---|---|
| Disk usage crosses a known threshold | | | |
| Cluster unfamiliar log patterns | | | |
| Categorize tickets with historical labels | | | |
| Draft an incident explanation | | | |
| Restart a critical production service | | | |

**Expected direction:** fixed rule; unsupervised ML; supervised ML; optional GenAI with review; controlled operational automation requiring authorization.

### Exercise B — Training versus inference
Run the Python example if possible. Identify the **labeled data**, the learned **threshold**, and the **new-input prediction**. Change the unseen input from 92% to 30%; observe the expected "Low". Try a missing class and show the negative test.

**Expected evidence:** command, output, explanation of training/inference and limits. If Python is unavailable, calculate the threshold manually and label your evidence **manual, not executed**.

### Exercise C — Trainer teach-back
Explain the memory hooks without looking, then answer: **Does a prompt retrain the weights?** No. **Can this toy classifier establish production accuracy?** No. **Should an LLM restart a service without authorization?** No.

## 13. Best Practices

- Start with the simplest approach that meets the objective (KISS/YAGNI).
- Keep training data, evaluation data and business assumptions clearly separated.
- Prefer synthetic examples in teaching; protect production logs and credentials.
- Document model limits; use human approval for consequential operations.
- Keep code single-purpose and test expected as well as invalid inputs (SOLID where applicable).

## 14. Common Mistakes

| Mistake | Correction |
|---|---|
| "AI, ML and GenAI mean the same thing" | AI is broader; approaches overlap but differ |
| "Every prediction needs an LLM" | Often a fixed rule or classical ML suffices |
| "A normal prompt trains the model" | Ordinary prompting uses existing learned weights |
| "Four examples prove accuracy" | Test separately on representative held-out examples |
| "AI output is an approved command" | Operational authority is a separate permission decision |

**Troubleshooting:** No Python? Use the manual threshold exercise. The script fails with a missing class? That is the intended negative case. If the output differs, confirm you copied the four labeled examples and valid input values.

## 15. Interview Questions

1. **AI vs ML vs DL vs GenAI?** Explain the umbrella and overlap, with one concrete example.
2. **Supervised vs unsupervised vs reinforcement?** Contrast labels, no labels and reward feedback.
3. **Training vs inference?** Which stage changes parameters?
4. **What is a foundation model?** Broadly pretrained reusable model; not necessarily fit for every enterprise task.
5. **When avoid a model?** When deterministic logic is safer, cheaper and sufficient.
6. **How to validate incident classification?** Separate unseen labeled test data, failure cases and production review.
7. **What is wrong with giving a chat model root access?** Authorization, hallucination, audit and destructive-action risks.

## 16. Quick Revision

**AI family:** **Cover All → Learn Examples → Stack Layers → Create Content**.  
**Learning signals:** **Match Labels → Find Groups → Earn Rewards**.  
**Model lifecycle:** **Examples In → Weights Change → New Case In → Prediction Out → Verify**.

**Interview recall drill:** Say each action phrase, explain its technical meaning, then apply it to one fresh incident scenario **without reading**. If you can repeat the name but cannot trace the actions, the hook is not yet mastered.

**One-line takeaway:** Choose the technique based on data, task and operational risk—not because a model sounds advanced.

## 17. Assignment

**Foundation:** Explain the six core terms and draw the AI family.  
**Applied:** Finish Exercises A–C and submit the expected-vs-observed Python output or an explicitly manual demonstration.  
**Interview:** Defend one rule/ML/GenAI decision for DevOps incident triage.  
**Challenge:** Propose a privacy-safe, approval-controlled triage workflow and describe how it would be evaluated.

**Suggested 10-point rubric:** technique choices **4**, training/inference explanation **2**, worked-example evidence including negative case **2**, safety and teach-back **2**. **Passing recommendation: 8/10**, including correct production authorization. A trainer scores only observed work.

## 18. Additional Reading

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — ML foundations and evaluation.
- [Google Responsible AI practices](https://ai.google/responsibility/responsible-ai-practices/) — quality and safety concepts.
- [Python documentation](https://docs.python.org/3/) — run the standard-library example.

## Completion Check

- [ ] Explain AI/ML/DL/GenAI correctly with a real-life analogy.
- [ ] Explain supervised, unsupervised and reinforcement learning.
- [ ] Identify dataset, label, parameter, foundation model, training and inference.
- [ ] Complete the DevOps technique-choice table with safety reasoning.
- [ ] Run or manually reproduce the threshold example; label execution honestly.
- [ ] Describe the negative test and why the small sample does not establish accuracy.
- [ ] Complete a trainer-reviewed knowledge check without reading definitions.

**Evidence file:** `01_AI_Basics_Evidence.md` (one concise submission; never include sensitive data). **Status remains pending until learner evidence is reviewed.**

## Next Topic

[02 — LLM Building Blocks & Model Choices](02_LLM_Building_Blocks_and_Model_Choices.md): transformers, tokens, context windows, embeddings, multimodal systems and model/runtime choices.
