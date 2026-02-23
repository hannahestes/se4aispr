# Homework 2

By: Hannah, Saba, and Mohsen

## Part 3: Analysis

### Experiment A Results

| Seed | Final Best Score | Worst Score | Average | Standard Deviation |
| ---- | ---------------- | ----------- | ------- | ------------------ |
| 1    | 0.084            | 0.666       | 0.240   | 0.033              |
| 2    | 0.097            | 0.318       | 0.105   | 0.002              |
| 3    | 0.116            | 0.518       | 0.152   | 0.003              |
| 4    | 0.132            | 0.148       | 0.135   | 0.000              |
| 5    | 0.111            | 0.501       | 0.169   | 0.004              |
| 6    | 0.086            | 0.579       | 0.087   | 0.000              |
| 7    | 0.107            | 0.714       | 0.338   | 0.053              |
| 8    | 0.068            | 0.434       | 0.119   | 0.011              |
| 9    | 0.097            | 0.323       | 0.117   | 0.002              |
| 10   | 0.114            | 0.523       | 0.132   | 0.004              |

Avg: 0.101
Std: 0.0003
Best of the Best: 0.068
Worst of the Best: 0.132


### Experiment B Results

| m_rate | Mean Score (n=5) |
|--------|------------------|
| 0.1    | 0.108            |
| 0.3    | 0.117            |
| 0.5    | 0.107            |
| 0.7    | 0.103            |
| 0.9    | 0.123            |

### Why Accept Worse Solutions?

One of the main characteristics of what dsifferentiates Simulated Annealing from other similar algorithms is the chance of accepting worse solutions in hopes to find better ones. With algorithms that take a more greedy approach, oftentimes, the best solution is a local maxima and not the global maximum (or closer to the global maximum).

An example could be that a local maxima of .4 seems really high to the rest of the surrounding landscape of .05. However if the algorithm accepted this lower solution, there is actually an increase towards the actual global maximum of .9.

### Mutation Rate Analysis

The mutation rate of **0.7** achieved the best average performance, suggesting a better outcome based on exploration. Very low mutation rates (e.g., 0.1) explore the search space slowly and risk premature convergence, while very high mutation rates (e.g., 0.9) introduce excessive randomness, preventing the algorithm from refining promising solutions. This reflects the classic exploration–exploitation tradeoff in stochastic optimization.

## Part 4: Advanced Analysis

### Results

| Method | Mean final score | Std | Stuck runs (score > 0.2) |
|--------|------------------|-----|---------------------------|
| SA     | 0.117            | 0.001 | 0 / 20 |
| Greedy | 0.114            | 0.002 | 1 / 20 (.291) |

Best score observed: **0.053**  
Worst score observed: **0.183**

### Experimental Setup

We performed an ablation study to measure the impact of the Metropolis acceptance criterion in simulated annealing. We compared:

- **Simulated Annealing (SA):** accepts improving moves and occasionally accepts worse moves with probability `exp((e - en)/T)` where `T = 1 - heat/k`.
- **Greedy hill climbing:** identical mutation operator and iteration budget, but never accepts worse moves.

Both methods were run for **20 random seeds** on `auto93.csv` using `k = 4000` iterations and mutation rate `m_rate = 0.5`. Scores correspond to distance-to-heaven (lower is better). A run was considered “stuck” if the final score exceeded **0.2**.

### Discussion

Interestingly, the greedy variant performed nearly identically to simulated annealing on this dataset. Both approaches achieved similar mean scores and exhibited only one run that became trapped in poor local optima (scores > 0.2). This suggests that the search landscape for `auto93.csv` is relatively smooth or contains broad basins of attraction, allowing greedy search to find competitive solutions without requiring probabilistic acceptance of worse moves.

In theory (Advanced Topics A1), simulated annealing provides robustness on rugged landscapes by occasionally accepting worse solutions early in the search, enabling escape from local minima. However, when the objective landscape is less deceptive or the mutation operator provides sufficient exploration, the advantage of probabilistic acceptance diminishes. Our results illustrate this case: while SA retains its theoretical benefits, the empirical difference is minimal, highlighting that the effectiveness of stochastic acceptance depends strongly on the structure of the optimization problem.
