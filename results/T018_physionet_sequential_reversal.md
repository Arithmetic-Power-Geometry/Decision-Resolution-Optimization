# T018 — Sequential Decision-Reversal Benchmark

## Purpose
Test the post-T017 applied hypothesis: does model-world decision disagreement under partial evidence predict whether the apparent decision will reverse after richer evidence, better than standard uncertainty summaries?

## Dataset
Official PhysioNet/CinC Challenge 2012 Set A, matching T008. The workflow downloads the data at runtime and uses a deterministic 3000/1000 train/test split.

## Design
Nested evidence stages are formed from progressively larger groups of patient variables. At every stage, 25 bootstrap logistic-regression model-worlds are fitted. For each held-out patient we compute:
- binary model-world decision disagreement;
- confidence;
- predictive entropy;
- distance-to-threshold/margin uncertainty;
- across-world probability SD.

The target is whether the stage consensus decision reverses relative to the richest final evidence stage.

Primary metrics: AUROC and AUPRC for reversal prediction.

## Status
CODE + REPRODUCIBLE GITHUB ACTION ADDED. Numerical verdict pending workflow execution.

## Novelty boundary
Clinical prediction instability is established: Riley & Collins and later work recommend bootstrap-based individual prediction/decision stability diagnostics. A 2026 healthcare paper also proposes empirical decision flip rate. Therefore disagreement/flip-rate itself is not new.

The possible surviving contribution must be stronger: **evidence-stage disagreement as a prospective predictor of later evidence-induced decision reversal, coupled to cost-aware acquisition of the next measurement.** This must beat stability, confidence, entropy and ensemble-variance baselines and then survive an independent large dataset.

Do not write the paper from T018 unless that stronger result appears.
