#!/usr/bin/env python3 -B
"""hw2.py: tournament across MOOT data sets"""
import random, glob, statistics, traceback
from ez import csv, Data, shuffle, main, filename
from sa import sa
from locals import ls, lsRminus, saRplus
from stats import top

print("hw2 started")

ALGOS   = [sa, ls, lsRminus, saRplus]
REPEATS = 20
SAMPLE  = 50

def eg__tour(d:filename):
  "run tournament on moot/optimize/*/*.csv"
  files = glob.glob(d + "/*/*.csv")
  print(f"found {len(files)} csv files")
  wins = {a.__name__: 0 for a in ALGOS}

  for f in sorted(files):
    try:
      d0 = Data(csv(f))
      if len(d0.rows) < SAMPLE: continue
    except Exception:
      continue

    # --- baseline: untreated energies for eps ---
    baseline = []
    for _ in range(REPEATS):
      rows = shuffle(d0.rows[:])[:SAMPLE]
      d1   = Data([d0.cols.names] + rows)
      for r in d1.rows:
        baseline.append(d1.disty(r))
    sd = statistics.stdev(baseline) if len(baseline) > 1 else 1

    seen = {a.__name__: [] for a in ALGOS}
    for _ in range(REPEATS):
      rows = shuffle(d0.rows[:])[:SAMPLE]
      d1   = Data([d0.cols.names] + rows)
      for algo in ALGOS:
          print(f"Running {algo.__name__} on {f}")
          e = None
          for h, e, row in algo(d1): pass
          seen[algo.__name__].append(int(100*e))

    winners = top(seen, eps=0.35 * sd)
    for w in winners: wins[w] += 1

  print(f"\n{'algo':>12} {'wins':>6}")
  print("-" * 25)
  for name in sorted(wins):
    print(f"{name:>12} {wins[name]:>6}")

if __name__ == "__main__": eg__tour("../../moot/optimize")
#main(globals())

# Yes, restarts help a lot! It is a really easy and powerful mechanism. Restarts are an easy way to prevent the local search getting stuck. In many cases it depends on if simulated annealing compared to local search wins. In this case ls and saRplus have the highest number of wins based on the output.


        /* algo   wins */
/* ------------------------- */
        /*   ls    127 */
    /* lsRminus     16 */
        /*   sa    110 */
     /* saRplus    127 */
