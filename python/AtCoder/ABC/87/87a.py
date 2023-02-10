x = int(input())
a = int(input())
b = int(input())
n = x - a
n -= ((n // b) * b)
print(n)