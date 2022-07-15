a = int(input())
x = 0
for i in range(1, a+1):
    x += (i * int(1e4)) * (1/a)
print(f'{x:.0f}')
