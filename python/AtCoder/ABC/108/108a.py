k = int(input())
e = [x for x in range(1, k+1) if x % 2 == 0]
o = [x for x in range(1, k+1) if x % 2 != 0]
print(len(e) * len(o))
# ( k / 2 ) * ( ( k + 1 ) / 2 ) )