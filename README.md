# Decision-Resolution Optimization

A reproducible research software laboratory for minimum-cost decision resolution under mutually incompatible possible worlds.

## Scope

The repository implements and tests finite decision-resolution models in which current evidence induces a compatible set of possible worlds, a decision map assigns the required action in each world, and experiments reveal outcomes at explicit costs. The software evaluates when a decision can be resolved, the minimum cost of doing so, and which apparent extensions reduce to established finite experimental-design objects.

The completed programme contains exact reductions, counterexamples, synthetic stress tests, workflow-backed computational experiments, and large real-data studies. Positive and negative results are retained in the repository.

## Mathematical objects

Let \(W\) be the world set, \(D:W\to A\) the decision map, and \(C\subseteq W\) the worlds compatible with current evidence. Each experiment \(e\) has cost \(c(e)\) and outcome map \(O_e(w)\).

A state is decision-resolved when all worlds in \(C\) imply the same decision. For finite deterministic experiments, the exact worst-case value is

```text
V(C) = 0,                                             if C is decision-resolved

V(C) = min_e [ c(e) + max_o V(C_{e,o}) ],           otherwise
```

over currently available informative experiments.

## Main computational findings

- **Exact finite reduction to ECD (T017/T020).** Finite deterministic fixed-library decision resolution maps exactly to Equivalence Class Determination: worlds become hypotheses, decision values become equivalence classes, and experiment outcomes and costs are preserved.
- **Finite experiment creation reduction (T021).** A known one-shot creatable experiment with build cost \(k\) and execution cost \(c\) compiles into an enlarged ECD library with cost \(k+c\).
- **Escape-cost nonidentifiability (T022).** Systems with identical current observational/ECD structure can require external separating experiments whose synthesis costs differ by an arbitrarily large factor.
- **Resolver-choice uncertainty (T023).** Compatible worlds can disagree about the identity of the cheapest future resolver. A finite two-regime construction gives blind minimax cost \(M\) versus meta-probe plus resolver cost 2.
- **Decision-targeted separation (T024).** A decision-targeted generated probe can cost 1 while full-world identification costs \(n+1\); the family has an unbounded ratio.
- **Large real-data evidence (T025–T027).** Resolver-choice uncertainty occurs in 30.045% of 20,000 UCI Covertype evaluation cases, but only 3.524% of 11,293 NHANES evaluation cases. Covertype meta-routing reduces mean proxy loss by about 0.24%, establishing only a small practical effect.

These results define the boundary of the software: the fixed finite core is established ECD rather than a new planning primitive, while external escape cost and resolver identity require information not contained in current observational equivalence alone.

## Repository structure

```text
tests/          exact finite constructions, reductions, and stress tests
experiments/    real-data and larger empirical experiments
results/        retained result summaries
.github/        reproducible GitHub Actions workflows
TESTS.md        permanent test ledger
CITATION.cff    machine-readable citation metadata
```

## Reproducibility

The repository preserves executable tests, workflow definitions, result summaries, and the complete test ledger. Individual experiments can be run from their corresponding Python files. Workflow-backed tests record the exact computational path used for the retained results.

Real-data experiments use publicly available UCI Covertype and NHANES data. Feature/analyte counts used in T025–T027 are proxy acquisition costs and must not be interpreted as monetary prices.

## Test ledger

The full sequence T001–T027, including negative novelty tests and failed replication gates, is retained in [TESTS.md](TESTS.md).

## Citation

Akhtar, M. A. K. (2026). *Where Cheapest Decision-Resolving Experiments Become Old Theory—and Where They Do Not: Reductions, Escape Costs, and Resolver-Choice Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22833604

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
