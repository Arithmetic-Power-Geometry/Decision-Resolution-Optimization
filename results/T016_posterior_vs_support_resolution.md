# T016 — Posterior Decision vs Guaranteed Support Resolution

## Exact separation
Two incompatible decision classes remain after current evidence:
P(A|H)=1-delta and P(B|H)=delta.

A delta0-tolerant posterior decision rule may stop immediately whenever delta <= delta0. Its additional evidence cost is therefore 0.

Construct the experiment family so that B can be eliminated only after n unit-cost measurements (A and B remain observationally compatible through the first n-1 required checks and separate on the nth).

Then:
C_posterior(delta0)=0,
C_support=n,
GuaranteePremium=n.

The additive premium is unbounded as n grows.

## Interpretation
There is a mathematically sharp difference between:
- accepting a prescribed nonzero probability of decision error, and
- requiring every still-compatible world to imply the same decision.

## Novelty attack
**The separation is not a breakthrough by itself.** Fixed-confidence best-arm identification already makes the allowed error probability delta explicit and minimizes sampling/evidence cost subject to a delta-correctness guarantee. Recent work continues to derive instance-dependent lower bounds and asymptotically optimal fixed-confidence procedures. As delta approaches zero, evidence requirements can grow sharply; exact zero-error/support identification is a stronger criterion.

Therefore 'guarantees cost more than high posterior confidence' is established statistical decision theory territory.

## More useful consequence
The project should stop trying to derive novelty merely from zero-error/support guarantees versus probabilistic confidence. The remaining potentially useful object is computational/structural:

**Given a finite compatible-world representation and heterogeneous experiment costs, compute the minimum-cost experiment whose outcome partitions eliminate all currently decision-incompatible pairs, without requiring full world identification.**

But ECD/optimal decision-tree work is already extremely close. Before another theorem, run a direct equivalence test against ECD. If exact equivalence holds, the foundational branch is exhausted.

## Status
PASSED MATHEMATICALLY / CLAIM COLLISION.
