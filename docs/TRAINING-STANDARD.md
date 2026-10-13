# Techlambda Content Standard — Kanchan AI Foundation

**Source of structure:** `01-Introduction-to-DSA(3).md` (user-supplied DSA reference). Preserve its section order and separation. **Only one section is added: Memory Hook immediately after Real-Life Analogy.** Topic-specific technology substitutions (such as Python Example instead of Java Example) are allowed; no other headings are collapsed or skipped.

## Required section order for every topic

1. **Problem Statement**
2. **Learning Objectives**
3. **5W + H Framework** — What, Why, When, Where, Who, How
4. **Real-Life Analogy**
5. **Memory Hook** — **only new section** compared with the reference
6. **Visualization**
7. **Simple Explanation**
8. **Engineering Explanation**
9. **Real Project Usage**
10. **Python / AI Example** — equivalent role to Java Example in DSA reference
11. **Complexity Discussion** — resource, quality, latency, operational cost and trade-offs where applicable
12. **Hands-on Exercise**
13. **Best Practices**
14. **Common Mistakes**
15. **Interview Questions**
16. **Quick Revision**
17. **Assignment**
18. **Additional Reading**

Then retain the reference's two closing sections, unnumbered:
- **Completion Check** — checklist verified with evidence
- **Next Topic**

## Memory Hook — Interview Master Plan contract

The section **Memory Hook** must be a **recall system**, not a glossary of catchy labels. Adapt the approved DSA Memory Book pattern (e.g., **Two Pointers — Two Hands, Two Ends, One Meeting Point; Binary Search — Dictionary / Open Middle, Reject Half, Repeat; Array Rotation — Merry-Go-Round; Second Largest — Podium; XOR — Socks**).

For every important recall concept or coherent concept-group, provide all of:

1. **Real-life tag** — one short, concrete familiar object, scene or action.
2. **Picture/analogy** — a two-sentence scene the learner can visualize.
3. **Exact memory phrase** — a *sayable action sequence* (e.g., "Open Middle → Reject Half → Repeat"), not a title list.
4. **Precise technical mapping** — each word/action maps to the actual concept, with limits of the analogy.
5. **Trace / worked scenario** — walk a tiny real problem through the phrase in 2–4 visible steps. An action/state storyboard is welcome; do not call a static trace an interactive animation.
6. **Mind map connection** — show relationships in the existing **Visualization** section, without adding another top-level section.
7. **Interview recall + trap** — a short explanation the learner can speak and one common cross-question or edge case that tests understanding.
8. **Memory lock** — ask the learner to reproduce the phrase and use it on a new example **without reading**.

**Quality gates:** a label alone ("Umbrella", "Lego", "Gym") is **not sufficient**; an arrow-separated list of nouns is not an action-based hook. Keep the number of hooks minimal, reuse the same canonical phrase in Visualization/Quick Revision/Interview/Assignment, and do not replace the real technical definition with an inaccurate metaphor. **No additional top-level lesson headings**; preserve the user-supplied DSA section order and KISS/DRY/YAGNI/SOLID.

## Teaching quality rules

- Apply **KISS** within sections: concise, plain, precise explanations. Do **not** remove, merge, reorder or renumber sections to make the file shorter.
- Apply **DRY**: link or briefly reference a prior explanation; do not repeat paragraphs across sections.
- Apply **YAGNI**: do not add unrelated technologies, theoretical detours, libraries or labs. Include TOC-mandated concepts.
- Apply **SOLID** only when teaching code or design: small, single-purpose examples that are simple to test and reuse; no unnecessary design-pattern demonstrations.
- Progress from **Beginner → Engineering → Advanced awareness** with the same learning outcome, using real-life examples and a useful diagram.
- Maintain a **30% explanation / 70% applied-work** training objective; **do not cap content to 60 minutes** or label topic files Hour 1/Hour 2. Scheduled contact time is planning metadata only.
- Each code lab identifies prerequisites, how to run, expected output, negative/error case, validation and safe evidence; do not claim executions without records.
- Prefer free, local-first tools, synthetic training inputs and no API keys. Never submit customer records or credentials.
- Provide expected answers for checks, a simple assessment rubric and instructor review gating; never claim a learner passed without learner evidence.
- Keep **one ordered Markdown file per topic**; no folder per topic.

## Review gate

Review heading order, source TOC coverage, teaching clarity, lab reproducibility, mistakes and safe assumptions, expected versus actual evidence and cross-file README/COURSE-STATE references. An authored manuscript can be structurally **VALIDATED** while actual learner execution remains **PENDING**.
