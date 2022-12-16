import math

def gcd(a, b):
  if (b == 0): return a
  return gcd(b, a % b)

def lcm(a, b):
  d = gcd(a, b)
  return int(a / d * b)

a = int(input())
b = int(input())
n = int(input())
lcm = lcm(a, b)
print(lcm * math.ceil(n / lcm))