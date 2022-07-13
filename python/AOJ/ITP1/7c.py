R, C = map(int, input().split())
Csums = [0] * C

for r in range(R):
    d = list(map(int, input().split()))
    Rsum = 0
    for c in range(C):
        Csums[c] += d[c]
        Rsum += d[c]
        print(d[c], end=" ")
    print(Rsum, end="")
    print()
    if r == R - 1:
        Rsum = 0
        for S in Csums:
            Rsum += S
            print(S, end=" ")
print(Rsum)
