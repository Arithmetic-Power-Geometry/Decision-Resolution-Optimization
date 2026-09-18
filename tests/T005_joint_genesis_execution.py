"""T005: Joint genesis + execution separation.

Candidate capabilities have one-time genesis cost k and induce an adaptive
execution policy cost C. We compare:
A) genesis-only choice: minimize k, then execute optimally;
B) execution-only choice: minimize C, ignoring k;
C) joint choice: minimize k + C.

The witness shows both one-stage rules can be strictly suboptimal for total
decision-resolution cost.
"""

candidates={
    # cheapest to build, expensive to use repeatedly
    "cheap_build":{"genesis":1,"execution":100},
    # expensive to build, cheapest to execute
    "cheap_run":{"genesis":30,"execution":1},
    # balanced capability
    "balanced":{"genesis":10,"execution":10},
}
lam=1

total={z:v["genesis"]+lam*v["execution"] for z,v in candidates.items()}
genesis_only=min(candidates,key=lambda z:candidates[z]["genesis"])
execution_only=min(candidates,key=lambda z:candidates[z]["execution"])
joint=min(candidates,key=lambda z:total[z])

if __name__=="__main__":
    print("candidate, genesis, execution, total")
    for z,v in candidates.items():
        print(z,v["genesis"],v["execution"],total[z])
    print("genesis-only:",genesis_only,total[genesis_only])
    print("execution-only:",execution_only,total[execution_only])
    print("joint:",joint,total[joint])
    assert genesis_only=="cheap_build" and total[genesis_only]==101
    assert execution_only=="cheap_run" and total[execution_only]==31
    assert joint=="balanced" and total[joint]==20
    assert total[joint] < total[genesis_only]
    assert total[joint] < total[execution_only]
    print("PASS")
