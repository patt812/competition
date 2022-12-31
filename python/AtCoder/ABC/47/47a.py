rev = sorted(list(map(int, input().split())), reverse=True)
if rev[0] == rev[1] + rev[2]:
  print("Yes")
else:
  print("No")