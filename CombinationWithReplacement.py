from itertools import combinations_with_replacement

str, num = input().split()


for j in sorted(combinations_with_replacement(str, int(num))):
    print(''.join(j))