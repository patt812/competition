def fizzOrIncludeThree(n):
    if n % 3 == 0:
        return 'YES'
    while n > 0:
        n /= 10
        if int(n) % 10 == 3:
            return 'YES'
    return 'NO'


print(fizzOrIncludeThree(int(input())))
