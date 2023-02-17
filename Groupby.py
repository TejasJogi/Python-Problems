from itertools import groupby

str = input()

for i, j in groupby(str):
    print((sum(1 for _ in j),int(i)), end=' ')