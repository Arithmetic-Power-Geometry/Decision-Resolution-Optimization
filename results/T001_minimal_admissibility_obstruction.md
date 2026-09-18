# T001 — Minimal Admissibility Obstruction

## Question
Can the current experiment library contain an experiment that would resolve mutually incompatible decision worlds, while no such experiment is executable without presupposing which world is true?

## Witness
Two worlds remain possible:
- wA -> decision A
- wB -> decision B

Two cost-1 experiments perfectly distinguish the worlds:
- eA is admissible only in wA.
- eB is admissible only in wB.

Ignoring admissibility, either experiment resolves the decision at cost 1.

Under branchwise universal admissibility, neither experiment may be selected while {wA,wB} remains possible.

## Exact result
- Unconstrained decision-resolution cost: 1
- Branchwise-admissible resolution cost: infinity

Therefore:

C_D < infinity does not imply C_A < infinity.

## Interpretation
The obstruction is not lack of informative experiments. Informative experiments exist. The obstruction arises because executing any resolving experiment would require knowledge that the experiment itself is intended to obtain.

## Novelty status
Foundational witness only. This result is too small to support a novelty claim by itself. Next tests must determine whether the phenomenon reduces exactly to existing varying-query-set, safe active-learning, or hypothesis-dependent-cost decision-tree formulations, and whether nontrivial finite/infinite separations persist at scale.

## Citation

Akhtar, M. A. K. (2026). *Where Cheapest Decision-Resolving Experiments Become Old Theory—and Where They Do Not: Reductions, Escape Costs, and Resolver-Choice Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22833604
