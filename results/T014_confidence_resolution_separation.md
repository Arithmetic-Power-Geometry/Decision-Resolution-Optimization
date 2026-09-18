# T014 — Confidence–Resolution Separation

## Exact construction
Let two compatible worlds remain after history H:
- w_A requires decision A and has posterior mass 1-delta;
- w_B requires incompatible decision B and has posterior mass delta, for any delta>0.

Bayesian confidence in A is

Conf(A|H)=1-delta,

so Conf -> 1 as delta -> 0.

But the support-based decision-resolution certificate asks whether **all still-compatible worlds imply the same decision**. Since w_B remains compatible for every delta>0,

R_D(H)>0

for every delta>0.

Hence

Conf(A|H) -> 1 while RC(H)=0.

The supplied script verifies the finite construction down to delta=1e-12.

## Significance
This cleanly explains the empirical pattern seen in T008: high aggregate predictive confidence need not imply agreement across all retained model worlds.

## Novelty attack
**The separation is mathematically correct but is not sufficient novelty.**

Bayesian best-arm identification already distinguishes posterior confidence/error probability from exact certainty and develops fixed-confidence stopping rules. Robust Bayesian decision-making under adversarial uncertainty (Harikumar et al., 2026) explicitly reports that conventional decision-aware design can reach high-confidence yet fragile decisions. More generally, robust Bayes / imprecise-probability reasoning has long distinguished posterior mass from robustness over a set of plausible models.

Therefore the theorem 'confidence can approach one while a low-mass incompatible world remains possible' is expected once resolution is defined by support rather than posterior mass.

## Next sharper test
Do not stop at confidence. Test whether **entropy or expected information gain can rank experiments oppositely to minimum decision-resolution cost by an unbounded factor**.

Construct nuisance uncertainty with enormous entropy that is irrelevant to the decision, plus one low-entropy decision-critical bit. Information-gain acquisition should spend on nuisance bits, while a resolution-targeted experiment queries the critical bit immediately. If the ratio can be made unbounded and the exact criterion is not already covered by ECD/adaptive submodularity, that is a more meaningful theorem candidate.
