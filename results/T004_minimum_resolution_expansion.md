# T004 — Minimum Resolution Expansion and Decision-vs-Identification Genesis Cost

## Setup
The fixed experimental language is treated as insufficient. Candidate primitive measurements can be **created** at genesis cost 1 each.

For n latent binary components there are 2^n possible worlds. The downstream optimization decision depends only on the first component.

## Exact exhaustive result
To resolve the downstream decision, creating the first-component measurement is sufficient:

G_decision = 1.

To identify the complete world, all n component measurements are required:

G_full = n.

Therefore

G_full / G_decision = n,

which is unbounded as n grows.

The included exact enumerator verifies the minimum over every subset of candidate measurements for n = 2, 3, 4, 5, 8, 10 (up to 1,024 possible worlds).

## Interpretation
This demonstrates a strict distinction between **building enough observational capability to resolve a decision** and **building enough capability to identify the latent world**.

## Novelty status
**Significant structural result, but not yet a breakthrough claim.** Goal-oriented optimal experimental design already targets a downstream quantity of interest rather than full parameter inference. Thus the decision-vs-world saving alone overlaps goal-oriented sensing/OED.

What remains potentially stronger is the combination of:
- a fixed language with a decision-resolution obstruction;
- discrete synthesis/expansion of the experiment language itself;
- genesis cost distinct from execution cost;
- adaptive execution after expansion;
- joint optimization of expansion and execution.

T005 must test whether joint genesis+execution design yields a strict separation from optimizing either stage independently.
