"""T016: Posterior-decision stopping vs support-guaranteed resolution.

Two compatible decision classes remain. A has posterior 1-delta, B has delta.
A posterior policy may stop when Bayes error <= delta0. A support-resolution
policy cannot stop until B is eliminated.

Let the only B-eliminating evidence require n unit-cost tests in sequence
(e.g. B agrees with A on the first n-1 outcomes and differs only on test n).
For any delta <= delta0, posterior stopping cost is 0, while exact support
resolution cost is n. The additive guarantee premium is n and unbounded.

This is a valid separation, but fixed-confidence identification already
formalizes the tradeoff between allowed error delta and evidence/sample cost.
"""
def costs(n, delta, delta0):
    assert n>=1 and 0<delta<=delta0<0.5
    posterior_stop=0
    support_resolution=n
    return posterior_stop,support_resolution

if __name__=="__main__":
    for n in [1,2,4,8,16,32,64,128,1024]:
        cp,cr=costs(n,1e-6,1e-3)
        print({"n":n,"posterior_cost":cp,"support_resolution_cost":cr,"guarantee_premium":cr-cp})
        assert cp==0 and cr==n
    print("PASS: additive cost of zero-error support resolution is unbounded relative to delta-tolerant posterior stopping.")
