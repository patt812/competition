l = sorted(list(map(int, input().split())))
if l[2] - l[1] == l[1] - l[0]:
  print("Yes")
else:
  print("No")