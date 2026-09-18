# Test Ledger

| ID | Test | Status | Main result | Artifact |
|---|---|---|---|---|
| T001 | Minimal admissibility obstruction | PASSED | Ordinary decision-resolution cost is finite while branchwise-admissible resolution cost is infinite in a two-world witness | tests/T001_minimal_admissibility_obstruction.py |
| T002 | Nontrivial admissibility-penalty family | ADDED / exact family test | Tests whether admissibility creates an unbounded resolution-cost penalty while informative admissible tests remain available | tests/T002_admissibility_penalty_family.py |

## Novelty audit notes
- Varying-query-set adaptive submodularity already studies adaptively changing query availability; branch-dependent availability alone is not a novelty claim.
- Safe active learning already selects informative queries subject to safety constraints; safe information acquisition alone is not a novelty claim.
- Current surviving target: distinguish knowledge-state universal admissibility and, more importantly, minimum-cost expansion of the experiment language when fixed-library resolution is impossible.
