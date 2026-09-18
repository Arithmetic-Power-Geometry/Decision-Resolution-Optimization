"""T004: Exact Minimum Resolution Expansion (MRE).

We distinguish:
- execution cost: cost to run an experiment already in the language;
- genesis cost: cost to create/add a previously unavailable experiment.

The base language cannot resolve the decision. Candidate expansions are
enumerated exactly. We compare:
  (i) minimum genesis cost for decision resolution;
  (ii) minimum genesis cost for full world identification.

Family construction yields an unbounded ratio between full-identification
genesis cost and decision-resolution genesis cost.
"""

from itertools import combinations
from math import inf

def partitions_worlds(n_bits):
    return [tuple((i>>j)&1 for j in range(n_bits)) for i in range(2**n_bits)]

def decision(w):
    # downstream decision depends only on first bit
    return w[0]

def separates_decisions(worlds, sensors):
    groups={}
    for w in worlds:
        sig=tuple(w[j] for j in sensors)
        groups.setdefault(sig,set()).add(decision(w))
    return all(len(ds)==1 for ds in groups.values())

def identifies_world(worlds, sensors):
    sigs={tuple(w[j] for j in sensors) for w in worlds}
    return len(sigs)==len(worlds)

def min_cost(worlds,n_bits,target):
    # Each primitive sensor costs 1 to create.
    for k in range(n_bits+1):
        for S in combinations(range(n_bits),k):
            ok=separates_decisions(worlds,S) if target=="decision" else identifies_world(worlds,S)
            if ok:return k,S
    return inf,None

if __name__=="__main__":
    print("bits, worlds, decision_genesis, full_genesis, ratio")
    for n in [2,3,4,5,8,10]:
        W=partitions_worlds(n)
        gd,Sd=min_cost(W,n,"decision")
        gf,Sf=min_cost(W,n,"full")
        print(n,len(W),gd,gf,gf/gd)
        assert gd==1
        assert gf==n
    print("PASS: G_decision=1 while G_full=n; ratio n is unbounded.")
