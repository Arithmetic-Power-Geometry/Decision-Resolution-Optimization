"""T007: Exact-vs-greedy minimum language repair stress test.

Generate reproducible random weighted conflict-cover instances. Candidate
experiments cover decision-conflict edges and have genesis costs. Compare:
  - exact minimum repair by exhaustive subset enumeration
  - greedy minimum cost / newly covered conflict edge

This is the static repair core. It establishes empirical behavior of the
set-cover reduction before adaptive extensions.
"""
import random
from itertools import combinations

SEED=20260918
random.seed(SEED)

def exact(universe,cands):
    names=list(cands)
    best=(float("inf"),None)
    for r in range(len(names)+1):
        for S in combinations(names,r):
            cov=set()
            cost=0
            for z in S:
                cost+=cands[z][0]; cov |= cands[z][1]
            if universe <= cov and cost<best[0]: best=(cost,S)
    return best

def greedy(universe,cands):
    rem=set(universe); chosen=[]; cost=0
    while rem:
        feasible=[]
        for z,(k,cov) in cands.items():
            if z in chosen: continue
            gain=len(rem & cov)
            if gain: feasible.append((k/gain,k,z,cov))
        if not feasible:return float("inf"),tuple(chosen)
        _,k,z,cov=min(feasible)
        chosen.append(z); cost+=k; rem-=cov
    return cost,tuple(chosen)

def instance(m=12,q=10):
    U={f"p{i}" for i in range(m)}
    C={}
    for j in range(q):
        cov={p for p in U if random.random()<0.35}
        if not cov: cov={random.choice(tuple(U))}
        C[f"z{j}"]=(random.randint(1,9),cov)
    # ensure coverability
    C["fallback"]=(20,set(U))
    return U,C

if __name__=="__main__":
    N=500
    ratios=[]; exact_wins=0
    for _ in range(N):
        U,C=instance()
        eo,_=exact(U,C); go,_=greedy(U,C)
        ratios.append(go/eo)
        exact_wins += (go==eo)
    print("instances",N)
    print("greedy_exact_matches",exact_wins)
    print("mean_ratio",sum(ratios)/N)
    print("max_ratio",max(ratios))
    assert all(r>=1 for r in ratios)
    print("PASS")
