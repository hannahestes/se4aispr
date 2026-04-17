# Evaluation Framework, Survey Instrument, and Analysis Plan

## 1. Study Design Overview

### What we are testing

EZR generates decision trees from MOOT datasets, but the raw output is not human-readable without domain context. We hypothesize that LLM-generated text descriptions of these trees improve stakeholder understanding, increase decision confidence, and that different stakeholders prefer different trees based on their role priorities and cognitive style.

### Three-phase within-subjects design

Each of the 9 personas evaluates the same set of Pareto-frontier trees across three phases:

| Phase | What the persona sees | What we measure |
|-------|----------------------|-----------------|
| **Phase 1: Raw tree** | Raw EZR decision tree output (if-then rules, feature names, split values). No context, no explanation. | Selection or skip. Confidence. Reasoning. |
| **Phase 2: Tree + generic description** | Same trees, now with an LLM-generated plain-language description adding context about what attributes mean and what trade-offs exist. Same description for all personas. | Selection or skip. Confidence. Reasoning. Whether choice changed from Phase 1. |
| **Phase 3: Knee point + personalized description** | The knee point tree only, with a description tailored to the persona's role and cognitive style. | Acceptance of knee point as compromise. Whether personalized framing changes acceptance. |

### Why this ordering matters

The within-subjects design (same persona, same trees, three passes) lets us measure the **causal effect of adding descriptions** on selection behavior. Phase 1 establishes a baseline. Phase 2 measures the effect of generic descriptions. Phase 3 tests whether personalization helps alignment on the knee point.

The skip option is critical — it captures uncertainty and is our primary measure of whether descriptions help non-technical stakeholders engage with optimization output they would otherwise find inaccessible.

---

## 2. The 9-Square Hypothesis Framework

### Role × GenderMag Matrix

|  | **Abi** (task-motivated, comprehensive, low self-efficacy, risk-averse, process-oriented) | **Pat** (task-motivated, comprehensive, medium self-efficacy, risk-averse, reflective tinkerer) | **Tim** (tech-motivated, selective, high self-efficacy, risk-tolerant, tinkerer) |
|---|---|---|---|
| **Project Manager** (tech: 1, values: time/simplicity) | PjM-Abi | PjM-Pat | PjM-Tim |
| **Product Manager** (tech: 3, values: customer impact) | PdM-Abi | PdM-Pat | PdM-Tim |
| **Software Engineer** (tech: 5, values: accuracy) | SWE-Abi | SWE-Pat | SWE-Tim |

### Predicted tree preferences (Phase 2)

Each persona should gravitate toward a different region of the Pareto frontier based on their role priority:

|  | **Abi** | **Pat** | **Tim** |
|---|---|---|---|
| **PjM** | Simplest tree (fewest features). Likely to skip in Phase 1. High skip reduction in Phase 2. | Simplest tree, but more willing to engage with alternatives. Moderate skip reduction. | Simplest tree (role priority overrides risk tolerance), but will explore options. Low skip rate even in Phase 1. |
| **PdM** | Balanced tree (knee point region). Moderate skip rate in Phase 1. | Balanced tree. Engages with trade-off information purposefully. | High-accuracy tree (tech interest + risk tolerance push toward performance). Will explore full frontier. |
| **SWE** | Stable tree (high feature frequency). Concerned about deployment risk despite valuing accuracy. | Balanced-to-accurate tree. Medium self-efficacy lets them engage with complexity. | Most accurate tree (highest win%). Comfortable with complexity and instability. Will want raw data. |

### Hypotheses by dimension

**Role effects (reading across rows — holding GenderMag constant):**

- **H-Role-1:** PjM personas will prefer trees with fewer features (lower complexity) more than PdM and SWE personas.
- **H-Role-2:** SWE personas will prefer trees with higher accuracy (win%) more than PjM and PdM personas.
- **H-Role-3:** PjM personas will have the highest skip rate in Phase 1 (raw tree). SWE personas will have the lowest.
- **H-Role-4:** The skip-rate reduction from Phase 1 to Phase 2 will be largest for PjM personas (most helped by descriptions).

