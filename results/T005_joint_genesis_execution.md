# T005 — Joint Genesis + Execution Separation

## Result
A three-capability witness separates three design rules.

| Capability | Genesis cost | Optimal execution cost | Total |
|---|---:|---:|---:|
| cheap_build | 1 | 100 | 101 |
| cheap_run | 30 | 1 | 31 |
| balanced | 10 | 10 | 20 |

Thus:
- minimizing genesis cost alone selects total cost 101;
- minimizing execution cost alone selects total cost 31;
- joint optimization selects total cost 20.

So co-optimizing capability creation and subsequent experiment execution can strictly dominate optimizing either stage separately.

## Novelty attack / result
This is **not enough for a breakthrough**. A 2026 preprint, *Adaptive Sensing beyond Non-Adaptive Information Limits: End-to-End Co-Design of Geometry, Policy, and Inference*, explicitly formulates joint dynamic programming over sensing hardware geometry and an adaptive measurement policy. Dynamic joint sensor-selection/maintenance work also jointly optimizes sensing and downstream actions.

Therefore the generic claim "jointly design measurement hardware/capability and adaptive policy" is already occupied.

## Surviving distinction to test
Our candidate must rely on something those formulations do not already provide:
1. **decision-incompatible possible worlds** as the stopping target rather than estimation loss;
2. an **obstruction certificate** proving a current experiment language cannot resolve the decision;
3. **minimum language repair/expansion** specifically to cross from infinite resolution cost to finite resolution cost;
4. preferably a combinatorial theorem about the minimum repair set, not merely continuous hardware co-design.

Next test: T006 formal reduction/non-reduction against adaptive sensing co-design and goal-oriented sequential OED.
