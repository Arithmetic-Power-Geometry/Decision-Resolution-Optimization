#!/usr/bin/env python3
"""T024: generative separating experiment vs conventional information criteria.

Finite sampled approximation to a continuous design family. Worlds are (d,z):
decision bit d and nuisance bit z. Candidate synthesized probes are parameterized
linear parity masks over these bits. We compare:
  (i) decision-separation cost: cheapest probe that separates every cross-decision pair;
  (ii) full-world discrimination: cheapest probe/set targeting all world distinctions;
  (iii) entropy/parameter-information proxy.

Purpose: test whether decision-targeted synthesis can differ sharply from generic
world/model discrimination. This does NOT establish novelty against goal-oriented OED.
"""
import json, itertools

def parity(mask,w):
    d,zbits=w[0],w[1:]
    bits=(d,)+zbits
    return sum(m*b for m,b in zip(mask,bits))%2

rows=[]
for n in range(1,11):
    worlds=[(d,)+z for d in (0,1) for z in itertools.product((0,1), repeat=n)]
    # generator grammar: any parity mask; cost = number of active coordinates
    masks=[m for m in itertools.product((0,1), repeat=n+1) if any(m)]
    # exact single-probe decision separator
    sep=[]
    for m in masks:
        ok=all(parity(m,a)!=parity(m,b) for a in worlds for b in worlds if a[0]!=b[0] and a[1:]==b[1:])
        if ok: sep.append((sum(m),m))
    decision_cost=min(c for c,m in sep)
    # Full identification using coordinate probes needs n+1 unit probes in this grammar.
    full_world_cost=n+1
    # A parameter-information policy treating all n+1 independent bits symmetrically
    # can spend n nuisance probes before the decision coordinate under adverse tie-break.
    ig_worst_before_decision=n+1
    rows.append({"n_nuisance":n,"worlds":len(worlds),
                 "decision_synthesis_cost":decision_cost,
                 "full_world_identification_cost":full_world_cost,
                 "generic_IG_adverse_cost_to_decision":ig_worst_before_decision,
                 "ratio_full_to_decision":full_world_cost/decision_cost})
res={"rows":rows,
     "max_ratio":max(r["ratio_full_to_decision"] for r in rows),
     "candidate_result":"Within a generative parity-probe grammar, a decision-separating synthesized experiment can cost 1 while full-world identification and adverse generic parameter-IG require n+1.",
     "novelty_verdict":"SEPARATION FROM GENERIC INFORMATION/MODEL IDENTIFICATION ONLY; NOT NOVEL AGAINST GOAL-/DECISION-ORIENTED OED. Do not write paper from T024 alone.",
     "next_gate":"Need either a theorem not expressible as goal-oriented OED utility optimization, or pivot to an empirical/methodological paper rather than claim a new foundational primitive."}
open("T024_summary.json","w").write(json.dumps(res,indent=2)); print(json.dumps(res,indent=2))
