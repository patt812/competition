n, m, ll = map(int, input().split())

a_mat = [list(map(int, input().split())) for _ in range(n)]
b_mat = [list(map(int, input().split())) for _ in range(m)]
c_mat = [[0] * ll for _ in range(n)]

for i in range(n):
    for j in range(ll):
        for k in range(m):
            c_mat[i][j] += a_mat[i][k] * b_mat[k][j]

for i in range(n):
    print(*c_mat[i])
