# Homework 2

By: Hannah, Saba, and Mohsen

## Part 3: Analysis

### Experiment A

| Seed | Final Best Score | Worst Score | Average | Standard Deviation |
| ---- | ---------------- | ----------- | ------- | ------------------ |
| 1    | 0.212            | 0.143       | 0.189   | 0.001              |
| 2    | 0.514            | 0.084       | 0.260   | 0.027              |
| 3    | 0.248            | 0.084       | 0.186   | 0.004              |
| 4    | 0.517            | 0.084       | 0.249   | 0.022              |
| 5    | 0.514            | 0.084       | 0.263   | 0.020              |
| 6    | 0.655            | 0.084       | 0.375   | 0.044              |
| 7    | 0.641            | 0.084       | 0.301   | 0.031              |
| 8    | 0.478            | 0.084       | 0.284   | 0.016              |
| 9    | 0.267            | 0.084       | 0.190   | 0.005              |
| 10   | 0.212            | 0.084       | 0.163   | 0.003              |


Avg: 0.246 
Std: 0.004 
Best of the Best: 0.375 
Worst of the Best: 0.163


### Experiment B

| m_rate | Mean Score (n=5) |
|--------|------------------|
| 0.1    | 0.396            |
| 0.3    | 0.439            |
| 0.5    | 0.215            |
| 0.7    | 0.464            |
| 0.9    | 0.562            |

### Mutation Rate Analysis

The mutation rate of **0.5** achieved the best average performance, suggesting a good balance between exploration and stability. Very low mutation rates (e.g., 0.1) explore the search space slowly and risk premature convergence, while very high mutation rates (e.g., 0.9) introduce excessive randomness, preventing the algorithm from refining promising solutions. This reflects the classic exploration–exploitation tradeoff in stochastic optimization.

## Part 4: Advanced Analysis
### Results

| Method | Mean final score | Std | Stuck runs (score > 0.2) |
|--------|------------------|-----|---------------------------|
| SA     | 0.105            | 0.035 | 0 / 20 |
| Greedy | 0.107            | 0.036 | 0 / 20 |

Best score observed: **0.053**  
Worst score observed: **0.183**

### Experimental Setup
We performed an ablation study to measure the impact of the Metropolis acceptance criterion in simulated annealing. We compared:

- **Simulated Annealing (SA):** accepts improving moves and occasionally accepts worse moves with probability `exp((e - en)/T)` where `T = 1 - heat/k`.
- **Greedy hill climbing:** identical mutation operator and iteration budget, but never accepts worse moves.

Both methods were run for **20 random seeds** on `auto93.csv` using `k = 4000` iterations and mutation rate `m_rate = 0.5`. Scores correspond to distance-to-heaven (lower is better). A run was considered “stuck” if the final score exceeded **0.2**.

### Discussion

Interestingly, the greedy variant performed nearly identically to simulated annealing on this dataset. Both approaches achieved similar mean scores and exhibited no runs that became trapped in poor local optima (scores > 0.2). This suggests that the search landscape for `auto93.csv` is relatively smooth or contains broad basins of attraction, allowing greedy search to find competitive solutions without requiring probabilistic acceptance of worse moves.

In theory (Advanced Topics A1), simulated annealing provides robustness on rugged landscapes by occasionally accepting worse solutions early in the search, enabling escape from local minima. However, when the objective landscape is less deceptive or the mutation operator provides sufficient exploration, the advantage of probabilistic acceptance diminishes. Our results illustrate this case: while SA retains its theoretical benefits, the empirical difference is minimal, highlighting that the effectiveness of stochastic acceptance depends strongly on the structure of the optimization problem.
