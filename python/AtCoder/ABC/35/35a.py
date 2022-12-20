def gcd(a, b):
  if (b == 0): return a
  return gcd(b, a % b)

a, b = map(int, input().split())
gcd = gcd(a, b)
if int(a / gcd) == 4 and int(b / gcd) == 3:
  print('4:3')
if int(a / gcd) == 16 and int(b / gcd) == 9:
  print('16:9')
