a, b = map(int, input().split())
if b % a == 0:
  print(int(b/a))
else:
  print(int(b/a) + 1)