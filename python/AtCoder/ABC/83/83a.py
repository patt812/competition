a, b, c, d = map(int, input().split())
w = (a + b) - (c + d)
if w > 0:
  print("Left")
elif w < 0:
  print("Right")
else:
  print("Balanced")