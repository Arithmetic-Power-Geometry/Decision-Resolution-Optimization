# T015 — Information-Gain vs Decision-Resolution Separation

## Construction
Worlds are (d,z), where d is the binary decision-critical variable and z contains n independent nuisance bits. The prior is uniform.

Every unit-cost experiment reveals one bit. e_D reveals d; e_1,...,e_n reveal nuisance bits. Thus parameter-entropy information gain is one bit for every experiment at the initial state. A valid IG-maximizing tie-breaking can therefore consume all n nuisance probes before e_D.

Resolution-targeted policy executes e_D immediately.

C_resolution = 1,
C_IG = n+1,

so the ratio is n+1 and is unbounded.

## Important limitation
This is **not a breakthrough novelty theorem**. The construction attacks parameter-information gain, but the literature already recognized exactly this structural problem:
- Equivalence Class Determination (ECD) targets the class rather than complete hypothesis identification.
- Goal-oriented OED targets a downstream QoI rather than full parameter uncertainty.
- 2026 GoBOED explicitly states that reducing parameter uncertainty need not improve downstream decisions and proves insensitivity to decision-irrelevant parameter directions.
- Bayesian active learning with nuisance parameters explicitly separates target from nuisance uncertainty.

Moreover, ECD literature contains bad examples where information-gain and value-of-information heuristics can be asymptotically worse than optimal class-determination policies.

## Verdict
PASSED MATHEMATICALLY / CLAIM COLLISION.

Do not claim 'information gain wastes effort on nuisance uncertainty' as new.

## Next research gate
The next useful test must compare **decision-targeted** information criteria, not parameter IG. Specifically compare:
1. entropy of the decision/equivalence class,
2. EC2/ECD conflict-edge objective,
3. value of information on the downstream decision,
4. exact worst-case support-resolution cost.

Search for a family where posterior-weighted decision criteria terminate cheaply or assign negligible value to a low-probability incompatible class, while worst-case support resolution still requires expensive evidence. If that merely reproduces known ECD worst cases, stop this theoretical direction and focus the paper as an empirical/methodological application rather than a foundational theory claim.
