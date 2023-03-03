import re

T = int(input())

for _ in range(T):
    s = input()

    res = True
    try: 
        re.compile(s)
    except:
        res = False

    print(res)