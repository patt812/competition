l = [0] * 10
college = [
    [list(l), list(l), list(l)],
    [list(l), list(l), list(l)],
    [list(l), list(l), list(l)],
    [list(l), list(l), list(l)],
]

n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    college[x[0]-1][x[1]-1][x[2]-1] += x[3]

for z in range(0, len(college)):
    for y in range(0, len(college[z])):
        for x in range(0, len(college[z][y])):
            print(" ", end="")
            print(college[z][y][x], end="")
        print()
    if z != len(college) - 1:
        print('####################')
