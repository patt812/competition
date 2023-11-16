def solve(a, b, c, x):
  w = 0
  y = 0
  z = True
  for i in range(x):
    if z:
      if y < a:
        w += b
        y += 1
      else:
        y = 1
        z = False
    else:
      if y < c:
        y += 1
      else:
        y = 1
        w += b
        z = True
  return w

a, b, c, d, e, f, x = map(int, input().split())
t = solve(a, b, c, x)
u = solve(d, e, f, x)
if t == u:
  print("Draw")
elif t > u:
  print("Takahashi")
else:
  print("Aoki")