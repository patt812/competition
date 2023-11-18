s = input()
l = len(s)
i = 0
a = ""
while len(a) < 6:
  a += s[i % l]
  i += 1
print(a)