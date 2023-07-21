l = list(input())
for i in range(len(l)-1):
  if l[i] == l[i+1]:
    print("Bad")
    exit()
print("Good")