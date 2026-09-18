"""T018: sequential reversal benchmark on PhysioNet Challenge 2012.

Extends T008. Build nested evidence stages from patient-level summary variables,
fit bootstrap logistic model-worlds at each stage, and test whether early
model-world decision disagreement predicts reversal of the stage consensus
decision after richer evidence.

Runtime downloads the official PhysioNet Challenge 2012 Set A.
Outputs per-case CSV + JSON summary with AUROC/AUPRC for reversal prediction
using disagreement, confidence, entropy, margin, and probability SD.
"""
import io, json, tarfile, urllib.request
import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.preprocessing import StandardScaler

URL="https://physionet.org/files/challenge-2012/1.0.0/set-a.tar.gz"
SEED=20260918; B=25

def load():
    raw=urllib.request.urlopen(URL,timeout=120).read()
    tf=tarfile.open(fileobj=io.BytesIO(raw),mode="r:gz")
    rows=[]
    for m in tf.getmembers():
        if not m.isfile() or not m.name.endswith(".txt"): continue
        d=pd.read_csv(tf.extractfile(m))
        rec={}
        for name,g in d.groupby("Parameter"):
            vals=pd.to_numeric(g.Value,errors="coerce").dropna()
            if len(vals):
                rec[name+"_last"]=vals.iloc[-1]; rec[name+"_mean"]=vals.mean()
                rec[name+"_min"]=vals.min(); rec[name+"_max"]=vals.max()
        rows.append(rec)
    X=pd.DataFrame(rows)
    # outcomes file
    out=pd.read_csv("https://physionet.org/files/challenge-2012/1.0.0/Outcomes-a.txt")
    y=out.In_hospital_death.to_numpy()
    return X,y

def scores(y, s):
    if len(np.unique(y))<2: return {"auroc":None,"auprc":None}
    return {"auroc":float(roc_auc_score(y,s)),"auprc":float(average_precision_score(y,s))}

def main():
    X,y=load(); rng=np.random.default_rng(SEED)
    idx=rng.permutation(len(y)); tr,te=idx[:3000],idx[3000:4000]
    keep=X.iloc[tr].notna().mean()>=.20; X=X.loc[:,keep]
    # deterministic nested stages by base-variable alphabetical groups
    bases=sorted(set(c.rsplit("_",1)[0] for c in X.columns))
    cuts=[max(1,len(bases)//4),max(2,len(bases)//2),max(3,3*len(bases)//4),len(bases)]
    stage_probs=[]
    for cut in cuts:
        chosen=set(bases[:cut]); cols=[c for c in X.columns if c.rsplit("_",1)[0] in chosen]
        A=X[cols].copy()
        med=A.iloc[tr].median(); A=A.fillna(med).fillna(0)
        sc=StandardScaler().fit(A.iloc[tr]); Atr=sc.transform(A.iloc[tr]); Ate=sc.transform(A.iloc[te])
        P=[]
        for b in range(B):
            bs=rng.choice(len(tr),len(tr),replace=True)
            model=LogisticRegression(max_iter=1000,class_weight="balanced").fit(Atr[bs],y[tr][bs])
            P.append(model.predict_proba(Ate)[:,1])
        stage_probs.append(np.array(P))
    final=(stage_probs[-1].mean(0)>=.5).astype(int)
    records=[]; summary=[]
    for s,P in enumerate(stage_probs[:-1],1):
        mean=P.mean(0); decisions=P>=.5
        disagree=(decisions.min(0)!=decisions.max(0)).astype(float)
        early=(mean>=.5).astype(int); rev=(early!=final).astype(int)
        conf=np.maximum(mean,1-mean); entropy=-(mean*np.log(mean+1e-12)+(1-mean)*np.log(1-mean+1e-12))
        margin=1-np.abs(mean-.5)*2; sd=P.std(0)
        metrics={"stage":s,"n":len(rev),"reversal_rate":float(rev.mean()),"disagreement_rate":float(disagree.mean())}
        for name,val in [("disagreement",disagree),("low_confidence",1-conf),("entropy",entropy),("margin_uncertainty",margin),("prob_sd",sd)]:
            metrics[name]=scores(rev,val)
        summary.append(metrics)
        for j,k in enumerate(te):
            records.append({"stage":s,"case_index":int(k),"reversal":int(rev[j]),"disagreement":int(disagree[j]),"confidence":float(conf[j]),"entropy":float(entropy[j]),"margin_uncertainty":float(margin[j]),"prob_sd":float(sd[j])})
    pd.DataFrame(records).to_csv("T018_cases.csv",index=False)
    with open("T018_summary.json","w") as f: json.dump(summary,f,indent=2)
    print(json.dumps(summary,indent=2))
if __name__=="__main__": main()
