# 01 — AI Basics & How Machines Learn
**Kanchan · Module 01 · Hour 1 of 2 (60 min)**  
**18 min concepts + 42 min practice · No paid tools required**

> **Remember:** Choose the problem first, then decide whether rules, learning, or generation actually help.

## 1. The problem and learning goal — 4 min (concepts)

A DevOps team has alerts, error logs, tickets and maintenance messages. Should it use a rule, machine learning, or Generative AI?

After this hour, you should be able to:
- Explain **AI, ML, Deep Learning and Generative AI** in plain language.
- Distinguish **supervised, unsupervised and reinforcement learning**.
- Explain **dataset, model, weights, foundation model, training and inference**.
- Choose a suitable technique for five Linux/DevOps tasks.

**Prerequisites:** Basic Linux/DevOps familiarity, browser or paper, text editor. Use **synthetic** data, never real customer logs.

**5W+H:** AI techniques (what) for safe incident handling (why), chosen by DevOps teams (who/where), before automation (when), through task classification and verification (how).

## 2. One analogy + Memory Hooks — 6 min (concepts)

Think of a company with different teams:

| Term | Memory Hook | Remember it this way |
|---|---|---|
| AI | ☂️ **Umbrella** | The broad field, including rules, search and learning |
| ML | 🎓 **Apprentice** | Learns patterns from examples |
| Deep Learning | 🎂 **Layer Cake** | ML using neural networks with many layers |
| GenAI | 🎨 **Creative Studio** | Produces new text, code, images, etc. |
| Training | 🏋️ **Gym** | Learns/adjusts model weights |
| Inference | 🏟️ **Match Day** | Uses learned weights on new input |

**Say it aloud:** **Umbrella → Apprentice → Layer Cake → Creative Studio**.  
**Say it aloud:** **Gym → Match Day**.

*Technical accuracy:* AI is broader than ML; Deep Learning is part of ML. GenAI describes systems that generate content; modern LLM-based GenAI commonly uses Deep Learning, but the categories are not perfectly nested.

## 3. Understand the essentials — 8 min (concepts)

| Situation | Best basic explanation |
|---|---|
| CPU > 90% triggers a fixed alert | **Rule**; the system need not learn |
| Ticket + correct priority are provided as training examples | **Supervised ML** |
| Similar logs are grouped without category labels | **Unsupervised ML** |
| A simulated controller is rewarded for good decisions | **Reinforcement learning** |
| A model drafts a human-readable maintenance notice | **Generative AI** |

**Training vs inference:** During training, a learning algorithm adjusts the model's **weights** using a **dataset**. During inference, the trained model predicts or generates for a new request. Sending an ordinary prompt does **not** retrain its weights.

**Model basics:** A dataset contains examples; learned numerical weights define a trained model. **Foundation models:** A broadly pretrained model can be adapted through prompts, tools, retrieval or additional training.

**Depth progression:** Beginner: identify the technique. Engineer: inspect datasets, labels and weights. Advanced awareness: test reliability and the reward/validation design before deployment.

~~~mermaid
flowchart LR
    A[AI Umbrella] --> B[Rules and Search]
    A --> C[Machine Learning]
    C --> D[Deep Learning]
    D --> E[Modern LLM-based GenAI]
    F[Training examples] --> G[Training: Gym]
    G --> H[Learned Model]
    H --> I[Inference: Match Day]
    J[New Request] --> I
~~~

## 4. Do it yourself — 42 min (practice)

### Lab A — Map five DevOps tasks (20 min)
For each task, decide **rule / supervised ML / unsupervised ML / GenAI / approval-controlled operation**, and write why.

| Task | Your choice | Why + one risk |
|---|---|---|
| Send alert when disk usage exceeds 90% | | |
| Group unknown error messages | | |
| Classify tickets with labeled past examples | | |
| Draft a maintenance notice | | |
| Restart a production server | | |

**Self-check (after answering):** rule; unsupervised ML; supervised ML; optional GenAI with human review; authorized automation with explicit approval. **A generative model should not independently restart production.**

### Lab B — Gym or Match Day? (12 min)
Mark each statement **Training** or **Inference**.

1. Update weights using thousands of labeled tickets.
2. Predict severity for today's new ticket.
3. Fine-tune a model on approved examples.
4. Ask a deployed model to explain an alert.

**Check:** 1 Training; 2 Inference; 3 Training; 4 Inference.

**Discuss:** Why is a prompt usually inference, not training? Answer: the deployed model uses existing weights; normal prompting does not optimize them.

### Lab C — Teach-back (10 min)
Without reading the tables:
1. Explain the **Umbrella → Apprentice → Layer Cake → Creative Studio** chain.
2. Explain **Gym → Match Day** using one Linux incident.
3. Give one reason **not** to use GenAI for a simple alert.
4. Draw **data → training → model → inference → output** on paper.

**Expected:** a correct explanation plus a small diagram. If a step is unclear, revisit only the relevant memory hook.

## 5. Submit one piece of evidence

Create **01_Hour1_Evidence.md** (or one handwritten page) containing:
- Your five-row task map with rationale and risks.
- Four Gym/Match Day answers.
- Your simple model lifecycle diagram.
- One mistake you corrected.

**Assessment (10 points):** Five correct task choices with rationale (5); four training/inference answers (2); two memory chains explained (2); safe human approval (1). **Pass: 8/10 or higher**, with production safety reasoning correct.

**Troubleshooting:** No API/model access is needed. If unsure whether a task needs ML, ask whether labels, unknown clusters or a reward signal exist. Use a fixed rule when learning adds no value.

**Done when:** all five decisions are reasoned, all four training/inference cases are correct, and you can explain the two memory chains unaided. The trainer should review your results; reading this page alone is not completion.

**Avoid these mistakes:** AI ≠ only GenAI; DL ≠ all of AI; ordinary prompts ≠ model retraining; GenAI output ≠ permission to change infrastructure.

**Next:** [Hour 2 — LLM Building Blocks & Model Choices](02_LLM_Building_Blocks_and_Model_Choices.md).