**GenderMag effects (reading down columns — holding role constant):**

- **H-GM-1:** Abi-profile and Pat-profile personas (risk-averse) will prefer trees with higher stability, even within the same role.
- **H-GM-2:** Tim-profile personas (risk-tolerant) will prefer trees with higher accuracy, even within the same role.
- **H-GM-3:** Abi-profile personas will have higher skip rates than Tim-profile personas in Phase 1, within the same role.
- **H-GM-4:** Tim-profile personas (selective processing) will make faster selections and engage with fewer details in their reasoning.

**Interaction effects (specific cells):**

- **H-Int-1:** PjM-Abi will have the highest skip rate in Phase 1 (lowest tech level + lowest self-efficacy + risk-averse).
- **H-Int-2:** SWE-Tim will have the lowest skip rate and select the most complex/accurate tree (highest tech level + highest self-efficacy + risk-tolerant).
- **H-Int-3:** PdM-Pat will be the persona most likely to select the knee point (moderate role priority + medium self-efficacy + comprehensive processing + reflective tinkering = balanced decision-making).

**Description effects (Phase 1 → Phase 2 comparison):**

- **H-Desc-1:** Overall skip rate will decrease from Phase 1 to Phase 2 across all personas.
- **H-Desc-2:** The magnitude of skip reduction will be inversely proportional to technical level (PjM > PdM > SWE).
- **H-Desc-3:** Tree selections will shift toward role-appropriate priorities in Phase 2 (e.g., PjM selections move toward simpler trees when descriptions make complexity explicit).
- **H-Desc-4:** Clarity ratings will increase from Phase 1 to Phase 2 across all personas.

**Alignment effects (Phase 3):**

- **H-Align-1:** When given a personalized description of the knee point, acceptance rate will be higher than when given a generic description.
- **H-Align-2:** All 9 personas will accept the knee point as a reasonable compromise at a rate above 50%.
- **H-Align-3:** Personas whose Phase 2 selection was NOT the knee point will still accept it as a compromise when the personalized description frames it in terms of their priorities.

---

## 3. Survey Instrument

### Phase 1: Raw Tree Evaluation

For each frontier tree, present the raw EZR output (decision rules, feature names, split values, accuracy, number of features). No additional context.

#### Questions per tree:

**Q1.1 (Multiple choice):** Based on this decision tree, would you select this as your team's recommendation?
- Yes, I would select this tree
- No, I would not select this tree
- Skip — I am unsure or do not have enough information to decide

**Q1.2 (Likert 1-5):** How confident are you in your assessment of this tree?
- 1 = Not at all confident
- 2 = Slightly confident
- 3 = Moderately confident
- 4 = Very confident
- 5 = Extremely confident

**Q1.3 (Likert 1-5):** How well do you understand what this tree is telling you?
- 1 = I do not understand it at all
- 2 = I understand very little
- 3 = I understand some of it
- 4 = I understand most of it
- 5 = I fully understand it

**Q1.4 (Open-ended):** In your own words, what does this tree recommend and what trade-offs does it make?

**Q1.5 (Open-ended):** What information is missing or unclear that would help you make a decision?

#### Summary question after all trees (Phase 1):

**Q1.6 (Multiple choice):** Of all the trees you just evaluated, which ONE would you recommend for your team? (List tree IDs + "I would not recommend any of them — skip")

**Q1.7 (Open-ended):** Why did you choose that tree (or why did you skip)?

---

### Phase 2: Tree + Generic Text Description

Present the same frontier trees, now with an LLM-generated text description for each. The description adds context about what the attributes mean, explains the trade-offs in plain language, and includes stability metadata (how frequently each feature appeared across runs).

#### Questions per tree:

**Q2.1 (Multiple choice):** Now that you have a text description, would you select this as your team's recommendation?
- Yes, I would select this tree
- No, I would not select this tree
- Skip — I am unsure or do not have enough information to decide

