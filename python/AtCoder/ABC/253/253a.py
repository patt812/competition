a, b, c = map(int, input().split())
if sorted([a, b, c])[1] == b:
  print("Yes")
else:
  print("No")