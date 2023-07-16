l, i = map(int, input().split())
s = list(input())
s[i-1] = s[i-1].lower()
print("".join(s))