**Q2.2 (Likert 1-5):** How confident are you in your assessment of this tree now?
- 1 = Not at all confident → 5 = Extremely confident

**Q2.3 (Likert 1-5):** How well do you understand what this tree is telling you now?
- 1 = I do not understand it at all → 5 = I fully understand it

**Q2.4 (Likert 1-5):** How clear was the text description?
- 1 = Very unclear → 5 = Very clear

**Q2.5 (Likert 1-5):** How much did the text description change your understanding of this tree compared to seeing the tree alone?
- 1 = It did not change my understanding at all
- 2 = It changed my understanding slightly
- 3 = It changed my understanding moderately
- 4 = It changed my understanding significantly
- 5 = It completely changed my understanding

**Q2.6 (Open-ended):** What new information did the text description give you that the raw tree did not?

**Q2.7 (Open-ended):** Is there anything in the text description that you found confusing, misleading, or that you disagree with?

#### Summary question after all trees (Phase 2):

**Q2.8 (Multiple choice):** Of all the trees you just evaluated with descriptions, which ONE would you recommend for your team? (List tree IDs + "I would not recommend any of them — skip")

**Q2.9 (Open-ended):** Why did you choose that tree (or why did you skip)?

**Q2.10 (Multiple choice):** Did your preferred tree change from Phase 1 to Phase 2?
- Yes — I selected a different tree
- No — I selected the same tree
- I skipped in Phase 1 but selected a tree now
- I selected a tree in Phase 1 but skipped now
- I skipped both times

**Q2.11 (Open-ended):** If your choice changed, what caused the change?

---

### Phase 3: Knee Point + Personalized Description

Present only the knee point tree with a description tailored to the persona's role priorities and GenderMag cognitive style.

#### Questions:

**Q3.1 (Likert 1-5):** This recommendation was identified as the most balanced trade-off across accuracy, simplicity, and stability. To what extent do you agree that this is a reasonable recommendation for your team?
- 1 = Strongly disagree → 5 = Strongly agree

**Q3.2 (Likert 1-5):** How well does this recommendation align with your priorities as a [Project Manager / Product Manager / Software Engineer]?
- 1 = Not at all aligned → 5 = Perfectly aligned

**Q3.3 (Multiple choice):** Would you accept this recommendation as a compromise that your entire cross-functional team (project managers, product managers, and engineers) could agree on?
- Yes — I would accept this as a team compromise
- Yes, with modifications (please specify below)
- No — I would not accept this as a compromise
- Unsure

**Q3.4 (Open-ended):** What about this description made it more or less convincing compared to the generic description you saw in Phase 2?

**Q3.5 (Open-ended):** If you would not accept this recommendation, what would need to change for you to accept it?

**Q3.6 (Open-ended):** If your team had to align on a single recommendation, what information would be most important for everyone to see?

---

## 4. Analysis Plan

### 4.1 Quantitative Analysis

#### Skip rate analysis (primary outcome)

| Metric | Comparison | Expected result | Test |
|--------|-----------|-----------------|------|
| Overall skip rate | Phase 1 vs. Phase 2 | Decrease (H-Desc-1) | McNemar's test (paired binary) |
| Skip rate by role | PjM vs. PdM vs. SWE in Phase 1 | PjM highest, SWE lowest (H-Role-3) | Chi-square or Fisher's exact |
| Skip reduction by role | (Phase 1 skip - Phase 2 skip) per role | PjM largest reduction (H-Desc-2) | Compare proportions |
| Skip rate by GenderMag | Abi vs. Pat vs. Tim in Phase 1 | Abi highest, Tim lowest (H-GM-3) | Chi-square or Fisher's exact |

#### Tree selection analysis

| Metric | Comparison | Expected result | Test |
|--------|-----------|-----------------|------|
| Preferred tree complexity | By role | PjM prefers fewest features (H-Role-1) | Kruskal-Wallis |
| Preferred tree accuracy | By role | SWE prefers highest accuracy (H-Role-2) | Kruskal-Wallis |
| Preferred tree stability | By GenderMag | Abi/Pat prefer higher stability (H-GM-1) | Mann-Whitney U |
| Selection change rate | Phase 1 → Phase 2 | Selections shift toward role priorities (H-Desc-3) | Descriptive + chi-square |

