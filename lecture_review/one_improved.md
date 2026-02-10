# CSC491/591 — Review Answers (Improved)

## Topic 1: Data Representation & Pre-processing

### 1. Normalization (Min–Max)

**(a) Why is it algorithmically necessary to normalize data before calculating distances?**  
Distance-based algorithms assume all dimensions contribute comparably. Without normalization, attributes with large numeric ranges dominate distance calculations regardless of importance, distorting similarity judgments.

**(b) Min–max normalization formula**  
\[
\text{norm}(x) = \frac{x - \min}{\max - \min}
\]

---

### 2. Handling Symbolic Data

**(a) How does the CSV standard distinguish numeric vs symbolic columns?**  
Column names starting with **uppercase letters** denote numeric data; lowercase letters denote symbolic data.

**(b) How is central tendency represented for symbols?**  
Use the **mode** as the expected value and **entropy** to measure dispersion.

---

### 3. The “Heaven” Point

**(a) Define the Heaven point.**  
The Heaven point is an idealized reference vector where every objective achieves its best possible normalized value (1 for maximization goals, 0 for minimization goals).

**(b) Heaven point for minimizing weight and maximizing safety**  
Heaven = **(0, 1)**

---

### 4. Euclidean Distance

**(a) What does Euclidean distance measure here?**  
It measures how far a configuration is from the ideal (Heaven) across all objectives simultaneously.

**(b) Distance formula**  
\[
d(\mathbf{x}, \mathbf{h}) = \sqrt{\sum_{i=1}^{n} (x_i - h_i)^2}
\]

---

### 5. Data Headers & Goals

**(a) Meaning of `+` and `-` in headers**  
`+` indicates a goal to maximize; `-` indicates a goal to minimize.

**(b) How are columns without `+` or `-` treated?**  
They are **decision variables (inputs)**, not optimization goals.

---

## Topic 2: Statistical Heuristics

### 6. Cohen’s Rule (Effect Size)

**(a) Definition of a small effect**  
A difference smaller than **0.35 × standard deviation** is considered negligible.

**(b) Apply Cohen’s rule**  
Difference = 82 − 80 = 2  
Threshold = 0.35 × 10 = 3.5  
Since 2 < 3.5, the difference is a **small (non-meaningful) effect**.

---

### 7. Standard Deviation

**(a) What does standard deviation measure?**  
The spread or variability of values around the mean.

**(b) SD near zero indicates**  
Loss of diversity; the population has converged to nearly identical solutions.

---

### 8. Expected Values (Symbols)

**(a) Expected value for symbolic data**  
The **mode**.

**(b) Probability of expected value**  
For `[A, B, A, C, A, B]`:
- A = 3/6 = 0.50  
- B = 2/6 ≈ 0.33  
- C = 1/6 ≈ 0.17  

Expected value = **A**

---

### 9. “Half of You Die” Heuristic

**(a) Strategy explanation**  
Recursively discard the half of the population farthest from Heaven, focusing computation on promising regions.

**(b) Why this is powerful**  
Logarithmic reduction (\(O(\log n)\)) drastically reduces evaluations compared to deep learning or brute force.

---

### 10. Sampling Validity

**(a) Why small samples work**  
SE performance spaces often have smooth structure and many near-optimal solutions.

**(b) Assumption about solution space**  
The space has **low intrinsic dimensionality** and broad plateaus.

---

## Topic 3: Optimization Algorithms

### 11. Genetic Algorithms

**(a) What does the “Kid” represent?**  
A new candidate solution created by recombining parent genomes.

**(b) Single-point crossover example**  
Parents:  
A = [1 | 1 1]  
B = [0 | 0 0]  

Kid = **[1, 0, 0]**

---

### 12. Mutation

**(a) Purpose of mutation**  
Maintain diversity and allow escape from local optima.

**(b) Risk of 0% mutation**  
Premature convergence to local optima.

---

### 13. Simulated Annealing

**(a) Acceptance of worse solutions**  
Worse solutions are accepted probabilistically based on temperature and loss magnitude.

**(b) Breakfast metaphor explanation**  
Temperature allows exploration early (trying new cereals) and exploitation later (settling on the best).

---

### 14. Stochasticity

**(a) Why results differ between runs**  
Random initialization and stochastic decisions.

**(b) Responding to “not deterministic” complaints**  
Use Cohen’s effect size to show differences are statistically insignificant.

---

### 15. Local vs Global Optima

**(a) Define a local optimum**  
A solution better than its neighbors but not globally optimal.

**(b) Why greedy algorithms fail**  
They cannot escape local optima.

---

## Topic 4: Software Analytics & Research Concepts

### 16. Configuration Optimization (FLASH)

**(a) SQLite optimization goal**  
Maximize performance while minimizing cost using very few evaluations.

**(b) Why brute force is impossible**  
\(2^{50}\) configurations is computationally infeasible.

---

### 17. Transfer Learning

**(a) Definition**  
Reusing models or insights from prior systems to accelerate optimization on new systems.

**(b) Why 2020 models fail in 2026**  
**Concept drift** due to changes in workloads, hardware, or environments.

---

### 18. Garbage In, Garbage Out (Labeling)

**(a) Effect of label quality**  
Model performance is capped by label accuracy; noisy labels limit achievable performance.

**(b) Cost-effective strategy**  
Label a small informative subset (active learning or surrogates), then infer the rest.

---

### 19. Multi-Objective Trade-offs

**(a) Conflicting goals**  
Improving one objective degrades another.

**(b) Using Distance to Heaven**  
Aggregates all objectives into a single measure of closeness to the ideal solution.

---

### 20. “Less Is More” Principle

**(a) Core technical argument**  
Many problems have simple structure; additional complexity yields diminishing returns.

**(b) Model choice**  
Choose linear regression: nearly identical accuracy with far lower cost and higher interpretability.

