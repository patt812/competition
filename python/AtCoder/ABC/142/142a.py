n = int(input())
if n % 2 == 0:
  print(f'{(n // 2) / n:06f}')
else:
  print(f'{((n // 2) + 1) / n:06f}')