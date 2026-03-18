#!/usr/bin/env python3 -B
"""hw1b.py: top() with pragmatic eps"""
import random, math, statistics
from stats import top

random.seed(1)

def weibull(n=20):
  shape = random.uniform(0.5, 3)
  scale = random.uniform(1, 4)
  return [min(10,
    scale*(-math.log(random.random()))**(1/shape)*2.5)
    for _ in range(n)]

sizes = []
for trial in range(50):
  rxs = {i: weibull() for i in range(20)}

  pooled = [x for vals in rxs.values() for x in vals] 
  sd     = statistics.stdev(pooled)

  winners = top(rxs, eps=0.35 * sd)

  means = {k: sum(rxs[k]) / len(rxs[k]) for k in winners}
  best = max(means.values())

  winners = {k for k in winners if best - means[k] <= 0.35 * sd}

  sizes.append(len(winners))

  means = [sum(rxs[k]) / len(rxs[k]) for k in winners]

  if len(means) > 1:
     assert max(means) - min(means) <= 0.35 * sd, means

print(f"avg winners: {sum(sizes)/len(sizes):.1f}/20")
print(f"min winners: {min(sizes)}")
print(f"max winners: {max(sizes)}")

# The larger the eps, the more winners there are. Essentially, the larger the value is for eps, there is an increased variance and acceptable range which increases the number of acceptable winners.

/* avg winners: 3.8/20 */
/* min winners: 1 */
/* max winners: 8 */
