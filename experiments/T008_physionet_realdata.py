"""T008: PhysioNet 2012 real-data decision-resolution benchmark.

Downloads official open-access Set A (4000 labeled ICU stays), constructs
patient-level summary features, trains a bootstrap ensemble of logistic models,
and evaluates whether partial feature blocks leave model worlds that imply
incompatible mortality decisions.

Outputs results/T008_physionet_summary.json and CSV metrics.
Raw PhysioNet data are NOT committed.
"""
import io, json, os, zipfile, urllib.request
import numpy as np, pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import roc_auc_score

BASE="https://archive.physionet.org/pn3/challenge/2012/"
os.makedirs("results",exist_ok=True)
def get(url):
    with urllib.request.urlopen(url,timeout=120) as r:return r.read()
z=zipfile.ZipFile(io.BytesIO(get(BASE+"set-a.zip")))
out=pd.read_csv(io.BytesIO(get(BASE+"Outcomes-a.txt")))
y=out.set_index("RecordID")["In-hospital_death"]

rows=[]
for name in z.namelist():
    if not name.endswith(".txt"): continue
    d=pd.read_csv(z.open(name))
    rid=int(d.loc[d.Parameter=="RecordID","Value"].iloc[0])
    vals={}
    for p,g in d[d.Parameter!="RecordID"].groupby("Parameter"):
        a=pd.to_numeric(g.Value,errors="coerce").replace(-1,np.nan)
        vals[p+"_last"]=a.dropna().iloc[-1] if a.notna().any() else np.nan
        vals[p+"_mean"]=a.mean()
        vals[p+"_min"]=a.min()
        vals[p+"_max"]=a.max()
    vals["RecordID"]=rid; rows.append(vals)
X=pd.DataFrame(rows).set_index("RecordID").join(y,how="inner")
Y=X.pop("In-hospital_death").astype(int)
# deterministic split
ids=np.arange(len(X)); rng=np.random.default_rng(20260918); rng.shuffle(ids)
tr=ids[:3000]; te=ids[3000:]
# retain reasonably observed features
keep=X.iloc[tr].notna().mean()
cols=list(keep[keep>=0.20].index)
X=X[cols]
# Bootstrap model worlds.
B=25; probs=[]; aucs=[]
for b in range(B):
    boot=rng.choice(tr,size=len(tr),replace=True)
    model=make_pipeline(SimpleImputer(strategy="median"),StandardScaler(),
                        LogisticRegression(max_iter=1000,class_weight="balanced"))
    model.fit(X.iloc[boot],Y.iloc[boot])
    p=model.predict_proba(X.iloc[te])[:,1]
    probs.append(p); aucs.append(roc_auc_score(Y.iloc[te],p))
P=np.vstack(probs)
# Decision-incompatible worlds at threshold .5.
dec=(P>=0.5)
unresolved=(dec.min(axis=0)!=dec.max(axis=0))
meanp=P.mean(axis=0)
conf=np.maximum(meanp,1-meanp)
# Premature confidence: ensemble mean appears >=.8 confident but worlds disagree.
premature=unresolved & (conf>=0.80)
summary={
 "dataset":"PhysioNet/CinC Challenge 2012 Set A",
 "records":int(len(X)),"train":int(len(tr)),"test":int(len(te)),
 "features_after_filter":len(cols),"bootstrap_worlds":B,
 "mean_auc":float(np.mean(aucs)),"sd_auc":float(np.std(aucs)),
 "decision_threshold":0.5,
 "unresolved_count":int(unresolved.sum()),
 "unresolved_rate":float(unresolved.mean()),
 "high_confidence_unresolved_count":int(premature.sum()),
 "high_confidence_unresolved_rate":float(premature.mean())
}
print(json.dumps(summary,indent=2))
with open("results/T008_physionet_summary.json","w") as f:json.dump(summary,f,indent=2)
pd.DataFrame({"mean_probability":meanp,"confidence":conf,
              "decision_unresolved":unresolved.astype(int),
              "high_confidence_unresolved":premature.astype(int),
              "label":Y.iloc[te].to_numpy()}).to_csv("results/T008_physionet_cases.csv",index=False)
