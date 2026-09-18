# Test Ledger

| ID | Test | Status | Main result | Artifact |
|---|---|---|---|---|
| T001 | Minimal admissibility obstruction | PASSED | Ordinary decision-resolution cost is finite while branchwise-admissible resolution cost is infinite in a two-world witness | tests/T001_minimal_admissibility_obstruction.py |
| T002 | Nontrivial admissibility-penalty family | ADDED / exact family test | Tests whether admissibility creates an unbounded resolution-cost penalty while informative admissible tests remain available | tests/T002_admissibility_penalty_family.py |
| T003 | Fixed-library reduction attack | NEGATIVE NOVELTY RESULT | Branchwise universal admissibility is exactly representable as a state-dependent available-query map Q(C); do not claim changing query availability itself as novel | tests/T003_fixed_library_reduction.py |
| T004 | Minimum Resolution Expansion | PASSED / SIGNIFICANT | Exact family: decision-targeted genesis cost G_D=1 while full-identification genesis cost G_W=n over 2^n worlds; ratio n is unbounded | tests/T004_minimum_resolution_expansion.py |
| T005 | Joint genesis + execution separation | PASSED, CLAIM COLLISION | Joint design beats genesis-only and execution-only on an exact witness, but 2026 adaptive-sensing work already co-designs sensing hardware and adaptive policy | tests/T005_joint_genesis_execution.py |
| T006 | Minimum experiment-language repair | PASSED / SIGNIFICANT | Minimum repair contains weighted set cover as a special case; exact witness cost 2; restricted problem is NP-hard by reduction | tests/T006_minimum_language_repair.py |
| T007 | Exact vs greedy repair stress test | ADDED / BASELINE | 500 reproducible weighted random conflict-cover instances compare exact repair with greedy cost-per-conflict repair | tests/T007_exact_vs_greedy_repair.py |
| T008 | PhysioNet real-data decision-resolution benchmark | PASSED / SIGNIFICANT EMPIRICAL SIGNAL | 392/1000 held-out cases decision-unresolved; 61/1000 high-confidence yet unresolved; mean AUROC 0.8050 across 25 bootstrap worlds | results/T008_physionet_realdata.md |
| T009 | Cheapest resolving experiment novelty audit | CLAIM COLLISION / STOP | 2025–2026 prior art already covers minimum-cost interventions for identifiability, minimal-cost classifying experiments, and even cheapest additional experiments over possible physical worlds | results/T009_cheapest_experiment_collision.md |
| T010 | Admissibility-unlocking family | PASSED / STRUCTURAL, NOVELTY COLLISION | Exact family has C_ordinary=1 and C_admissible=M with useful universally admissible routing experiments, but belief-support safe-POMDP literature already has belief-dependent allowed-action sets | tests/T010_admissibility_unlocking_family.py |
| T011 | Adaptive experiment genesis vs ex-ante creation | PASSED / UNBOUNDED SEPARATION, PARTIAL NOVELTY COLLISION | J_static=M+2 versus J_adaptive=3, ratio unbounded; adaptive sensor placement and 2026 hardware-policy co-design occupy the broad claim | tests/T011_adaptive_genesis_vs_exante.py |
| T012 | Resolution Genesis Cost reduction attack | NEGATIVE NOVELTY RESULT / NARROWING | Generic minimum-cost creation of new sensing capability to restore a target property reduces to established sensor-network retrofit/minimum-cost instrumentation; G_R alone is not breakthrough novelty | results/T012_resolution_genesis_reduction_attack.md |\n| T013 | Full dynamic reduction attack | NEGATIVE NOVELTY RESULT / BRANCH REDUCED | Finite contingent experiment-language repair maps cost-preservingly to augmented belief-state/POMDP planning: state=(C,E), execute/create are actions, resolved classes are targets | tests/T013_dynamic_reduction_to_pomdp.py |

## Novelty audit notes
- Varying-query-set adaptive submodularity already studies adaptively changing query availability.
- Safe active learning already selects informative queries subject to safety constraints.
- Goal-oriented OED targets downstream quantities of interest rather than full latent-state identification.
- Sequential OED already optimizes non-myopic sequences for model discrimination, inference, and goal-oriented prediction.
- 2026 adaptive-sensing work explicitly co-designs sensor hardware geometry and adaptive measurement policy; generic genesis+execution co-design is therefore not a novelty claim.
- Current strongest surviving target: **not a new generic planning framework. Pivot to restricted separation theorems for decision-resolution certificates versus confidence/entropy/information-gain criteria, then validate the surviving theorem on large real data.**

## Stop/write criterion
Do not start the manuscript until the surviving target has:
1. a non-reduction argument against closest prior frameworks,
2. theorem-level strict separation,
3. exact finite verification,
4. large synthetic stress test,
5. substantial real-data validation.
