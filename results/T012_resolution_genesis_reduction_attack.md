# T012 — Reduction Attack: Resolution Genesis Cost

## Candidate object
For compatible-world class C and current experiment language E,

G_R(C,E)=min_Z K(Z) subject to C_R(C; E union Z)<infinity.

The intended interpretation is the minimum genesis/development cost of adding previously unavailable observational capability that changes a decision from non-resolvable to resolvable.

## Literature attack

### 1. Sensor-network retrofit / minimum-cost instrumentation
**Strong collision.** Process-systems literature explicitly studies adding new instrumentation to an existing sensor network at minimum cost, including retrofit, observability, precision, and fault-detection constraints. This occupies generic 'minimum-cost new sensors to restore/achieve observability or detectability.'

### 2. Value-of-information sensor-network design
**Strong collision.** Sensor-network design has also optimized economic value of information minus sensor cost rather than only full observability.

### 3. Endogenous costly information acquisition
**Collision at the acquisition layer.** Decision makers choosing when/whether to purchase informative signals is established.

### 4. Minimum-cost experimental design
**Collision at generic cost-constrained information targets.** Minimum-cost designs satisfying prescribed information requirements are established.

## Reduction verdict
A completely general G_R can be encoded as a minimum-cost instrumentation/retrofit problem by treating each candidate experiment as a candidate instrument and decision resolution as the required monitoring property. Therefore **G_R alone is not a defensible breakthrough object.**

The extra requirement 'decision-incompatible worlds rather than full state observability' is useful, but task/goal-oriented information design already weakens the need for full-state recovery. That distinction alone is insufficient.

## Surviving direction
The remaining candidate must exploit a property not present in ordinary retrofit:

1. capability creation is **contingent on evidence obtained after deployment begins**;
2. creation changes the future experiment language;
3. admissibility of the created experiment must hold over the current compatible-world class;
4. terminal requirement is decision resolution, not state reconstruction;
5. the object should admit a separation theorem that cannot be reproduced by a static sensor-set selection problem.

This is now an **adaptive epistemic retrofit / contingent language repair** problem. T013 should try to reduce that full dynamic object to multistage stochastic programming with recourse or POMDP sensor-purchase actions. If exact reduction succeeds, this branch should be abandoned rather than renamed.

## Status
NEGATIVE NOVELTY RESULT / important narrowing test.
