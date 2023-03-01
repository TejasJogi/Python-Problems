# Task

# You are given a 2-D array of size NXM.
# Your task is to find:

# 1. The mean along axis 1
# 2. The var along axis 0
# 3. The std along axis None

# Input Format

# The first line contains the space separated values of N and M.
# The next N lines contains M space separated integers.

# Output Format

# First, print the mean.
# Second, print the var.
# Third, print the std.

# Sample Input

# 2 2
# 1 2
# 3 4
# Sample Output

# [ 1.5  3.5]
# [ 1.  1.]
# 1.11803398875

import numpy
numpy.set_printoptions(legacy='1.13')


N, M = list(map(int, input().split()))

A = numpy.array([input().split() for i in range(N)], int)

print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(numpy.round(numpy.std(A), 11))