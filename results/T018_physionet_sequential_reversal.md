# T018 — PhysioNet Sequential Decision-Reversal Benchmark

## Status
**COMPLETED — NEGATIVE FOR THE CURRENT DISAGREEMENT HYPOTHESIS**

GitHub Actions run: 35351053995 (success).

Dataset: PhysioNet/CinC Challenge 2012 Set A; 4,000 records; deterministic 3,000/1,000 train/test split; 25 bootstrap logistic model-worlds per evidence stage.

## Results
| Stage | Reversal rate | Disagreement rate | Disagreement AUROC | Disagreement AUPRC | Confidence/Entropy/Margin AUROC | Confidence/Entropy/Margin AUPRC | Probability-SD AUROC | Probability-SD AUPRC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.320 | 0.945 | 0.5221 | 0.3299 | 0.6307 | 0.4274 | 0.4447 | 0.2855 |
| 2 | 0.270 | 0.936 | 0.5362 | 0.2851 | 0.7088 | 0.4296 | 0.4707 | 0.2550 |
| 3 | 0.221 | 0.942 | 0.5285 | 0.2313 | 0.7456 | 0.4042 | 0.4791 | 0.2243 |

## Verdict
Binary model-world disagreement is nearly saturated (93.6–94.5%) and is only weakly predictive of later decision reversal. Standard probability-level uncertainty (confidence/entropy/margin) substantially outperforms it at every stage.

Therefore the proposed headline claim **“current model-world disagreement predicts future evidence-induced decision reversal better than standard uncertainty” is rejected on T018**.

This is scientifically useful: do not proceed to a paper or T019 using the binary-disagreement statistic. The next test must change the object, not rename this failed statistic. A viable next candidate is a **pairwise reversal margin / minimum-cost conflict certificate** that weights incompatible worlds by how much evidence is required to move them across the decision boundary, and must be compared against confidence/entropy and modern decision-aware experimental design.
