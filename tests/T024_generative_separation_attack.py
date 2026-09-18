#!/usr/bin/env python3
"""T024 optimized exact/analytic generative separation attack.

Worlds are (d,z1,...,zn). Generator grammar contains parity probes. A probe of the
decision coordinate alone has cost 1 and separates paired worlds differing only in d.
Full identification requires n+1 independent binary probes. Under an adverse symmetric
parameter-information tie-break, n nuisance coordinates may be acquired first.

We verify the decision-separation property exhaustively for moderate n and use the
rank/information lower bound for the scalable family, avoiding exponential all-pairs
enumeration that made the original workflow unnecessarily slow.
"""
import itertools,json
rows=[]
for n in range(1,21):
    mask=(1,)+(0,)*n
    # exhaustive paired-world verification up to n=14; analytic thereafter
    verified=True
    if n<=14:
        for z in itertools.product((0,1),repeat=n):
            a=(0,)+z; b=(1,)+z
            oa=sum(m*x for m,x in zip(mask,a))%2
            ob=sum(m*x for m,x in zip(mask,b))%2
            if oa==ob: verified=False; break
    decision_cost=1
    full_world_cost=n+1 # n+1 independent bits => >=n+1 binary observations; coordinate probes attain it
    ig_adverse=n+1
    rows.append({"n_nuisance":n,"worlds":2**(n+1),
      "decision_separator_verified":verified,
      "decision_synthesis_cost":decision_cost,
      "full_world_identification_cost":full_world_cost,
      "generic_IG_adverse_cost_to_decision":ig_adverse,
      "ratio_full_to_decision":n+1})
res={"rows":rows,"max_tested_ratio":21,
 "family_ratio":"n+1 -> infinity",
 "candidate_result":"Decision-targeted synthesized parity probe costs 1; full-world identification and adverse generic parameter-information acquisition cost n+1.",
 "novelty_verdict":"Mathematical separation only. It collides conceptually with goal-/decision-oriented OED, which already targets decision-relevant rather than parameter-wide information.",
 "research_decision":"Do not claim T024 as foundational novelty. Preserve as a boundary theorem/example; focus any next empirical work on T022/T023 experiment-choice/escape-cost uncertainty."}
open("T024_summary.json","w").write(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
