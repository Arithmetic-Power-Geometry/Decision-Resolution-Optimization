# T002 — Nontrivial Admissibility-Penalty Family

## Aim
Move beyond the trivial two-world obstruction and test whether branchwise admissibility can impose an arbitrarily large resolution penalty even when admissible informative tests continue to exist.

## Construction
For integer M, construct one decision-A world and M decision-B variants.

An unconstrained cost-1 experiment directly separates A from B, but is not branchwise admissible initially. A sequence of admissible prerequisite tests progressively removes B-variants until a final decision separator becomes admissible.

## Target phenomenon
- Unconstrained decision-resolution cost stays at 1.
- Branchwise-admissible resolution cost grows with M.
- Hence the admissibility penalty can be unbounded over the family.

## Why this matters
This is stronger than T001 because information acquisition remains possible throughout the admissible path; the issue is not simply that every useful experiment is forbidden.

## Novelty caution
An unbounded penalty may still be representable in existing varying-query-set or constrained adaptive-testing frameworks. The result is therefore a structural witness, not yet a novelty claim. The next test must compare exact representability/reduction and then examine minimum experiment-language expansion.

## Citation

Akhtar, M. A. K. (2026). *Where Cheapest Decision-Resolving Experiments Become Old Theory—and Where They Do Not: Reductions, Escape Costs, and Resolver-Choice Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22833604
