def average(array):
    # your code goes here
    add = sum(set(array))/len(set(array))
    return round(add, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)