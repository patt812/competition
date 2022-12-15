a, b = map(int, input().split())
l = (a + 1) * b
m = (b + 1) * a
if l >= m:
  print(l)
else:
  print(m)