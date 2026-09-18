# T009 — Cheapest-Experiment Novelty Collision Audit

## Question
Can the headline contribution be:

> Given current knowledge that leaves mutually incompatible possible worlds, find the cheapest experiment that resolves the decision?

## Verdict
**NO as a standalone novelty claim.**

Fresh prior-art attack found multiple close formulations.

1. Healy & Leo, *Which experiments test a model?*, Journal of Economic Theory 235 (2026), explicitly characterize experiments that classify/test a model and then identify minimal experiments, including cost orderings.
2. Akbari, Etesami & Kiyavash, *Optimal Experiment Design for Causal Effect Identification*, JMLR 26 (2025), asks for a minimum-cost collection of interventions that turns a non-identifiable target into an identifiable one; proves NP-completeness and a hitting-set connection.
3. A September 2026 benchmark, *New Evidence, Same Choice*, explicitly gives multiple possible physical worlds and asks a model to select the **cheapest additional experiment that can resolve the question**.

Therefore "cheapest resolving experiment" is now decisively occupied territory.

## Consequence
Do not build the paper around cheapest resolution alone. T006's minimum-repair/set-cover result also has a strong structural collision with minimum-cost intervention design for causal identification.

## Surviving research question
The candidate must add a mathematically non-reducible ingredient, likely:

**Decision-relative admissibility deadlock + language repair under universal branchwise admissibility.**

The key object is not merely whether an experiment separates worlds, but whether it can be legitimately executed *before* knowing which unresolved world is true. A repair may need to create a new experiment that is universally admissible over the current epistemic class and unlocks later experiments.

Next test: construct a family where ordinary minimum-cost identification/experiment-design has a cheap solution, but every such solution is epistemically inadmissible; only a multi-stage admissibility-unlocking repair resolves the decision. Then test exact reducibility to robust/safe POMDP belief-support action constraints.
