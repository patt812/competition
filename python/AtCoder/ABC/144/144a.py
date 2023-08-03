a, b = map(int, input().split())
n = [x for x in range(1, 10)]
if a in n and b in n:
  print(a * b)
else:
  print(-1)