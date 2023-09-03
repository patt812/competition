S = input()
h = 0
c = 0
for s in S:
  if s == 'R':
    c += 1
    h = c
  else:
    c = 0
print(h)