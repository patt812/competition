n, a, x, y = map(int, input().split())
if n - a > 0:
  print((a * x) + ((n - a) * y))
else:
  print(n * x)