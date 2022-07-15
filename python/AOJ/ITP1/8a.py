for c in input():
    if c.isalpha():
        if c.islower():
            print(c.upper(), end="")
        else:
            print(c.lower(), end="")
    else:
        print(c, end="")
print()
