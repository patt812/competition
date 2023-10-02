x, y = map(int, input().split())
if x == y:
  print(x)
else:
  N = [0, 1, 2]
  del N[N.index(x)]
  del N[N.index(y)]
  print(N[0])
# print((6-x-y)%3)