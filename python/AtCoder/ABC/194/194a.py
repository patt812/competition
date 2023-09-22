a, b = map(int, input().split())
k = a + b
if k > 14 and b > 7:
  print(1)
  exit()
if k > 9 and b > 2:
  print(2)
  exit()
if k > 2:
  print(3)
  exit()
print(4)