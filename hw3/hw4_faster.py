#!/usr/bin/env python3 -B
"""hw4_fast.py: hyperparameter sensitivity (grad only, faster)"""
import random, glob, statistics, os
from ez import csv, Data, shuffle, main, filename
from sa import sa
from locals import ls
from stats import top
from multiprocessing import Pool, cpu_count

SA_MS    = [0.1, 0.3, 0.5, 0.7, 0.9]
LS_RS    = [0, 25, 50, 100, 200]
REPEATS  = 5   # reduced from 20 for speed
SAMPLE   = 50

def process_file(f):
    """Run one CSV file and return wins dict for that file."""
    try:
        d0 = Data(csv(f))
        if len(d0.rows) < SAMPLE: return None
    except Exception:
        return None

    # baseline eps
    baseline = []
    for _ in range(REPEATS):
        rows = shuffle(d0.rows[:])[:SAMPLE]
        d1   = Data([d0.cols.names] + rows)
        for r in d1.rows:
            baseline.append(d1.disty(r))
    sd = statistics.stdev(baseline) if len(baseline) > 1 else 1

    # treatments
    treatments = ([("sa",m) for m in SA_MS] +
                  [("ls",rs) for rs in LS_RS])
    seen = {t: [] for t in treatments}

    for _ in range(REPEATS):
        rows = shuffle(d0.rows[:])[:SAMPLE]
        d1   = Data([d0.cols.names] + rows)
        for name, param in treatments:
            if name == "sa":
                for _, e, _ in sa(d1, m=param): pass
            elif name == "ls":
                for _, e, _ in ls(d1, restarts=param): pass
            else:
                continue
            seen[(name, param)].append(int(100 * e))

    winners = top(seen, eps=0.35 * sd)
    return winners

def eg__hparam(d:filename):
    "hyperparameter sensitivity across MOOT, parallel version"
    files = glob.glob(os.path.join(d, "*/*.csv"))
    print(f"found {len(files)} csv files")

    wins = {t: 0 for t in ([("sa",m) for m in SA_MS] + [("ls",rs) for rs in LS_RS])}

    # --- parallel processing ---
    with Pool(cpu_count()) as pool:
        results = pool.map(process_file, files)

    for winners in results:
        if winners is None: continue
        for w in winners:
            wins[w] += 1

    # --- print table ---
    print(f"\n{'treatment':>15} {'wins':>6}")
    print("-" * 25)
    for t in sorted(wins, key=lambda t: -wins[t]):
        print(f"{str(t):>15} {wins[t]:>6}")

if __name__ == "__main__":
    eg__hparam("../../moot/optimize")
