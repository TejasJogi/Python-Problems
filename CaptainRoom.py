number_of_members = int(input())

list_of_room_numbers = list(map(int, input().split()))

once = set()
repeats = set()

for i in list_of_room_numbers:
    if i not in once:
        once.add(i)
    else:
        repeats.add(i)

diff = once.difference(repeats).pop()

print(diff)