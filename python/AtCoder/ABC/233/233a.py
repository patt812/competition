x, y = map(int, input().split())
if y - x < 0:
  print(0)
else:
  print(((y - x) + 9) // 10)