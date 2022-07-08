n = int(input())
z = {
    "S": [],
    "H": [],
    "C": [],
    "D": []
}

for i in range(n):
    a, b = input().split()
    z[a].append(int(b))

for i in ["S", "H", "C", "D"]:
    for j in range(1, 14):
        if (j not in z[i]):
            print(f'{i} {j}')
