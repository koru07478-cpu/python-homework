# Упражнение 6.6
def gcd(a: int, b: int) -> int:
 if b == 0:
  return a
 return gcd(b, a%b)

print(gcd(5, 17))

#алгоритм Евклида:)
