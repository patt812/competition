c = [i for i in range(2, 14)]
c.append(1)
a, b = map(int, input().split())
if c.index(a) > c.index(b):
  print("Alice")
elif c.index(a) < c.index(b):
  print("Bob")
else:
  print("Draw")