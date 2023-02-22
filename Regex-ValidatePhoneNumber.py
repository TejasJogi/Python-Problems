import re

N = int(input())

for i in range(N):
    num = input()
    res = re.search(r"\b[7-9]{1}[0-9]{2,9}\b", num)
    if res:
        print('YES')
    else:
        print('NO')