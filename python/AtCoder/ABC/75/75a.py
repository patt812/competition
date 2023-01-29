l = list(map(int, input().split()))
l = [x for x in l if l.count(x) == 1]
print(l[0])
