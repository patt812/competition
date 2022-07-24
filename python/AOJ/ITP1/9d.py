s = input()
for i in range(int(input())):
    c = list(input().split())
    a = int(c[1])
    b = int(c[2])
    if c[0] == "replace":
        s = s[:a] + c[3] + s[b + 1:]
    elif c[0] == "reverse":
        t = s[a: b + 1]
        s = s[:a] + t[::-1] + s[b + 1:]
    elif c[0] == "print":
        print(s[a:b + 1])
