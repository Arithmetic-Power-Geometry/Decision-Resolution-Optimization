# T023 — Meta-Resolution / Experiment-Choice Identifiability

## Status
**COMPLETED — STRONG PHENOMENON, FINITE REDUCTION COLLISION**

GitHub Actions run 35354758712 succeeded.

Two design regimes swap the costs of two resolving experiments x and y. Under current evidence the regime is unknown, so the identity of the cheapest resolving experiment is itself unresolved. A unit-cost meta-probe reveals the regime.

For M = 2,4,8,16,32,64,128:
- blind minimax resolver cost = M;
- meta-probe then resolver cost = 2;
- advantage ratio = M/2, reaching 64 in the run and unbounded as M grows.

## Positive phenomenon
The cheapest experiment for resolving the scientific decision can itself be unresolved. Learning which experiment is cheapest can have an unbounded value relative to blindly committing to a resolver.

## Reduction attack
When the design regime is included in the hidden state and meta-probes are represented as information-gathering actions, the finite formulation is representable by augmented hidden-state planning / ECD-POMDP machinery.

## Verdict
Keep experiment-choice unidentifiability and the unbounded meta-information value as a useful phenomenon. Do not claim a new finite foundational computational primitive. The next novelty test must address non-enumerable/generative experiment synthesis and compare directly with continuous OED / automated experiment design.
