a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
l = [a, b, c]
x, y = map(int, input().split())

z = False
for i in l:
  if x in i and y in i:
    z = True
    break
if z:
  print("Yes")
else:
  print("No")
# n,m=map(int,input().split())
# a=[4,6,9,11]
# b=[1,3,5,7,8,10,12]
# if (n in a and m in a) or (n in b and m in b):
#   print('Yes')
# else:
#   print('No')