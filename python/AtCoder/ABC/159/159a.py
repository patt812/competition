n, m = map(int, input().split())
s = 0
for i in range(1, n):
  s += i
for i in range(1, m):
  s += i
print(s)