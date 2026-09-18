# Test Ledger

| ID | Test | Status | Main result | Artifact |
|---|---|---|---|---|
| T001 | Minimal admissibility obstruction | PASSED | Ordinary decision-resolution cost is finite while branchwise-admissible resolution cost is infinite in a two-world witness | tests/T001_minimal_admissibility_obstruction.py |
| T002 | Nontrivial admissibility-penalty family | ADDED / exact family test | Tests whether admissibility creates an unbounded resolution-cost penalty while informative admissible tests remain available | tests/T002_admissibility_penalty_family.py |
| T003 | Fixed-library reduction attack | NEGATIVE NOVELTY RESULT | Branchwise universal admissibility is exactly representable as a state-dependent available-query map Q(C); do not claim changing query availability itself as novel | tests/T003_fixed_library_reduction.py |
| T004 | Minimum Resolution Expansion | PASSED / SIGNIFICANT | Exact family: decision-targeted genesis cost G_D=1 while full-identification genesis cost G_W=n over 2^n worlds; ratio n is unbounded | tests/T004_minimum_resolution_expansion.py |

## Novelty audit notes
- Varying-query-set adaptive submodularity already studies adaptively changing query availability; branch-dependent availability alone is not a novelty claim.
- Safe active learning already selects informative queries subject to safety constraints; safe information acquisition alone is not a novelty claim.
- Goal-oriented OED already targets downstream quantities of interest rather than full latent-state identification; T004's decision-vs-world saving is therefore not sufficient alone.
- Current surviving target: **experiment-language expansion with distinct genesis cost, followed by adaptive execution, and joint optimization of genesis + execution cost under decision-resolution constraints.**

## Stop/write criterion
Do not start the manuscript until the surviving target has:
1. a non-reduction argument against closest prior frameworks,
2. theorem-level strict separation,
3. exact finite verification,
4. large synthetic stress test,
5. substantial real-data validation.
