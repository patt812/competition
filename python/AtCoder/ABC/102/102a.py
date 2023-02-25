def gcd(a, b):
  if (b == 0): return a
  return gcd(b, a % b)

def lcm(a, b):
  d = gcd(a, b)
  return int(a / d * b)

print(lcm(2, int(input())))