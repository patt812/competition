abc = []
for _ in range(3):
  abc.append(int(input()))
rev = sorted(abc, reverse=True)
for i in abc:
  print(rev.index(i) + 1)