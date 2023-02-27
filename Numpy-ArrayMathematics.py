# Task

# You are given two integer arrays, A and B of dimensions NXM.
# Your task is to perform the following operations:

# Add (A + B)
# Subtract (A - B)
# Multiply (A * B)
# Integer Division (A / B)
# Mod (A % B)
# Power (A ** B)

# Note
# There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

# Input Format

# The first line contains two space separated integers, N and M.
# The next N lines contains M space separated integers of array A.
# The following N lines contains M space separated integers of array B.

# Output Format

# Print the result of each operation in the given order under Task.

# Sample Input

# 1 4
# 1 2 3 4
# 5 6 7 8
# Sample Output

# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]] 
# Use // for division in Python 3.

import numpy



N, M = list(map(int, input().split()))

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)