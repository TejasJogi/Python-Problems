import re
import email.utils

n = int(input())

for i in range(n):
    inp = input().split()

    name = inp[0]
    email = inp[1]

    res = re.search(r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>", email)
    if res:
        print(name, email)