if __name__ == '__main__':
    s = input()

    out = False
    for i in s:
        if i.isalnum():
            out = True
            break
    print(out)

    out = False  
    for i in s:
        if i.isalpha():
            out = True
            break
    print(out)

    out = False        
    for i in s:
        if i.isdigit():
            out = True
            break
    print(out)

    out = False
    for i in s:
        if i.islower():
            out = True
            break
    print(out)

    out = False
    for i in s:
        if i.isupper():
            out = True
            break
    print(out)
      