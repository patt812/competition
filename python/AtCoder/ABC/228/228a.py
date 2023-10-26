s, t, x = map(int, input().split())
x = float(x + 0.5)
if (s > t and (s <= x <= 24 or 0 <= x <= t)) or (s <= t and s <= x <= t):
  print("Yes")
else:
  print("No")