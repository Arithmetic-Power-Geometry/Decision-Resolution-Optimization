# T010 — Admissibility-Unlocking Family

## Exact family
There are 2M worlds (A,i) and (B,i), i=1,...,M. The decision is A versus B.

For each index i there is a unit-cost direct discriminator d_i. It perfectly separates (A,i) from (B,i), but it is not legitimate to execute until the nuisance index i has been certified.

A chain of universally admissible routing experiments identifies i but does not resolve A versus B. After routing, d_i becomes admissible.

## Separation
Ignoring branchwise admissibility, the relevant direct discriminator costs 1.

Under branchwise admissibility, worst-case routing costs M-1 and the final direct discriminator costs 1:

C_ordinary = 1,
C_admissible = M.

Therefore C_admissible / C_ordinary = M -> infinity.

Unlike the trivial two-world obstruction, informative and universally admissible experiments remain available throughout the unlocking stage.

## Novelty audit
This theorem family is mathematically useful but **not sufficient as a novelty claim**. POMDP literature already uses belief-support states and restricts allowed/safe actions as a function of current belief support; safe POMDP shielding likewise prunes actions that can leave a winning belief-support region.

Hence 'information changes which actions are safe/allowed' is established in POMDPs.

## Surviving question
Can **creating a new experiment/capability** (not merely selecting an existing safe action) repair a decision-resolution deadlock at minimum genesis cost, where the created experiment changes the reachable belief-support/action structure? This is the next reduction target.
