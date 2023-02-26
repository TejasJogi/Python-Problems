# Task

# You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

# Input Format

# The first line contains space separated integers ,  and .
# The next  lines contains the space separated elements of the  columns.
# After that, the next  lines contains the space separated elements of the  columns.

# Output Format

# Print the concatenated array of size X.

# Sample Input

# 4 3 2
# 1 2
# 1 2 
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4 
# Sample Output

# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]] 

import numpy



N, M, P = map(int, input().split())

arrayN= numpy.array(list(input().split()  for i in range(N)), int)
print(arrayN)
arrayM = numpy.array(list(input().split()  for i in range(M)), int)
print(arrayM)
print(numpy.concatenate((arrayN,arrayM), axis=0))