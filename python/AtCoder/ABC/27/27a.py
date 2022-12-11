l = list(map(int, input().split()))
dup = [x for x in set(l) if l.count(x) > 1]
unique = [x for x in set(l) if l.count(x) == 1]
if len(unique) == 0:
  print(dup[0])
else:
  print(unique[0])