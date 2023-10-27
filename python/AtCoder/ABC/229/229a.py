s = input()
t = input()
d = s.count(".") + t.count(".")
if d == 2 and (s[0] == "." and t[1] == ".") or (s[1] == "." and t[0] == "."):
  print("No")
else:
  print("Yes")