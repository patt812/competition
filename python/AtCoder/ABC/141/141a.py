W = ['Sunny', 'Cloudy', 'Rainy']
s = input()
if W.index(s) == 2:
  print(W[0])
else:
  print(W[W.index(s) + 1])