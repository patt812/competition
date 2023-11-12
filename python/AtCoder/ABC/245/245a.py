a, b, c, d = map(int, input().split())
if (a*100) + b < (c*100) + d + 0.1:
  print("Takahashi")
else:
  print("Aoki")