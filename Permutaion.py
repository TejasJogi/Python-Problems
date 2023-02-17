from itertools import permutations

n = list(input().split())

permutation = list(permutations(n[0], int(n[1])))

sort_permute = sorted(permutation)

for i in sort_permute:
    for j in i:
        print(j,end='')
    print()