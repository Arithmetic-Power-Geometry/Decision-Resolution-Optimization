# Real-Data Validation Plan

## Candidate benchmark: PhysioNet 2012 ICU challenge
Published adaptive covariate-acquisition work has used a PhysioNet dataset with about 12,000 patient records and 30 health variables for mortality prediction. This makes it a credible comparison benchmark for sequential feature acquisition.

## Important novelty boundary
Cost-sensitive feature acquisition is established: algorithms already choose which feature/test to acquire next and when to stop classification. Therefore our real-data experiment must NOT claim that cheap sequential feature acquisition is new.

## Proposed DRO-specific test
Treat a family of calibrated predictive models / bootstrap worlds as the compatible-world set. The downstream decision is a thresholded intervention/classification decision, not exact model identity.

At each partial feature set:
1. compute which model worlds remain observationally compatible;
2. detect whether they imply incompatible downstream decisions;
3. compare ordinary uncertainty/confidence stopping with decision-resolution stopping;
4. measure the minimum additional feature/test cost required to eliminate decision incompatibility;
5. if the allowed feature language cannot resolve it, evaluate candidate feature blocks as language repairs.

## Comparators
- all features;
- confidence/entropy acquisition;
- greedy cost-sensitive feature acquisition;
- decision-targeted conflict reduction;
- exact repair on reduced subproblems.

## Metrics
- feature acquisition cost;
- unresolved-decision rate at stopping;
- decision reversal after acquiring all features;
- classification error/AUROC as secondary predictive metrics;
- repair cost when fixed feature language is insufficient.

## Status
Dataset integration pending. We should use the original public PhysioNet source and preserve its license/terms rather than commit the raw dataset blindly to GitHub.

## Citation

Akhtar, M. A. K. (2026). *Where Cheapest Decision-Resolving Experiments Become Old Theory—and Where They Do Not: Reductions, Escape Costs, and Resolver-Choice Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22833604
