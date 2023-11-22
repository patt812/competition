i, j = map(int, input().split())
l = [list(map(int, input().split()))]
l.append(list(map(int, input().split())))
print(l[i - 1][j - 1])