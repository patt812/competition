n, x = map(int, input().split())
s = ""
for i in range(ord('A'), ord('Z')+1):
  for _ in range(n):
    s += chr(i)
print(s[x-1])