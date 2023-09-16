a, b = map(int, input().split())
if min(a, b) + 3 > max(a, b):
  print("Yes")
else:
  print("No")