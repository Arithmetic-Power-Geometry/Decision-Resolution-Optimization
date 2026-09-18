# T017 — Exact Decision Resolution ↔ ECD Reduction

## Mapping
For any finite deterministic Decision Resolution instance:
- each possible world w becomes an ECD hypothesis h_w;
- decision classes are exactly the ECD equivalence classes induced by D(w);
- each experiment becomes the same ECD test with identical outcomes and cost;
- the compatible-world set becomes the ECD version space.

Decision Resolution stops exactly when all surviving worlds require the same decision:

forall w_i,w_j in C, D(w_i)=D(w_j).

ECD stops exactly when the version space is contained in one equivalence class.

Therefore the feasible adaptive policies, branch structure, test costs, and terminal states coincide. Expected-cost objectives coincide under the same prior; worst-case-cost objectives coincide under the same max-over-branches convention.

## Computational check
The accompanying script verifies equality of the two Bellman recursions on a nontrivial six-world, three-decision, heterogeneous-cost instance, and checks equality for every nonempty compatible-world subset.

## Literature confirmation
Golovin, Krause & Ray (NIPS 2010) define ECD as hypotheses partitioned into equivalence classes, with the goal of adaptively selecting costly tests until the version space lies inside one class. Decision Region Determination later generalizes this to overlapping regions. Later work continues to optimize costly decision trees and class-identification variants.

## Verdict
**FOUNDATIONAL FINITE BRANCH EXHAUSTED.**

Finite deterministic Decision Resolution with fixed experiments is not merely similar to ECD; under the mapping above it is the same mathematical problem.

This means the project must not claim a new general theory from:
- decision-equivalence classes,
- minimum-cost resolving experiments,
- adaptive resolving trees,
- conflict-edge cutting,
- confidence/information-gain failures,
- or finite fixed-library resolution certificates.

## Next pivot
The strongest publishable opportunity now is empirical/methodological:
use the T008 real-data phenomenon and test whether a support/model-world disagreement diagnostic predicts later decision reversal or failure better than strong uncertainty baselines on large clinical data.

Required next benchmark:
- large cohort (prefer MIMIC-IV if access/licensing permits; otherwise another open large tabular dataset);
- patient-level split;
- sequential/nested feature blocks;
- baselines: confidence, entropy, ensemble variance/disagreement, margin, conformal-set size where applicable, and cost-aware active feature acquisition;
- primary target: future decision reversal / unresolved decision after additional evidence;
- report AUROC/AUPRC for reversal prediction plus acquisition cost.

This would be an applied contribution, not a claim that ECD mathematics is new.
