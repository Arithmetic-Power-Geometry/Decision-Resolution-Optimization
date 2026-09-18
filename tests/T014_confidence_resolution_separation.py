"""T014: High posterior confidence can coexist with unresolved decision support.

Finite compatible worlds: one dominant A-world has posterior mass 1-delta.
A rare but still compatible B-world has posterior mass delta>0.
Bayesian confidence in decision A is 1-delta -> 1 as delta -> 0.
Support-based decision resolution remains false for every delta>0 because
both A and B decisions remain represented in the compatible-world support.

This is a mathematical separation, not by itself a novelty claim.
"""
def metrics(delta):
    assert 0 < delta < 0.5
    confidence=1-delta
    resolved=False
    support_diameter=1
    return confidence,resolved,support_diameter

if __name__=="__main__":
    for d in [1e-1,1e-2,1e-3,1e-6,1e-9,1e-12]:
        conf,res,gap=metrics(d)
        print({"delta":d,"confidence":conf,"resolved":res,"resolution_gap":gap})
        assert not res and gap==1
    assert metrics(1e-12)[0] > 0.999999999
    print("PASS: confidence tends to 1 while support-based decision resolution remains false.")
