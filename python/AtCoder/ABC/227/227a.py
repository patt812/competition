n, k, a = map(int, input().split())
for i in range(k-1):
  if a == n:
    a = 1
  else:
    a += 1
print(a)
