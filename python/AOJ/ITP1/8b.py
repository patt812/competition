while 1:
    i = input()
    if int(i) == 0:
        break
    sum = int(i[0])
    for d in range(1, len(i)):
        sum += int(i[d])
    print(sum)