#### Likert scale analysis

| Metric | Comparison | Expected result | Test |
|--------|-----------|-----------------|------|
| Confidence | Phase 1 vs. Phase 2 | Increase (H-Desc-4) | Wilcoxon signed-rank (paired) |
| Understanding | Phase 1 vs. Phase 2 | Increase | Wilcoxon signed-rank |
| Clarity of description | By role | PjM rates lower than SWE (more technical content may confuse) | Kruskal-Wallis |
| Knee point acceptance | By role | All roles > 50% (H-Align-2) | One-sample proportion test |
| Knee point alignment | Phase 2 generic vs. Phase 3 personalized | Higher acceptance with personalized (H-Align-1) | McNemar's |

#### 9-square interaction analysis

For each cell in the 3×3 matrix, compute:
- Skip rate (Phase 1 and Phase 2)
- Modal tree selection (which tree was picked most often)
- Mean confidence score
- Mean understanding score
- Knee point acceptance rate

Present as a 3×3 heatmap for each metric. Look for:
- Row patterns (role effects)
- Column patterns (GenderMag effects)
- Diagonal patterns or outlier cells (interaction effects)

### 4.2 Qualitative Analysis (Open Coding)

#### Coding scheme for open-ended responses

Apply open coding to Q1.4, Q1.5, Q1.7, Q2.6, Q2.7, Q2.9, Q2.11, Q3.4, Q3.5, Q3.6. After initial coding, group codes into themes.

**Suggested initial code categories** (to be refined during analysis):

| Category | What to look for | Example codes |
|----------|-----------------|---------------|
| **Comprehension** | Does the persona understand the tree? | understood, misunderstood, partial-understanding, confused-by-terminology |
| **Priority expression** | What does the persona prioritize? | prioritizes-simplicity, prioritizes-accuracy, prioritizes-stability, prioritizes-coverage |
| **Risk reasoning** | How does the persona reason about uncertainty? | concerns-about-generalization, comfortable-with-risk, wants-validation, flags-instability |
| **Information needs** | What information is missing? | needs-attribute-definitions, needs-domain-context, needs-confidence-intervals, needs-examples |
| **Description impact** | How did the text description affect reasoning? | description-clarified, description-changed-mind, description-added-context, description-was-confusing |
| **Alignment reasoning** | How does the persona reason about compromise? | willing-to-compromise, unwilling-to-compromise, suggests-modification, defers-to-team |
| **Self-efficacy signals** | Does the persona express confidence or self-doubt? | blames-self, blames-explanation, confident-in-judgment, uncertain |

#### Qualitative analysis process

