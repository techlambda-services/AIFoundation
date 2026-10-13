# COURSE-STATE — AI Foundation + Kanchan AI Infrastructure & Agentic Systems

Updated: 2026-10-13
Repository: https://github.com/techlambda-services/AIFoundation
Current phase: **M01 REBUILT TO MATCH UPLOADED DSA TEMPLATE / LEARNER EVIDENCE PENDING**
Status vocabulary: NOT_STARTED | IN_PROGRESS | BLOCKED | VALIDATED

## Decisions and open gates
- Source TOC: 30h stated, but module breakdown sums to 32h. Corrected 30h distribution is **PROPOSED**, not yet approved in source document.
- Shared foundation: Modules 01–05 (10h).
- Kanchan specialization: Modules 06–13 (20h under proposed correction).
- Delivery schedule from the TOC: 15 × 2h; 30% theory / 70% practice goal. This is a schedule, **not a limit on depth or the amount of teaching content**.
- Capstone should be developed progressively instead of in the final two hours.
- M01 uses two topic-based teaching files without any one-hour content cap, covering the source M01 concepts and three required lab themes (DevOps map, token/context experiment, model comparison). The lessons now include concise 5W+H, limited memory hooks, depth progression, 10-point rubrics and troubleshooting. The original 40-section file is removed from main (available in Git history). No learner lab execution, independent CI run or live deployment is claimed.

## Checkpoints
| Deliverable | Status | Evidence / next action |
|---|---|---|
| Repo baseline and governance docs | VALIDATED | README, alignment, plan, standard, architecture, labs placeholder and ignore rules are committed and verified in main |
| Source TOC 30h correction | BLOCKED | Confirm replacement durations in Word source |
| Session-by-session content files | IN_PROGRESS | M01 authored in `content/module-01/`; M02 onward pending |
| M01 manuscript / TOC alignment | VALIDATED | Both topic files follow the attached DSA reference: 17 original numbered sections, Memory Hook as section 5, Completion Check, Next Topic; AI-specific Python examples and complexity trade-offs; content review only |
| M01 Topic 01 content quality audit | VALIDATED | Python 3.13.5 run passed: learned threshold=65.0, prediction at 92%=High, missing-class negative test, additional overlap and out-of-range negative cases; teaching-only synthetic classifier, **not a production accuracy claim**; learner acceptance pending |
| M01 Topic 02 context example | VALIDATED | Executed with Python 3.13.5: 13 words; budget 6 retains 6/drops 7; budget 20 retains 13/drops 0; invalid budget rejected. **This is word-count practice, not real model token measurement.** Model comparison and learner run pending |
| M01 Interview Master Plan memory hooks | VALIDATED | Both topics now use real-life recall tags, sayable **action phrases**, technical mapping, a worked trace, a cross-question/trap, mind map and memory-lock drill. This is **authoring verification**, not an observed learner recall test. |
| M01 learner lab evidence | NOT_STARTED | Instructor/learner to execute activities; capture expected vs actual evidence and teach-back |
| Starter lab environment | NOT_STARTED | Python, virtualenv, FastAPI, model/mock adapter |
| Foundation capstone | NOT_STARTED | S03–05 |
| AI Infrastructure labs | NOT_STARTED | S06–09 |
| Agent & MCP labs | NOT_STARTED | S10–12 |
| Ops/K8s/FinOps lab | NOT_STARTED | S13–14 |
| Integrated capstone and teach-back | NOT_STARTED | S15 |
| CI + reproducibility | NOT_STARTED | Add after runnable code exists |

## Independent authoring verification
- Both lesson files match the uploaded DSA reference section order with Memory Hook as the sole added structural section (20 headings per topic, including Completion Check and Next Topic).
- Memory Hook format now follows the Interview Master Plan: real-life tag → picture → action phrase → concept mapping → worked trace → interview trap → memory lock; mind maps live in Visualization. Prior labels-only hook tables were not compliant.
- Python examples executed under Python 3.13.5; assertions and stated negative cases passed. Scripts are teaching examples, not demonstrations of deployed LLMs.
- **Outstanding evidence:** actual model tokenizer measurement, real-model comparison outputs, observed learner teach-back, scored submissions, and instructor sign-off. These are not to be marked completed based on the manuscripts alone.

## Next executable step
Both authored M01 topics match the source reference section order; collect actual learner lab evidence and scored assessments before signing off delivery, then proceed to M02. Do not claim learner sign-off or live execution without evidence.

## Governance
GitHub stores code, curriculum markdown, lab steps, diagrams and checkpoints. Original approved corporate Word TOC remains separately maintained until its discrepancies are explicitly resolved.
