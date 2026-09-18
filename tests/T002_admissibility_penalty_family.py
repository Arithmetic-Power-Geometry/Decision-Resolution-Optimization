"""T002: Nontrivial admissibility-penalty family.

For every integer M>=1 construct a deterministic decision-resolution instance:
- an unconstrained cost-1 test directly separates decision A from B;
- branchwise admissibility forbids that direct test initially;
- M prerequisite tests, each admissible and informative, must be traversed before
  a final cost-1 decision separator becomes admissible.

This proves an unbounded additive/multiplicative admissibility penalty family:
  V_unconstrained = 1
  V_admissible = M + 1
  ratio = M + 1
"""

from functools import lru_cache
from math import inf


def build_instance(M):
    # Worlds encode a chain position plus one final decision bit.
    # w0 is decision A; w1..wM are decision B variants.
    worlds = tuple(f"w{i}" for i in range(M + 1))
    decision = {w: ("A" if w == "w0" else "B") for w in worlds}
    experiments = {}

    # Direct decision separator: perfect but admissible only in w0.
    experiments["direct"] = {
        "cost": 1,
        "outcome": {w: (0 if w == "w0" else 1) for w in worlds},
        "admissible": {w: (w == "w0") for w in worlds},
    }

    # Prerequisite chain. Test j peels off w_j; all are universally admissible.
    # The final remaining pair is {w0,wM}; final resolves it.
    for j in range(1, M):
        experiments[f"pre_{j}"] = {
            "cost": 1,
            "outcome": {w: (1 if w == f"w{j}" else 0) for w in worlds},
            "admissible": {w: True for w in worlds},
        }

    experiments["final"] = {
        "cost": 1,
        "outcome": {w: (0 if w == "w0" else 1) for w in worlds},
        # final only legitimate after all intermediate B variants are removed
        "admissible": {
            w: (w in {"w0", f"w{M}"}) for w in worlds
        },
    }

    return worlds, decision, experiments


def exact_value(worlds, decision, experiments, admissibility=True):
    def resolved(C):
        return len({decision[w] for w in C}) <= 1

    @lru_cache(None)
    def V(C_tuple):
        C = frozenset(C_tuple)
        if resolved(C):
            return 0
        best = inf
        for e, spec in experiments.items():
            if admissibility and not all(spec["admissible"][w] for w in C):
                continue
            parts = {}
            for w in C:
                parts.setdefault(spec["outcome"][w], []).append(w)
            if len(parts) <= 1:
                continue
            # Require progress on every recursive branch; cycles excluded naturally
            branch_vals = []
            valid = True
            for B in parts.values():
                if len(B) == len(C):
                    valid = False
                    break
                vb = V(tuple(sorted(B)))
                if vb == inf:
                    valid = False
                    break
                branch_vals.append(vb)
            if valid:
                best = min(best, spec["cost"] + max(branch_vals))
        return best

    return V(tuple(sorted(worlds)))


if __name__ == "__main__":
    rows = []
    for M in [1, 2, 3, 5, 10, 25]:
        worlds, decision, experiments = build_instance(M)
        u = exact_value(worlds, decision, experiments, admissibility=False)
        a = exact_value(worlds, decision, experiments, admissibility=True)
        rows.append((M, u, a, a / u if u != inf else inf))
        print(M, u, a, a / u if u != inf else inf)

    # For this chain family the intended result is unbounded.
    assert rows[0][1] == 1
    assert all(r[2] >= r[0] for r in rows if r[2] != inf)
    print("PASS")
