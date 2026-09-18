# T019 — Quantitative Decision-Conflict Benchmark

## Status
**COMPLETED — IMPROVES ON BINARY CONFLICT, BUT DOES NOT BEAT STANDARD UNCERTAINTY**

GitHub Actions run: 35352412064 (success).

Dataset/protocol: same reproducible PhysioNet/CinC Challenge 2012 Set A benchmark as T018; 4,000 records, deterministic 3,000/1,000 split, 25 bootstrap logistic model-worlds per evidence stage.

| Stage | Reversal | Binary conflict AUROC | Conflict-mass AUROC | Conflict-mass AUPRC | Standard uncertainty AUROC | Standard uncertainty AUPRC |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 0.320 | 0.5221 | 0.6087 | 0.3947 | 0.6307 | 0.4274 |
| 2 | 0.270 | 0.5362 | 0.6901 | 0.4019 | 0.7088 | 0.4296 |
| 3 | 0.221 | 0.5285 | 0.7128 | 0.3669 | 0.7456 | 0.4042 |

Vote-margin gave essentially the same result (AUROC 0.6068, 0.6904, 0.7119).

## Verdict
Quantifying the mass of cross-decision model worlds fixes much of T018's saturation problem and substantially improves reversal prediction over a binary incompatibility indicator. However, it remains consistently below ordinary probability-level uncertainty (confidence/entropy/margin) at all three stages.

Therefore conflict mass is **not a standalone breakthrough statistic** and should not be the paper's headline. The next experiment must test the actual cost-aware object: minimum cost of acquiring evidence that removes/reduces decision-incompatible worlds, compared directly against information-gain/cost and uncertainty/cost acquisition.
