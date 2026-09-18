# T013 — Full Dynamic Reduction Attack

## Question
Is contingent experiment-language repair mathematically outside POMDP / multistage recourse planning?

## Result
**No, not in the finite general form we have defined.**

For a finite repair problem, augment the planning state with both:
- the current compatible-world set C (equivalently a belief/support representation), and
- the current experiment/capability set E.

Then:
- executing experiment e is an action with cost c(e), observation-conditioned transition C -> C_{e,o};
- creating capability z is an action with cost k(z), transition (C,E)->(C,E union {z});
- branchwise admissibility is an action-feasibility condition at state (C,E);
- decision-resolved classes are target states.

Thus the native Bellman recursion is a cost-preserving reachability/planning recursion on the augmented state space.

The accompanying exact finite witness computes the native recursion and the constructed planning recursion and asserts equality.

## Prior-art pressure
This is not merely a formal possibility. Cost-sensitive feature acquisition has been formulated as a POMDP since at least Ji & Carin (Pattern Recognition, 2007). Li & Oliva (AISTATS 2025) explicitly propose an Active-Acquisition POMDP that chooses additional features while balancing acquisition cost and decision reward. Cost-optimal almost-sure target reachability in POMDPs is established by Chatterjee et al. (Artificial Intelligence, 2016). Multistage stochastic programming likewise permits recourse decisions after uncertainty is progressively revealed.

## Verdict
**NEGATIVE NOVELTY RESULT / BRANCH REDUCED.**

The generic dynamic language-repair Bellman formulation is representable inside existing sequential decision frameworks. Renaming the augmented state or create action does not create a new theory.

## What survives
The empirical phenomenon from T008 remains useful: high predictive confidence can coexist with decision disagreement across compatible model worlds.

The theoretical project should now pivot away from claiming a new general sequential-planning framework. A potentially defensible next direction is a **restricted structural theorem** about the resolution certificate itself: find conditions under which confidence/entropy/information-gain criteria provably cannot certify a decision although a small decision-separating witness can, with a gap that grows with problem size. That theorem must be compared directly with equivalence-class determination, best-arm identification, and hypothesis testing.

No paper should be written from the current generic framework yet.
