#!/usr/bin/env python3
"""T022: current-observation equivalence does not determine escape cost.

Construct paired systems A_m and B_m with identical worlds, decisions, and current
experiment library E0 (hence identical ECD/current observational structure), but
different costs for the first synthesized experiment outside E0 that separates the
decision-incompatible worlds.

This is a separation from CURRENT ECD information only, not yet a novelty theorem
against full experiment-design models that include the synthesis space.
"""
import json
rows=[]
for m in [2,4,8,16,32,64,128,256,512,1024]:
    # Worlds w0,w1 require opposite decisions. Current library returns same outcome.
    current_signature={"w0":[0,0],"w1":[0,0]}
    # Same realizable current experiments in A and B.
    assert current_signature["w0"]==current_signature["w1"]
    current_resolution_cost=float("inf")
    # Outside-language synthesis: same separating outcome map, different physical/design cost.
    GA=1
    GB=m
    rows.append({"m":m,"current_ECD_identical":True,
                 "current_resolution_cost":"infinity",
                 "escape_cost_A":GA,"escape_cost_B":GB,"ratio_B_over_A":GB/GA})
res={"construction":"paired systems with identical current worlds/decisions/experiment outcomes",
     "rows":rows,
     "max_ratio":max(r["ratio_B_over_A"] for r in rows),
     "theorem_candidate":"Current ECD/observational-equivalence structure alone does not determine the minimum cost of escaping that equivalence; paired systems can have identical current ECD structure and arbitrarily different external synthesis costs.",
     "limitation":"Once the full synthesis/design space and its costs are included in the state/problem specification, the difference is visible. Therefore this is not yet irreducibility against general optimal experimental design."}
open("T022_summary.json","w").write(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
