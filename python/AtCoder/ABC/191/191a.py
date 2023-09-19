v, t, s, d = map(int, input().split())
if d < t * v or v * s < d:
  print("Yes")
else:
  print("No")