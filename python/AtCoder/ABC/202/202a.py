l = list(map(int, input().split()))
s = 0
for i in l:
  s += 7 - i
print(s)