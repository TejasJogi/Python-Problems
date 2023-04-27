# Task

# You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

# Input Format

# The first line contains an integer N. N is the total number of integers in the list.
# The second line contains the space separated list of N integers.

# Output Format

# Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

# Sample Input

# 5
# 12 9 61 5 14 

# Sample Output

# True


N = int(input())

integers = input().split()

print(all(int(i) >= 0 for i in integers) and any(i == i[::-1] for i in integers))