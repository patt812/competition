import math
a = int(input())
b = int(input())

if a == b:
  print(0)
else:
  print((math.ceil(a / b) * b) - a)
  # print((b-a%b)%b)