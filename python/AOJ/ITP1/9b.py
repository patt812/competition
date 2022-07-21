i = 0
w = ''
while i < 10:
    i += 1
    x = input()
    if x == '-':
        break
    elif x.isnumeric():
        for _ in range(int(x)):
            c = int(input())
            w = w[c:] + w[0:c]
        print(w)
    else:
        w = x
