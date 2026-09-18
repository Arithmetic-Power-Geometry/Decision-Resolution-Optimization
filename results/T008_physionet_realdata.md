# T008 — PhysioNet 2012 Real-Data Benchmark

This test uses the official open-access PhysioNet/CinC Challenge 2012 Set A.

The official challenge contains 12,000 adult ICU stays, with 4,000 labeled records in training Set A and up to 42 recorded variables during the first 48 hours. Raw data are downloaded at runtime and are not committed to this repository.

## Resolution test
A bootstrap ensemble is treated as a finite set of model worlds. For each held-out patient, the downstream decision is binary mortality classification at threshold 0.5.

A case is **decision-unresolved** when surviving model worlds disagree on the decision. A stronger diagnostic is **high-confidence unresolved**: the ensemble mean probability is at least 0.80 confident in one class while individual model worlds still imply incompatible decisions.

This is intentionally different from claiming a new feature-acquisition classifier.

## Status
Workflow added. Numerical results must only be reported after the GitHub Actions run completes successfully.
