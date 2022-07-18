s = input()
p = input()

if p in s[len(s) - len(p):] + s:
    print('Yes')
else:
    print('No')
