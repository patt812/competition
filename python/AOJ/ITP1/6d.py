a, b = []
n, m = map(int, input().split())

for x in range(n):
    a.append(list(map(int, input().split())))
for x in range(m):
    b.append(int(input()))

for i in range(len(a)):
    sum = 0
    for j in range(len(b)):
        sum += (a[i][j] * b[j])
    print(sum)

