from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))

count = Counter(shoe_sizes)

N = int(input())

sum = 0
for i in range(1, N + 1):
    size_price = list(map(int, input().split()))
    size = size_price[0]
    price = size_price[1]

    if (count[size] != 0):
        count[size] = count[size] - 1
        sum = sum + price

print(sum)