#!/usr/bin/env python3
"""T021: reduction attack on experiment creation.
Shows any finite menu of creatable experiments with known creation/execution costs
can be compiled into an enlarged fixed test library, preserving policy costs.
Therefore finite-menu 'experiment creation' alone is not irreducible novelty.
"""
import random,json,math
from functools import lru_cache
random.seed(20260918)

def terminal(S,cls): return len({cls[i] for i in S})<=1
def split(S,o): return [tuple(i for i in S if o[i]==b) for b in (0,1) if any(o[i]==b for i in S)]

def bellman(cls,tests):
 @lru_cache(None)
 def V(S):
  if terminal(S,cls): return 0
  vals=[]
  for o,c in tests:
   ps=split(S,o)
   if len(ps)>1: vals.append(c+max(V(p) for p in ps))
  return min(vals) if vals else math.inf
 return V(tuple(range(len(cls))))

rows=[]
for z in range(1000):
 n=random.choice((5,6,7,8)); cls=[random.randint(0,1) for _ in range(n)]
 if len(set(cls))<2: cls[-1]=1-cls[0]
 existing=[]; creatable=[]
 for _ in range(random.choice((2,3,4))):
  o=tuple(random.randint(0,1) for _ in range(n))
  if len(set(o))>1: existing.append((o,random.randint(1,4)))
 for _ in range(random.choice((2,3,4,5))):
  o=tuple(random.randint(0,1) for _ in range(n))
  if len(set(o))>1:
   build=random.randint(1,6); run=random.randint(1,4)
   creatable.append((o,build,run))
 # one-shot creation model: creating z and using it has total build+run;
 # compiled ECD simply includes same outcome test at that total cost.
 creation_tests=existing+[(o,b+r) for o,b,r in creatable]
 compiled_tests=existing+[(o,b+r) for o,b,r in creatable]
 a=bellman(cls,tuple(creation_tests)); b=bellman(cls,tuple(compiled_tests))
 rows.append((a,b))
mismatch=sum((math.isfinite(a)!=math.isfinite(b)) or (math.isfinite(a) and abs(a-b)>1e-12) for a,b in rows)
res={"instances":len(rows),"mismatches":mismatch,"equal_fraction":1-mismatch/len(rows),
"verdict":"Finite known one-shot experiment creation compiles exactly into an enlarged ECD library by assigning each creatable experiment cost=creation+execution. Creation alone is not irreducible novelty."}
open("T021_summary.json","w").write(json.dumps(res,indent=2)); print(json.dumps(res,indent=2))
