# T020 — Exact Cheapest Decision Resolution vs EC2 and Information Gain

## Status
**COMPLETED — FOUNDATIONAL COLLISION CONFIRMED**

GitHub Actions run: 35353367847 (success).

1000 reproducible random heterogeneous-cost finite instances were generated; 847 were decision-resolvable.

| Policy | Mean cost / exact optimum | Maximum ratio | Exactly optimal fraction |
|---|---:|---:|---:|
| Exact Bellman / optimal ECD | 1.000 | 1.000 | 1.000 |
| EC2-style edge cutting / cost | 1.1614 | 2.000 | 0.4545 |
| Information gain / cost | 1.3299 | 2.750 | 0.2751 |

## Interpretation
The exact Bellman objective for the cheapest sequence of experiments that eliminates all decision-incompatible surviving worlds is precisely the optimal finite deterministic Equivalence Class Determination problem. EC2 and information-gain/cost are heuristic/approximate policies for that problem, not different foundational problem definitions.

The numerical benchmark is therefore a **collision result**, not a novelty claim. It independently confirms T017's exact reduction on a larger heterogeneous-cost family.

## Research decision
Do not claim finite fixed-library cheapest decision resolution as a new foundational theory. Close this branch. Any next breakthrough candidate must introduce a property that cannot be encoded as an enlarged ECD/decision-tree/POMDP state and must survive a formal reduction attack before real-data investment.
