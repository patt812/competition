x, a, b = map(int, input().split())
e = ((x - a) + b) - x
if e >= x + 1:
  print("dangerous")
elif e <= 0:
  print("delicious")
else:
  print("safe")