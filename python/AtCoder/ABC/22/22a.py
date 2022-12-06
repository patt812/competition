c, w = [0]*2
n, s, t = map(int, input().split())
for _ in range(n):
  w += int(input())
  if s <= w and w <= t:
    c += 1
print(c)