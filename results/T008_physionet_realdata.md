# T008 — PhysioNet 2012 Real-Data Decision-Resolution Benchmark

## Reproducible run
GitHub Actions run 35332269932 completed successfully.

Dataset: PhysioNet/CinC Challenge 2012 Set A.
- records: 4,000
- train: 3,000
- held-out test: 1,000
- derived features after missingness filter: 156
- bootstrap model worlds: 25
- mean held-out AUROC: 0.80505
- AUROC SD: 0.00863

## Decision-resolution result
At decision threshold 0.5:
- decision-unresolved held-out cases: **392 / 1,000 = 39.2%**
- high-confidence yet decision-unresolved cases: **61 / 1,000 = 6.1%**

High-confidence unresolved means the ensemble mean is at least 0.80 confident in one class while at least two compatible bootstrap model worlds still imply opposite decisions.

## Interpretation
This is a meaningful empirical signal: predictive confidence and decision resolution are not equivalent on this benchmark.

It is **not yet a novelty proof**. UAI 2026 work on adversarially robust decision-aware experimental design already reports that conventional decision-aware design can reach high-confidence but fragile decisions under adversarial variation. Our remaining distinction must therefore be the explicit finite compatible-world resolution certificate plus minimum-cost experiment-language repair.

## Next test
T009 must turn the diagnostic into an acquisition problem: from a restricted measurement set, find the cheapest additional measurement block that eliminates model-world decision disagreement, and compare against confidence/entropy or uncertainty-based acquisition.