1. Two researchers independently code responses
2. Calculate inter-rater reliability (Cohen's kappa)
3. Resolve disagreements through discussion
4. Group codes into themes
5. Map themes to the 9-square matrix to identify role × GenderMag patterns

### 4.3 Before/After Comparison Framework

The core comparison is Phase 1 (before description) vs. Phase 2 (after description). For each persona:

```
┌─────────────────────────────────────────────┐
│           PHASE 1 (Raw Tree)                │
│                                             │
│  Selection: [tree_id or SKIP]               │
│  Confidence: [1-5]                          │
│  Understanding: [1-5]                       │
│  Reasoning: [open text]                     │
│  Missing info: [open text]                  │
├─────────────────────────────────────────────┤
│           PHASE 2 (Tree + Description)      │
│                                             │
│  Selection: [tree_id or SKIP]               │
│  Confidence: [1-5]                          │
│  Understanding: [1-5]                       │
│  Clarity of description: [1-5]              │
│  Change in understanding: [1-5]             │
│  Reasoning: [open text]                     │
│  Confusing/misleading elements: [open text] │
├─────────────────────────────────────────────┤
│           DELTA (computed)                  │
│                                             │
│  Selection changed: [yes/no]                │
│  Skip → Select: [yes/no]                    │
│  Confidence delta: [Phase2 - Phase1]        │
│  Understanding delta: [Phase2 - Phase1]     │
│  Direction of change: [toward role priority  │
│                        / away / no change]  │
└─────────────────────────────────────────────┘
```

### 4.4 Reporting Structure

The results section of the paper should present findings in this order:

1. **Phase 1 results:** Baseline skip rates and selections across the 9-square. Do role and GenderMag effects appear even without descriptions?

2. **Phase 2 results:** How do descriptions change behavior? Report skip reduction, selection shifts, confidence/understanding increases. Present the 9-square heatmaps.

3. **Phase 1 → Phase 2 deltas:** Which personas were most affected by descriptions? Does technical level predict the magnitude of change?

4. **Phase 3 results:** Knee point acceptance rates. Does personalization improve alignment? Can all 9 personas agree on the knee point?

5. **Qualitative themes:** What reasoning patterns emerge? Do they map to GenderMag facets and role priorities as predicted?

6. **Hypothesis summary table:** For each hypothesis (H-Role-1 through H-Align-3), report supported/not supported/partially supported with the relevant statistic.

---

## 5. Data Collection Schema

Each evaluation produces one record:

```json
{
  "persona_id": "PjM-Abi",
  "phase": 1,
  "tree_id": "frontier_tree_3",
  "tree_accuracy": 77,
  "tree_complexity": 3,
  "tree_stability": 57,
  "selection": "skip",
  "confidence": 2,
  "understanding": 2,
  "clarity_of_description": null,
  "change_in_understanding": null,
  "reasoning": "I don't understand what these feature names mean...",
  "missing_info": "What does Total_Amt_Chng_Q4_Q1 refer to?",
  "confusing_elements": null
}
```

Phase 2 adds clarity_of_description and change_in_understanding fields. Phase 3 adds knee_point_acceptance and alignment_score fields.

**Total data points:**
- Phase 1: 9 personas × ~7 trees = 63 per-tree evaluations + 9 summary selections
- Phase 2: 9 personas × ~7 trees = 63 per-tree evaluations + 9 summary selections
- Phase 3: 9 personas × 1 knee point = 9 evaluations
- **Total: ~144 structured evaluations + ~144 open-text responses**

---

## 6. GenderMag Alignment Verification

To confirm the evaluation design follows GenderMag precisely:

| GenderMag principle | How our design follows it |
|---|---|
| Facet values are fixed, backgrounds are customizable | We customize role/job only; all five facets use verbatim Foundations Document language |
| Personas are equally competent with math and familiar technology | Stated in every system prompt: "comfortable with mathematics and with the technology you use regularly" |
| Differences are strictly in the five cognitive facets | Stated in every system prompt: "Your differences from other people are strictly in how you approach technology" |
| Abi, Pat, Tim represent points on research-derived spectra, not stereotypes | Our hypotheses are framed as predictions from facet values, not assumptions about people |
| Pat shares 3/5 facet values with Abi | Our analysis explicitly accounts for this; we predict similar tree selection but different engagement patterns |

---

## 7. Open Questions for Discussion

1. **Is row coverage a Pareto dimension?** The current frontier uses accuracy × complexity × stability. If PdM's priority is customer impact (row coverage), should we add it as a fourth dimension or map it to an existing one?

2. **How many frontier trees?** The evaluation scales linearly with frontier size. 7 trees × 9 personas × 2 phases = 126 evaluations. If the frontier has 10+ trees, consider pruning to representative samples (e.g., the extremes + knee point + 2-3 intermediate).

3. **LLM for persona simulation:** Which model are we using (Ollama/Llama, GPT-4, Claude)? The model choice may affect how distinctly the personas behave. More capable models may differentiate personas better.

4. **Multiple runs per persona?** Should we run each persona evaluation multiple times (e.g., 5 runs) to measure LLM response variance? This would let us distinguish genuine persona effects from LLM randomness, but it multiplies the data 5x.
