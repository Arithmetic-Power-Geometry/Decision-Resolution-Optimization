# T007 — Exact vs Greedy Minimum-Language-Repair Stress Test

## Purpose
Stress-test the static conflict-cover core derived in T006.

The script generates 500 reproducible weighted random instances. Each unresolved decision-conflict pair is an element of the universe; each candidate new experiment covers the conflict pairs it can separate and has a genesis cost.

Two solvers are compared:
1. exact exhaustive minimum repair;
2. greedy cost-per-newly-separated-conflict repair.

## Significance
This is an algorithmic benchmark artifact, not a novelty claim. Because the restricted problem is weighted set cover, greedy approximation behavior is expected to inherit established set-cover structure.

## Why retain it
It gives us a reproducible baseline that later adaptive/admissible repair algorithms must beat or generalize. It also prevents us from presenting a standard greedy set-cover heuristic as a new algorithm.

## Next
Move to a real large feature-acquisition dataset only after defining a decision-resolution criterion that is not merely ordinary classification accuracy.

## Citation

Akhtar, M. A. K. (2026). *Where Cheapest Decision-Resolving Experiments Become Old Theory—and Where They Do Not: Reductions, Escape Costs, and Resolver-Choice Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22833604
