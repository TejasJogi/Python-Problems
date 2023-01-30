set_A = set(map(int, input().split()))

numbers_of_other_sets = int(input())

for i in range(numbers_of_other_sets):
    other_set = set(map(int, input().split()))

false_set = set()

for i in other_set:
    if (set_A.issuperset(other_set)):
        continue
    else:
        false_set.add(False)

print(false_set)

if False in false_set:
    print(False)
else:
    print(True)