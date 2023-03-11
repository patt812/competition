s = ''
for i in input():
  if i == '9':
    s += '1'
  elif i == '1':
    s += '9'
  else:
    s += i
print(s)