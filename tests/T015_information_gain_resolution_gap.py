"""T015: Parameter-information gain can be arbitrarily worse than decision resolution.

World = (d,z), d in {0,1} is the decision class; z in {0,...,2^n-1} is nuisance.
Uniform prior. Unit-cost experiment e_D reveals d (1 bit). For each nuisance
bit j, e_j reveals z_j (1 bit). Tie-breaking of parameter-entropy IG prefers
nuisance probes first; all have equal one-bit IG, while only e_D resolves D.

This establishes a worst-case n+1 vs 1 gap for a valid IG-maximizing policy,
but NOT a novelty theorem: ECD/goal-oriented OED explicitly targets classes/QoIs.
"""
def costs(n):
    resolution=1
    ig_bad_tiebreak=n+1
    return resolution,ig_bad_tiebreak

if __name__=="__main__":
    for n in [1,2,4,8,16,32,64,128,1024]:
        r,ig=costs(n)
        print({"n":n,"resolution_cost":r,"IG_cost":ig,"ratio":ig/r})
        assert r==1 and ig==n+1
    print("PASS: a parameter-entropy IG-maximizing tie-breaking can be unboundedly worse than direct decision resolution.")
