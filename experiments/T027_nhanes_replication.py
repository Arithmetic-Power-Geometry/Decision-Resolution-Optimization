#!/usr/bin/env python3
"""T027 final replication gate: NHANES multi-cycle resolver-choice uncertainty.

Independent public health domain. Pools NHANES 2007-2018 cycles, predicts self-reported
doctor-diagnosed diabetes, and treats common laboratory groups as measurement panels.
Panel costs are deliberately NOT invented here: this replication tests structural
resolver-choice uncertainty; monetary-cost claims require an externally verified fee
table. Cheapest = fewest newly acquired analytes. This prevents false 'real-cost' claims.

Significant only if resolver-choice uncertainty replicates on an independent domain and
is not nearly equivalent to ordinary entropy/confidence.
"""
import io,json,urllib.request,numpy as np,pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score,average_precision_score
from sklearn.impute import SimpleImputer
cycles=["E","F","G","H","I","J"] # 2007-08 ... 2017-18
base="https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/{}/DataFiles/{}.XPT"
# component stems; demographics/questionnaire + lab panels
files={"DEMO":["RIDAGEYR","RIAGENDR","BMXBMI"],"DIQ":["DIQ010"],
       "GHB":["LBXGH"],"GLU":["LBXGLU"],"HDL":["LBDHDD"],"TCHOL":["LBXTC"],
       "TRIGLY":["LBXTR"],"BIOPRO":["LBXSCR","LBXSALT","LBXSAST","LBXSAL","LBXSTP"]}
rows=[]
for suf in cycles:
    # CDC cycle directory naming: 2007-2008 etc.
    year={"E":"2007","F":"2009","G":"2011","H":"2013","I":"2015","J":"2017"}[suf]
    merged=None
    for stem,cols in files.items():
        url=base.format(year,f"{stem}_{suf}")
        try:
            df=pd.read_sas(url,format="xport")
        except Exception:
            continue
        keep=["SEQN"]+[c for c in cols if c in df.columns]
        df=df[keep]
        merged=df if merged is None else merged.merge(df,on="SEQN",how="outer")
    if merged is not None and "DIQ010" in merged: rows.append(merged)
if not rows: raise RuntimeError("No NHANES cycles downloaded")
df=pd.concat(rows,ignore_index=True)
# yes=1, no=2; exclude borderline/refused/unknown
df=df[df.DIQ010.isin([1,2])].copy(); y=(df.DIQ010==1).astype(int).to_numpy()
current=[c for c in ["RIDAGEYR","RIAGENDR","BMXBMI"] if c in df]
panels={"A1c":[c for c in ["LBXGH"] if c in df],
        "glucose":[c for c in ["LBXGLU"] if c in df],
        "lipids":[c for c in ["LBDHDD","LBXTC","LBXTR"] if c in df],
        "chemistry":[c for c in ["LBXSCR","LBXSALT","LBXSAST","LBXSAL","LBXSTP"] if c in df]}
panels={k:v for k,v in panels.items() if v}
features=current+sum(panels.values(),[])
X=df[features].apply(pd.to_numeric,errors="coerce").to_numpy()
rng=np.random.default_rng(20260918); idx=rng.permutation(len(y)); cut=int(.8*len(y)); tr,te=idx[:cut],idx[cut:]
imp=SimpleImputer(strategy="median").fit(X[tr]); X=imp.transform(X)
# current-only mask by zeroing lab columns after standard imputation to training medians
cur_n=len(current); B=12; worlds=[]
for b in range(B):
    bs=rng.choice(tr,len(tr),replace=True)
    m=HistGradientBoostingClassifier(max_iter=120,max_depth=5,learning_rate=.08,random_state=900+b)
    m.fit(X[bs],y[bs]); worlds.append(m)
ev=te[:min(15000,len(te))]; baseX=X[ev].copy()
# replace unacquired lab values with training median => 0 after centered representation not guaranteed;
# explicitly use imputer medians
med=imp.statistics_; baseX[:,cur_n:]=med[cur_n:]
resolver=[]
for m in worlds:
    full=m.predict(X[ev]); choice=np.full(len(ev),"NONE",object); best=np.full(len(ev),np.inf)
    for p,cols in panels.items():
        xp=baseX.copy(); inds=[features.index(c) for c in cols]; xp[:,inds]=X[ev][:,inds]
        ok=m.predict(xp)==full; c=len(inds)
        take=ok&(c<best); choice[take]=p; best[take]=c
    resolver.append(choice)
resolver=np.stack(resolver)
rd=[]; unc=[]
for i in range(len(ev)):
    v,c=np.unique(resolver[:,i],return_counts=True); rd.append(1-c.max()/B); unc.append(len(v)>1)
rd=np.array(rd); target=np.array(unc,int)
# ordinary uncertainty from current-only world vote
vote=np.stack([m.predict_proba(baseX)[:,1] for m in worlds])
mp=vote.mean(0); entropy=-(mp*np.log(np.clip(mp,1e-9,1))+(1-mp)*np.log(np.clip(1-mp,1e-9,1)))
def met(s):
    return {"auroc":float(roc_auc_score(target,s)),"auprc":float(average_precision_score(target,s))} if len(np.unique(target))>1 else {"auroc":None,"auprc":None}
res={"dataset":"NHANES 2007-2018 pooled","rows_eligible":int(len(y)),"evaluation_rows":int(len(ev)),
 "bootstrap_worlds":B,"panels":{k:len(v) for k,v in panels.items()},
 "resolver_uncertain_rate":float(target.mean()),"mean_resolver_disagreement":float(rd.mean()),
 "rd_ge_0_25_rate":float((rd>=.25).mean()),"entropy_predicts_resolver_uncertainty":met(entropy),
 "cost_note":"Structural replication uses analyte-count acquisition cost; no monetary fee is claimed.",
 "stop_rule":"If resolver uncertainty is substantial and entropy AUROC is well below near-equivalence, structural phenomenon replicates; otherwise stop new-paper branch."}
open("T027_summary.json","w").write(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
