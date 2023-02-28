# Task

# You are given a 2-D array with dimensions NXM.
# Your task is to perform the min function over axis 1 and then find the max of that.

# Input Format

# The first line of input contains the space separated values of N and M.
# The next N lines contains M space separated integers.

# Output Format

# Compute the min along axis 1 and then print the max of that result.

# Sample Input

# 4 2
# 2 5
# 3 7
# 1 3
# 4 0
# Sample Output

# 3
# Explanation

# The min along axis 1 = [2, 3, 1, 0]
# The max of [2, 3, 1, 0] = 3

import numpy



N, M = list(map(int, input().split()))

arr = []

for i in range(N):
    A = list(map(int, input().split()))
    arr.append(A)

print(arr)
min = list(numpy.min(arr, axis = 1))
print(numpy.max(min))