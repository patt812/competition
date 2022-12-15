a, b, c, d = map(int, input().split())
ret = (b/a) - (d/c)
if ret == 0:
  print("DRAW")
elif ret > 0:
  print("TAKAHASHI")
else:
  print("AOKI")
