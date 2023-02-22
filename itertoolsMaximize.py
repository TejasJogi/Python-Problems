from itertools import product

k, m = map(int, input().split())
lists = []
for i in range(m):
    lst = list(map(int, input().split()))[1:]
    lists.append(lst)

max_sum = 0
for c in product(*lists):
    s = sum(x**2 for x in c) % m
    max_sum = max(max_sum, s)

print(max_sum)
