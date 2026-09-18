# T026 — Real-data meta-resolution value

## Status
**COMPLETED — WEAK POSITIVE / PRACTICALLY SMALL; DOES NOT PASS BREAKTHROUGH GATE**

GitHub Actions run 35357711499 succeeded on UCI Covertype.

## Data
581,012 total rows; 464,809 training; 10,000 evaluation; 54 features; 7 classes; 10 bootstrap worlds.

## Results
- mean static direct loss: 12.7339
- mean best meta-routing loss: 12.70357
- mean reduction: 0.03033 (~0.24%)
- fraction meta better: 0.0242
- fraction >=10% better: 0.0159
- median improvement conditional on improvement: 1.0
- selected meta panel: hillshade 9,118; distances 749; wilderness 133.

## Interpretation
Meta-routing technically lowers mean proxy loss, but the effect is tiny and occurs in only 2.42% of evaluated cases. This is not strong enough to support a practical breakthrough claim.

## Novelty boundary
Sequential/adaptive OED, POMDP formulations, deep adaptive design, and goal-oriented sequential design already permit early observations to change later experiment choices. T026 therefore does not establish a new primitive.

## Research decision
Do not write a breakthrough paper from the meta-routing algorithm. Preserve T022/T023/T025 as boundary/diagnostic results. One final test is justified only if it targets the structural claim directly with meaningful real acquisition costs or a dataset where measurement panels have semantics; otherwise stop the branch or write a limits/boundary paper.
