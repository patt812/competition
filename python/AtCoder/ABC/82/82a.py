a, b = map(int, input().split())
s = a + b
if s % 2 == 0:
  print(int(s / 2))
else:
  print(int(s / 2) + 1)