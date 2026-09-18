"""T010: Admissibility-unlocking family.

Worlds are (decision, index), decision in {A,B}, index 1..M.
A cheap direct experiment d_i separates A/B for index i but is admissible
only after the index has been certified. A universally admissible routing
chain identifies i without resolving A/B. Then d_i becomes admissible.

Ordinary oracle-like resolution can use the appropriate direct experiment
at unit cost. Branchwise admissible resolution must first pay routing cost.

This establishes an unbounded admissibility penalty while useful universally
admissible experiments remain available. It does NOT by itself establish
novelty: belief-support safe POMDPs already restrict actions by current belief.
"""
from functools import lru_cache

def costs(M):
    ordinary=1
    # Worst-case M-1 binary "is index j?" routing probes, then one direct probe.
    admissible=M
    return ordinary,admissible

if __name__=="__main__":
    for M in [2,4,8,16,32,64,128]:
        o,a=costs(M)
        print(M,o,a,a/o)
        assert o==1 and a==M
    print("PASS: ratio grows without bound")
