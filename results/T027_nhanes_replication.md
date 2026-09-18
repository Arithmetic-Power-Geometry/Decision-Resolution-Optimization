# T027 — Independent NHANES replication gate

## Status
**COMPLETED — WEAK / NON-REPLICATION; PREDECLARED NEW-PAPER GATE FAILED**

Successful GitHub Actions run: 35360121210.

## Data
- NHANES 2007–2018 pooled
- eligible rows: 56,463
- evaluation rows: 11,293
- bootstrap worlds: 12
- panels: A1c (1 analyte), glucose (1), lipids (3), chemistry (3)

## Results
- resolver-uncertain rate: **0.0352431**
- mean resolver disagreement: **0.0088624**
- RD >= 0.25 rate: **0.0175330**
- entropy predicting resolver uncertainty: AUROC **0.823793**, AUPRC **0.101931**

## Interpretation
Resolver-choice uncertainty exists in this independent health domain, but at only 3.52%, versus 30.045% in T025 Covertype. Ordinary entropy predicts it fairly strongly (AUROC 0.824). Under the predeclared stop rule, this is not a substantial independent replication.

## Cost limitation
Costs are analyte-count proxies, not monetary fees. No real-cost clinical claim is made.

## Research decision
The T022/T023 structural phenomenon remains mathematically valid and T025 remains a positive domain-specific empirical observation, but the independent replication gate for a new breakthrough paper failed. Do not continue adding datasets merely to search for a positive replication. The principled next move is to stop the new resolver-choice paper branch, or consciously pivot to a boundary/limits paper integrating exact reductions and negative results.
