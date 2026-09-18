"""T001: Minimal admissibility obstruction.

Construct the smallest deterministic witness where decision-incompatible
worlds are distinguishable by available experiments, but every separating
experiment is inadmissible in at least one currently possible world.

Result:
  unconstrained resolution cost = 1
  branchwise-admissible resolution cost = infinity
"""

from math import inf

worlds = ("wA", "wB")
decision = {"wA": "A", "wB": "B"}

experiments = {
    "eA": {
        "cost": 1,
        "outcome": {"wA": 0, "wB": 1},
        "admissible": {"wA": True, "wB": False},
    },
    "eB": {
        "cost": 1,
        "outcome": {"wA": 1, "wB": 0},
        "admissible": {"wA": False, "wB": True},
    },
}

def resolved(C):
    return len({decision[w] for w in C}) <= 1

def branches(C, e):
    out = {}
    for w in C:
        out.setdefault(experiments[e]["outcome"][w], set()).add(w)
    return list(out.values())

def exact_value(C, admissibility=True, memo=None):
    C = frozenset(C)
    memo = {} if memo is None else memo
    key = (C, admissibility)
    if key in memo:
        return memo[key]
    if resolved(C):
        return 0

    best = inf
    for e, spec in experiments.items():
        if admissibility and not all(spec["admissible"][w] for w in C):
            continue
        bs = branches(C, e)
        if len(bs) == 1:
            continue
        v = spec["cost"] + max(exact_value(b, admissibility, memo) for b in bs)
        best = min(best, v)

    memo[key] = best
    return best

if __name__ == "__main__":
    C0 = set(worlds)
    ordinary = exact_value(C0, admissibility=False)
    admissible = exact_value(C0, admissibility=True)

    print("T001 minimal admissibility obstruction")
    print("ordinary decision-resolution cost:", ordinary)
    print("branchwise-admissible resolution cost:", admissible)

    assert ordinary == 1
    assert admissible == inf
    print("PASS")
