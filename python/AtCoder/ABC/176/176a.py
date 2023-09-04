n, x, t = map(int, input().split())
if n % x == 0:
  print((n // x) * t)
else:
  print((1 + n // x) * t)