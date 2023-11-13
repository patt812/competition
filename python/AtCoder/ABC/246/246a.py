a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
l = [a, c, e]
ux = [x for x in l if l.count(x) == 1]
l = [b, d, f]
uy = [y for y in l if l.count(y) == 1]
print(f'{ux[0]} {uy[0]}')