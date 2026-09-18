# T003 — Exact Reduction Attack: Fixed-Library Branchwise Admissibility

## Verdict
**Negative novelty result.**

For a fixed experiment library, define the query set available at epistemic state C as

Q(C) = {e : e is admissible in every world still contained in C}.

The branchwise-admissible Bellman recursion is then exactly a state-dependent-query adaptive decision process. T003 implements both recursions on the same finite witness and checks equality.

## Literature comparison
Fern et al. (ALT 2017) already extend adaptive submodularity to varying query sets. Their motivating mechanism is randomly constrained query availability, so their exact assumptions are not identical to our world-intersection rule; nevertheless, the existence of a state-dependent available-query set is not by itself a safe novelty claim.

Goal-oriented experimental design also already targets uncertainty in a downstream quantity of interest rather than complete parameter identification. Recent 2026 work extends this to nonlinear and risk-aware goal-oriented design.

## Consequence
We should **drop fixed-library branchwise availability as the headline contribution**. It remains a constraint in the model, but not the claimed breakthrough.

## Surviving target
The stronger target is a meta-design problem:

1. the current fixed experiment language is unable to resolve decision-incompatible worlds;
2. candidate new experiments have development/genesis costs;
3. choose the minimum-cost expansion of the experiment language that makes decision resolution possible;
4. jointly optimize genesis cost and subsequent adaptive execution cost.

Next: T004 exact Minimum Resolution Expansion.

## Citation

Akhtar, M. A. K. (2026). *Where Cheapest Decision-Resolving Experiments Become Old Theory—and Where They Do Not: Reductions, Escape Costs, and Resolver-Choice Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22833604
