# T011 — Adaptive Experiment Genesis vs Ex-Ante Creation

## Construction
Worlds are W_M={(A,i),(B,i): i=1,...,M}. The decision is A/B.

An existing unit-cost routing experiment r reveals nuisance branch i but does not distinguish A from B. For every branch i, a not-yet-existing capability z_i can be created at genesis cost 1. Once z_i exists, unit-cost experiment e_i separates A/B on branch i and is non-resolving elsewhere.

## Exact separation
A robust ex-ante design that must decide what capabilities exist before observing r must create all M branch-specific capabilities:

J_static = M + 2.

An evidence-conditioned genesis policy executes r, observes i, creates only z_i, and executes e_i:

J_adaptive = 3.

Therefore

J_static/J_adaptive = (M+2)/3 -> infinity.

This proves an unbounded value of delaying experimental-capability creation until after informative evidence.

## Novelty attack
**Structural theorem passed; headline novelty did not survive intact.**

Adaptive sensor placement already chooses sensor locations sequentially from feedback (Grant et al., ICML 2019). Stochastic sensor-placement literature has long modeled staged decisions/recourse under uncertainty. Most importantly, Keshvari, Tuxbury & Lin (2026), *Adaptive Sensing beyond Non-Adaptive Information Limits*, jointly optimizes physical sensing hardware geometry and an adaptive measurement policy by dynamic programming.

Thus 'adaptive sensing beats non-adaptive sensing' and generic 'hardware + policy co-design' are occupied.

## Remaining distinction to test
Our potentially different object is **post-evidence genesis of a previously unavailable experiment language**, with a decision-resolution obstruction certificate before genesis and a proof that the created capability changes resolution cost from infinity to finite.

T012 must test whether that object is exactly reducible to:
- multistage stochastic programming with recourse,
- adaptive sensor placement,
- configurable/reconfigurable sensing,
- POMDP actions that buy/activate sensors,
- value-of-information with endogenous information structures.

If reducible, stop this branch. If not, formalize the non-reduction theorem before any manuscript.
