#!/usr/bin/env python3
import itertools, math, random, json
from functools import lru_cache
random.seed(20260918)
def term(S,c): return len({c[i] for i in S})<=1
def parts(S,o):
    return [tuple(i for i in S if o[i]==b) for b in (0,1) if any(o[i]==b for i in S)]
def solve(cls,tests,mode):
    @lru_cache(None)
    def V(S):
        if term(S,cls): return 0
        cand=[]
        for k,(o,cost) in enumerate(tests):
            ps=parts(S,o)
            if len(ps)<2: continue
            if mode=="opt": score=0
            elif mode=="ec2":
                score=sum(cls[i]!=cls[j] and o[i]!=o[j] for i,j in itertools.combinations(S,2))/cost
            else:
                m=len(S); score=(math.log2(m)-sum(len(p)/m*math.log2(len(p)) for p in ps))/cost
            val=cost+max(V(p) for p in ps)
            cand.append((val if mode=="opt" else -score,val))
        return min(cand)[1] if cand else math.inf
    return V(tuple(range(len(cls))))
rows=[]
for z in range(1000):
    n=random.choice((6,7,8)); cls=[0]*(n//2)+[1]*(n-n//2); random.shuffle(cls)
    tests=[]
    for q in range(random.choice((5,6,7,8))):
        o=tuple(random.randint(0,1) for _ in range(n))
        if len(set(o))>1: tests.append((o,random.randint(1,5)))
    op=solve(cls,tuple(tests),"opt")
    if math.isfinite(op):
        ec=solve(cls,tuple(tests),"ec2"); ig=solve(cls,tuple(tests),"ig")
        rows.append((op,ec,ig))
def stats(j):
    a=[r[j]/r[0] for r in rows if math.isfinite(r[j])]
    return dict(mean=sum(a)/len(a),maximum=max(a),optimal_fraction=sum(abs(x-1)<1e-12 for x in a)/len(a))
res={"generated":1000,"resolvable":len(rows),"ec2_ratio":stats(1),"information_gain_ratio":stats(2),
"verdict":"Exact finite cheapest decision-resolution is the optimal ECD policy; EC2 and IG/cost are approximations, not distinct problem definitions."}
print(json.dumps(res,indent=2))
open("T020_summary.json","w").write(json.dumps(res,indent=2))
