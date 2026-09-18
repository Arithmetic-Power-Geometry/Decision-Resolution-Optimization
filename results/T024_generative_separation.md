# T024 — Generative Decision-Separation Attack

## Status
**COMPLETED — UNBOUNDED MATHEMATICAL SEPARATION / NOVELTY COLLISION**

Corrected GitHub Actions run 35355923946 succeeded.

Worlds are (d,z1,...,zn), with d decision-relevant and z nuisance. A generated parity probe of d alone has cost 1 and separates the decision-paired worlds. Full identification of n+1 independent bits requires n+1 unit binary probes; a generic symmetric parameter-information policy can also spend the n nuisance probes before d under adverse tie-breaking.

The corrected implementation verifies the decision separator exhaustively through n=14 and extends the family analytically through n=20.

- decision synthesis cost = 1
- full-world identification cost = n+1
- tested ratio reaches 21 at n=20
- family ratio n+1 -> infinity

## Interpretation
This is a valid unbounded separation between decision-targeted synthesis and full parameter/world identification.

## Novelty boundary
It is not sufficient as a foundational novelty claim because goal-/decision-oriented OED already targets decision-relevant or QoI-relevant experimental information rather than full parameter identification. Preserve T024 as a boundary theorem/example, not the headline invention.

## Research decision
Close the generic decision-vs-parameter-information branch. The next empirical test should target the less-settled T022/T023 phenomenon: uncertainty over the identity/cost of the cheapest resolving measurement itself.
