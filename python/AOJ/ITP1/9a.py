w = input().upper()
a = 0
while 1:
    p = input()
    if p == 'END_OF_TEXT':
        break
    a += p.upper().split().count(w)
print(a)
