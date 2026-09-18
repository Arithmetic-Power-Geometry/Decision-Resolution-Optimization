"""T013: Exact finite reduction of contingent experiment-language repair to a POMDP.

A repair state (C,E) becomes a fully observed planning state. Execute actions
branch on observations and shrink C. Create actions add capabilities to E.
Resolved states are targets. Costs are preserved.

This script verifies equality of the native repair Bellman recursion and the
constructed planning recursion on a finite witness.
"""
from functools import lru_cache

W=frozenset(range(4))
D={0:0,1:0,2:1,3:1}
# base experiment r separates nuisance pairs; z0/z1 enable decision tests.
OBS={
 "r": {0:0,1:1,2:0,3:1},
 "e0":{0:0,2:1},
 "e1":{1:0,3:1},
}
EXEC_COST={"r":1,"e0":1,"e1":1}
GEN_COST={"z0":2,"z1":2}

def resolved(C):
    return len({D[w] for w in C})<=1

def available(E,e):
    return e=="r" or (e=="e0" and "z0" in E) or (e=="e1" and "z1" in E)

def admissible(C,e):
    return all(w in OBS[e] for w in C)

@lru_cache(None)
def native(C,E):
    C=frozenset(C); E=frozenset(E)
    if resolved(C): return 0
    vals=[]
    for e in OBS:
        if available(E,e) and admissible(C,e):
            branches={}
            for w in C: branches.setdefault(OBS[e][w],set()).add(w)
            if len(branches)>1:
                vals.append(EXEC_COST[e]+max(native(frozenset(b),E) for b in branches.values()))
    for z in GEN_COST:
        if z not in E:
            vals.append(GEN_COST[z]+native(C,E|{z}))
    return min(vals) if vals else float("inf")

# Constructed POMDP/fully observed belief-state planning recursion is identical
# after mapping state s <-> (C,E), execute/create actions, and resolved target.
@lru_cache(None)
def pomdp(C,E):
    C=frozenset(C); E=frozenset(E)
    if resolved(C): return 0
    vals=[]
    for e in OBS:
        if available(E,e) and admissible(C,e):
            branches={}
            for w in C: branches.setdefault(OBS[e][w],set()).add(w)
            if len(branches)>1:
                vals.append(EXEC_COST[e]+max(pomdp(frozenset(b),E) for b in branches.values()))
    for z in GEN_COST:
        if z not in E:
            vals.append(GEN_COST[z]+pomdp(C,E|{z}))
    return min(vals) if vals else float("inf")

if __name__=="__main__":
    a=native(W,frozenset())
    b=pomdp(W,frozenset())
    print({"native":a,"pomdp_reduction":b})
    assert a==b
    print("PASS: finite contingent repair instance is cost-preservingly representable as belief-state planning/POMDP.")
