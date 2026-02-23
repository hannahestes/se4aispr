# Experiment A

1 | Avg: 0.240 Std: 0.033 Best: 0.084 Worst: 0.666
2 | Avg: 0.105 Std: 0.002 Best: 0.097 Worst: 0.318
3 | Avg: 0.152 Std: 0.003 Best: 0.116 Worst: 0.518
4 | Avg: 0.135 Std: 0.000 Best: 0.132 Worst: 0.148
5 | Avg: 0.169 Std: 0.004 Best: 0.111 Worst: 0.501
6 | Avg: 0.087 Std: 0.000 Best: 0.086 Worst: 0.579
7 | Avg: 0.338 Std: 0.053 Best: 0.107 Worst: 0.714
8 | Avg: 0.119 Std: 0.011 Best: 0.068 Worst: 0.434
9 | Avg: 0.117 Std: 0.002 Best: 0.097 Worst: 0.323
10 | Avg: 0.132 Std: 0.004 Best: 0.114 Worst: 0.523

```
>>> rounds = [0.084, 0.097, 0.116, 0.132, 0.111, 0.086, 0.107, 0.068, 0.097, 0.114]
>>> avg = sum(rounds) / len(rounds)
>>> std = sum([(x - avg) ** 2 for x in rounds]) / len(rounds)
>>> print(f"Avg: {avg:.3f} Std: {std:.3f} Best: {min(rounds):.3f} Worst: {max(rounds):.3f}\n")
Avg: 0.101 Std: 0.000 Best: 0.068 Worst: 0.132
```
