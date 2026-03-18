#!/usr/bin/env python3 -B
"""hw5_fast.py: sample size sensitivity (grad only), faster with progress"""

import os, glob, statistics, random
from multiprocessing import Pool
from ez import csv, Data, shuffle, filename
from sa import sa
from locals import ls, lsRminus, saRplus
from stats import top

ALGOS   = [sa, ls, lsRminus, saRplus]
SAMPLES = [30, 50, 100, 200]
REPEATS = 10  # reduce for speed; can restore to 20 for final runs

PROGRESS_FILE = "hw5_progress.log"
open(PROGRESS_FILE, "w").close()  # clear previous log

# --- helper function to process one CSV ---
def process_file(f):
    print(f"\n=== Processing CSV: {f} ===")
    with open(PROGRESS_FILE, "a") as pf:
        pf.write(f"Starting: {f}\n")

    try:
        d0 = Data(csv(f))
        if len(d0.rows) < max(SAMPLES):
            print(f"Skipping {f}: not enough rows")
            return None
    except Exception:
        print(f"Skipping {f}: failed to read")
        return None

    # baseline eps from largest sample
    baseline = []
    for _ in range(REPEATS):
        rows = shuffle(d0.rows[:])[:max(SAMPLES)]
        d1 = Data([d0.cols.names] + rows)
        for r in d1.rows:
            baseline.append(d1.disty(r))
    sd = statistics.stdev(baseline) if len(baseline) > 1 else 1

    treatments = [(a.__name__, n) for a in ALGOS for n in SAMPLES]
    algo_by_name = {a.__name__: a for a in ALGOS}
    seen = {t: [] for t in treatments}

    for _ in range(REPEATS):
        for name, n in treatments:
            rows = shuffle(d0.rows[:])[:n]
            d1 = Data([d0.cols.names] + rows)
            algo = algo_by_name[name]
            for h, e, row in algo(d1): pass
            seen[(name, n)].append(int(100 * e))

    winners = top(seen, eps=0.35 * sd)
    best_n = min(n for (_, n) in winners)
    winners = {w for w in winners if w[1] == best_n}

    print(f"  Winners for {f}: {winners}")
    with open(PROGRESS_FILE, "a") as pf:
        pf.write(f"Completed: {f} -> {winners}\n")

    return winners

# --- main ---
def eg__sample(d:filename):
    files = glob.glob(os.path.join(d, "*/*.csv"))
    print(f"found {len(files)} csv files")

    wins = {(a.__name__, n): 0 for a in ALGOS for n in SAMPLES}

    # --- parallel processing across CSVs ---
    with Pool() as pool:
        results = pool.map(process_file, files)

    # accumulate wins
    for wset in results:
        if wset is None: continue
        for w in wset:
            wins[w] += 1

    print(f"\n{'treatment':>20} {'wins':>6}")
    print("-" * 30)
    for t in sorted(wins, key=lambda t: -wins[t]):
        print(f"{str(t):>20} {wins[t]:>6}")


if __name__ == "__main__":
    eg__sample("../../moot/optimize")  # adjust path as needed
