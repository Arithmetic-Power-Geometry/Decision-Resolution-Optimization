# Test Ledger

| ID | Test | Status | Main result | Artifact |
|---|---|---|---|---|
| T001 | Minimal admissibility obstruction | PASSED | Ordinary decision-resolution cost is finite while branchwise-admissible resolution cost is infinite in a two-world witness | tests/T001_minimal_admissibility_obstruction.py |
| T002 | Nontrivial admissibility-penalty family | ADDED / exact family test | Tests whether admissibility creates an unbounded resolution-cost penalty while informative admissible tests remain available | tests/T002_admissibility_penalty_family.py |
| T003 | Fixed-library reduction attack | NEGATIVE NOVELTY RESULT | Branchwise universal admissibility is exactly representable as a state-dependent available-query map Q(C); do not claim changing query availability itself as novel | tests/T003_fixed_library_reduction.py |
| T004 | Minimum Resolution Expansion | PASSED / SIGNIFICANT | Exact family: decision-targeted genesis cost G_D=1 while full-identification genesis cost G_W=n over 2^n worlds; ratio n is unbounded | tests/T004_minimum_resolution_expansion.py |
| T005 | Joint genesis + execution separation | PASSED, CLAIM COLLISION | Joint design beats genesis-only and execution-only on an exact witness, but 2026 adaptive-sensing work already co-designs sensing hardware and adaptive policy | tests/T005_joint_genesis_execution.py |
| T006 | Minimum experiment-language repair | PASSED / SIGNIFICANT | Minimum repair contains weighted set cover as a special case; exact witness cost 2; restricted problem is NP-hard by reduction | tests/T006_minimum_language_repair.py |

## Novelty audit notes
- Varying-query-set adaptive submodularity already studies adaptively changing query availability.
- Safe active learning already selects informative queries subject to safety constraints.
- Goal-oriented OED targets downstream quantities of interest rather than full latent-state identification.
- Sequential OED already optimizes non-myopic sequences for model discrimination, inference, and goal-oriented prediction.
- 2026 adaptive-sensing work explicitly co-designs sensor hardware geometry and adaptive measurement policy; generic genesis+execution co-design is therefore not a novelty claim.
- Current strongest surviving target: **certify decision-resolution obstruction, then compute a minimum discrete repair of the experiment language that changes resolution cost from infinity to finite, followed by an adaptive decision-resolution policy.**

## Stop/write criterion
Do not start the manuscript until the surviving target has:
1. a non-reduction argument against closest prior frameworks,
2. theorem-level strict separation,
3. exact finite verification,
4. large synthetic stress test,
5. substantial real-data validation.
