"""T006: Minimum language repair as a hitting/set-cover instance.

A fixed experiment language leaves decision-conflict pairs unresolved.
Each candidate new experiment separates a subset of conflict pairs and has
genesis cost. The minimum expansion that makes all conflict pairs separable is
a weighted set-cover instance.

This establishes:
- a clean combinatorial formulation;
- NP-hardness by immediate reduction from weighted set cover (theoretical);
- exact finite solver for small instances.

Caution: set-cover structure itself is established mathematics; novelty, if any,
must come from the resolution-obstruction -> minimum-repair formulation and
its adaptive/admissible extensions.
"""
from itertools import combinations

conflicts={"ab","ac","ad","bc","bd","cd"}
cand={
 "z1":(2,{"ab","ac","ad"}),
 "z2":(2,{"bc","bd","cd"}),
 "z3":(1,{"ab","bc","cd"}),
 "z4":(1,{"ac","ad","bd"}),
}

def solve():
    names=list(cand)
    best=None
    for r in range(len(names)+1):
        for S in combinations(names,r):
            covered=set().union(*(cand[z][1] for z in S)) if S else set()
            if conflicts <= covered:
                cost=sum(cand[z][0] for z in S)
                if best is None or cost<best[0]:
                    best=(cost,S)
    return best

if __name__=="__main__":
    ans=solve()
    print("minimum repair:",ans)
    assert ans==(2,("z3","z4"))
    print("PASS")
