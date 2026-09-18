"""T017: Exact reduction of finite deterministic Decision Resolution to ECD.

Decision Resolution instance:
 worlds W, decision map D, tests with deterministic outcomes and costs.
 Terminal iff all surviving worlds have the same D-value.

ECD instance:
 hypotheses H=W, equivalence classes induced by D, same tests/outcomes/costs.
 Terminal iff version space is contained in one equivalence class.

The Bellman recursions are therefore identical. This script verifies equality
on a nontrivial finite instance and documents the general bijection.
"""
from functools import lru_cache

W=frozenset(range(6))
D={0:"A",1:"A",2:"B",3:"B",4:"C",5:"C"}
tests={
 "t1":(2,{0:0,1:0,2:1,3:1,4:1,5:1}),
 "t2":(1,{0:0,1:1,2:0,3:1,4:0,5:1}),
 "t3":(3,{0:0,1:0,2:0,3:0,4:1,5:1}),
 "t4":(1,{0:0,1:0,2:1,3:1,4:0,5:0}),
}

def terminal(C):
    return len({D[w] for w in C})<=1

def solve(C):
    C=frozenset(C)
    if terminal(C): return 0
    vals=[]
    for _,(cost,out) in tests.items():
        parts={}
        for w in C: parts.setdefault(out[w],set()).add(w)
        if len(parts)>1:
            vals.append(cost+max(solve(frozenset(p)) for p in parts.values()))
    return min(vals) if vals else float("inf")
solve=lru_cache(None)(solve)

# ECD is the same recursion after h<->w and class(h)=D(w).
def ecd(C):
    C=frozenset(C)
    if len({D[h] for h in C})<=1: return 0
    vals=[]
    for _,(cost,out) in tests.items():
        parts={}
        for h in C: parts.setdefault(out[h],set()).add(h)
        if len(parts)>1:
            vals.append(cost+max(ecd(frozenset(p)) for p in parts.values()))
    return min(vals) if vals else float("inf")
ecd=lru_cache(None)(ecd)

if __name__=="__main__":
    a=solve(W); b=ecd(W)
    print({"decision_resolution":a,"ECD":b})
    assert a==b
    for mask in range(1,1<<len(W)):
        C=frozenset(i for i in W if mask>>i & 1)
        assert solve(C)==ecd(C)
    print("PASS: equality holds for every nonempty compatible-world subset in the witness.")
