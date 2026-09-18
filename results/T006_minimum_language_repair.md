# T006 — Minimum Experiment-Language Repair as Conflict-Cover

## Construction
Let unresolved decision-incompatible world pairs be conflict edges. Each candidate new experiment separates a subset of those edges and has a genesis cost.

If resolution requires every conflict edge to be separated by at least one newly available experiment, the minimum language expansion is:

min sum k(z)
subject to every decision-conflict edge being covered.

This contains weighted set cover as a special case.

## Exact witness
The included exhaustive solver finds the minimum repair set {z3,z4} with total genesis cost 2.

## Complexity consequence
Because arbitrary weighted set-cover instances can be encoded as conflict-edge/candidate-experiment instances, this restricted Minimum Language Repair problem is NP-hard. This is a reduction observation, not yet a fully written formal proof.

## Significance
This is stronger than merely saying "design a sensor." It turns a **resolution obstruction** into a minimum discrete repair problem over an experimental language.

## Novelty caution
Weighted set cover, test cover, sensor placement, and experiment design are established. The potentially publishable contribution would have to be the full chain:
decision-resolution obstruction -> minimum repair -> adaptive post-repair policy -> strict separations/approximation results.

Next: large random exact instances and then a real dataset whose feature/measurement acquisition has meaningful costs.
