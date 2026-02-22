#!/usr/bin/env python3 -B
"""
sa.py: simulated annealing optimizer
Homework skeleton - complete the TODOs
Part 4 Option B (SA vs Greedy)
"""
import sys, math, random
from ezr import csv, disty, gauss, sd, pick, Data, nearest, o, clone


def sa(data, k=4000, m_rate=0.5, loud=False, greedy=False):
  # ------------------------------------------------------------
  # Per TODO2: create a separate "scoring" space of 50 random rows
  # ------------------------------------------------------------
  random.shuffle(data.rows)
  scoring = clone(data, data.rows[:50])
  data    = clone(data, data.rows[50:])   # do not shuffle again

  # Extract bounds for numeric columns (from the non-scoring data)
  LO, HI = {}, {}
  for c in data.cols.x:
    if "mu" in c:
      xs = [r[c.at] for r in data.rows if r[c.at] != "?"]
      LO[c.at], HI[c.at] = min(xs), max(xs)

  # ---------------------------
  # TODO 1: mutate(c, v)
  # ---------------------------
  def mutate(c, v):
    """Return mutated value.
    - For symbolic cols ("has" in c): use pick(c.has, c.n)
    - For numeric cols: Gaussian mutation within [LO, HI] bounds
      Use: LO[c.at] + (gauss(v, sd(c)) - LO[c.at]) % (HI[c.at] - LO[c.at] + 1E-32)
    """
    # Symbolic
    if "mu" not in c:
      return pick(c.has, c.n)

    # Numeric
    lo, hi = LO[c.at], HI[c.at]
    if v == "?":
      return lo + random.random() * (hi - lo)
    return lo + (gauss(v, sd(c)) - lo) % (hi - lo + 1E-32)

  # ---------------------------
  # TODO 2: score(row)
  # ---------------------------
  def score(row):
    """Estimate row's quality using nearest neighbor surrogate.

    - Find nearest neighbor in scoring.rows using:
        near = nearest(scoring, row, scoring.rows)
    - Copy neighbor's y-values into a NEW row:
        for y in data.cols.y: new[y.at] = near[y.at]
    - Return disty(scoring, new)
    """
    near = nearest(scoring, row, scoring.rows)
    new = row[:]  # do not overwrite caller's row in-place
    for y in data.cols.y:
      new[y.at] = near[y.at]
    return disty(scoring, new)

  # Initialize: random starting point
  s = random.choice(data.rows)[:]
  e = score(s)
  best, ebest = s[:], e

  for heat in range(1, k + 1):
    # Generate neighbor by mutating some features
    sn = s[:]
    for c in random.choices(data.cols.x, k=max(1, int(m_rate * len(data.cols.x)))):
      sn[c.at] = mutate(c, sn[c.at])

    en = score(sn)

    # ---------------------------
    # TODO 3: acceptance criterion
    # ---------------------------
    # Accept if:
    #   (1) en < e (better), OR
    #   (2) random.random() < exp((e - en) / T)
    # where T = 1 - heat/k (cooling from ~1 to ~0).
    # For greedy ablation: only accept improvements.
    T = max(1E-12, 1 - heat / k)  # avoid divide-by-zero at end

    accept = False
    if en < e:
      accept = True
    elif not greedy:
      accept = (random.random() < math.exp((e - en) / T))

    if accept:
      s, e = sn, en
      if e < ebest:
        best, ebest = s[:], e
        if loud:
          print(f"{heat:<5} {ebest:.3f}", o(best))

  # Return best row AND best score so experiments can compute stats
  return best, ebest


def _parse_args(argv):
  """Minimal argument parser to keep starter style."""
  seed = int(argv[1])
  file = argv[2]
  greedy = ("--greedy" in argv[3:])
  # optional mutation rate:
  m_rate = 0.5
  if "--mrate" in argv[3:]:
    i = argv.index("--mrate")
    m_rate = float(argv[i + 1])
  return seed, file, m_rate, greedy


if __name__ == "__main__":
  if len(sys.argv) < 3:
    print(__doc__)
    sys.exit(1)

  seed, file, m_rate, greedy = _parse_args(sys.argv)
  random.seed(seed)

  best, best_score = sa(Data(csv(file)), m_rate=m_rate, loud=(not greedy), greedy=greedy)
  
  mode = "GREEDY" if greedy else "SA"
  # Single parseable summary line (useful for scripts)
  print(f"{mode}\tseed={seed}\tm_rate={m_rate}\tscore={best_score:.3f}\tbest={o(best)}")