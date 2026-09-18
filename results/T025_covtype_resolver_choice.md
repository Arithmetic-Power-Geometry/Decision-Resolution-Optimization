# T025 — Large real-data resolver-choice uncertainty

## Status
**COMPLETED — POSITIVE REAL-DATA PHENOMENON / NOT YET A FOUNDATIONAL NOVELTY CLAIM**

GitHub Actions run 35356856837 completed the scientific computation successfully on UCI Covertype.

## Data
- total rows: 581,012
- training rows: 464,809
- evaluation rows: 20,000
- features: 54
- classes: 7
- bootstrap predictive worlds: 12

## Results
- resolver-uncertain rate: **0.30045**
- mean resolver disagreement: **0.0800375**
- high resolver disagreement (RD >= 0.25): **0.17025**
- entropy -> resolver uncertainty: AUROC **0.694894**, AUPRC **0.469984**
- low confidence -> resolver uncertainty: AUROC **0.693983**, AUPRC **0.470575**

Consensus cheapest-resolver counts:
- hillshade: 15,402
- distances: 1,110
- soil: 436
- wilderness: 48
- NONE: 3,004

## Interpretation
On a large real dataset, evidence-compatible bootstrap predictive worlds disagree about the identity of the cheapest additional feature panel for roughly 30% of evaluated cases. Ordinary entropy/confidence is informative but far from determinative (AUROC about 0.695), so resolver-choice uncertainty is not simply identical to ordinary predictive uncertainty in this benchmark.

## Limitation / novelty boundary
Panel costs are proxy feature-count costs and the resolver criterion is recovery of each world's own full-information decision. This establishes a real-data T023 phenomenon, not yet a new OED primitive or practical cost-saving algorithm.

## Next gate
T026 must test **meta-resolution value**: whether a cheap preliminary panel can identify which resolver should be acquired and reduce total acquisition cost relative to direct decision-aware / uncertainty / information-gain baselines. A second domain with meaningful real measurement costs is required before paper-writing.
