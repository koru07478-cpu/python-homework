import math

def estimate_pi():
    total, k = 0, 0
    while (term := (2 * math.sqrt(2) / 9801) * (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k) ** 4 * 396 ** (4 * k))) >= 1e-15:
        total, k = total + term, k + 1
    return 1 / total
    
print(estimate_pi())
print(math.pi)
