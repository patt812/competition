n, x = map(int, input().split())
t = x - 1
b = n - x
print(t if t < b else b)