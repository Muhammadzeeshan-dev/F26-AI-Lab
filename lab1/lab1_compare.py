def symbolic(score, complete):
    if complete and score >= 70:
        return "Review"
    else:
        return "Hold"

def threshold(prob):
    if prob >= 0.70:
        return "Review"
    else:
        return "Hold"

cases = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70)
]

for name, score, complete, prob in cases:
    res1 = symbolic(score, complete)
    res2 = threshold(prob)
    print(name, res1, res2, res1 != res2)
