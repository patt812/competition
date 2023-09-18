a, b, c = map(int, input().split())
if not c:
  if a - 1 >= b:
    print("Takahashi")
  else:
    print("Aoki")
elif c:
  if b - 1 >= a:
    print("Aoki")
  else:
    print("Takahashi")