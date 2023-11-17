h, w = map(int, input().split())
i, j = map(int, input().split())
s = 0

if i - 1 > 0: s += 1
if j - 1 > 0: s += 1
if i + 1 <= h: s += 1
if j + 1 <= w: s += 1

print(s)