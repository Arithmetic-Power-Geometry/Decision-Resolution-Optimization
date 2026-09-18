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
| T012 | Resolution Genesis Cost reduction attack | NEGATIVE NOVELTY RESULT / NARROWING | Generic minimum-cost creation of new sensing capability to restore a target property reduces to established sensor-network retrofit/minimum-cost instrumentation; G_R alone is not breakthrough novelty | results/T012_resolution_genesis_reduction_attack.md |
| T013 | Full dynamic reduction attack | NEGATIVE NOVELTY RESULT / BRANCH REDUCED | Finite contingent experiment-language repair maps cost-preservingly to augmented belief-state/POMDP planning: state=(C,E), execute/create are actions, resolved classes are targets | tests/T013_dynamic_reduction_to_pomdp.py |
| T014 | Confidence–resolution separation | PASSED / NOT NOVEL ALONE | Posterior confidence 1-delta tends to 1 while a delta-mass incompatible world keeps support-based decision resolution false for every delta>0 | tests/T014_confidence_resolution_separation.py |
| T015 | Parameter-information-gain vs resolution | PASSED / CLAIM COLLISION | A valid parameter-IG policy can spend n nuisance probes before the one decision-critical probe, giving cost n+1 versus 1; ECD/goal-oriented OED already targets this distinction | tests/T015_information_gain_resolution_gap.py |
| T016 | Posterior decision vs guaranteed support resolution | PASSED / CLAIM COLLISION | For delta-tolerant stopping additional cost can be 0 while exact support resolution costs n; unbounded additive guarantee premium, but fixed-confidence identification already studies error-vs-evidence tradeoffs | tests/T016_posterior_vs_support_resolution.py |
| T017 | Exact Decision Resolution to ECD reduction | EXACT REDUCTION / FOUNDATIONAL BRANCH EXHAUSTED | Worlds map to hypotheses, decision values to equivalence classes, experiments/outcomes/costs unchanged; terminal and Bellman conditions coincide | tests/T017_exact_reduction_to_ECD.py |

## Novelty audit notes
- Varying-query-set adaptive submodularity already studies adaptively changing query availability.
- Safe active learning already selects informative queries subject to safety constraints.
- Goal-oriented OED targets downstream quantities of interest rather than full latent-state identification.
- Sequential OED already optimizes non-myopic sequences for model discrimination, inference, and goal-oriented prediction.
- 2026 adaptive-sensing work explicitly co-designs sensor hardware geometry and adaptive measurement policy; generic genesis+execution co-design is therefore not a novelty claim.

## Completed extended tests

- **T018 — PhysioNet sequential decision-reversal benchmark — COMPLETED NEGATIVE.** Real-data run 35351053995 succeeded on 4,000 PhysioNet Challenge 2012 Set A records. Binary model-world disagreement was nearly saturated (0.936–0.945) and weak for future reversal (AUROC 0.522–0.536), while confidence/entropy/margin achieved AUROC 0.631–0.746. Current disagreement hypothesis rejected; do not build T019 on binary disagreement.

- **T019 — Quantitative decision-conflict benchmark — COMPLETED / PARTIAL NEGATIVE.** Run 35352412064 succeeded. Conflict mass substantially improves over binary disagreement (AUROC 0.609/0.690/0.713 vs 0.522/0.536/0.529 across stages) but remains below confidence/entropy/margin (0.631/0.709/0.746). Not a standalone breakthrough; proceed to actual cost-aware resolving acquisition.

- **T020 — Exact cheapest decision resolution vs EC2 / IG-cost — COMPLETED / FOUNDATIONAL COLLISION.** Run 35353367847 succeeded: 1,000 heterogeneous-cost instances, 847 resolvable. EC2 mean/maximum cost ratio to exact optimum = 1.1614/2.0 (45.45% exactly optimal); IG/cost = 1.3299/2.75 (27.51% exactly optimal). Confirms exact finite cheapest decision-resolution is optimal ECD; close fixed-library foundational branch.

