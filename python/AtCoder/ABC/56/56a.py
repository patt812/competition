a, b = map(str, input().split())
b = True if b == 'H' else False
if a == 'D':
  b = not b
if b:
  print("H")
else:
  print("D")