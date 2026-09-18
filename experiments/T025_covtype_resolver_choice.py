#!/usr/bin/env python3
"""T025: large-real-data resolver-choice uncertainty on UCI Covertype.

Tests the T022/T023 phenomenon on ~581k real observations. Bootstrap SGD-logistic
models are treated as evidence-compatible predictive worlds. For each held-out case,
we begin with a cheap current panel and ask, for each world, which remaining natural
feature panel is the cheapest single acquisition that reproduces that world's
full-information decision. We then measure disagreement over the identity of that
cheapest resolver and compare it with ordinary predictive uncertainty.

This is a research benchmark, not a clinical decision system.
"""
import io, json, urllib.request, numpy as np
from sklearn.datasets import fetch_covtype
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, average_precision_score

rng=np.random.default_rng(20260918)
X,y=fetch_covtype(return_X_y=True, as_frame=False)
y=y.astype(int)-1
N=len(y)
idx=rng.permutation(N); ntr=int(.8*N)
tr,te=idx[:ntr],idx[ntr:]
# cap evaluation only; training uses full 80%
eval_idx=te[:20000]
sc=StandardScaler().fit(X[tr])
Xs=sc.transform(X).astype(np.float32)
# Natural Covertype groups: terrain geometry; horizontal distances; hillshade;
# wilderness indicators; soil indicators. Current panel = terrain geometry.
panels={
 "current_terrain":[0,1,2],
 "distances":[3,4,5,9],
 "hillshade":[6,7,8],
 "wilderness":list(range(10,14)),
 "soil":list(range(14,54)),
}
cost={"distances":4.0,"hillshade":3.0,"wilderness":4.0,"soil":40.0}
B=12
models=[]
for b in range(B):
    bs=rng.choice(tr,size=len(tr),replace=True)
    m=SGDClassifier(loss="log_loss",alpha=1e-5,max_iter=35,tol=1e-3,random_state=100+b)
    m.fit(Xs[bs],y[bs]); models.append(m)

E=len(eval_idx); classes=np.arange(7)
current=np.zeros((E,54),dtype=np.float32)
current[:,panels["current_terrain"]]=Xs[eval_idx][:,panels["current_terrain"]]
cur_probs=[]; resolver=[]
for m in models:
    cp=m.predict_proba(current); cur_probs.append(cp)
    full=m.predict(Xs[eval_idx])
    choices=np.full(E,"NONE",dtype=object)
    best=np.full(E,np.inf)
    for p in ("distances","hillshade","wilderness","soil"):
        xp=current.copy(); cols=panels[p]; xp[:,cols]=Xs[eval_idx][:,cols]
        pred=m.predict(xp)
        ok=pred==full
        take=ok & (cost[p]<best)
        choices[take]=p; best[take]=cost[p]
    resolver.append(choices)
cur_probs=np.stack(cur_probs) # B,E,7
resolver=np.stack(resolver)   # B,E
meanp=cur_probs.mean(0)
entropy=-(meanp*np.log(np.clip(meanp,1e-12,1))).sum(1)
confidence=meanp.max(1)
# resolver disagreement: 1 - modal fraction
rd=np.empty(E); unresolved=np.empty(E,dtype=bool)
for i in range(E):
    vals,cnt=np.unique(resolver[:,i],return_counts=True)
    rd[i]=1-cnt.max()/B
    unresolved[i]=len(vals)>1
# Does ordinary uncertainty identify cases where cheapest resolver itself is uncertain?
target=unresolved.astype(int)
def metric(score):
    if target.min()==target.max(): return {"auroc":None,"auprc":None}
    return {"auroc":float(roc_auc_score(target,score)),
            "auprc":float(average_precision_score(target,score))}
# How often a unique non-NONE resolver exists across worlds
consensus=[]
for i in range(E):
    vals,cnt=np.unique(resolver[:,i],return_counts=True)
    consensus.append(vals[cnt.argmax()])
consensus=np.array(consensus)
res={
 "dataset":"UCI Covertype",
 "rows_total":int(N),"train_rows":int(len(tr)),"evaluation_rows":int(E),
 "features":54,"classes":7,"bootstrap_worlds":B,
 "resolver_uncertain_rate":float(unresolved.mean()),
 "mean_resolver_disagreement":float(rd.mean()),
 "high_resolver_disagreement_rate_rd_ge_0_25":float((rd>=.25).mean()),
 "ordinary_entropy_predicts_resolver_uncertainty":metric(entropy),
 "low_confidence_predicts_resolver_uncertainty":metric(1-confidence),
 "consensus_resolver_counts":{str(k):int(v) for k,v in zip(*np.unique(consensus,return_counts=True))},
 "interpretation":"Measures whether evidence-compatible predictive worlds disagree about the cheapest additional feature panel needed to recover their own full-information decision.",
 "novelty_caution":"A positive result establishes a real-data T023 phenomenon, not by itself a new optimal-experimental-design primitive."
}
open("T025_summary.json","w").write(json.dumps(res,indent=2)); print(json.dumps(res,indent=2))
