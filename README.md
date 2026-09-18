# Decision-Resolution-Optimization

Research lab for optimization under unresolved possible worlds.

## Current research question
Given current knowledge that leaves mutually incompatible possible worlds, determine the minimum-cost experiment policy that resolves the required optimization decision. If the current experiment language cannot do so under branchwise admissibility, determine the minimum-cost expansion of that experiment language.

## Core objects
- Possible worlds W
- Decision map D(w)
- Experiments e with execution cost c(e)
- Outcomes O_e(w)
- World-dependent admissibility A_e(w)
- Branchwise admissible experiment set E_A(C) = {e : A_e(w)=1 for all w in current compatible set C}
- Exact worst-case resolution value:
  V(C)=0 if all worlds in C imply equivalent decisions;
  otherwise V(C)=min_e [c(e)+max_o V(C_{e,o})] over branchwise-admissible informative experiments.
- If no admissible informative experiment exists while incompatible decisions remain, V(C)=infinity.

## Research policy
We do not write the paper until the theory survives novelty attacks and the repository contains:
1. exact finite witnesses,
2. strict separation results,
3. comparison with closest prior formulations,
4. large synthetic stress tests,
5. at least one substantial real-data validation where the decision/world distinction is operationally meaningful.

## Test ledger
See TESTS.md.
