while True:
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        break
    for i in range(x):
        for j in range(y):
            print('#', end="")
        print()
    print()
