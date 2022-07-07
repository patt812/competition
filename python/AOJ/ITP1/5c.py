sharp = True
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break

    for i in range(0, h):
        if i % 2 == 0:
            sharp = True
        else:
            sharp = False

        for j in range(0, w):
            if sharp:
                print('#', end="")
            else:
                print('.', end="")
            sharp = not bool(sharp)
        print()
    print()
