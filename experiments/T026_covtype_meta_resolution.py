#!/usr/bin/env python3
"""T026: meta-resolution value on UCI Covertype.

A cheap meta-panel is valuable if it helps select which downstream resolver panel to
buy, even when the meta-panel is not itself the final resolver. We use bootstrap
predictive worlds, natural Covertype feature panels, and compare a meta-routing policy
against static direct resolver selection. Proxy acquisition costs equal panel sizes.

For each evaluation case/world, loss(panel)=1 if adding that panel to the current
terrain panel fails to reproduce that world's full-information decision. Total loss is
acquisition cost + lambda*decision failure. A meta-policy observes one candidate cheap
panel, updates which bootstrap worlds remain locally compatible by their predictions,
then routes to the downstream panel minimizing conditional expected loss.
"""
import json, numpy as np
from sklearn.datasets import fetch_covtype
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

rng=np.random.default_rng(20260918)
X,y=fetch_covtype(return_X_y=True,as_frame=False); y=y.astype(int)-1
idx=rng.permutation(len(y)); ntr=int(.8*len(y)); tr,te=idx[:ntr],idx[ntr:]
ev=te[:10000]
sc=StandardScaler().fit(X[tr]); Z=sc.transform(X).astype(np.float32)
panels={"current":[0,1,2],"distances":[3,4,5,9],"hillshade":[6,7,8],
        "wilderness":list(range(10,14)),"soil":list(range(14,54))}
cost={k:float(len(v)) for k,v in panels.items() if k!="current"}
B=10; models=[]
for b in range(B):
    bs=rng.choice(tr,size=len(tr),replace=True)
    m=SGDClassifier(loss="log_loss",alpha=1e-5,max_iter=30,tol=1e-3,random_state=700+b)
    m.fit(Z[bs],y[bs]); models.append(m)
base=np.zeros((len(ev),54),np.float32); base[:,panels["current"]]=Z[ev][:,panels["current"]]
names=["distances","hillshade","wilderness","soil"]
pred={p:[] for p in names}; full=[]
for m in models:
    full.append(m.predict(Z[ev]))
    for p in names:
        q=base.copy(); q[:,panels[p]]=Z[ev][:,panels[p]]
        pred[p].append(m.predict(q))
full=np.stack(full); pred={p:np.stack(v) for p,v in pred.items()}
# lambda makes wrong final decision expensive relative to all proxy costs
LAM=50.0
# static direct policy per case: choose panel minimizing mean world loss
static=np.empty(len(ev)); static_choice=[]
for i in range(len(ev)):
    vals=[]
    for p in names:
        fail=(pred[p][:,i]!=full[:,i]).mean()
        vals.append(cost[p]+LAM*fail)
    j=int(np.argmin(vals)); static[i]=vals[j]; static_choice.append(names[j])
# Meta-routing: acquire meta m; its vector of world predictions partitions worlds.
# For each possible observed prediction, choose best downstream p conditional on worlds
# producing that prediction. Evaluate expected cost over uniformly weighted worlds.
meta_best=np.full(len(ev),np.inf); meta_name=np.empty(len(ev),object)
for meta in ["hillshade","distances","wilderness"]:
    for i in range(len(ev)):
        mp=pred[meta][:,i]; total=cost[meta]
        future=0.0
        for o in np.unique(mp):
            ws=np.where(mp==o)[0]; pr=len(ws)/B
            vals=[]
            for p in names:
                # meta may itself be enough; allow stop after meta
                if p==meta:
                    vals.append(LAM*np.mean(pred[meta][ws,i]!=full[ws,i]))
                else:
                    # conservative additive panel test: downstream panel prediction proxy
                    vals.append(cost[p]+LAM*np.mean(pred[p][ws,i]!=full[ws,i]))
            future+=pr*min(vals)
        total+=future
        if total<meta_best[i]: meta_best[i]=total; meta_name[i]=meta
improve=static-meta_best
res={"dataset":"UCI Covertype","rows_total":int(len(y)),"train_rows":int(len(tr)),
 "evaluation_rows":int(len(ev)),"features":54,"classes":7,"bootstrap_worlds":B,
 "failure_penalty_lambda":LAM,
 "mean_static_direct_loss":float(static.mean()),
 "mean_best_meta_routing_loss":float(meta_best.mean()),
 "mean_loss_reduction":float(improve.mean()),
 "fraction_meta_better":float((improve>1e-9).mean()),
 "fraction_meta_10pct_better":float((meta_best<=.9*static).mean()),
 "median_improvement_when_better":float(np.median(improve[improve>1e-9])) if np.any(improve>1e-9) else 0.0,
 "meta_choice_counts":{str(k):int(v) for k,v in zip(*np.unique(meta_name,return_counts=True))},
 "verdict_rule":"Positive only if mean meta-routing loss is lower and advantage occurs on a nontrivial fraction; result remains a proxy-cost benchmark, not a novelty proof."}
open("T026_summary.json","w").write(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