- **T021 — Experiment-creation reduction attack — COMPLETED / COLLISION.** Run 35354211768: 1,000 instances, 0 mismatches, equal optimal-cost fraction 1.0. Finite known one-shot creation compiles into enlarged ECD with test cost = creation + execution. Close this branch.

- **T022 — Escape-cost nonidentifiability from current ECD structure — COMPLETED / MATHEMATICAL SEPARATION.** Run 35354518854 succeeded. Paired systems have identical current ECD structure but synthesis escape costs 1 vs m; tested ratio through 1024 and family is unbounded. Not yet irreducible to full OED because synthesis space/costs are externally supplied.

- **T023 — Meta-resolution / experiment-choice identifiability — COMPLETED / STRONG PHENOMENON + FINITE REDUCTION COLLISION.** Run 35354758712. Cheapest resolver is itself unresolved; blind minimax cost M vs meta-probe+resolver cost 2, ratio M/2 (64 at M=128; unbounded family). But finite model reduces to augmented hidden-state planning/ECD-POMDP. Preserve phenomenon; do not claim new finite primitive.

- **T024 — Generative decision-separation attack — COMPLETED / UNBOUNDED SEPARATION + NOVELTY COLLISION.** Corrected run 35355923946. Decision-targeted generated probe cost 1; full-world identification and adverse generic parameter-IG cost n+1. Exhaustively verified through n=14, scalable family tested through n=20 (ratio 21) and unbounded analytically. Valid boundary result, but conceptually occupied by goal-/decision-oriented OED; do not use as headline novelty.

- **T025 — Large real-data resolver-choice uncertainty — COMPLETED / POSITIVE PHENOMENON.** UCI Covertype: 581,012 rows, 54 features, 7 classes; 464,809 training rows and 20,000 evaluation cases, 12 bootstrap worlds. Resolver-uncertain rate 0.30045; RD>=0.25 rate 0.17025. Entropy AUROC 0.694894/AUPRC 0.469984 and low-confidence AUROC 0.693983/AUPRC 0.470575 for detecting resolver uncertainty. Thus compatible predictive worlds disagree about the cheapest additional panel in a substantial real-data subset and ordinary uncertainty is informative but not equivalent. Proxy panel costs/criterion limit practical claims. Next gate: T026 meta-resolution value and real-cost replication.

- **T026 — Real-data meta-resolution value — COMPLETED / WEAK POSITIVE, BREAKTHROUGH GATE FAILED.** UCI Covertype (581,012 rows), 10,000 evaluation cases, 10 bootstrap worlds. Static direct proxy loss 12.7339 vs meta-routing 12.70357 (reduction 0.03033, ~0.24%). Meta-routing better on only 2.42% of cases and >=10% better on 1.59%. Preserve as a negative/limiting result; do not claim practical meta-resolution advantage. Sequential OED/POMDP prior art also absorbs generic adaptive routing.

- **T027 — Independent NHANES replication gate — COMPLETED / WEAK NON-REPLICATION; NEW-PAPER GATE FAILED.** NHANES 2007–2018 pooled: 56,463 eligible rows, 11,293 evaluation cases, 12 bootstrap worlds. Resolver uncertainty 3.5243%; mean RD 0.008862; RD>=0.25 only 1.7533%. Ordinary entropy predicts resolver uncertainty at AUROC 0.823793 (AUPRC 0.101931). The phenomenon exists but did not substantially replicate T025's 30.045% rate and is much more aligned with ordinary uncertainty. Costs are analyte-count proxies, not monetary fees. Per preregistered stop rule: stop the new breakthrough-paper branch; preserve result and consider only an explicit limits/boundary synthesis.

## Archived research record

Akhtar, M. A. K. (2026). *Where Cheapest Decision-Resolving Experiments Become Old Theory—and Where They Do Not: Reductions, Escape Costs, and Resolver-Choice Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22833604
