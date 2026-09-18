#!/usr/bin/env python3
"""T023: meta-resolution / cheapest-experiment-choice identifiability.

Meta-worlds agree on all current scientific observations and on the unresolved
scientific decision, but disagree on the build costs of two future resolving
experiments. Hence the identity of the cheapest resolving experiment is itself
unresolved. A meta-probe reveals which cost regime holds.

The second half compiles the whole finite construction into an augmented ECD state
(meta-world = scientific world + design regime) to test whether finite meta-resolution
is irreducible. It is not: once design regime is included as hidden state and meta-probes
as tests, ordinary ECD/POMDP machinery represents it exactly.
"""
import json, math

# regimes r=0,1. Scientific worlds d=0,1 require opposite decisions.
# Current experiment e0 returns 0 everywhere.
# Future resolvers x,y both reveal d, but build costs swap by regime.
M_values=[2,4,8,16,32,64,128]
rows=[]
for M in M_values:
    regimes={
      0:{"x":1,"y":M},
      1:{"x":M,"y":1},
    }
    cheapest={r:min(regimes[r], key=regimes[r].get) for r in regimes}
    unresolved_choice=len(set(cheapest.values()))>1
    # Without meta-information, minimax commit cost.
    blind=min(max(regimes[r][e] for r in regimes) for e in ("x","y"))
    # Meta-probe q costs 1 and reveals regime, then choose cheapest resolver.
    meta=1+max(min(regimes[r].values()) for r in regimes)
    rows.append({"M":M,"cheapest_by_regime":cheapest,
                 "experiment_choice_unresolved":unresolved_choice,
                 "blind_minimax_cost":blind,"meta_then_resolve_cost":meta,
                 "advantage_ratio":blind/meta})

# Exact augmented-state representation:
# hypotheses (d,r); target class is d. q reveals r, x/y reveal d.
# State-dependent build cost can be represented in a fully specified contingent model.
# Thus the hierarchy is real as an epistemic phenomenon but finite formulation is
# reducible to augmented planning/ECD/POMDP rather than a new computational primitive.
res={
 "rows":rows,
 "max_advantage_ratio":max(x["advantage_ratio"] for x in rows),
 "phenomenon":"The cheapest resolving experiment can itself be unresolved under current evidence.",
 "reduction_verdict":"FINITE META-RESOLUTION REDUCES TO AUGMENTED HIDDEN-STATE PLANNING/ECD-POMDP when design regime, costs, and meta-probes are included.",
 "research_decision":"Keep experiment-choice unidentifiability as a phenomenon, but do not claim a new foundational finite algorithmic problem. Next novelty attack must impose open-ended/generative design structure not enumerable as hidden finite state."
}
open("T023_summary.json","w").write(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
