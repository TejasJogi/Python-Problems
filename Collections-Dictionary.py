# from collections import defaultdict
# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not . Print the indices of each occurrence of m in group A. If it does not appear, print -1.

# Example

# Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

# For the first word in group B, 'a', it appears at positions and in group A. The second word, 'c', does not appear in group A, so print .

# Expected output:

# 1 3
# -1
# Input Format

# The first line contains integers, n and n separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.


# Output Format

# Output m lines.
# The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.

# Sample Input

# STDIN   Function
# ----- --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'
# b
# Sample Output

# 1 2 4
# 3 5


from collections import defaultdict

dic = defaultdict(list)

lst = []

n, m = map(int, input().split())

for i in range(1, n+1):
    inp_A = input()

    dic[inp_A].append(str(i))

for i in range(m):
    inp_B = input()
    
    if inp_B in dic:
        print(' '.join(dic[inp_B]))
    else:
        print(-1)
