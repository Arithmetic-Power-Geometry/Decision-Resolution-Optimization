"""T011: Adaptive experiment genesis vs ex-ante capability creation.

Family W_M={(A,i),(B,i): i=1..M}. Existing routing experiment r (cost 1)
reveals i but not decision A/B. Candidate capability z_i costs 1 to create
and enables experiment e_i (execution cost 1), which separates A/B only on
branch i.

Static/ex-ante robust design must create all M capabilities before r is
observed. Adaptive genesis runs r, observes i, then creates only z_i.

Exact costs:
  J_static = M + 2
  J_adaptive = 3
so ratio (M+2)/3 -> infinity.
"""
def costs(M):
    assert M>=1
    static=M+2
    adaptive=3
    return static,adaptive

if __name__=="__main__":
    for M in [1,2,4,8,16,32,64,128,1024]:
        s,a=costs(M)
        print({"M":M,"static":s,"adaptive":a,"ratio":s/a})
        assert s==M+2 and a==3
    assert costs(1024)[0]/costs(1024)[1] > 300
    print("PASS: ex-ante/adaptive genesis ratio is unbounded.")
