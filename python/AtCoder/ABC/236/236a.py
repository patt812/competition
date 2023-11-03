S = list(input())
a, b = map(int, input().split())
t = S[a-1]
S[a-1] = S[b-1]
S[b-1] = t
print("".join(S))