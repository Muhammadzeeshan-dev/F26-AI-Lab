def advanced_symbolic(score, complete, fee_paid, verified):
    if complete and fee_paid and verified and score >= 70:
        return "Review"
    else:
        return "Hold"

cases = [
    ("all_pass", 85, True, True, True),
    ("fee_unpaid", 85, True, False, True),
    ("not_verified", 85, True, True, False),
    ("boundary_score", 70, True, True, True)
]

for name, score, complete, fee, verified in cases:
    result = advanced_symbolic(score, complete, fee, verified)
    print(name, "-->", result)
