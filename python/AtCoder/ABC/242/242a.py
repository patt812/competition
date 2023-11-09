a, b, c, x = map(int, input().split())
if x > b:
  print(0)
elif x > a:
  print(f'{c / (b - a):06f}')
else:
  print(1.0)