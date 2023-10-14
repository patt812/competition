n = float(input())
x = int(n // 1)
y = int((n - x) * 10)
x = str(x)
if (0 <= y <= 2):
  x += "-"
elif (7 <= y <= 9):
  x += "+"
print(x)