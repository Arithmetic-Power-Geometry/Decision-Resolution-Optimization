# T021 — Experiment-Creation Reduction Attack

## Status
**COMPLETED — COLLISION / BRANCH CLOSED**

GitHub Actions run 35354211768 succeeded.

1000 finite heterogeneous-cost instances were tested. A known one-shot creatable experiment with build cost k and execution cost c was compiled into an enlarged fixed experiment library with cost k+c.

- instances: 1000
- mismatches: 0
- equal optimal-cost fraction: 1.000

## Result
For this finite known-menu model, experiment creation adds no irreducible decision-resolution structure: it compiles exactly into enlarged ECD by treating each creatable experiment as an available test with total cost creation + execution.

## Research decision
Do not claim finite known-menu experiment creation as foundational novelty. Any surviving candidate must involve structure not faithfully compilable into a fixed finite test library (for example genuinely generative/continuous design with a structural theorem), and must still survive comparison with optimal experimental design and sensor-design literature.
