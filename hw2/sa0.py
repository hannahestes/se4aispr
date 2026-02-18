#!/usr/bin/env python3 -B
"""
sa.py: simulated annealing optimizer
Homework skeleton - complete the TODOs
"""
import sys, math, random
from ezr import csv, distx, disty, gauss, sd, pick, Data, nearest, o, clone, spread

def sa(data, k=4000, m_rate=0.5, loud=False):
  # Extract bounds for numeric columns
  LO, HI = {}, {}
  for c in data.cols.x:
    if "mu" in c:
      LO[c.at], *_, HI[c.at] = sorted(r[c.at] for r in data.rows if r[c.at] != "?")

  def mutate(c, v):
    """TODO 1: Return mutated value.
    - For symbolic cols ("has" in c): use pick(c.has, c.n)
    - For numeric cols: Gaussian mutation within [LO, HI] bounds
      Use: LO[c.at] + (gauss(v, sd(c)) - LO[c.at]) % (HI[c.at] - LO[c.at] + 1E-32)
    """
    return pick(c.has, c.n) if "mu" not in c else LO[c.at] + (gauss(v, sd(c)) - LO[c.at]) % (HI[c.at] - LO[c.at] + 1E-32)
  

  def score(row):
    """TODO 2: Estimate row's quality using nearest neighbor surrogate.
    - Prior to running SA, take 50 rows at random and place them in a seperate space.
      - `random.shuffle(data.rows)`
      - `scoring = clone(data,data.rows[:50])`
    - Reset data from rest:
      - `data = clone(data, data.rows[:50])` # do not shuffle again
      - Use data to control (e.g.) the mutation rates in `mutate`.
    - To score a mutant:
      - Find nearest neighbor in scoring.rows using `near=nearest(scoring, row, scoring.rows)`
    - Copy neighbor's y-values to row: 
      - `for y in data.cols.y: new[y.at] = near[y.at]`
    - Return `disty(scoring, new)` # i.e. new's scrore comes from `scoring`.
    """
    # Score a mutant and copy NN y values
    near = nearest(scoring, row, scoring.rows)
    for y in data.cols.y:
      row[y.at] = near[y.at]
    return disty(scoring, row)
    

  # Initialize: random starting point
  s = random.choice(data.rows)[:]
  e, best = score(s), s[:]
  
  # Mean
  rounds = []

  for heat in range(k):
    # Generate neighbor by mutating some features
    sn = s[:]
    for c in random.choices(data.cols.x, k=max(1, int(m_rate * len(data.cols.x)))):
      sn[c.at] = mutate(c, sn[c.at])

    en = score(sn)
    
    # TODO 3: Replace "False" with Metropolis-Hastings acceptance criterion
    # Accept if: (1) en < e (better), OR (2) random.random() < exp((e - en) / T)
    # where T = 1 - heat/k (temperature that cools from 1 to 0)
    if en < e or random.random() < math.exp((e - en) / (1-heat/k)):
      s, e = sn, en
      if en < disty(data, best):
        best = s[:]
        if loud: print(f"{heat:<5} {e:.3f}", o(best))
        rounds.append(e)
  
  if len(rounds) > 0:         
    avg = sum(rounds) / len(rounds)
    std = sum([(x - avg) ** 2 for x in rounds]) / len(rounds)  
    print(f"Avg: {avg:.3f} Std: {std:.3f} Best: {max(rounds):.3f} Worst: {min(rounds):.3f}\n")
    return best, max(rounds)
  else:
    return best, 0

if __name__ == "__main__":
  # Original
  seed, file = sys.argv[1:]
  # random.seed(int(seed))
  
  data = Data(csv(file))
  # # Take 50 random rows
  # random.shuffle(data.rows)
  # scoring = clone(data, data.rows[:50])
  # # Reset Data from rest
  # data = clone(data, data.rows[:50])
  
  # sa(data, loud=True)

  # Experiment A
  # for i in range(1,11):
  #   random.seed(int(i))
    
  #   # Take 50 random rows
  #   random.shuffle(data.rows)
  #   scoring = clone(data, data.rows[:50])
  #   # Reset Data from rest
  #   data = clone(data, data.rows[:50])
    
  #   sa(data, loud=True)
  
  # Experiment B
  m_rates = {0.1, 0.3, 0.5, 0.7, 0.9}
  
  # for mut in m_rates:
  #   print(f"############# Mutation Rate: {mut} #############")
  #   bests = []
  #   for i in range(1,6):
  #     random.seed(int(i))
      
  #     # Take 50 random rows
  #     random.shuffle(data.rows)
  #     scoring = clone(data, data.rows[:50])
  #     # Reset Data from rest
  #     data = clone(data, data.rows[:50])
      
  #     best, rounds_best = sa(data, m_rate=mut, loud=True)
  #     bests.append(rounds_best)
  #   if len(bests)> 0: avg = sum(bests) / len(bests)  
  #   print(f"Mean Final Score:{avg:.3f}\n")
  
  rounds = [0.189, 0.260, 0.186, 0.249, 0.263, 0.375, 0.301, 0.284, 0.190, 0.163]
  avg = sum(rounds) / len(rounds)
  std = sum([(x - avg) ** 2 for x in rounds]) / len(rounds)  
  print(f"Avg: {avg:.3f} Std: {std:.3f} Best: {max(rounds):.3f} Worst: {min(rounds):.3f}\n")