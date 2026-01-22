#!/usr/bin/env python3 -B
# ./rand.py $RANDOM ~/gits/moot/optimize/misc/auto93.csv

import random, sys, xai
xai.the.data=sys.argv[2]
random.seed(int(sys.argv[1]))

data = xai.Data(xai.csv(xai.the.data))

def Y(r): return round(xai.disty(data,r),2)
def top(a): a.sort(); return a[0]
def mid(a): a.sort(); n=len(a)//10; return a[5*n]  
def sd(a):  a.sort(); n=len(a)//10; return (a[9*n]-a[n])/2.56

cohen = 0.35

def shuffle(rows):
    random.shuffle(rows)
    return rows

def report(what,rows):
    a=sorted(rows[:],key=Y)
    print(f":n {len(a):4} :lo {Y(a[0]):5.2f} :mid {Y(a[len(a)//2]):5.2f}", what)

def report_lowest(what, rows):
    a=sorted(rows[:],key=Y)
    print(f":lo {Y(a[0]):5.2f}", what)
    
def extremes(rows):
    a=sorted(rows[:],key=Y)
    n=len(rows)//10
    ok = a[n]
    no = a[1-n]
    return ok, no
  
def project(r, ok, no):
  c=xai.distx(data,ok,no)
  a=xai.distx(data,r,ok)
  b=xai.distx(data,r,no)
  return (a**2 + c**2 - b**2) / (2*c + 1e-32)

def prune(rows, ok, no):
  a=sorted(rows[:],key=lambda r: project(r, ok, no)) 
  return a[:len(a)//2]

fn = sd  # or mid or top
eps = fn([Y(r) for r in data.rows]) * cohen
print(f"Convergence threshold: {eps:.2f}")

budget = 100
step = 5
labelled, rows = [], shuffle(data.rows[:])
b4 = 1e32

report("total rows", rows)
print(round(eps, 2))

for _ in range(20):  
  while len(labelled) < budget:
    labelled += shuffle(rows)[:step]
    ok, no = extremes(labelled)
    rows = prune(labelled, ok, no)
    report("loop labelled", labelled)
    now = fn([Y(r) for r in labelled])
    if abs(b4 - now) > eps:
      b4 = now
    else:
      break
  print(", ", len(labelled), end=", \n")
  report("final labelled", labelled)
  print("")

# # Exercise 1
# report("baseline",data.rows)
# report("sample", xai.shuffle(data.rows)[:30])

# # Exercise 2
# report_lowest("lowest", data.rows)

# # Exercise 3
# rows = shuffle(data.rows[:])[:30]
# ok, no = extremes(rows)
# print(f"Good: {Y(ok):.2f}, Bad: {Y(no):.2f}")

# # Exercise 4
  # proj = (a² + c² - b²) / (2c)
# rows = shuffle(data.rows[:])[:30]
# ok, no = extremes(rows)
# for r in rows[:5]:
#     p = project(r, ok, no)
#     print(f"Y={Y(r):.2f}, proj={p:.3f}")

# # Exercise 5
# rows = shuffle(data.rows[:])[:40]
# ok, no = extremes(rows)
# before = [Y(r) for r in rows]
# after = [Y(r) for r in prune(rows, ok, no)]  
# print(f"Before prune - median: {sorted(before)[20]:.2f}")
# print(f"After prune  - median: {sorted(after)[10]:.2f}")