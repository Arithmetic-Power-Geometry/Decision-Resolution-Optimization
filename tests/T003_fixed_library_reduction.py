"""T003: Reduction attack for branchwise admissibility.

Purpose
-------
Show that, for a fixed experiment library, branchwise universal admissibility
can be represented exactly as a state-dependent query-availability map.

For compatible-world state C define:
    Q(C) = {e : A_e(w)=1 for every w in C}.

The admissibility-aware Bellman recursion is then identical to a generic
adaptive decision process whose available action/query set is Q(C).

This is a NEGATIVE novelty test: branchwise admissibility by itself should not
be claimed as a new optimization primitive. The surviving research target is
experiment-language expansion (genesis), not fixed-library availability.
"""

from functools import lru_cache
from math import inf

W=("a","b","c")
D={"a":"A","b":"B","c":"B"}
E={
 "direct":{"cost":1,"outcome":{"a":0,"b":1,"c":1},
           "adm":{"a":True,"b":False,"c":False}},
 "screen":{"cost":2,"outcome":{"a":0,"b":0,"c":1},
           "adm":{"a":True,"b":True,"c":True}},
 "pair":{"cost":1,"outcome":{"a":0,"b":1,"c":0},
         "adm":{"a":True,"b":True,"c":False}},
}

def Q(C):
    return tuple(e for e,s in E.items() if all(s["adm"][w] for w in C))

def resolved(C):
    return len({D[w] for w in C})<=1

def parts(C,e):
    z={}
    for w in C:z.setdefault(E[e]["outcome"][w],set()).add(w)
    return list(z.values())

@lru_cache(None)
def V_adm(Ct):
    C=frozenset(Ct)
    if resolved(C): return 0
    best=inf
    for e in Q(C):
        bs=parts(C,e)
        if len(bs)==1: continue
        best=min(best,E[e]["cost"]+max(V_adm(tuple(sorted(b))) for b in bs))
    return best

@lru_cache(None)
def V_state_query(Ct):
    C=frozenset(Ct)
    if resolved(C): return 0
    # Generic state-dependent query process: available actions are exactly Q(C).
    available=Q(C)
    best=inf
    for e in available:
        bs=parts(C,e)
        if len(bs)==1: continue
        best=min(best,E[e]["cost"]+max(V_state_query(tuple(sorted(b))) for b in bs))
    return best

if __name__=="__main__":
    C=tuple(sorted(W))
    a=V_adm(C); b=V_state_query(C)
    print("admissibility recursion:",a)
    print("state-dependent query recursion:",b)
    assert a==b
    print("PASS: exact representation on the finite instance")
