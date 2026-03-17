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

  # baseline = pool all observations
  pooled = [x for vals in rxs.values() for x in vals]
  sd     = statistics.stdev(pooled)

  winners = top(rxs, eps=0.35 * sd)
  sizes.append(len(winners))

  # TODO: check that all winner means are
  #       within eps of each other
  means = [sum(rks[k]) / len(rks[k]) for k in winners]
  assert max(means) - min(means) <= 0.35 * sd, means

print(f"avg winners: {sum(sizes)/len(sizes):.1f}/20")
print(f"min winners: {min(sizes)}")
print(f"max winners: {max(sizes)}")
# TODO: does larger eps -> more or fewer winners? why?

# The larger the eps, the more winners there are. Essentially, the larger the value is for eps, there is an increased variance and acceptable range which increases the number of acceptable winners.
