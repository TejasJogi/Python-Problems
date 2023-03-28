# Task
# You are given three integers: a, b, and m. Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

# Input Format
# The first line contains a, the second line contains b, and the third line contains m.

# Constraints



# Sample Input

# 3
# 4
# 5
# Sample Output

# 81
# 1


import math

a = int(input())
b = int(input())
m = int(input())


power  = math.pow(a,b)
print(int(power))
print(int(math.fmod(power, m)))