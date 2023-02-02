s = input()
if len(set(s[0:3])) == 1 or len(set(s[1:4])) == 1:
  print("Yes")
else:
  print("No")